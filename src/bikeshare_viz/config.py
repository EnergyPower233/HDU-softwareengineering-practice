from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "raw" / "uci-bike-sharing" / "hour.csv"
DEFAULT_OUTPUT = PROJECT_ROOT / "reports" / "figures"
