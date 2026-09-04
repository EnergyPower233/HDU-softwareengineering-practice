# 五人团队分工与交付物

本项目采用“后端数据库—数据算法—前端大屏—文档质量—调研答辩”的五人协作方式。每位成员对本岗位的产物负责，并共同理解全项目的数据流、代码结构和答辩内容。

## 邹晓谦25051220：项目队长 / 后端开发与数据库

成员 1 负责项目总体推进、数据库设计与后端查询接口。具体包括：下载或整理原始 CSV 数据；使用 SQLite 在本地建立 `bike_usage` 数据表；实现数据导入、字段校验和索引创建；编写 KPI、天气统计、小时统计等查询接口，并将查询结果转换为 JSON 格式供前端使用；组织项目进度、协调各模块接口、完成最终代码整合。

交付物：`src/bikeshare_viz/database/init_db.py`、`src/bikeshare_viz/database/db_helper.py`、`src/bikeshare_viz/database/api.py`、`data/database/bike_sharing.db`。

答辩重点：说明为什么选择 SQLite、`bike_usage` 表存储哪些字段、如何导入 CSV、三个查询接口分别服务于什么业务需求。

## 侯季南25051213：数据分析与算法工程师

成员 2 负责数据清洗、预处理和指标计算。具体包括：使用 Python 的 pandas 对日期、季节、天气、温度、湿度、风速、临时用户、注册用户和总租车量等字段进行类型规范化；处理异常与缺失值；设计核心统计指标，包括总租车量、日均租车量、月度趋势、小时平均租车量、季节平均租车量、天气条件影响和用户结构；为前端图表提供清洗后的结构化数据。

交付物：`src/bikeshare_viz/data/loader.py`、`src/bikeshare_viz/data/cleaner.py`、`src/bikeshare_viz/analysis/metrics.py`、`web/dashboard/process_data.py`、`web/dashboard/data.json`。

答辩重点：说明原始数据字段含义、清洗规则、为何采用分组平均值、17:00 高峰和天气影响等结论如何得出。

## 高轩25051216：前端开发与可视化大屏搭建

成员 3 负责共享单车数据大屏页面。具体包括：使用 HTML、CSS、JavaScript 与 ECharts 完成仪表盘布局；展示总租车数、日均租车数、最高单日租车数和注册用户占比；绘制月度趋势折线图、小时租车量柱状图、季节对比图、温度与租车量散点图和用户结构饼图；完成前端读取 `data.json` 的数据接口对接，并检查图表在浏览器中的显示效果。

交付物：`web/dashboard/index.html`、`web/dashboard/data.json`、`reports/figures/` 中的静态分析图表。

答辩重点：说明大屏每个指标和图表回答什么问题、前端如何通过 `fetch('data.json')` 加载数据、为何选择 ECharts。

## 赵轩逸25051229：文档工程师与质量控制

成员 4 负责课程报告、结构化文档和代码质量检查。具体包括：根据课程报告要求整合项目背景、需求分析、系统架构、数据库设计、数据处理、运行结果和结论；检查每个模块的代码注释、命名、异常处理和测试结果；将数据来源、建库导入、查询接口测试三张过程截图插入报告对应章节；维护运行手册、项目结构图、课程要求对应说明和提交清单。

交付物：`docs/final-report.md`、`docs/system-design.md`、`docs/project-evidence.md`、`docs/operation-manual.md`、`docs/code-structure.svg`、`docs/requirement-mapping.md`。

答辩重点：说明项目如何覆盖课程的需求分析、Python 实现、团队协作、技术调研、文档质量和持续学习要求，并展示测试通过结果。

## 王浩轩25051218：前沿技术调研与演示汇报（防踩坑与答辩）

成员 5 负责新技术研学报告、项目 PPT 与答辩组织。具体包括：调研共享单车数据分析、数据大屏可视化、ECharts、Streamlit、需求预测等方向；整理不少于 5 篇参考资料并写明技术选择理由；制作项目展示 PPT，组织全员进行交叉讲解和现场问答演练；检查每位成员能否解释其他成员的代码与模块，避免答辩时只会自己的部分。

交付物：`docs/tech-research.md`、`docs/team-reading-guide.md`、答辩 PPT、演示讲稿与问答记录。

答辩重点：说明技术调研成果、后续预测与交互式大屏的扩展方向，并组织五名成员完成完整流程演示。

## 团队共同要求

五名成员都必须能够讲清楚：数据从 Kaggle/UCI 等来源如何获得；CSV 如何导入 SQLite；查询接口如何输出 KPI 和天气统计；`data.json` 如何生成；前端如何展示图表；报告中的结论、局限性与后续扩展是什么。成员之间在答辩前至少进行一次完整交叉讲解。
