from pathlib import Path

from bikeshare_viz.analysis.metrics import hourly_summary
from bikeshare_viz.data.cleaner import clean_bikeshare
from bikeshare_viz.data.loader import load_bikeshare


DATA = Path(__file__).parents[1] / "data/raw/uci-bike-sharing/hour.csv"


def test_uci_dataset_pipeline():
    frame = clean_bikeshare(load_bikeshare(DATA))
    assert len(frame) == 17379
    assert frame["cnt"].sum() > 0
    assert len(hourly_summary(frame)) == 24
