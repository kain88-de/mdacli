import click
import MDAnalysis as mda

from .cli import cli

@cli.command()
@click.option('--top', help='topology', type=str)
@click.option('--trj', help='trajectory (optional)', default=None, type=str)
@click.option('--sel', help='selection to act on', default='all', type=str,
        show_default=True)
@click.option('--out', help='output')
def trjconv(top, trj, sel, out):
    if trj is None:
        u = mda.Universe(top)
    else:
        u = mda.Universe(top, trj)

    atoms = u.select_atoms(sel)

    click.echo('write new file {} with {} atoms'.format(out, atoms.n_atoms))
    with mda.Writer(out) as w:
        w.write(atoms)
