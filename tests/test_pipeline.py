from pathlib import Path

from air_quality_viz.analysis.metrics import city_summary
from air_quality_viz.data.cleaner import clean_air_quality
from air_quality_viz.data.loader import load_air_quality


DATA = Path(__file__).parents[1] / "data/raw/air_quality_sample.csv"


def test_load_and_clean_pipeline():
    frame = clean_air_quality(load_air_quality(DATA))
    assert len(frame) == 9
    assert frame["date"].notna().all()
    assert set(city_summary(frame)["city"]) == {"杭州", "宁波", "绍兴"}
