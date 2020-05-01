import click
import os
import hashlib


@click.command()
@click.argument('path')
def cli(path):
    """Simple tool that recursively lists a directory with the MD5 Hashes of the files"""
    walk(path)


def walk(path):
    try:
        with os.scandir(path) as it:
            for entry in it:
                if os.path.isdir(entry):
                    click.echo("{:30.30}  {:60}".format(entry.name, "<dir>"))
                    walk(entry.path)
                if os.path.isfile(entry):
                    click.echo("{:30.30}  {:60.60}  {:10}".format(entry.name, entry.path, md5(entry.path)))
    except OSError as error:
        click.echo(error)


def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()