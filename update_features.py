from pathlib import Path

root = Path('/home/ubuntu/jingxuan-store/client/src')

home = root / 'pages/Home.tsx'
s = home.read_text()

s = s.replace('import { Link } from "wouter";', 'import { Link } from "wouter";')
s = s.replace('const mentors = [\n  { name: "K 博士", role: "机器学习 · 算法研究", school: "博士 / 计算机科学研究与教学", initials: "K", color: "#d9e4e5", tags: ["深度学习", "实验设计"] },\n  { name: "陈老师", role: "系统 · 工程实践", school: "博士 / 分布式系统与性能优化", initials: "陈", color: "#e7dcc8", tags: ["系统论文", "代码复现"] },\n  { name: "林老师", role: "论文 · 学术表达", school: "博士 / 计算机论文写作与评审", initials: "林", color: "#dce2d5", tags: ["结构梳理", "英文润色"] },\n];', '''const mentors = [
  { name: "K 博士", role: "机器学习 · 算法研究", school: "博士 / 计算机科学研究与教学", initials: "K", color: "#d9e4e5", tags: ["深度学习", "实验设计"], directions: ["机器学习", "算法研究"] },
  { name: "陈老师", role: "系统 · 工程实践", school: "博士 / 分布式系统与性能优化", initials: "陈", color: "#e7dcc8", tags: ["系统论文", "代码复现"], directions: ["系统工程", "工程实践"] },
  { name: "林老师", role: "论文 · 学术表达", school: "博士 / 计算机论文写作与评审", initials: "林", color: "#dce2d5", tags: ["结构梳理", "英文润色"], directions: ["论文写作", "学术表达"] },
];''')
s = s.replace('  const [consultOpen, setConsultOpen] = useState(false);\n  const jumpAndClose', '  const [consultOpen, setConsultOpen] = useState(false);\n  const [mentorFilter, setMentorFilter] = useState("全部");\n  const mentorFilters = ["全部", "机器学习", "系统工程", "论文写作"];\n  const visibleMentors = mentors.filter((mentor) => mentorFilter === "全部" || mentor.directions.some((direction) => direction.includes(mentorFilter)));\n  const jumpAndClose')
s = s.replace('<Link href="/compliance" onClick={jumpAndClose}>研究规范</Link>', '<Link href="/compliance" onClick={jumpAndClose}>研究规范</Link><Link href="/records" onClick={jumpAndClose}>咨询记录</Link>')
s = s.replace('<div className="section-heading-row"><div><p className="academic-kicker">MEET YOUR MENTOR</p><h2>找到适合你问题的<br /><em>那位技术同行者。</em></h2></div><button className="simple-link" onClick={() => toast("更多导师资料正在整理中")}>查看导师筛选 <ArrowRight size={17} /></button></div><div className="mentor-grid">{mentors.map((mentor) =>', '<div className="section-heading-row"><div><p className="academic-kicker">MEET YOUR MENTOR</p><h2>找到适合你问题的<br /><em>那位技术同行者。</em></h2></div><Link className="simple-link" href="/records">查看咨询记录 <ArrowRight size={17} /></Link></div><div className="mentor-filter" role="tablist" aria-label="按技术方向筛选导师">{mentorFilters.map((filter) => <button key={filter} className={mentorFilter === filter ? "active" : ""} onClick={() => setMentorFilter(filter)} role="tab" aria-selected={mentorFilter === filter}>{filter}<span>{filter === "全部" ? mentors.length : mentors.filter((mentor) => mentor.directions.some((direction) => direction.includes(filter))).length}</span></button>)}</div><div className="mentor-grid">{visibleMentors.map((mentor) =>')
s = s.replace('<div className="mentor-grid">{visibleMentors.map((mentor) => <article', '<div className="mentor-grid">{visibleMentors.length ? visibleMentors.map((mentor) => <article')
s = s.replace('</article>)}</div></section>\n\n      <section className="integrity-callout-section">', '</article>) : <div className="mentor-empty">该方向的导师档案正在更新中，欢迎先提交预约意向。</div>}</div></section>\n\n      <section className="integrity-callout-section">')
s = s.replace('<Link href="/compliance">研究规范</Link></div><div><h3>联系工作室</h3>', '<Link href="/compliance">研究规范</Link><Link href="/records">咨询记录</Link></div><div><h3>联系工作室</h3>')
home.write_text(s)

app = root / 'App.tsx'
app.write_text('''import { Toaster } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { Route, Switch } from "wouter";
import ErrorBoundary from "./components/ErrorBoundary";
import { ThemeProvider } from "./contexts/ThemeContext";
import Compliance from "./pages/Compliance";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import Process from "./pages/Process";
import Records from "./pages/Records";

function Router() {
  return <Switch><Route path="/" component={Home} /><Route path="/process" component={Process} /><Route path="/compliance" component={Compliance} /><Route path="/records" component={Records} /><Route path="/404" component={NotFound} /><Route component={NotFound} /></Switch>;
}

export default function App() {
  return <ErrorBoundary><ThemeProvider defaultTheme="light"><TooltipProvider><Toaster position="top-center" richColors /><Router /></TooltipProvider></ThemeProvider></ErrorBoundary>;
}
''')

records = root / 'pages/Records.tsx'
records.write_text('''import { useState } from "react";
import { ArrowLeft, ArrowRight, CalendarDays, Check, Circle, Clock3, FileCode2, Filter, Flag, MoreHorizontal, ShieldCheck } from "lucide-react";
import { Link } from "wouter";
import { toast } from "sonner";

type Item = { id: number; title: string; detail: string; due: string; status: "进行中" | "待开始" | "已完成"; tag: string };

const initialItems: Item[] = [
  { id: 1, title: "补充 Transformer 基线实验", detail: "完成 3 个随机种子，记录验证集 F1 与运行时间。", due: "9 月 24 日", status: "进行中", tag: "机器学习" },
  { id: 2, title: "整理数据预处理流程", detail: "在 README 中写清楚数据划分、清洗和特征处理步骤。", due: "9 月 26 日", status: "待开始", tag: "实验复现" },
  { id: 3, title: "修改论文方法章节", detail: "补充复杂度分析，并解释模型选择与研究问题的关系。", due: "9 月 28 日", status: "待开始", tag: "论文写作" },
  { id: 4, title: "确认实验指标定义", detail: "已完成会谈复盘，明确 Accuracy、F1 和 AUC 的使用边界。", due: "9 月 18 日", status: "已完成", tag: "研究设计" },
];

const statusTabs = ["全部", "进行中", "待开始", "已完成"];

export default function Records() {
  const [items, setItems] = useState(initialItems);
  const [activeStatus, setActiveStatus] = useState("全部");
  const [showAdd, setShowAdd] = useState(false);
  const visibleItems = items.filter((item) => activeStatus === "全部" || item.status === activeStatus);
  const completed = items.filter((item) => item.status === "已完成").length;
  const progress = Math.round((completed / items.length) * 100);

  const markDone = (id: number) => {
    setItems((current) => current.map((item) => item.id === id ? { ...item, status: "已完成" } : item));
    toast.success("已更新行动状态");
  };

  return <div className="academic-site records-page">
    <div className="integrity-bar"><ShieldCheck size={14} /><span>研究诚信优先</span><i /><span>不代写 · 不伪造实验 · 不代替学生完成考核</span><Link href="/compliance">查看规范</Link></div>
    <header className="academic-header"><div className="container academic-header-row"><Link href="/" className="academic-brand"><span className="academic-brand-mark">K</span><span><b>K 博士工作室</b><small>K. RESEARCH STUDIO</small></span></Link><nav className="academic-nav process-nav"><Link href="/">首页</Link><Link href="/process">辅导流程</Link><Link href="/records" className="active">咨询记录</Link><Link href="/compliance">研究规范</Link></nav><Link href="/process" className="header-cta">预约咨询 <ArrowRight size={16} /></Link></div></header>
    <main><section className="records-hero"><div className="container"><p className="academic-kicker light">YOUR RESEARCH DASHBOARD</p><h1>把每次会谈，<br /><em>变成下一步行动。</em></h1><p>这里汇总你的咨询纪要与课后行动清单。完成一个小动作，研究就向前推进一步。</p></div></section>
      <section className="container records-content"><div className="records-summary"><div><p className="academic-kicker">CURRENT PROJECT</p><h2>推荐系统中的冷启动问题</h2><p>最近一次咨询：2026 年 9 月 18 日 · 林老师</p></div><div className="progress-ring"><strong>{progress}%</strong><span>行动完成</span></div></div><div className="records-layout"><aside className="records-sidebar"><div className="sidebar-label"><CalendarDays size={16} /> 会谈记录</div><button className="session-link active"><span>09.18</span><b>实验设计与指标讨论</b><small>林老师 · 已完成</small></button><button className="session-link"><span>09.11</span><b>研究问题与基线选择</b><small>K 博士 · 已完成</small></button><button className="session-link"><span>预约下一次</span><b>带着实验日志继续</b><small>建议 9 月 25 日后</small></button><Link href="/process" className="records-side-link">了解辅导流程 <ArrowRight size={15} /></Link></aside><div className="actions-panel"><div className="actions-heading"><div><p className="academic-kicker">ACTION ITEMS</p><h2>课后行动清单</h2><p>来自你的最近一次咨询，共 {items.length} 项。</p></div><button className="add-action-button" onClick={() => setShowAdd(true)}><span>+</span> 添加行动</button></div><div className="status-tabs" role="tablist">{statusTabs.map((tab) => <button key={tab} className={activeStatus === tab ? "active" : ""} onClick={() => setActiveStatus(tab)} role="tab" aria-selected={activeStatus === tab}>{tab}<span>{tab === "全部" ? items.length : items.filter((item) => item.status === tab).length}</span></button>)}</div><div className="action-list">{visibleItems.map((item) => <article className={`action-item ${item.status === "已完成" ? "done" : ""}`} key={item.id}><button className="action-check" onClick={() => markDone(item.id)} aria-label={item.status === "已完成" ? "已完成" : `完成：${item.title}`}>{item.status === "已完成" ? <Check size={14} /> : <Circle size={17} />}</button><div className="action-copy"><div className="action-title-row"><h3>{item.title}</h3><span className={`status-badge ${item.status === "进行中" ? "working" : item.status === "已完成" ? "finished" : ""}`}>{item.status}</span></div><p>{item.detail}</p><div className="action-meta"><span><Flag size={13} /> {item.tag}</span><span><Clock3 size={13} /> 截止 {item.due}</span></div></div><button className="action-more" onClick={() => toast("行动详情编辑功能即将上线")} aria-label="更多操作"><MoreHorizontal size={18} /></button></article>)}{visibleItems.length === 0 && <div className="empty-actions">这个状态下暂时没有行动项。</div>}</div><div className="records-note"><FileCode2 size={18} /><p><b>建议</b> 每次会谈后先完成一个最小可验证动作，再预约下一次支持。行动清单只记录你的计划与进度，不代表工作室代替你完成任何研究任务。</p></div></div></div></section>
    </main><footer className="academic-footer"><div className="container academic-footer-bottom standalone-footer"><span>© 2026 K 博士工作室 · K. Research Studio</span><Link href="/">返回首页 <ArrowLeft size={14} /></Link></div></footer>
    {showAdd && <div className="simple-modal-backdrop" onClick={() => setShowAdd(false)}><div className="simple-booking-modal add-action-modal" onClick={(event) => event.stopPropagation()}><button className="modal-close-button" onClick={() => setShowAdd(false)}>×</button><p className="academic-kicker">ADD AN ACTION</p><h2>记录一个下一步</h2><form onSubmit={(event) => { event.preventDefault(); toast.success("行动项已添加"); setShowAdd(false); }}><input required placeholder="行动标题，例如：补充一个基线实验" /><textarea required placeholder="写下完成标准或需要准备的材料"></textarea><button className="navy-button" type="submit">保存行动项 <ArrowRight size={17} /></button></form></div></div>}
  </div>;
}
''')

css = root / 'index.css'
style = css.read_text()
insert = '''
/* Mentor filtering */
.mentor-filter { display: flex; align-items: center; gap: 8px; margin-top: 32px; padding-bottom: 14px; border-bottom: 1px solid var(--line); }
.mentor-filter button, .status-tabs button { display: inline-flex; align-items: center; gap: 7px; padding: 7px 11px; border: 1px solid transparent; background: transparent; color: #75848b; font-size: 11px; cursor: pointer; }
.mentor-filter button span, .status-tabs button span { color: #a0aaad; font-family: "DM Mono", monospace; font-size: 9px; }
.mentor-filter button:hover, .mentor-filter button.active, .status-tabs button:hover, .status-tabs button.active { border-color: #b9c3c0; background: #edf0ec; color: var(--ink); }
.mentor-filter button.active { border-color: var(--amber); }
.mentor-empty { grid-column: 1 / -1; padding: 42px; border: 1px dashed #c4ccc7; color: #718087; text-align: center; font-size: 12px; }

/* Action items dashboard */
.records-hero { min-height: 330px; display: flex; align-items: center; background: var(--ink); color: var(--white); }
.records-hero h1 { margin: 0; font-family: "Noto Serif SC", serif; font-size: clamp(40px, 5vw, 63px); line-height: 1.3; font-weight: 500; letter-spacing: -.08em; }
.records-hero h1 em { font-style: normal; font-weight: 500; }
.records-hero p:not(.academic-kicker) { max-width: 520px; margin: 20px 0 0; color: #bfccd2; font-size: 13px; line-height: 1.9; }
.records-content { padding-top: 82px; padding-bottom: 105px; }
.records-summary { display: flex; align-items: center; justify-content: space-between; gap: 25px; padding: 27px 31px; background: #e7ece8; border: 1px solid #d3dbd5; }
.records-summary h2 { margin: 0; font-family: "Noto Serif SC", serif; font-size: 25px; letter-spacing: -.06em; }
.records-summary p:last-child { margin: 9px 0 0; color: #708078; font-size: 11px; }
.progress-ring { width: 85px; height: 85px; display: grid; place-items: center; align-content: center; border: 2px solid var(--amber); border-radius: 50%; }
.progress-ring strong { font-family: "DM Mono", monospace; font-size: 17px; }
.progress-ring span { margin-top: 3px; color: #74827d; font-size: 9px; }
.records-layout { display: grid; grid-template-columns: 255px 1fr; gap: 28px; margin-top: 28px; }
.records-sidebar { align-self: start; border-top: 1px solid var(--line); }
.sidebar-label { display: flex; align-items: center; gap: 7px; padding: 16px 0 12px; color: #637681; font-family: "DM Mono", monospace; font-size: 10px; }
.session-link { width: 100%; display: block; padding: 15px 12px; border: 0; border-bottom: 1px solid var(--line); background: transparent; color: var(--ink); text-align: left; cursor: pointer; }
.session-link.active { background: #edf0ec; border-left: 2px solid var(--amber); }
.session-link span, .session-link b, .session-link small { display: block; }
.session-link span { color: var(--amber); font-family: "DM Mono", monospace; font-size: 9px; }
.session-link b { margin: 7px 0 4px; font-size: 12px; }
.session-link small { color: #89969a; font-size: 10px; }
.records-side-link { display: inline-flex; align-items: center; gap: 7px; margin-top: 21px; color: var(--ink); border-bottom: 1px solid var(--ink); padding-bottom: 5px; font-size: 11px; font-weight: 700; }
.actions-panel { padding: 30px 32px 26px; background: var(--paper-light); border: 1px solid var(--line); }
.actions-heading { display: flex; align-items: end; justify-content: space-between; gap: 20px; }
.actions-heading h2 { margin: 0; font-family: "Noto Serif SC", serif; font-size: 28px; letter-spacing: -.07em; }
.actions-heading p:last-child { margin: 8px 0 0; color: #7a878e; font-size: 11px; }
.add-action-button { display: inline-flex; align-items: center; gap: 7px; min-height: 35px; padding: 0 11px; border: 1px solid #b7c0bc; background: transparent; color: var(--ink); font-size: 11px; font-weight: 700; cursor: pointer; }
.add-action-button:hover { border-color: var(--amber); color: var(--amber); }
.add-action-button span { font-size: 18px; line-height: 0; }
.status-tabs { display: flex; gap: 5px; margin-top: 25px; padding-bottom: 12px; border-bottom: 1px solid var(--line); }
.status-tabs button { padding: 6px 10px; }
.status-tabs button.active { border-color: var(--amber); background: #f0eee7; }
.action-list { border-top: 0; }
.action-item { display: grid; grid-template-columns: 25px 1fr 24px; gap: 13px; padding: 21px 5px; border-bottom: 1px solid var(--line); }
.action-check { width: 22px; height: 22px; display: grid; place-items: center; margin-top: 1px; border: 1px solid #afbbb5; border-radius: 50%; background: transparent; color: #698274; cursor: pointer; }
.action-item.done .action-check { border-color: #759782; background: #dce9df; }
.action-item.done .action-copy h3 { color: #8a9698; text-decoration: line-through; }
.action-title-row { display: flex; align-items: center; flex-wrap: wrap; gap: 9px; }
.action-copy h3 { margin: 0; font-size: 13px; }
.action-copy > p { margin: 7px 0 10px; color: #6d7b81; font-size: 11px; line-height: 1.7; }
.status-badge { padding: 3px 6px; background: #e8e8df; color: #77837c; font-size: 9px; }
.status-badge.working { background: #f2e4d5; color: #a3673b; }
.status-badge.finished { background: #dfeae1; color: #5b7b65; }
.action-meta { display: flex; flex-wrap: wrap; gap: 13px; color: #89969a; font-size: 9px; }
.action-meta span { display: inline-flex; align-items: center; gap: 4px; }
.action-more { align-self: start; padding: 3px; border: 0; background: transparent; color: #9aa5a8; cursor: pointer; }
.empty-actions { padding: 45px 10px; color: #7d8b90; text-align: center; font-size: 12px; }
.records-note { display: flex; align-items: start; gap: 10px; margin-top: 21px; padding: 15px 17px; background: #edf0ec; color: #6e7d76; }
.records-note svg { flex: none; color: var(--amber); }
.records-note p { margin: 0; font-size: 10px; line-height: 1.8; }
.records-note b { color: var(--ink); }
.add-action-modal { width: min(510px, 100%); }

@media (max-width: 920px) {
  .records-layout { grid-template-columns: 205px 1fr; gap: 18px; }
  .actions-panel { padding: 24px 22px; }
}
@media (max-width: 680px) {
  .mentor-filter { overflow-x: auto; margin-top: 24px; }
  .mentor-filter button { white-space: nowrap; }
  .records-hero { min-height: 320px; }
  .records-content { padding-top: 60px; padding-bottom: 72px; }
  .records-summary { align-items: start; padding: 20px; }
  .records-summary h2 { font-size: 20px; }
  .progress-ring { width: 67px; height: 67px; flex: none; }
  .progress-ring strong { font-size: 14px; }
  .records-layout { display: block; }
  .records-sidebar { margin-bottom: 29px; }
  .session-link { display: none; }
  .session-link.active { display: block; }
  .records-side-link { margin-top: 13px; }
  .actions-panel { padding: 22px 14px; }
  .actions-heading { align-items: start; flex-direction: column; }
  .status-tabs { overflow-x: auto; }
  .status-tabs button { white-space: nowrap; }
  .action-item { grid-template-columns: 24px 1fr 18px; gap: 9px; padding: 18px 0; }
  .action-copy h3 { font-size: 12px; }
  .action-copy > p { font-size: 10px; }
}
'''
marker = '@media (max-width: 920px) {'
if '/* Mentor filtering */' not in style:
    style = style.replace(marker, insert + '\n' + marker, 1)
css.write_text(style)

# Update HTML title and metadata for the new brand.
html = Path('/home/ubuntu/jingxuan-store/client/index.html')
h = html.read_text().replace('研途 Research Path——以学术诚信为前提，提供研究方法、论文结构、文献规范与答辩表达辅导。', 'K 博士工作室——面向计算机专业的算法、系统、代码与论文研究支持。').replace('研途 Research Path｜合规学术支持平台', 'K 博士工作室｜计算机研究支持平台')
html.write_text(h)
''
