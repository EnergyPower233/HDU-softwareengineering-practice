from __future__ import annotations

from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {"ride_id", "started_at", "ended_at", "start_station", "end_station", "user_type"}


def load_bikeshare(path: str | Path) -> pd.DataFrame:
    """读取共享单车 CSV 并校验字段。"""
    frame = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"缺少必需字段: {', '.join(sorted(missing))}")
    return frame
