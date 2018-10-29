# RFD

Hot deals on the command line.

[![Build Status](https://travis-ci.org/davegallant/rfd.svg?branch=master)](https://travis-ci.org/davegallant/rfd)
[![PyPI version](https://badge.fury.io/py/rfd.svg)](https://badge.fury.io/py/rfd)

## Installation

```bash
pip install rfd
```

## Usage

![rfd_demo_gif](https://user-images.githubusercontent.com/4519234/47625817-d3375500-dafd-11e8-9d86-491d4a4fb225.gif)


```bash
rfd threads <topic-id> [--limit 10]
```

## Tab Completion

### bash

```bash
echo 'eval "$(_RFD_COMPLETE=source rfd)"' >> ~/.profile
```

### zsh


```zsh
echo 'eval "$(_RFD_COMPLETE=source_zsh rfd)"' >> ~/.zshrc
```
