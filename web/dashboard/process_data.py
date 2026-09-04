"""生成前端大屏使用的 data.json。"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = PROJECT_ROOT / "data" / "raw" / "kaggle-bike-demand" / "bike_data.csv"
OUTPUT_PATH = Path(__file__).with_name("data.json")


def build_dashboard_data() -> dict:
    """从 Kaggle 数据生成大屏需要的统计 JSON。"""
    frame = pd.read_csv(CSV_PATH)
    frame["datetime"] = pd.to_datetime(frame["datetime"])

    total_count = int(frame["count"].sum())
    daily_total = frame.groupby(frame["datetime"].dt.date)["count"].sum()
    registered_total = frame["registered"].sum()
    casual_total = frame["casual"].sum()
    trend = frame.assign(month=frame["datetime"].dt.to_period("M")).groupby("month")["count"].sum().reset_index()
    trend["month"] = trend["month"].astype(str)
    hourly = frame.groupby(frame["datetime"].dt.hour)["count"].mean().reset_index()
    hourly.columns = ["hour", "count"]
    hourly["hour"] = hourly["hour"].astype(str) + "点"
    seasonal = frame.groupby("season")["count"].mean().reset_index()
    seasonal["season"] = seasonal["season"].map({1: "春季", 2: "夏季", 3: "秋季", 4: "冬季"})
    scatter = frame[["temp", "count"]].sample(min(200, len(frame)), random_state=42).to_dict("records")

    return {
        "total_count": total_count,
        "avg_daily": int(daily_total.mean()),
        "max_daily": int(daily_total.max()),
        "registered_ratio": round(registered_total / (registered_total + casual_total) * 100, 1),
        "trend": trend.to_dict("records"),
        "hourly": hourly.to_dict("records"),
        "seasonal": seasonal.to_dict("records"),
        "scatter": scatter,
    }


if __name__ == "__main__":
    result = build_dashboard_data()
    OUTPUT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"data.json 已生成：{OUTPUT_PATH}")
