"""面向大屏和答辩演示的 SQLite 查询接口。"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

from bikeshare_viz.database.init_db import DATABASE_PATH


def _query(sql: str, db_path: Path = DATABASE_PATH) -> list[dict[str, Any]]:
    """执行只读查询并将结果转换为 JSON 友好的字典列表。"""
    with sqlite3.connect(db_path) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(sql).fetchall()
    return [dict(row) for row in rows]


def get_kpi_summary(db_path: Path = DATABASE_PATH) -> dict[str, Any]:
    """查询总租车量、用户构成和平均温度等核心指标。"""
    result = _query(
        """
        SELECT SUM(count) AS total_rides,
               SUM(registered) AS total_registered,
               SUM(casual) AS total_casual,
               ROUND(AVG(temp), 2) AS avg_temp
        FROM bike_usage
        """,
        db_path,
    )
    return result[0]


def get_weather_stat(db_path: Path = DATABASE_PATH) -> list[dict[str, Any]]:
    """按天气编码汇总租车量，供前端图表调用。"""
    return _query(
        """
        SELECT weather, SUM(count) AS rides
        FROM bike_usage
        GROUP BY weather
        ORDER BY weather
        """,
        db_path,
    )


def get_hourly_stat(db_path: Path = DATABASE_PATH) -> list[dict[str, Any]]:
    """按小时汇总平均租车量。"""
    return _query(
        """
        SELECT CAST(strftime('%H', datetime) AS INTEGER) AS hour,
               ROUND(AVG(count), 2) AS avg_rides
        FROM bike_usage
        GROUP BY hour
        ORDER BY hour
        """,
        db_path,
    )


if __name__ == "__main__":
    print("=== 测试 KPI 查询接口 ===")
    print(get_kpi_summary())
    print("\n=== 测试天气统计查询接口 ===")
    print(get_weather_stat())
