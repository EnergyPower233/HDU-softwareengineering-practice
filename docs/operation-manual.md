# 项目运行与提交说明

## 环境安装

建议使用 Python 3.10 或更高版本：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## 运行分析

```bash
PYTHONPATH=src python3 -m bikeshare_viz.main
```

自定义输入和输出：

```bash
PYTHONPATH=src python3 -m bikeshare_viz.main \
  --input data/raw/uci-bike-sharing/hour.csv \
  --output reports/figures
```

## 运行测试

```bash
PYTHONPATH=src python3 -m pytest -q
```

## 数据库与查询接口

创建 SQLite 数据库并导入 Kaggle 整理数据：

```bash
PYTHONPATH=src python3 -m bikeshare_viz.database.init_db
```

运行 KPI 与天气查询接口测试：

```bash
PYTHONPATH=src python3 -m bikeshare_viz.database.db_helper
```

启动本地 JSON API：

```bash
PYTHONPATH=src python3 -m bikeshare_viz.database.api
```

浏览器访问 `http://127.0.0.1:8000/api/kpi`、`/api/weather` 或 `/api/hourly` 查看返回数据。

## 前端数据大屏

重新生成大屏数据：

```bash
python3 web/dashboard/process_data.py
```

进入 `web/dashboard/` 后启动本地静态服务器，再访问浏览器：

```bash
cd web/dashboard
python3 -m http.server 8080
```

打开 `http://127.0.0.1:8080`。不能直接双击 `index.html`，否则浏览器可能阻止 `fetch('data.json')` 读取本地 JSON。

## 提交清单

- [ ] `src/` 源代码
- [ ] `tests/` 测试代码
- [ ] `data/raw/uci-bike-sharing/hour.csv`
- [ ] `data/raw/uci-bike-sharing/day.csv`
- [ ] `data/raw/uci-bike-sharing/Readme.txt`
- [ ] `reports/figures/` 图表
- [ ] `docs/final-report.md` 实验报告
- [ ] `docs/system-design.md` 系统设计
- [ ] `docs/team-plan.md` 团队分工
- [ ] `README.md` 项目说明
- [ ] `pyproject.toml` 依赖配置

## 演示顺序

1. 介绍问题背景和数据来源。
2. 展示项目结构和代码结构图。
3. 执行主程序，展示三张图表。
4. 解释高峰时段、用户结构和天气影响。
5. 执行测试，说明项目可复现。
6. 介绍局限性和后续需求预测扩展。
