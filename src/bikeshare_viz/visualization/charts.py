from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from bikeshare_viz.analysis.metrics import hourly_summary, station_summary


def create_charts(frame: pd.DataFrame, output_dir: str | Path) -> list[Path]:
    """生成时段、用户类型和热门站点图。"""
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    plt.style.use("ggplot")
    paths: list[Path] = []

    hourly = hourly_summary(frame)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(hourly["hour"], hourly["rides"], marker="o", color="#2563eb")
    ax.set(title="Rides by Start Hour", xlabel="Hour", ylabel="Rides")
    fig.tight_layout()
    path = output / "rides_by_hour.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    paths.append(path)

    users = frame.groupby("user_type").size().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(users.index, users.values, color=["#1d4ed8", "#93c5fd"][: len(users)])
    ax.set(title="Rides by User Type", xlabel="User Type", ylabel="Rides")
    fig.tight_layout()
    path = output / "rides_by_user_type.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    paths.append(path)

    stations = station_summary(frame).head(5).sort_values("rides")
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.barh(stations["start_station"], stations["rides"], color="#3b82f6")
    ax.set(title="Top 5 Start Stations", xlabel="Rides", ylabel="Station")
    fig.tight_layout()
    path = output / "top_start_stations.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    paths.append(path)
    return paths
