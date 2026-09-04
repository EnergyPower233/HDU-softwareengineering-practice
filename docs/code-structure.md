# 项目代码结构阅读指南

```text
UCI hour.csv → loader.py → cleaner.py → metrics.py → charts.py → PNG 图表

Kaggle bike_data.csv → init_db.py → bike_sharing.db → db_helper.py → JSON API

Kaggle bike_data.csv → web/dashboard/process_data.py → data.json → index.html（ECharts 大屏）
```

`main.py` 是静态分析入口，负责把 UCI 数据分析模块按顺序串起来；`config.py` 保存默认数据路径；`tests/` 对分析和数据库模块进行验证。`web/dashboard/index.html` 是数据大屏入口。

答辩时先展示 `main.py`，再依次讲解 `loader.py`、`cleaner.py`、`metrics.py` 和 `charts.py`，最后展示图表和测试结果。
