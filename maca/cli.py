import click

settings = dict(help_option_names=['-h', '--help'])
from .make_zipped_csvs import clean_and_zip

@click.group(options_metavar='', subcommand_metavar='<command>', context_settings=settings)
def cli():
    """
    Hi! This is a small command line utility to work with outputs from RNA-sequencing data
    """
    pass


cli.add_command(clean_and_zip)

if __name__ == '__main__':
    cli()
