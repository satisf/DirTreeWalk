import click
import os
import hashlib


@click.command()
@click.argument('path')
def cli(path):
    """Simple tool that recursively lists a directory with the MD5 Hashes of the files"""
    walk(path)


def walk(path):
    absolute_path = os.path.abspath(path)
    with os.scandir(absolute_path) as it:
        for entry in it:
            if os.path.isdir(entry):
                walk(entry.path)
            if os.path.isfile(entry):
                click.echo(entry.path)