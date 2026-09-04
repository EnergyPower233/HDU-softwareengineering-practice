# 城市共享单车出行数据分析与可视化

《软件开发实践1》“数据分析与可视化”方向课程项目。项目包含 Python 数据清洗与统计分析、SQLite 建库与查询接口、ECharts 数据大屏和完整项目文档。

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -e ".[dev]"
python -m bikeshare_viz.main
pytest
```

运行后会在 `reports/figures/` 生成小时租车量、用户类型和天气影响图。

数据库和前端大屏运行方式见 [`docs/operation-manual.md`](docs/operation-manual.md)。

## 项目结构

```text
.
├── data/raw/                    # UCI 真实数据
├── data/database/               # SQLite 数据库文件
├── data/processed/              # 清洗后的中间数据
├── docs/                        # 需求、方案、调研与实验报告
├── notebooks/                   # 探索性分析 Notebook
├── reports/figures/             # 运行生成的图表
├── web/dashboard/               # ECharts 共享单车数据大屏
├── src/bikeshare_viz/
│   ├── config.py                # 路径与默认参数
│   ├── main.py                  # CLI 入口
│   ├── data/loader.py           # 数据读取与校验
│   ├── data/cleaner.py          # 数据清洗
│   ├── analysis/metrics.py      # 指标与统计分析
│   └── visualization/charts.py  # 图表生成
│   └── database/                # 建库、查询接口与本地 JSON API
└── tests/                       # 单元测试
```

完整结构图见 [`docs/code-structure.svg`](docs/code-structure.svg)、[`docs/code-structure.mmd`](docs/code-structure.mmd) 和 [`docs/code-structure.md`](docs/code-structure.md)。组员共同阅读手册见 [`docs/team-reading-guide.md`](docs/team-reading-guide.md)。完整实验报告见 [`docs/final-report.md`](docs/final-report.md)。前端入口为 [`web/dashboard/index.html`](web/dashboard/index.html)。

答辩演示讲稿见 [`docs/presentation-script.md`](docs/presentation-script.md)。

## 与大纲要求的对应

- 目标 1：`docs/requirements.md`、`analysis/metrics.py` 体现需求分析与模块设计。
- 目标 2：使用 pandas、NumPy、matplotlib 完成功能实现。
- 目标 3/4：预留团队分工、代码评审和演示记录位置。
- 目标 5：`docs/` 目录包含技术调研、方案设计、实验报告和答辩阅读手册。
- 目标 6：`docs/tech-research.md` 记录数据分析工具与可视化技术调研。

## 后续可扩展

当前项目已接入 UCI Bike Sharing 真实数据集；后续可增加 Streamlit 页面、需求预测、天气影响建模和交互式地图。项目保留离线运行方式，便于课程验收与复现。
