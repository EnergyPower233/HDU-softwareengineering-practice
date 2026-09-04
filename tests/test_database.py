from bikeshare_viz.database.db_helper import get_hourly_stat, get_kpi_summary, get_weather_stat
from bikeshare_viz.database.init_db import build_database


def test_database_import_and_queries(tmp_path):
    database = build_database(db_path=tmp_path / "bike_sharing.db")
    kpi = get_kpi_summary(database)
    weather = get_weather_stat(database)
    hourly = get_hourly_stat(database)

    assert kpi["total_rides"] == 2085476
    assert kpi["total_registered"] + kpi["total_casual"] == kpi["total_rides"]
    assert len(weather) == 4
    assert len(hourly) == 24
