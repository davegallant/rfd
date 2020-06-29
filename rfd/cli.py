from __future__ import unicode_literals


import logging
import os
import sys
import click
from colorama import init, Fore, Style
from .api import get_threads, get_posts
from .search import search_threads
from .parsing import parse_threads
from .__version__ import version as current_version

init()
print()

logging.getLogger()
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())


def get_version():
    return "rfd " + current_version


def get_terminal_width():
    _, columns = os.popen("stty size", "r").read().split()
    return int(columns)


def get_vote_color(score):
    if score > 0:
        return Fore.GREEN + " [+" + str(score) + "] "
    if score < 0:
        return Fore.RED + " [" + str(score) + "] "
    return Fore.BLUE + " [" + str(score) + "] "


def print_version(ctx, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(get_version())
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
        click.echo("-" * get_terminal_width())
        for post in get_posts(post=post_id):
            click.echo(
                " -"
                + get_vote_color(post.score)
                + Fore.RESET
                + post.body
                + Fore.YELLOW
                + " ({})".format(post.user)
            )
            click.echo(Style.RESET_ALL)
            click.echo("-" * get_terminal_width())
    except ValueError:
        click.echo("Invalid post id.")
        sys.exit(1)
    except AttributeError:
        click.echo("The RFD API did not return the expected data.")
        sys.exit(1)


@cli.command(short_help="Displays threads in the forum. Defaults to hot deals.")
@click.option("--limit", default=10, help="Number of topics.")
@click.option("--forum-id", default=9, help="The forum id number")
def threads(limit, forum_id):
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
    _threads = parse_threads(get_threads(forum_id, limit), limit)
    for count, thread in enumerate(_threads, 1):
        click.echo(
            " "
            + str(count)
            + "."
            + get_vote_color(thread.score)
            + Fore.RESET
            + "[%s] %s" % (thread.dealer_name, thread.title)
            + Fore.LIGHTYELLOW_EX
            + " (%d views)" % thread.total_views
            + Fore.RESET
        )
        click.echo(Fore.BLUE + " {}".format(thread.url))
        click.echo(Style.RESET_ALL)


@cli.command(short_help="Search deals based on a regular expression.")
@click.option("--num-pages", default=5, help="Number of pages to search.")
@click.option(
    "--forum-id", default=9, help="The forum id number. Defaults to 9 (hot deals)."
)
@click.argument("regex")
def search(num_pages, forum_id, regex):
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

    count = 0
    for page in range(1, num_pages):
        _threads = parse_threads(get_threads(forum_id, 100, page=page), limit=100)
        for thread in search_threads(threads=_threads, regex=regex):
            count += 1
            click.echo(
                " "
                + str(count)
                + "."
                + get_vote_color(thread.score)
                + Fore.RESET
                + "[%s] %s" % (thread.dealer_name, thread.title)
            )
            click.echo(Fore.BLUE + " {}".format(thread.url))
            click.echo(Style.RESET_ALL)
