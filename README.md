# RFD

Hot deals on the command line.

[![Build Status](https://travis-ci.org/davegallant/rfd.svg?branch=master)](https://travis-ci.org/davegallant/rfd)

[![PyPI version](https://badge.fury.io/py/rfd.svg)](https://badge.fury.io/py/rfd)

## Installation

```bash
pip install rfd
```

## Usage

![rfd_peek](https://user-images.githubusercontent.com/4519234/42729852-d43a7768-87b3-11e8-81f2-36cb81bf4b58.gif)

```bash
rfd threads <topic-id> [--limit 10]
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
eval "$(_RFD_COMPLETE=source rfd)"' >> ~/.zshrc
```
