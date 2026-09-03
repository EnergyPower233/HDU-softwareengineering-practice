from __future__ import annotations

from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {"instant", "dteday", "hr", "workingday", "weathersit", "casual", "registered", "cnt"}


def load_bikeshare(path: str | Path) -> pd.DataFrame:
    """读取 UCI Bike Sharing CSV 并校验字段。"""
    frame = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"缺少必需字段: {', '.join(sorted(missing))}")
    return frame
