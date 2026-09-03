import pandas as pd


def clean_air_quality(frame: pd.DataFrame) -> pd.DataFrame:
    """规范日期、数值字段并去除无法用于分析的记录。"""
    result = frame.copy()
    result["date"] = pd.to_datetime(result["date"], errors="coerce")
    numeric = ["pm25", "pm10", "no2", "aqi"]
    for column in numeric:
        result[column] = pd.to_numeric(result[column], errors="coerce")
    result = result.dropna(subset=["date", "city", *numeric])
    return result.sort_values(["date", "city"]).reset_index(drop=True)
