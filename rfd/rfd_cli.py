import sys
import os
import click
from colorama import init, Fore, Style
from api import get_threads, get_posts

init()
print()


def get_terminal_width():
    _, columns = os.popen('stty size', 'r').read().split()
    return int(columns)


def get_vote_color(score):
    if score > 0:
        return Fore.GREEN + " [+" + str(score) + "] "
    elif score < 0:
        return Fore.RED + " [" + str(score) + "] "
    return Fore.BLUE + " [" + str(score) + "] "


@click.group()
def cli():
    """Welcome to the RFD CLI. (RedFlagDeals.com)"""
    pass


@cli.command(short_help="Displays posts in a specific thread.")
@click.option('--count', default=5, help='Number of topics. 0 for all topics')
@click.option('--tail/--head', default=False, help='Number of topics.')
@click.argument('post_id')
def posts(count, post_id, tail):
    """Displays posts in a specific thread.

    post_id can be a full url or post id only

    Example:

    \b
    url: https://forums.redflagdeals.com/koodo-targeted-public-mobile-12-120-koodo-5gb-40-no-referrals-2173603
    post_id: 2173603
    """
    if count < 0:
        click.echo("Invalid count.")
        sys.exit(1)

    try:
        click.echo("-" * get_terminal_width())
        for post in get_posts(post=post_id, count=count, tail=tail):
            click.echo(" -" + get_vote_color(post.get('score')) + Fore.RESET +
                       post.get('body') + Fore.YELLOW + " ({})".format(post.get('user')))
            click.echo(Style.RESET_ALL)
            click.echo("-" * get_terminal_width())
    except ValueError:
        click.echo("Invalid post id.")
        sys.exit(1)
    except AttributeError:
        click.echo("AttributeError: RFD API did not return expected data.")


@cli.command(short_help="Displays threads in the specified forum.")
@click.option('--count', default=5, help='Number of topics.')
@click.argument('forum_id')
def threads(count, forum_id):
    """Displays threads in the specified forum id.

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
    _threads = get_threads(forum_id, count)
    for i, thread in enumerate(_threads, 1):
        click.echo(" " + str(i) + "." +
                   get_vote_color(thread.get('score')) + Fore.RESET + thread.get('title'))
        click.echo(Fore.BLUE + " {}".format(thread.get('url')))
        click.echo(Style.RESET_ALL)


if __name__ == '__main__':
    cli()
