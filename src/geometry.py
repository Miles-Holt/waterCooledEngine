import numpy as np
from pathlib import Path
from typing import Tuple


def parse_contour_csv(path: str) -> Tuple[np.ndarray, np.ndarray]:
    """Parse a CSV contour file with two columns: x (mm), radius (mm).

    The file may contain header/comment lines starting with '#'.
    Returns arrays in meters: (x, r).
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Contour file not found: {path}")

    xs = []
    rs = []
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            parts = s.split(",") if "," in s else s.split()
            if len(parts) < 2:
                continue
            try:
                x_mm = float(parts[0])
                r_mm = float(parts[1])
            except ValueError:
                continue
            xs.append(x_mm / 1000.0)
            rs.append(r_mm / 1000.0)

    if not xs:
        raise ValueError("No data points parsed from contour file")

    x = np.array(xs)
    r = np.array(rs)
    # Ensure sorted by x
    order = np.argsort(x)
    return x[order], r[order]


def compute_outer_profiles(x: np.ndarray, r_inner: np.ndarray, config: dict) -> Tuple[np.ndarray, np.ndarray]:
    """Compute derived geometry arrays (e.g., outer radius of liner and jacket).

    Currently assumes constant liner thickness and jacket thickness from config (in meters).
    Returns (r_liner_outer, r_jacket_outer).
    """
    t_liner = config.get("geometry_params", {}).get("liner_thickness", 0.002)
    t_jacket = config.get("geometry_params", {}).get("jacket_thickness", 0.005)
    r_liner_outer = r_inner + t_liner
    r_jacket_outer = r_liner_outer + config.get("geometry_params", {}).get("gap_thickness_axial", [0.005])[0] + t_jacket
    return r_liner_outer, r_jacket_outer
