import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const workspaceDir = "/Users/epower/Documents/New project";
const skillDir = "/Users/epower/.codex/plugins/cache/openai-primary-runtime/presentations/26.903.11726/skills/presentations";
const buildDir = path.join(workspaceDir, ".pptx-build");
const candidatePath = path.join(buildDir, "bike-sharing-defense-draft.pptx");
const { resolvePresentationFont, applyPresentationChartFont } = await import(
  pathToFileURL(path.join(skillDir, "container_tools/artifact_tool_utils.mjs")).href,
);
const font = resolvePresentationFont();
const deck = Presentation.create({ slideSize: { width: 1280, height: 720 } });
const navy = "#071B33";
const blue = "#0B79D0";
const cyan = "#19C1D1";
const ink = "#10243B";
const muted = "#587084";
const pale = "#EAF4FB";

function shape(slide, left, top, width, height, fill = "none", line = "none", radius = false) {
  return slide.shapes.add({
    geometry: radius ? "roundRect" : "rect",
    position: { left, top, width, height },
    fill,
    line: { fill: line, width: line === "none" ? 0 : 1 },
    ...(radius ? { borderRadius: "rounded-xl" } : {}),
  });
}
function text(slide, value, left, top, width, height, options = {}) {
  const box = slide.shapes.add({
    geometry: "textbox",
    position: { left, top, width, height },
    fill: "none",
    line: { fill: "none", width: 0 },
  });
  box.text = value;
  box.text.style = {
    typeface: font,
    fontSize: options.size ?? 20,
    color: options.color ?? ink,
    bold: options.bold ?? false,
    alignment: options.align ?? "left",
    autoFit: "shrinkText",
  };
  return box;
}
async function image(slide, file, left, top, width, height, alt, fit = "contain") {
  const blob = new Uint8Array(await fs.readFile(file));
  slide.images.add({ blob, contentType: file.endsWith(".png") ? "image/png" : "image/jpeg", alt, fit, position: { left, top, width, height }, geometry: "roundRect", borderRadius: "rounded-xl" });
}
function title(slide, main, sub = "") {
  text(slide, main, 64, 42, 900, 48, { size: 32, bold: true });
  if (sub) text(slide, sub, 66, 94, 920, 30, { size: 15, color: muted });
  shape(slide, 64, 128, 1152, 3, cyan);
}
function footer(slide, page) {
  text(slide, "共享单车租赁需求分析、数据库查询与可视化大屏", 64, 682, 900, 18, { size: 11, color: muted });
  text(slide, String(page).padStart(2, "0"), 1160, 680, 56, 18, { size: 11, color: muted, align: "right" });
}
function note(slide, content) { slide.speakerNotes.textFrame.setText(content); }
function bullet(slide, lines, left, top, width, size = 18, color = ink, gap = 45) {
  lines.forEach((line, index) => {
    shape(slide, left, top + index * gap + 10, 7, 7, cyan, "none", true);
    text(slide, line, left + 20, top + index * gap, width - 20, 34, { size, color });
  });
}

// 1 Cover
{
  const s = deck.slides.add(); s.background.fill = navy;
  shape(s, 0, 0, 1280, 720, navy);
  shape(s, 820, 0, 460, 720, "#0D3157");
  shape(s, 850, 95, 290, 290, "#0C4E7A", "none", true);
  shape(s, 920, 165, 150, 150, cyan, "none", true);
  text(s, "共享单车租赁需求分析", 74, 174, 690, 72, { size: 44, bold: true, color: "#FFFFFF" });
  text(s, "数据库查询与可视化大屏系统", 76, 256, 680, 42, { size: 27, color: "#B8D9F1" });
  shape(s, 76, 334, 210, 4, cyan);
  text(s, "软件开发实践 1 · 数据分析与可视化方向", 76, 370, 650, 28, { size: 18, color: "#D5E5F1" });
  text(s, "五人课程项目答辩", 76, 455, 360, 25, { size: 16, color: "#B8D9F1" });
  text(s, "数据来源：UCI Bike Sharing Dataset / Kaggle Bike Sharing Demand", 76, 505, 650, 20, { size: 13, color: "#8AB4D4" });
  note(s, "封面。演讲者：成员 1。数据来源见项目数据说明与报告。" );
}

// 2 Problem and scope
{
  const s = deck.slides.add(); s.background.fill = "#FFFFFF"; title(s, "项目问题与交付范围", "从共享单车需求数据到数据库查询与前端展示");
  text(s, "我们希望回答的运营问题", 72, 174, 500, 32, { size: 23, bold: true });
  bullet(s, ["一天中哪些时段租车需求最高", "天气变化会带来怎样的租车量差异", "注册用户和临时用户的使用结构如何"], 80, 226, 520, 19, ink, 58);
  shape(s, 670, 160, 500, 420, pale, "#CDE0EE", true);
  text(s, "项目交付", 710, 195, 230, 28, { size: 23, bold: true, color: blue });
  bullet(s, ["Python 数据清洗与统计分析", "SQLite 建库、导入与查询接口", "ECharts 数据大屏与完整文档"], 720, 252, 400, 18, ink, 58);
  text(s, "核心思路：分析、数据库和页面分层实现，便于测试与展示", 72, 570, 1080, 36, { size: 19, color: muted }); footer(s, 2);
  note(s, "演讲者：成员 1。说明项目不是单纯画图，而是包含数据、数据库与前端三层。" );
}

// 3 Data source
{
  const s = deck.slides.add(); s.background.fill = "#FFFFFF"; title(s, "真实数据来源", "UCI 用于小时级分析，Kaggle 整理数据用于数据库与大屏");
  await image(s, path.join(workspaceDir, "docs/evidence/01-kaggle-dataset.jpg"), 650, 158, 530, 420, "Kaggle 共享单车需求数据集页面", "contain");
  text(s, "数据使用方式", 74, 175, 330, 32, { size: 24, bold: true });
  bullet(s, ["UCI hour.csv：17,379 条小时记录，用于清洗、统计和静态图表", "Kaggle bike_data.csv：10,886 条记录，用于 SQLite、查询接口和前端 JSON", "两份数据均包含时间、天气、用户数量和总租车量等核心字段"], 80, 230, 510, 17, ink, 68);
  text(s, "Kaggle 页面截图保留为数据获取过程证据", 74, 572, 500, 25, { size: 15, color: muted }); footer(s, 3);
  note(s, "演讲者：成员 1。右侧图片为项目实际数据获取截图。" );
}

// 4 Architecture
{
  const s = deck.slides.add(); s.background.fill = "#FFFFFF"; title(s, "系统架构", "三条数据链路共同组成完整项目");
  const cols = [84, 450, 816];
  const names = ["静态分析", "数据库查询", "前端大屏"];
  const details = ["UCI hour.csv\nloader → cleaner → metrics → charts\n输出 PNG 分析图表", "Kaggle CSV\ninit_db → SQLite → db_helper → API\n返回 KPI、天气、小时查询结果", "Kaggle CSV\nprocess_data → data.json → ECharts\n输出浏览器端仪表盘"];
  cols.forEach((x, i) => { shape(s, x, 190, 300, 310, i === 1 ? "#EAF4FB" : "#F6FAFD", "#CDE0EE", true); text(s, names[i], x + 28, 223, 250, 33, { size: 24, bold: true, color: blue }); text(s, details[i], x + 28, 282, 244, 130, { size: 17, color: ink }); });
  text(s, "测试覆盖 UCI 分析流程和 SQLite 导入查询流程", 84, 555, 1010, 30, { size: 20, color: muted }); footer(s, 4);
  note(s, "演讲者：成员 1。完整结构图见项目 docs/code-structure.svg。" );
}

// 5 Results
{
  const s = deck.slides.add(); s.background.fill = "#FFFFFF"; title(s, "小时需求与天气差异", "统计结果来自 UCI 小时级数据");
  const hchart = s.charts.add("line", { position: { left: 68, top: 170, width: 620, height: 390 }, categories: ["0", "3", "6", "8", "12", "17", "20", "23"], series: [{ name: "平均租车量", values: [53, 6, 76, 359, 253, 461, 350, 87], fill: blue }], hasLegend: false, lineOptions: { smooth: true }, dataLabels: { showValue: false } }); applyPresentationChartFont(hchart, { fontFamily: font });
  const wchart = s.charts.add("bar", { position: { left: 734, top: 192, width: 430, height: 350 }, categories: ["晴朗", "雾/多云", "小雨雪", "强雨雪"], series: [{ name: "平均租车量", values: [205, 175, 112, 74], fill: cyan }], barOptions: { direction: "column", grouping: "clustered" }, hasLegend: false, dataLabels: { showValue: true, position: "outEnd" } }); applyPresentationChartFont(wchart, { fontFamily: font });
  text(s, "17 点平均租车量最高，约 461 次", 86, 585, 500, 30, { size: 18, bold: true, color: blue });
  text(s, "天气越恶劣，平均租车量越低。该结果属于描述性统计", 734, 585, 440, 40, { size: 17, color: muted }); footer(s, 5);
  note(s, "演讲者：成员 2。数据结论：17 点最高；天气统计仅说明关联趋势，不宣称因果。" );
}

// 6 database evidence
{
  const s = deck.slides.add(); s.background.fill = "#FFFFFF"; title(s, "SQLite 建库与数据导入", "Kaggle 整理后的 CSV 写入 bike_usage 表");
  await image(s, path.join(workspaceDir, "docs/evidence/02-database-import.jpg"), 610, 150, 570, 430, "SQLite 数据库导入成功截图", "contain");
  text(s, "实现内容", 72, 180, 300, 30, { size: 24, bold: true });
  bullet(s, ["读取 bike_data.csv 并检查 12 个业务字段", "创建 bike_usage 表，建立时间和天气索引", "数据库文件随项目提交，便于现场复现"], 78, 235, 450, 19, ink, 62);
  text(s, "对应代码：database/init_db.py", 72, 538, 430, 26, { size: 17, color: blue, bold: true }); footer(s, 6);
  note(s, "演讲者：成员 1。右侧是实际导入成功截图。" );
}

// 7 query API
{
  const s = deck.slides.add(); s.background.fill = "#FFFFFF"; title(s, "查询接口与数据服务", "KPI、天气和小时统计封装为可复用接口");
  await image(s, path.join(workspaceDir, "docs/evidence/03-query-api-test.jpg"), 635, 150, 540, 420, "KPI 和天气统计查询接口测试截图", "contain");
  text(s, "三个查询接口", 72, 180, 340, 32, { size: 24, bold: true });
  bullet(s, ["get_kpi_summary：总租车量、用户数量、平均温度", "get_weather_stat：按天气编码汇总租车量", "get_hourly_stat：按小时计算平均租车量"], 78, 235, 475, 18, ink, 62);
  text(s, "接口测试结果：总租车量 2,085,476 次", 72, 536, 490, 28, { size: 18, bold: true, color: blue }); footer(s, 7);
  note(s, "演讲者：成员 1。右侧是项目实际 KPI 与天气查询测试截图。" );
}

// 8 dashboard
{
  const s = deck.slides.add(); s.background.fill = "#FFFFFF"; title(s, "ECharts 数据大屏", "前端读取 data.json 并展示关键指标与趋势");
  shape(s, 70, 165, 1140, 390, "#071B33", "#0B79D0", true);
  text(s, "共享单车租车数据分析大屏", 105, 194, 540, 34, { size: 25, bold: true, color: "#FFFFFF" });
  const cards = [["2,085,476", "总租车数"], ["4,573", "日均租车"], ["8,714", "最高单日"], ["81.2%", "注册用户占比"]];
  cards.forEach((card, i) => { const x=105+i*260; shape(s,x,250,220,104,"#102C4A","#1B4E78",true); text(s,card[0],x+18,270,184,34,{size:25,bold:true,color:cyan,align:"center"}); text(s,card[1],x+18,315,184,20,{size:14,color:"#B8D9F1",align:"center"}); });
  text(s, "月度趋势", 110, 395, 190, 25, { size: 17, color: "#FFFFFF", bold: true });
  shape(s, 110, 435, 450, 70, "#0D3157", "none", true); text(s, "折线图：观察需求在不同月份的变化", 132, 460, 400, 20, { size: 14, color: "#B8D9F1" });
  text(s, "小时 / 季节 / 温度 / 用户结构", 630, 395, 370, 25, { size: 17, color: "#FFFFFF", bold: true });
  shape(s, 630, 435, 470, 70, "#0D3157", "none", true); text(s, "柱状图、散点图、饼图：支持快速阅读", 652, 460, 420, 20, { size: 14, color: "#B8D9F1" });
  text(s, "数据更新流程：bike_data.csv → process_data.py → data.json → index.html", 76, 590, 1050, 30, { size: 19, color: muted }); footer(s, 8);
  note(s, "演讲者：成员 3。现场可启动 web/dashboard 的 http.server 后展示真实页面。" );
}

// 9 Team
{
  const s = deck.slides.add(); s.background.fill = "#FFFFFF"; title(s, "五人协作与交付物", "每位成员负责一个岗位，同时理解完整数据链路");
  const roles = [
    ["成员 1", "项目管理、后端与数据库", "建库、接口、整合"],
    ["成员 2", "数据分析与算法", "清洗、指标、结论"],
    ["成员 3", "前端与可视化大屏", "ECharts、页面、展示"],
    ["成员 4", "文档与质量控制", "报告、证据、测试"],
    ["成员 5", "技术调研与答辩", "调研、PPT、演练"],
  ];
  roles.forEach((r,i)=>{ const x=70+(i%3)*375; const y=170+Math.floor(i/3)*190; shape(s,x,y,330,140, i===0?"#EAF4FB":"#F6FAFD", "#CDE0EE", true); text(s,r[0],x+24,y+22,100,24,{size:16,bold:true,color:blue}); text(s,r[1],x+24,y+55,270,26,{size:19,bold:true}); text(s,r[2],x+24,y+95,270,20,{size:15,color:muted}); });
  text(s, "答辩前全员完成一次“建库 → 查询 → 生成 JSON → 启动大屏 → 运行测试”的交叉演练", 72, 575, 1100, 30, { size: 18, color: muted }); footer(s, 9);
  note(s, "演讲者：成员 4 或成员 5。正式分工见 docs/team-plan.md。" );
}

// 10 Summary
{
  const s = deck.slides.add(); s.background.fill = navy;
  text(s, "项目总结", 76, 76, 400, 52, { size: 36, bold: true, color: "#FFFFFF" });
  shape(s, 76, 145, 155, 4, cyan);
  bullet(s, ["完成真实数据的清洗、统计分析与静态图表", "完成 SQLite 数据导入、KPI 与天气查询接口", "完成 ECharts 数据大屏与项目实施证据整理", "保留需求预测和实时数据接入的扩展空间"], 86, 220, 770, 20, "#D5E5F1", 66);
  shape(s, 900, 190, 220, 220, "#0D3157", "none", true);
  text(s, "感谢聆听", 930, 260, 160, 34, { size: 25, bold: true, color: cyan, align: "center" });
  text(s, "欢迎提问", 930, 310, 160, 28, { size: 18, color: "#D5E5F1", align: "center" });
  text(s, "答辩演示：数据库 → 接口 → 大屏 → 测试", 76, 618, 900, 26, { size: 17, color: "#8AB4D4" });
  note(s, "演讲者：成员 5。总结项目价值和可扩展方向，进入提问环节。" );
}

await (await PresentationFile.exportPptx(deck)).save(candidatePath);
console.log(candidatePath);
