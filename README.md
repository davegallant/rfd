# RFD

[![PyPI version](https://badge.fury.io/py/rfd.svg)](https://badge.fury.io/py/rfd)
[![Dependabot](https://badgen.net/badge/Dependabot/enabled/green?icon=dependabot)](https://dependabot.com/)
[![Downloads](https://pepy.tech/badge/rfd)](https://pepy.tech/project/rfd)

<!-- BEGIN mktoc -->
- [Description](#description)
- [Motivation](#motivation)
- [Installation](#installation)
- [Usage](#usage)
  - [View Hot Deals](#view-hot-deals)
  - [View and Sort Hot Deals](#view-and-sort-hot-deals)
  - [Search](#search)
    - [Advanced](#advanced)
  - [View Posts](#view-posts)
- [Shell Completion](#shell-completion)
  - [bash](#bash)
  - [zsh](#zsh)
<!-- END mktoc -->

## Description

This is a CLI utility that allows you to view [RedFlagDeals.com](https://forums.redflagdeals.com) on the command line.

![screenshot](https://user-images.githubusercontent.com/4519234/85969861-e10a4100-b996-11ea-9a31-6203322c60ee.png)

## Motivation

It is often faster to use a CLI than to load up a web page and navigate web elements. This tool can search for deals and sort them based on score and views. It is also able to load entire threads (without pagination) for additional analysis.

## Installation

### pip

```sh
pip3 install --user rfd
```

This can also be installed with [pipx](https://github.com/pypa/pipx).

### brew

If you have [brew](https://brew.sh):

```sh
brew install davegallant/public/rfd
```


## Usage

All commands open up in a [terminal pager](https://en.wikipedia.org/wiki/Terminal_pager).

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

### View Hot Deals

To view the threads on most popular sub-forum:

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

### Search

```sh
rfd search 'pizza'
```

#### Advanced

Regular expressions can be used for search.

```sh
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
