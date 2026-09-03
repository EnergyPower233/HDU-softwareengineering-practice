# 城市共享单车出行数据分析与可视化

《软件开发实践1》“数据分析与可视化”方向 Skeleton。项目以 Python、NumPy、pandas、matplotlib 为基础，演示从共享单车数据读取、清洗、统计分析到图表输出的完整流程。

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -e ".[dev]"
python -m bikeshare_viz.main
pytest
```

运行后会在 `reports/figures/` 生成小时租车量、用户类型和天气影响图。

## 项目结构

```text
.
├── data/raw/                    # UCI 真实数据
├── data/processed/              # 清洗后的中间数据
├── docs/                        # 需求、方案、调研与实验报告
├── notebooks/                   # 探索性分析 Notebook
├── reports/figures/             # 运行生成的图表
├── src/bikeshare_viz/
│   ├── config.py                # 路径与默认参数
│   ├── main.py                  # CLI 入口
│   ├── data/loader.py           # 数据读取与校验
│   ├── data/cleaner.py          # 数据清洗
│   ├── analysis/metrics.py      # 指标与统计分析
│   └── visualization/charts.py  # 图表生成
└── tests/                       # 单元测试
```

完整结构图见 [`docs/code-structure.svg`](docs/code-structure.svg) 和 [`docs/code-structure.mmd`](docs/code-structure.mmd)。完整实验报告见 [`docs/final-report.md`](docs/final-report.md)。

## 与大纲要求的对应

- 目标 1：`docs/requirements.md`、`analysis/metrics.py` 体现需求分析与模块设计。
- 目标 2：使用 pandas、NumPy、matplotlib 完成功能实现。
- 目标 3/4：预留团队分工、代码评审和演示记录位置。
- 目标 5：`docs/` 目录包含技术调研、方案设计、实验报告模板。
- 目标 6：`docs/tech-research.md` 记录数据分析工具与可视化技术调研。

## 后续可扩展

当前项目已接入 UCI Bike Sharing 真实数据集；后续可增加 Streamlit 页面、需求预测、天气影响建模和交互式地图。项目保留离线运行方式，便于课程验收与复现。
