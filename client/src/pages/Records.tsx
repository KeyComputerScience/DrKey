import { useState } from "react";
import { ArrowLeft, ArrowRight, CalendarDays, Check, Circle, Clock3, FileCode2, Filter, Flag, MoreHorizontal, ShieldCheck } from "lucide-react";
import { Link } from "wouter";
import { toast } from "sonner";

type Item = { id: number; title: string; detail: string; due: string; status: "进行中" | "待开始" | "已完成"; tag: string };

const initialItems: Item[] = [
  { id: 1, title: "补充 Transformer 基线实验", detail: "完成 3 个随机种子，记录验证集 F1 与运行时间。", due: "9 月 24 日", status: "进行中", tag: "人工智能与深度学习" },
  { id: 2, title: "整理数据预处理流程", detail: "在 README 中写清楚数据划分、清洗和特征处理步骤。", due: "9 月 26 日", status: "待开始", tag: "系统与架构研究" },
  { id: 3, title: "修改论文方法章节", detail: "补充复杂度分析，并解释模型选择与研究问题的关系。", due: "9 月 28 日", status: "待开始", tag: "信息安全" },
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
    <header className="academic-header"><div className="container academic-header-row"><Link href="/" className="academic-brand"><span className="academic-brand-mark">K</span><span><b>K 博士工作室</b><small>K. RESEARCH STUDIO</small></span></Link><nav className="academic-nav process-nav"><Link href="/">首页</Link><Link href="/process">辅导流程</Link><Link href="/records" className="active">咨询记录</Link><Link href="/appointments">我的预约</Link><Link href="/compliance">研究规范</Link></nav><Link href="/process" className="header-cta">预约咨询 <ArrowRight size={16} /></Link></div></header>
    <main><section className="records-hero"><div className="container"><p className="academic-kicker light">YOUR RESEARCH DASHBOARD</p><h1>把每次会谈，<br /><em>变成下一步行动。</em></h1><p>这里汇总你的咨询纪要与课后行动清单。完成一个小动作，研究就向前推进一步。</p></div></section>
      <section className="container records-content"><div className="records-summary"><div><p className="academic-kicker">CURRENT PROJECT</p><h2>推荐系统中的冷启动问题</h2><p>最近一次咨询：2026 年 9 月 18 日 · 林老师</p></div><div className="progress-ring"><strong>{progress}%</strong><span>行动完成</span></div></div><div className="records-layout"><aside className="records-sidebar"><div className="sidebar-label"><CalendarDays size={16} /> 会谈记录</div><button className="session-link active"><span>09.18</span><b>实验设计与指标讨论</b><small>林老师 · 已完成</small></button><button className="session-link"><span>09.11</span><b>研究问题与基线选择</b><small>K 博士 · 已完成</small></button><button className="session-link"><span>预约下一次</span><b>带着实验日志继续</b><small>建议 9 月 25 日后</small></button><Link href="/process" className="records-side-link">了解辅导流程 <ArrowRight size={15} /></Link></aside><div className="actions-panel"><div className="actions-heading"><div><p className="academic-kicker">ACTION ITEMS</p><h2>课后行动清单</h2><p>来自你的最近一次咨询，共 {items.length} 项。</p></div><button className="add-action-button" onClick={() => setShowAdd(true)}><span>+</span> 添加行动</button></div><div className="status-tabs" role="tablist">{statusTabs.map((tab) => <button key={tab} className={activeStatus === tab ? "active" : ""} onClick={() => setActiveStatus(tab)} role="tab" aria-selected={activeStatus === tab}>{tab}<span>{tab === "全部" ? items.length : items.filter((item) => item.status === tab).length}</span></button>)}</div><div className="action-list">{visibleItems.map((item) => <article className={`action-item ${item.status === "已完成" ? "done" : ""}`} key={item.id}><button className="action-check" onClick={() => markDone(item.id)} aria-label={item.status === "已完成" ? "已完成" : `完成：${item.title}`}>{item.status === "已完成" ? <Check size={14} /> : <Circle size={17} />}</button><div className="action-copy"><div className="action-title-row"><h3>{item.title}</h3><span className={`status-badge ${item.status === "进行中" ? "working" : item.status === "已完成" ? "finished" : ""}`}>{item.status}</span></div><p>{item.detail}</p><div className="action-meta"><span><Flag size={13} /> {item.tag}</span><span><Clock3 size={13} /> 截止 {item.due}</span></div></div><button className="action-more" onClick={() => toast("行动详情编辑功能即将上线")} aria-label="更多操作"><MoreHorizontal size={18} /></button></article>)}{visibleItems.length === 0 && <div className="empty-actions">这个状态下暂时没有行动项。</div>}</div><div className="records-note"><FileCode2 size={18} /><p><b>建议</b> 每次会谈后先完成一个最小可验证动作，再预约下一次支持。行动清单只记录你的计划与进度，不代表工作室代替你完成任何研究任务。</p></div></div></div></section>
    </main><footer className="academic-footer"><div className="container academic-footer-bottom standalone-footer"><span>© 2026 K 博士工作室 · K. Research Studio</span><Link href="/">返回首页 <ArrowLeft size={14} /></Link></div></footer>
    {showAdd && <div className="simple-modal-backdrop" onClick={() => setShowAdd(false)}><div className="simple-booking-modal add-action-modal" onClick={(event) => event.stopPropagation()}><button className="modal-close-button" onClick={() => setShowAdd(false)}>×</button><p className="academic-kicker">ADD AN ACTION</p><h2>记录一个下一步</h2><form onSubmit={(event) => { event.preventDefault(); toast.success("行动项已添加"); setShowAdd(false); }}><input required placeholder="行动标题，例如：补充一个基线实验" /><textarea required placeholder="写下完成标准或需要准备的材料"></textarea><button className="navy-button" type="submit">保存行动项 <ArrowRight size={17} /></button></form></div></div>}
  </div>;
}
