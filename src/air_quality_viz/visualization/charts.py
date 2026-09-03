from __future__ import annotations

from pathlib import Path

import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from air_quality_viz.analysis.metrics import city_summary, daily_summary


def create_charts(frame: pd.DataFrame, output_dir: str | Path) -> list[Path]:
    """生成趋势图和城市对比图，返回输出文件列表。"""
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")
    paths: list[Path] = []

    trend = daily_summary(frame)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(trend["date"], trend["aqi"], marker="o", color="#2563eb")
    ax.set(title="Daily Average AQI", xlabel="Date", ylabel="AQI")
    fig.tight_layout()
    trend_path = output / "daily_aqi_trend.png"
    fig.savefig(trend_path, dpi=160)
    plt.close(fig)
    paths.append(trend_path)

    summary = city_summary(frame)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    colors = ["#1d4ed8", "#3b82f6", "#93c5fd"][: len(summary)]
    ax.bar(summary["city"], summary["aqi"], color=colors)
    ax.set(title="Average AQI by City", xlabel="City", ylabel="AQI")
    fig.tight_layout()
    city_path = output / "city_aqi_comparison.png"
    fig.savefig(city_path, dpi=160)
    plt.close(fig)
    paths.append(city_path)
    return paths
