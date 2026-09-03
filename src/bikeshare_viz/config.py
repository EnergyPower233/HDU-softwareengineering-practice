from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "raw" / "bikeshare_sample.csv"
DEFAULT_OUTPUT = PROJECT_ROOT / "reports" / "figures"
