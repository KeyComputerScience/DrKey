import { useState } from "react";
import { ArrowLeft, ArrowRight, CalendarDays, Check, CheckCircle2, ChevronRight, Clock3, Download, FileCode2, FileText, Mail, MessageCircle, Send, ShieldCheck, Star, UserRound, X } from "lucide-react";
import { Link } from "wouter";
import { toast } from "sonner";

type Appointment = {
  id: string;
  status: "已确认" | "待确认" | "已完成";
  date: string;
  time: string;
  mentor: string;
  mentorRole: string;
  mentorInitial: string;
  mentorColor: string;
  topic: string;
  request: string;
  attachments: { name: string; type: string; size: string }[];
};

const appointments: Appointment[] = [
  {
    id: "KS-20260918-01",
    status: "已确认",
    date: "2026 年 9 月 25 日",
    time: "19:00 — 19:50",
    mentor: "K 博士",
    mentorRole: "机器学习 · 算法研究",
    mentorInitial: "K",
    mentorColor: "#d9e4e5",
    topic: "实验设计与复现支持",
    request: "论文方法已经理解，但 Transformer 基线实验无法稳定复现，想一起检查环境、随机种子与指标记录。",
    attachments: [
      { name: "experiment_log.txt", type: "TXT", size: "18 KB" },
      { name: "reproduction_notes.pdf", type: "PDF", size: "1.2 MB" },
    ],
  },
  {
    id: "KS-20260911-02",
    status: "待确认",
    date: "2026 年 10 月 2 日",
    time: "14:30 — 15:20",
    mentor: "陈老师",
    mentorRole: "系统 · 工程实践",
    mentorInitial: "陈",
    mentorColor: "#e7dcc8",
    topic: "分布式系统论文结构",
    request: "希望梳理系统架构、性能指标与实验章节之间的论证关系。",
    attachments: [{ name: "system_architecture.zip", type: "ZIP", size: "4.8 MB" }],
  },
  {
    id: "KS-20260905-03",
    status: "已完成",
    date: "2026 年 9 月 5 日",
    time: "10:30 — 11:20",
    mentor: "林老师",
    mentorRole: "论文 · 学术表达",
    mentorInitial: "林",
    mentorColor: "#dce2d5",
    topic: "论文方法章节梳理",
    request: "梳理研究问题、方法选择和实验设计之间的论证关系。",
    attachments: [{ name: "paper_outline.pdf", type: "PDF", size: "860 KB" }],
  },
];

export default function Appointments() {
  const [selectedId, setSelectedId] = useState(appointments[0].id);
  const [messages, setMessages] = useState([{ from: "导师", text: "你好，收到你的材料了。我们会先从随机种子和指标记录开始排查。", time: "9 月 18 日 16:20" }]);
  const [messageText, setMessageText] = useState("");
  const [managementAction, setManagementAction] = useState<"cancel" | "reschedule" | null>(null);
  const [showReview, setShowReview] = useState(false);
  const [reviewRating, setReviewRating] = useState(0);
  const [reviewText, setReviewText] = useState("");
  const [cancelledIds, setCancelledIds] = useState<string[]>([]);
  const selected = appointments.find((item) => item.id === selectedId) || appointments[0];
  const isCancelled = cancelledIds.includes(selected.id);

  return <div className="academic-site appointments-page">
    <div className="integrity-bar"><ShieldCheck size={14} /><span>研究诚信优先</span><i /><span>不代写 · 不伪造实验 · 不代替学生完成考核</span><Link href="/compliance">查看规范</Link></div>
    <header className="academic-header"><div className="container academic-header-row"><Link href="/" className="academic-brand"><span className="academic-brand-mark">K</span><span><b>K 博士工作室</b><small>K. RESEARCH STUDIO</small></span></Link><nav className="academic-nav process-nav"><Link href="/">首页</Link><Link href="/records">咨询记录</Link><Link href="/appointments" className="active">我的预约</Link><Link href="/compliance">研究规范</Link></nav><Link href="/process" className="header-cta">预约咨询 <ArrowRight size={16} /></Link></div></header>
    <main>
      <section className="appointments-hero"><div className="container"><p className="academic-kicker light">PERSONAL CENTER · MY APPOINTMENTS</p><h1>每一次预约，<br /><em>都有清楚的下一步。</em></h1><p>查看已提交的预约详情、导师信息与附件材料。预约确认后，我们会通过邮箱与你联系。</p></div></section>
      <section className="container appointments-content">
        <div className="appointments-topline"><div><p className="academic-kicker">APPOINTMENT HISTORY</p><h2>我的预约</h2><p>共 {appointments.length} 条预约记录</p></div><Link href="/process" className="navy-outline-button">提交新需求 <ArrowRight size={17} /></Link></div>
        <div className="appointments-layout">
          <aside className="appointment-list"><div className="appointment-list-label"><CalendarDays size={16} /> 全部预约</div>{appointments.map((appointment) => <button className={`appointment-list-item ${selected.id === appointment.id ? "active" : ""}`} key={appointment.id} onClick={() => setSelectedId(appointment.id)}><div><span>{appointment.date.replace("2026 年 ", "")}</span><b>{appointment.topic}</b><small>{appointment.mentor} · {appointment.time.split(" — ")[0]}</small></div><span className={`appointment-status ${appointment.status === "已确认" || appointment.status === "已完成" ? "confirmed" : "pending"}`}>{appointment.status}</span><ChevronRight size={16} /></button>)}</aside>
          <article className="appointment-detail">
            <div className="appointment-detail-header"><div><span className={`appointment-status large ${selected.status === "已确认" || selected.status === "已完成" ? "confirmed" : "pending"}`}>{selected.status}</span><h2>{selected.topic}</h2><p>预约编号：{selected.id}</p></div><div className="appointment-actions"><button onClick={() => setManagementAction("reschedule")} disabled={isCancelled || selected.status === "已完成"}><Clock3 size={14} /> 修改时间</button><button className="danger-action" onClick={() => setManagementAction("cancel")} disabled={isCancelled || selected.status === "已完成"}><X size={14} /> 取消预约</button></div></div>
            <div className="appointment-facts"><div><CalendarDays size={17} /><span><small>预约日期</small><b>{selected.date}</b></span></div><div><Clock3 size={17} /><span><small>预约时段</small><b>{selected.time}</b></span></div><div><Mail size={17} /><span><small>通知方式</small><b>邮箱确认</b></span></div></div>
            <section className="appointment-section"><div className="appointment-section-title"><UserRound size={17} /><h3>导师信息</h3></div><div className="appointment-mentor"><div className="appointment-mentor-avatar" style={{ background: selected.mentorColor }}>{selected.mentorInitial}</div><div><h3>{selected.mentor}<span><Check size={12} /> 已认证</span></h3><p>{selected.mentorRole}</p><small>计算机科学研究与技术辅导</small></div><button onClick={() => toast("消息功能即将上线")}><MessageCircle size={15} /> 联系导师</button></div></section>
            <section className="appointment-section"><div className="appointment-section-title"><MessageCircle size={17} /><h3>预约问题</h3></div><div className="appointment-request">{selected.request}</div></section>
            {selected.status !== "已完成" && !isCancelled && <section className="appointment-section message-board-section"><div className="appointment-section-title"><MessageCircle size={17} /><h3>留言板 <span>{messages.length}</span></h3><small>预约前沟通</small></div><div className="message-board">{messages.map((message, index) => <div className={`message-bubble ${message.from === "学生" ? "student" : ""}`} key={`${message.time}-${index}`}><div><b>{message.from}</b><small>{message.time}</small></div><p>{message.text}</p></div>)}</div><form className="message-form" onSubmit={(event) => { event.preventDefault(); if (!messageText.trim()) return; setMessages((current) => [...current, { from: "学生", text: messageText.trim(), time: "刚刚" }]); setMessageText(""); toast.success("留言已发送"); }}><input value={messageText} onChange={(event) => setMessageText(event.target.value)} placeholder="给导师留一句话，例如：我已补充实验日志" aria-label="留言内容" /><button type="submit" aria-label="发送留言"><Send size={15} /></button></form><p className="message-note"><ShieldCheck size={13} /> 仅用于本次预约的简单沟通，请勿发送隐私或敏感数据。</p></section>}
            {selected.status === "已完成" && <section className="appointment-section review-section"><div className="appointment-section-title"><Star size={17} /><h3>评价本次辅导</h3></div><div className="review-panel"><p>这次辅导是否帮助你更清楚地推进了研究？</p><div className="rating-stars">{[1, 2, 3, 4, 5].map((rating) => <button key={rating} className={reviewRating >= rating ? "active" : ""} onClick={() => setReviewRating(rating)} aria-label={`${rating} 分`}><Star size={23} fill={reviewRating >= rating ? "currentColor" : "none"} /></button>)}</div><textarea value={reviewText} onChange={(event) => setReviewText(event.target.value)} placeholder="写下你对导师讲解、反馈或节奏的感受（可选）" /><button className="navy-button review-submit" disabled={!reviewRating} onClick={() => { toast.success("感谢你的评价"); setShowReview(true); }}>{showReview ? "评价已提交" : "提交评价"} <ArrowRight size={16} /></button></div></section>}
            <section className="appointment-section"><div className="appointment-section-title"><FileCode2 size={17} /><h3>已上传附件 <span>{selected.attachments.length}</span></h3><button className="download-all" onClick={() => toast("附件下载功能即将上线")}><Download size={14} /> 下载全部</button></div><div className="attachment-list">{selected.attachments.map((file) => <div className="appointment-attachment" key={file.name}><div className={`file-icon ${file.type.toLowerCase()}`}>{file.type === "PDF" ? <FileText size={16} /> : <FileCode2 size={16} />}</div><div><b>{file.name}</b><small>{file.type} · {file.size}</small></div><button aria-label={`下载 ${file.name}`} onClick={() => toast(`${file.name} 下载功能即将上线`)}><Download size={15} /></button></div>)}</div><p className="attachment-privacy"><ShieldCheck size={14} /> 附件仅用于本次咨询准备。请勿上传他人隐私、未授权数据或违反机构规定的材料。</p></section>
          </article>
        </div>
      </section>
    </main>
    <footer className="academic-footer"><div className="container academic-footer-bottom standalone-footer"><span>© 2026 K 博士工作室 · K. Research Studio</span><Link href="/">返回首页 <ArrowLeft size={14} /></Link></div></footer>
    {managementAction && <div className="simple-modal-backdrop" onClick={() => setManagementAction(null)}><div className="appointment-confirm-modal" onClick={(event) => event.stopPropagation()}><button className="modal-close-button" onClick={() => setManagementAction(null)}><X size={19} /></button><div className={`confirm-icon ${managementAction === "cancel" ? "cancel" : ""}`}>{managementAction === "cancel" ? <X size={25} /> : <Clock3 size={25} />}</div><p className="academic-kicker">{managementAction === "cancel" ? "CANCEL APPOINTMENT" : "RESCHEDULE APPOINTMENT"}</p><h2>{managementAction === "cancel" ? "确认取消这次预约？" : "选择新的预约时间"}</h2>{managementAction === "cancel" ? <p>取消后，当前时段将被释放。你仍可以稍后重新发起预约。</p> : <><p>当前时间：{selected.date} · {selected.time}</p><select className="reschedule-select" defaultValue=""><option value="" disabled>请选择新的时间</option><option>2026 年 9 月 27 日 · 19:00 — 19:50</option><option>2026 年 9 月 29 日 · 14:30 — 15:20</option><option>2026 年 10 月 1 日 · 10:00 — 10:50</option></select></>}<div className="confirm-actions"><button className="plain-cancel" onClick={() => setManagementAction(null)}>暂不操作</button><button className={`navy-button ${managementAction === "cancel" ? "danger-button" : ""}`} onClick={() => { if (managementAction === "cancel") { setCancelledIds((current) => [...current, selected.id]); toast.success("预约已取消"); } else { toast.success("修改时间申请已提交"); } setManagementAction(null); }}>{managementAction === "cancel" ? "确认取消" : "提交修改"} <ArrowRight size={16} /></button></div></div></div>}
  </div>;
}
