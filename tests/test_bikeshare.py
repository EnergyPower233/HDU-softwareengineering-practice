from pathlib import Path

from bikeshare_viz.analysis.metrics import station_summary
from bikeshare_viz.data.cleaner import clean_bikeshare
from bikeshare_viz.data.loader import load_bikeshare


DATA = Path(__file__).parents[1] / "data/raw/bikeshare_sample.csv"


def test_load_and_clean_pipeline():
    frame = clean_bikeshare(load_bikeshare(DATA))
    assert len(frame) == 12
    assert (frame["duration_min"] > 0).all()
    assert station_summary(frame).iloc[0]["start_station"] == "西湖东门"
