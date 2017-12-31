import click
import MDAnalysis as mda
import numpy as np
import os.path
import sys

from .cli import cli


@cli.command()
@click.option('--top', help='topology', type=str)
@click.option('--trj', help='trajectory (optional)', default=None, type=str)
@click.option(
    '--sel',
    help='selection to act on',
    default='all',
    type=str,
    show_default=True)
@click.option('--out', help='output')
@click.option(
    '--randomframes',
    type=int,
    default=0,
    help='select x random frames from trajectory')
def trjconv(top, trj, sel, out, randomframes):
    """convert topology formats only for now.
    """
    if trj is None:
        u = mda.Universe(top)
    else:
        u = mda.Universe(top, trj)

    atoms = u.select_atoms(sel)

    if randomframes == 0:
        click.echo(
            'write new file {} with {} atoms'.format(out, atoms.n_atoms))
        with mda.Writer(out) as w:
            w.write(atoms)
    else:
        if trj is None:
            click.echo("Oh no please give me a trajectory")
            sys.exit(1)
        nframes = u.trajectory.n_frames
        frames = np.random.choice(np.arange(nframes), size=randomframes)
        fname, ext = os.path.splitext(out)
        click.echo("Using frames: {}".format(frames))
        for i, f in enumerate(frames):
            u.trajectory[f]
            with mda.Writer(
                    "{}_{}.{}".format(fname, i, ext),
                    atoms=u.atoms.n_atoms) as w:
                w.write(atoms)
