# RFD

Hot deals on the command line.

[![Build Status](https://travis-ci.org/davegallant/rfd.svg?branch=master)](https://travis-ci.org/davegallant/rfd)
[![PyPI version](https://badge.fury.io/py/rfd.svg)](https://badge.fury.io/py/rfd)
[![Dependabot](https://badgen.net/badge/Dependabot/enabled/green?icon=dependabot)](https://dependabot.com/)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/davegallant/rfd.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/davegallant/rfd/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/davegallant/rfd.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/davegallant/rfd/context:python)


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

### view hot deals
```shell
rfd threads
```

### search for pizza
```shell
rfd search 'pizza'
```

## Tab Completion

To enable:

### bash

```bash
echo 'eval "$(_RFD_COMPLETE=source rfd)"' >> ~/.profile
```

### zsh


```zsh
echo 'eval "$(_RFD_COMPLETE=source_zsh rfd)"' >> ~/.zshrc
```
