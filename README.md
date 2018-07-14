# RFD CLI

Hot Deals on the command line.

[![Build Status](https://travis-ci.org/davegallant/rfd_cli.svg?branch=master)](https://travis-ci.org/davegallant/rfd_cli)

[![PyPI version](https://badge.fury.io/py/rfd.svg)](https://badge.fury.io/py/rfd)

## Installation

```bash
pip install rfd
```

## Usage

```bash
rfd threads <topic-id> [--count 10]
```

### Display first 5 threads from hot deals

![screenshot](https://user-images.githubusercontent.com/4519234/37319853-3a03fb9c-2647-11e8-806e-17156541cf43.png)

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
