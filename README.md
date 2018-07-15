# RFD CLI

Hot Deals on the command line.

[![Build Status](https://travis-ci.org/davegallant/rfd_cli.svg?branch=master)](https://travis-ci.org/davegallant/rfd_cli)

[![PyPI version](https://badge.fury.io/py/rfd.svg)](https://badge.fury.io/py/rfd)

## Installation

```bash
pip install rfd
```

## Usage

![rfd_peek](https://user-images.githubusercontent.com/4519234/42729829-b75dccae-87b2-11e8-8509-593effcecd25.gif)

```bash
rfd threads <topic-id> [--count 10]
```

### tail a post

```bash
▶ rfd posts https://forums.redflagdeals.com/koodo-targeted-public-mobile-12-120-koodo-6gb-40-no-referrals-2176935/ --tail 4
```

## Tab Completion

### bash

```bash
echo 'eval "$(_RFD_COMPLETE=source rfd)"' >> ~/.profile
```

### zsh

There isn't native support for zsh but zsh's bash completion compatibility mode works:

```zsh
echo 'autoload bashcompinit \
bashcompinit \
eval "$(_FOO_BAR_COMPLETE=source foo-bar)"' >> ~/.zshrc
```
