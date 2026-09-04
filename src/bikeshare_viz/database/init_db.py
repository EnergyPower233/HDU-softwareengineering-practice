"""从 Kaggle 共享单车数据创建 SQLite 数据库。"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd

from bikeshare_viz.config import PROJECT_ROOT

KAGGLE_DATA = PROJECT_ROOT / "data" / "raw" / "kaggle-bike-demand" / "bike_data.csv"
DATABASE_PATH = PROJECT_ROOT / "data" / "database" / "bike_sharing.db"


def build_database(csv_path: Path = KAGGLE_DATA, db_path: Path = DATABASE_PATH) -> Path:
    """创建 bike_usage 表并导入 Kaggle 整理后的共享单车数据。"""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.read_csv(csv_path)
    required = {
        "datetime", "season", "holiday", "workingday", "weather", "temp",
        "atemp", "humidity", "windspeed", "casual", "registered", "count",
    }
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"CSV 缺少字段: {', '.join(sorted(missing))}")

    with sqlite3.connect(db_path) as connection:
        connection.execute("DROP TABLE IF EXISTS bike_usage")
        frame.to_sql("bike_usage", connection, if_exists="replace", index=False)
        connection.execute("CREATE INDEX IF NOT EXISTS idx_bike_usage_datetime ON bike_usage(datetime)")
        connection.execute("CREATE INDEX IF NOT EXISTS idx_bike_usage_weather ON bike_usage(weather)")
    return db_path


if __name__ == "__main__":
    path = build_database()
    print("数据库搭建成功")
    print(f"数据库文件: {path}")
