from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from bikeshare_viz.analysis.metrics import hourly_summary, weather_summary


def create_charts(frame: pd.DataFrame, output_dir: str | Path) -> list[Path]:
    """生成小时、用户类型、天气影响三张图。"""
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    plt.style.use("ggplot")
    paths: list[Path] = []

    hourly = hourly_summary(frame)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(hourly["hr"], hourly["rides"], marker="o", color="#2563eb")
    ax.set(title="Average Bike Rentals by Hour", xlabel="Hour", ylabel="Average Rentals")
    fig.tight_layout()
    path = output / "rentals_by_hour.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    paths.append(path)

    users = frame[["casual", "registered"]].mean()
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(["Casual users", "Registered users"], users.values, color=["#60a5fa", "#1d4ed8"])
    ax.set(title="Average Rentals by User Type", xlabel="User Type", ylabel="Average Rentals")
    fig.tight_layout()
    path = output / "rentals_by_user_type.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    paths.append(path)

    weather = weather_summary(frame)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    labels = ["Clear", "Mist", "Light rain/snow", "Heavy rain/snow"]
    ax.bar(weather["weathersit"].astype(str), weather["rides"], color="#0ea5e9")
    ax.set(title="Average Rentals by Weather", xlabel="Weather Code", ylabel="Average Rentals")
    ax.set_xticks(weather["weathersit"], [labels[int(v) - 1] for v in weather["weathersit"]])
    fig.tight_layout()
    path = output / "rentals_by_weather.png"
    fig.savefig(path, dpi=160)
    plt.close(fig)
    paths.append(path)
    return paths
