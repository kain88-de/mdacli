import click
import panedr
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import os

from .cli import cli


@cli.command()
@click.option('--edr', help='energy file', type=str)
@click.option('--col', help='columnname', type=str)
@click.option('--out', help='output name', type=str)
def edr(edr, col, out):
    """
    plot timeseries of field in a edr file
    """
    edr = panedr.edr_to_df(edr)
    series = edr[col]

    if os.path.splitext(os.path.basename(out))[-1] == '':
        out = out + '.png'

    f = Figure()
    FigureCanvas(f)
    ax = f.add_subplot(111)
    ax.set(ylabel=col, xlabel='frame')

    series.plot(ax=ax)

    f.tight_layout()
    f.savefig(out)

