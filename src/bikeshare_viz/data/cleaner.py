import pandas as pd


def clean_bikeshare(frame: pd.DataFrame) -> pd.DataFrame:
    """规范时间字段，计算骑行时长并去除异常记录。"""
    result = frame.copy()
    result["started_at"] = pd.to_datetime(result["started_at"], errors="coerce")
    result["ended_at"] = pd.to_datetime(result["ended_at"], errors="coerce")
    result["duration_min"] = (result["ended_at"] - result["started_at"]).dt.total_seconds() / 60
    result = result.dropna(subset=["ride_id", "started_at", "ended_at", "start_station", "end_station", "user_type"])
    result = result[(result["duration_min"] > 0) & (result["duration_min"] <= 180)]
    return result.sort_values("started_at").reset_index(drop=True)
