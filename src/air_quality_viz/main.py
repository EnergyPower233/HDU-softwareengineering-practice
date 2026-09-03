import argparse

from air_quality_viz.config import DEFAULT_INPUT, DEFAULT_OUTPUT
from air_quality_viz.data.cleaner import clean_air_quality
from air_quality_viz.data.loader import load_air_quality
from air_quality_viz.visualization.charts import create_charts


def main() -> None:
    parser = argparse.ArgumentParser(description="城市空气质量分析与可视化")
    parser.add_argument("--input", default=DEFAULT_INPUT, help="输入 CSV 文件路径")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="图表输出目录")
    args = parser.parse_args()
    frame = clean_air_quality(load_air_quality(args.input))
    paths = create_charts(frame, args.output)
    print(f"分析完成：清洗后 {len(frame)} 条记录")
    for path in paths:
        print(f"已生成：{path}")


if __name__ == "__main__":
    main()
