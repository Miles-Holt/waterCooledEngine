import matplotlib.pyplot as plt
from typing import Sequence


def plot_liner_contour(x: Sequence[float], r: Sequence[float], show=True, save_path=None):
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(x, r, "-k", label="liner inner radius")
    ax.set_xlabel("Axial position (m)")
    ax.set_ylabel("Radius (m)")
    ax.set_title("Liner inner contour")
    ax.grid(True)
    ax.legend()
    if save_path:
        fig.savefig(save_path, dpi=200)
    if show:
        plt.show()
    return fig, ax
