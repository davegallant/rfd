# RFD

Hot deals on the command line.

[![PyPI version](https://badge.fury.io/py/rfd.svg)](https://badge.fury.io/py/rfd)
[![Dependabot](https://badgen.net/badge/Dependabot/enabled/green?icon=dependabot)](https://dependabot.com/)
[![Downloads](https://pepy.tech/badge/rfd)](https://pepy.tech/project/rfd)

![screenshot](https://user-images.githubusercontent.com/4519234/85969861-e10a4100-b996-11ea-9a31-6203322c60ee.png)

## Install

```bash
pip install rfd
```

## Usage

```sh
Usage: rfd [OPTIONS] COMMAND [ARGS]...

  CLI for https://forums.redflagdeals.com

Options:
  -v, --version
  --help         Show this message and exit.

Commands:
  posts    Display all posts in a thread.
  search   Search deals based on a regular expression.
  threads  Displays threads in the forum. Defaults to hot deals.
```

## Examples

All commands open up in a [terminal pager](https://en.wikipedia.org/wiki/Terminal_pager).

### View Hot Deals

```sh
rfd threads
```

### View and Sort Hot Deals

```sh
rfd threads --sort-by score
```

To view and sort multiple pages, use `--pages`:

```sh
rfd threads --sort-by views --pages 10
```

### Simple Search

```sh
rfd search 'pizza'
```

### Advanced Search

Regular expressions can be used for search.

```console
rfd search '(coffee|starbucks)' --pages 10 --sort-by views
```

### View Posts

It's possible to view an entire post and all comments by running:

```sh
rfd posts https://forums.redflagdeals.com/kobo-vs-kindle-2396227/
```

This allows for easy grepping and searching for desired expressions.

## Shell Completion

Shell completion can be enabled if using `bash` or `zsh`.

### bash

```sh
echo 'eval "$(_RFD_COMPLETE=source rfd)"' >> ~/.profile
```

### zsh

```sh
echo 'eval "$(_RFD_COMPLETE=source_zsh rfd)"' >> ~/.zshrc
```
