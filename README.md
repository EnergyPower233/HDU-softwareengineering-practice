# 城市空气质量数据分析与可视化

《软件开发实践1》“数据分析与可视化”方向 Skeleton。项目以 Python、NumPy、pandas、matplotlib、seaborn 为基础，演示从数据读取、清洗、统计分析到图表输出的完整流程。

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -e ".[dev]"
python -m air_quality_viz.main --input data/raw/air_quality_sample.csv --output reports/figures
pytest
```

运行后会在 `reports/figures/` 生成趋势图和城市对比图。

## 项目结构

```text
.
├── data/raw/                    # 原始数据（示例数据已提供）
├── data/processed/              # 清洗后的中间数据
├── docs/                        # 需求、方案、调研与实验报告
├── notebooks/                   # 探索性分析 Notebook
├── reports/figures/             # 运行生成的图表
├── src/air_quality_viz/
│   ├── config.py                # 路径与默认参数
│   ├── main.py                  # CLI 入口
│   ├── data/loader.py           # 数据读取与校验
│   ├── data/cleaner.py          # 数据清洗
│   ├── analysis/metrics.py      # 指标与统计分析
│   └── visualization/charts.py  # 图表生成
└── tests/                       # 单元测试
```

完整结构图见 [`docs/code-structure.mmd`](docs/code-structure.mmd)。

## 与大纲要求的对应

- 目标 1：`docs/requirements.md`、`analysis/metrics.py` 体现需求分析与模块设计。
- 目标 2：使用 pandas、NumPy、matplotlib、seaborn 完成功能实现。
- 目标 3/4：预留团队分工、代码评审和演示记录位置。
- 目标 5：`docs/` 目录包含技术调研、方案设计、实验报告模板。
- 目标 6：`docs/tech-research.md` 记录数据分析工具与可视化技术调研。

## 后续可扩展

可接入真实公开数据源、增加 Streamlit 页面、加入异常检测/预测模型，并补充数据库或缓存层。当前 Skeleton 刻意保持离线可运行，便于课程验收与复现。
