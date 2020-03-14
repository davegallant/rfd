# RFD

Hot deals on the command line.

[![Build Status](https://travis-ci.org/davegallant/rfd.svg?branch=master)](https://travis-ci.org/davegallant/rfd)
[![PyPI version](https://badge.fury.io/py/rfd.svg)](https://badge.fury.io/py/rfd)
[![Dependabot](https://badgen.net/badge/Dependabot/enabled/green?icon=dependabot)](https://dependabot.com/)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/davegallant/rfd.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/davegallant/rfd/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/davegallant/rfd.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/davegallant/rfd/context:python)


![screenshot](https://user-images.githubusercontent.com/4519234/76671943-c9d24f80-656f-11ea-872e-85897add37db.png)

## Install

```bash
pip install rfd
```

## Use

### view threads
```bash
rfd threads [--forum-id 9] [--limit 10]
```

### search
```bash
rfd search pizza [--num-pages 100]
```

## Support Tab Completion

### bash

```bash
echo 'eval "$(_RFD_COMPLETE=source rfd)"' >> ~/.profile
```

### zsh


```zsh
echo 'eval "$(_RFD_COMPLETE=source_zsh rfd)"' >> ~/.zshrc
```
