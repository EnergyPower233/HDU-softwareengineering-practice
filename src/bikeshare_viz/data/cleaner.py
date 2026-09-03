import pandas as pd


def clean_bikeshare(frame: pd.DataFrame) -> pd.DataFrame:
    """规范日期、类别与租车量字段。"""
    result = frame.copy()
    result["date"] = pd.to_datetime(result["dteday"], errors="coerce")
    numeric = ["hr", "workingday", "weathersit", "temp", "hum", "windspeed", "casual", "registered", "cnt"]
    for column in numeric:
        result[column] = pd.to_numeric(result[column], errors="coerce")
    result = result.dropna(subset=["date", *numeric])
    result["user_ratio"] = result["casual"] / result["cnt"].replace(0, pd.NA)
    return result.sort_values(["date", "hr"]).reset_index(drop=True)
