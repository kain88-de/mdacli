import click
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import os
import MDAnalysis as mda
from MDAnalysis.analysis import rms


from .cli import cli

@cli.command()
@click.option('--top', help='topology', type=str)
@click.option('--trj', help='trajectory (optional)', default=None, type=str)
@click.option('--sel', help='selection to act on', default='protein', type=str,
              show_default=True)
@click.option('--ref', help='reference structure (optional)', default=None, type=str)
@click.option('--out', help='output')
def rmsd(top, trj, sel, out, ref):
    """rmsd against ref frame (first if none provided)"""
    u = mda.Universe(top, trj)
    if ref is None:
        ref = mda.Universe(top, trj)
    else:
        ref = mda.Universe(ref)

    rmsd = rms.RMSD(u, ref, select=sel, verbose=True).run()

    if os.path.splitext(os.path.basename(out))[-1] == '':
        out = out + '.png'

    f = Figure()
    FigureCanvas(f)
    ax = f.add_subplot(111)
    ax.plot(rmsd.rmsd[:, 0], rmsd.rmsd[:, 2])
    ax.set(ylabel=r'rmsd $\AA$', xlabel='frame')

    f.tight_layout()
    f.savefig(out)
