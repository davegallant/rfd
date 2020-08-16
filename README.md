# RFD

Hot deals on the command line.

[![Build Status](https://travis-ci.org/davegallant/rfd.svg?branch=master)](https://travis-ci.org/davegallant/rfd)
[![PyPI version](https://badge.fury.io/py/rfd.svg)](https://badge.fury.io/py/rfd)
[![Dependabot](https://badgen.net/badge/Dependabot/enabled/green?icon=dependabot)](https://dependabot.com/)
[![Downloads](https://pepy.tech/badge/rfd)](https://pepy.tech/project/rfd)

![screenshot](https://user-images.githubusercontent.com/4519234/85969861-e10a4100-b996-11ea-9a31-6203322c60ee.png)

## Install

```bash
pip install rfd
```

## Usage

```shell
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

All commands open up in a pager.

Search can be done using `/`.

Close pager with `q`.

### View Hot Deals

```console
$ rfd threads
```

### View and Sort Hot Deals

```console
$ rfd threads --sort-by score
```

```console
$ rfd threads --sort-by views --pages 10
```

### Simple Search

```console
$ rfd search 'pizza'
```

### Advanced Search

Regular expressions can be used for search.

```console
$ rfd search '(coffee|starbucks)' --pages 10 --sort-by views
```

### View Posts

```console
$ rfd posts https://forums.redflagdeals.com/kobo-vs-kindle-2396227/
```

## Shell Completion

Completion can be enabled if using `bash` or `zsh`.

### bash

```console
$ echo 'eval "$(_RFD_COMPLETE=source rfd)"' >> ~/.profile
```

### zsh

```console
$ echo 'eval "$(_RFD_COMPLETE=source_zsh rfd)"' >> ~/.zshrc
```
