"""Example: load config, parse contour CSV, and plot liner contour."""
import sys
from pathlib import Path

from src.config import load_default, load_config
from src.geometry import parse_contour_csv, compute_outer_profiles
from src.visualize import plot_liner_contour


def main(config_path=None, csv_path=None):
    cfg = load_default() if config_path is None else load_config(config_path)
    cont_path = csv_path or cfg["geometry"]["contour_csv"]
    cont_path = Path(cont_path)
    if not cont_path.exists():
        print(f"Contour file not found: {cont_path}")
        return
    x, r = parse_contour_csv(str(cont_path))
    plot_liner_contour(x, r)


if __name__ == "__main__":
    cfg = None
    csvp = None
    if len(sys.argv) > 1:
        cfg = sys.argv[1]
    if len(sys.argv) > 2:
        csvp = sys.argv[2]
    main(cfg, csvp)
