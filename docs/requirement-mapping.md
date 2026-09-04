# 大纲要求体现说明

## 1 课程目标对应

| 大纲要求 | 本项目中的具体体现 |
| --- | --- |
| 需求分析与系统设计 | `requirements.md` 明确用户、场景、功能和非功能需求；`system-design.md` 说明模块、接口和异常处理。 |
| Python 实现与第三方库 | `pyproject.toml` 配置 Python、pandas、NumPy、matplotlib 和 pytest；`src/` 给出完整实现。 |
| 团队合作 | `team-plan.md` 将五人分为后端数据库、数据分析、前端大屏、文档质量、调研答辩五个角色，并列出每项成果。 |
| 沟通与协作 | `team-plan.md` 规定共同需求评审、代码讲解、阶段汇报和最终答辩；`operation-manual.md` 统一复现步骤。 |
| 技术与非技术文档 | `final-report.md`、`system-design.md`、`tech-research.md`、`operation-manual.md` 和 `README.md` 构成完整文档体系。 |
| 前沿技术与持续学习 | `tech-research.md` 讨论 pandas、matplotlib、Streamlit、需求预测和数据集许可；报告中列出扩展路线。 |
| 思政元素 | 报告将数据真实性、可复现性、团队责任、规范引用和服务城市交通运营写入项目实施与质量要求。 |

## 2 教学内容对应

| 教学内容 | 项目文件 |
| --- | --- |
| Python 开发工具 | `pyproject.toml`、命令行入口 `main.py` |
| Python 基础语法 | 函数、模块、异常、路径和列表等基础实现 |
| NumPy/pandas/matplotlib | `cleaner.py`、`metrics.py`、`charts.py` |
| Python 综合项目 | 真实数据、需求分析、系统设计、图表输出、测试和报告 |

## 3 评分材料对应

| 评分项目 | 可检查证据 |
| --- | --- |
| 新技术研学 | UCI 数据集调研、工具选型、Streamlit 和预测扩展 |
| 实践作品 | 可运行源码、真实数据、三张图表和测试 |
| 源码质量 | 模块化目录、函数文档字符串、字段校验、异常处理 |
| 文档质量 | 完整实验报告、数据字典、系统设计、运行手册和参考文献 |
| 团队表现 | 五人分工、共同工作要求和个人贡献表 |

## 4 提交时如何填写

封面或学校模板只需填写课程名称、项目名称、五位成员姓名和学号、指导教师、日期。报告正文使用 `final-report.md`；把 `reports/figures/` 中的三张图插入“可视化结果”章节；把 `code-structure.svg` 插入“系统设计”章节；把 `team-plan.md` 中的五人分工放入“团队分工”章节。姓名和学号必须使用真实信息，个人贡献只能填写实际完成内容。
