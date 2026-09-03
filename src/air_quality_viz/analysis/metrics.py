import pandas as pd


def city_summary(frame: pd.DataFrame) -> pd.DataFrame:
    """按城市汇总平均 AQI 与污染物指标。"""
    return (
        frame.groupby("city", as_index=False)[["aqi", "pm25", "pm10", "no2"]]
        .mean()
        .sort_values("aqi", ascending=False)
        .reset_index(drop=True)
    )


def daily_summary(frame: pd.DataFrame) -> pd.DataFrame:
    """按日期计算整体平均 AQI。"""
    return frame.groupby("date", as_index=False)["aqi"].mean()
