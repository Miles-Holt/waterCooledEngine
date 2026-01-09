import yaml
from pathlib import Path


class ConfigError(Exception):
    pass


def load_config(path: str):
    p = Path(path)
    if not p.exists():
        raise ConfigError(f"Config file not found: {path}")
    with p.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    # Basic validation
    if "geometry" not in cfg or "contour_csv" not in cfg["geometry"]:
        raise ConfigError("Config must contain geometry.contour_csv")
    return cfg


def load_default():
    here = Path(__file__).resolve().parent.parent
    default = here / "configs" / "default.yaml"
    return load_config(str(default))
