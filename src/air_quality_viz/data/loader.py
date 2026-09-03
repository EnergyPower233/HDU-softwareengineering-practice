from __future__ import annotations

from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {"date", "city", "pm25", "pm10", "no2", "aqi"}


def load_air_quality(path: str | Path) -> pd.DataFrame:
    """读取 CSV 并校验字段，返回原始 DataFrame。"""
    frame = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"缺少必需字段: {', '.join(sorted(missing))}")
    return frame
