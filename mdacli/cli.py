import click

@click.group()
@click.version_option()
def cli():
    """Generate and run mdbenchmark jobs for GROMACS simulations"""
    pass
