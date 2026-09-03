# 项目代码结构阅读指南

```text
真实数据 hour.csv
        │
        ▼
 data/loader.py       读取并检查字段
        │
        ▼
 data/cleaner.py      日期、数值转换和清洗
        │
        ▼
 analysis/metrics.py   计算小时和天气指标
        │
        ▼
 visualization/charts.py 生成三张 PNG 图
        │
        ▼
 reports/figures/      报告插图
```

`main.py` 是总入口，负责把上述模块按顺序串起来；`config.py` 保存默认数据路径；`tests/` 对关键流程进行验证。

答辩时先展示 `main.py`，再依次讲解 `loader.py`、`cleaner.py`、`metrics.py` 和 `charts.py`，最后展示图表和测试结果。
