import pandas as pd


def hourly_summary(frame: pd.DataFrame) -> pd.DataFrame:
    """按小时统计骑行量。"""
    return frame.assign(hour=frame["started_at"].dt.hour).groupby("hour", as_index=False).size().rename(columns={"size": "rides"})


def station_summary(frame: pd.DataFrame) -> pd.DataFrame:
    """统计热门起点站。"""
    return frame.groupby("start_station", as_index=False).size().rename(columns={"size": "rides"}).sort_values("rides", ascending=False)
