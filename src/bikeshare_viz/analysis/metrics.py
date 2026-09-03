import pandas as pd


def hourly_summary(frame: pd.DataFrame) -> pd.DataFrame:
    """按小时统计平均租车量。"""
    return frame.groupby("hr", as_index=False)["cnt"].mean().rename(columns={"cnt": "rides"})


def weather_summary(frame: pd.DataFrame) -> pd.DataFrame:
    """按天气情况统计平均租车量。"""
    return frame.groupby("weathersit", as_index=False)["cnt"].mean().rename(columns={"cnt": "rides"})
