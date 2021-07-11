from __future__ import unicode_literals


import logging
import sys
import click
try:
    from importlib import metadata
except ImportError: # for Python<3.8
    import importlib_metadata as metadata
from colorama import init
from .api import get_threads, get_posts
from .threads import parse_threads, search_threads, sort_threads, generate_thread_output
from .posts import generate_posts_output


init()

logging.getLogger()
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())


def get_version():
    return "rfd v" + metadata.version("rfd")

def print_version(ctx, _, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(get_version(), nl=True)
    ctx.exit()


@click.group(invoke_without_command=True)
@click.option(
    "-v",
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
)
@click.pass_context
def cli(ctx):
    """CLI for https://forums.redflagdeals.com"""
    if not ctx.invoked_subcommand:
        click.echo(ctx.get_help())


@cli.command(short_help="Display all posts in a thread.")
@click.argument("post_id")
def posts(post_id):
    """Iterate all pages and display all posts in a thread.

    post_id can be a full url or post id only

    Example:

    \b
    rfd posts https://forums.redflagdeals.com/koodo-targeted-public-mobile-12-120-koodo-5gb-40-no-referrals-2173603
    """

    try:
        click.echo_via_pager(generate_posts_output(get_posts(post=post_id)))
    except ValueError:
        click.echo("Invalid post id.")
        sys.exit(1)
    except AttributeError:
        click.echo("The RFD API did not return the expected data.")
        sys.exit(1)


@cli.command(short_help="Displays threads in the forum. Defaults to hot deals.")
@click.option("--forum-id", default=9, help="The forum id number")
@click.option("--pages", default=1, help="Number of pages to show. Defaults to 1.")
@click.option("--sort-by", default=None, help="Sort threads by")
def threads(forum_id, pages, sort_by):
    """Display threads in the specified forum id. Defaults to 9 (hot deals).

    Popular forum ids:

    \b
    9 \t hot deals
    14 \t computer and electronics
    15 \t offtopic
    17 \t entertainment
    18 \t food and drink
    40 \t automotive
    53 \t home and garden
    67 \t fashion and apparel
    74 \t shopping discussion
    88 \t cell phones
    """
    _threads = sort_threads(parse_threads(get_threads(forum_id, pages)), sort_by=sort_by)
    click.echo_via_pager(generate_thread_output(_threads))


@cli.command(short_help="Search deals based on a regular expression.")
@click.option("--pages", default=5, help="Number of pages to search.")
@click.option(
    "--forum-id", default=9, help="The forum id number. Defaults to 9 (hot deals)."
)
@click.option("--sort-by", default=None, help="Sort threads by")
@click.argument("regex")
def search(pages, forum_id, sort_by, regex):
    """Search deals based on regex.

    Popular forum ids:

    \b
    9 \t hot deals
    14 \t computer and electronics
    15 \t offtopic
    17 \t entertainment
    18 \t food and drink
    40 \t automotive
    53 \t home and garden
    67 \t fashion and apparel
    74 \t shopping discussion
    88 \t cell phones
    """

    matched_threads = []

    _threads = parse_threads(get_threads(forum_id, pages=pages))
    for thread in search_threads(threads=_threads, regex=regex):
        matched_threads.append(thread)
    click.echo_via_pager(
        generate_thread_output(sort_threads(matched_threads, sort_by=sort_by))
    )
