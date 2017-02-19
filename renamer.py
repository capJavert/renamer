import click
# encoding=utf8
import os

# !/usr/bin/python
# -*- coding: utf8 -*-
__author__ = '@capJavert'


@click.command()
@click.option('--path', '-P', default=".", help='Path to directory where files/directories you want '
                                                'renamed are located. Defaults to current directory '
                                                'if not set. ')
@click.option('--change', '-c', default="", help='Part of the file/directory name you want to replace.')
@click.option('--to', '-t', default="", help='String you want to replace --change string to.')
def main(path, change, to):
    if change == "" or to == "":
        print("You are missing --change or --to params. Use --help for more info.")
        return

    # length = len(change)
    print("Files renamed: ")
    renamed_files_counter = 0
    for filename in os.listdir(path):
        if filename.find(change, 0, len(filename)) != -1:
            renamed_files_counter += 1
            print(filename.replace(change, to))
            os.rename(path+"/"+filename, path+"/"+filename.replace(change, to))

    if renamed_files_counter == 0:
        print("No files where matched.")
main()
