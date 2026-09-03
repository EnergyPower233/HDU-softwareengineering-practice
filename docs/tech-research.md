# 新技术研学报告

## 1 pandas 分组聚合

本项目使用 `groupby` 对小时和天气编码分组，再计算平均租车量。选择 pandas 的原因是接口清晰、适合表格数据，并能与 CSV 和 matplotlib 直接衔接。

## 2 matplotlib 可视化

项目使用折线图展示小时变化，柱状图展示用户结构和天气差异。图表包含标题、坐标轴标签和统一颜色，避免只展示代码而缺少结果解释。

## 3 UCI Bike Sharing 数据集

官方数据集包含 2011—2012 年小时和日租车量、天气、季节、工作日、临时用户和注册用户字段。项目使用 `hour.csv`，因为小时粒度更适合发现高峰时段。

## 4 Streamlit 扩展方案

后续可以把现有 `loader`、`cleaner` 和 `metrics` 函数接入 Streamlit 页面，通过下拉框选择月份、小时和天气条件，实现交互式筛选。当前版本不引入该依赖，以保证基础项目安装简单、离线可运行。

## 5 需求预测扩展方案

可以将 `cnt` 作为目标变量，将小时、季节、工作日、天气、温度和湿度作为特征，训练随机森林或梯度提升模型，并用 MAE、RMSE 和 R² 评价。预测模块应作为独立的 `models/` 包，避免影响当前描述性分析。

## 6 参考资料

1. UCI Machine Learning Repository, Bike Sharing Dataset，https://archive.ics.uci.edu/dataset/275/bike%2Bsharing%2Bdataset
2. Python Documentation，https://docs.python.org/3/
3. pandas Documentation，https://pandas.pydata.org/docs/
4. Matplotlib Documentation，https://matplotlib.org/stable/
5. pytest Documentation，https://docs.pytest.org/
