# Renamer
[![Build Status](https://travis-ci.org/capJavert/renamer.svg?branch=master)](https://travis-ci.org/capJavert/renamer)
## Simple shell tool for file renaming written in python
### Install
You will need pip tool for python to install renamer into your shell environment.

Tool is compatible with python v3.3+

$ git clone https://github.com/capJavert/renamer.git

$ cd renamer

$ pip install --editable .

After install you can use script as:

$ renamer --change=fizz --to=buzz
### Usage
Usage: renamer [OPTIONS]

Options:

  --path TEXT    - Path to directory where files/directories you want renamed are located. Defaults to current directory if not set.
  
  --change TEXT  - Part of the file/directory name you want to replace.
  
  --to TEXT      - String you want to replace --change string to.
  
  --help         - Show help.
