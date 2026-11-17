from pathlib import Path

root = Path('/home/ubuntu/jingxuan-store/client/src')
app = root / 'App.tsx'
s = app.read_text()
s = s.replace('import Records from "./pages/Records";', 'import Records from "./pages/Records";\nimport Appointments from "./pages/Appointments";')
s = s.replace('<Route path="/records" component={Records} />', '<Route path="/records" component={Records} /><Route path="/appointments" component={Appointments} />')
app.write_text(s)

home = root / 'pages/Home.tsx'
s = home.read_text()
s = s.replace('<Link href="/records" onClick={jumpAndClose}>咨询记录</Link>', '<Link href="/records" onClick={jumpAndClose}>咨询记录</Link><Link href="/appointments" onClick={jumpAndClose}>我的预约</Link>')
s = s.replace('<Link href="/records">咨询记录</Link></div><div><h3>联系工作室</h3>', '<Link href="/records">咨询记录</Link><Link href="/appointments">我的预约</Link></div><div><h3>联系工作室</h3>')
home.write_text(s)

records = root / 'pages/Records.tsx'
s = records.read_text()
s = s.replace('<Link href="/records" className="active">咨询记录</Link><Link href="/compliance">研究规范</Link>', '<Link href="/records" className="active">咨询记录</Link><Link href="/appointments">我的预约</Link><Link href="/compliance">研究规范</Link>')
records.write_text(s)

page = root / 'pages/Appointments.tsx'
page.write_text('''import { useState } from "react";
import { ArrowLeft, ArrowRight, CalendarDays, Check, ChevronRight, Clock3, Download, FileCode2, FileText, Mail, MessageCircle, ShieldCheck, UserRound } from "lucide-react";
import { Link } from "wouter";
import { toast } from "sonner";

type Appointment = {
  id: string;
  status: "已确认" | "待确认";
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
];

export default function Appointments() {
  const [selectedId, setSelectedId] = useState(appointments[0].id);
  const selected = appointments.find((item) => item.id === selectedId) || appointments[0];

  return <div className="academic-site appointments-page">
    <div className="integrity-bar"><ShieldCheck size={14} /><span>研究诚信优先</span><i /><span>不代写 · 不伪造实验 · 不代替学生完成考核</span><Link href="/compliance">查看规范</Link></div>
    <header className="academic-header"><div className="container academic-header-row"><Link href="/" className="academic-brand"><span className="academic-brand-mark">K</span><span><b>K 博士工作室</b><small>K. RESEARCH STUDIO</small></span></Link><nav className="academic-nav process-nav"><Link href="/">首页</Link><Link href="/records">咨询记录</Link><Link href="/appointments" className="active">我的预约</Link><Link href="/compliance">研究规范</Link></nav><Link href="/process" className="header-cta">预约咨询 <ArrowRight size={16} /></Link></div></header>
    <main>
      <section className="appointments-hero"><div className="container"><p className="academic-kicker light">PERSONAL CENTER · MY APPOINTMENTS</p><h1>每一次预约，<br /><em>都有清楚的下一步。</em></h1><p>查看已提交的预约详情、导师信息与附件材料。预约确认后，我们会通过邮箱与你联系。</p></div></section>
      <section className="container appointments-content">
        <div className="appointments-topline"><div><p className="academic-kicker">APPOINTMENT HISTORY</p><h2>我的预约</h2><p>共 {appointments.length} 条预约记录</p></div><Link href="/process" className="navy-outline-button">发起新预约 <ArrowRight size={17} /></Link></div>
        <div className="appointments-layout">
          <aside className="appointment-list"><div className="appointment-list-label"><CalendarDays size={16} /> 全部预约</div>{appointments.map((appointment) => <button className={`appointment-list-item ${selected.id === appointment.id ? "active" : ""}`} key={appointment.id} onClick={() => setSelectedId(appointment.id)}><div><span>{appointment.date.replace("2026 年 ", "")}</span><b>{appointment.topic}</b><small>{appointment.mentor} · {appointment.time.split(" — ")[0]}</small></div><span className={`appointment-status ${appointment.status === "已确认" ? "confirmed" : "pending"}`}>{appointment.status}</span><ChevronRight size={16} /></button>)}</aside>
          <article className="appointment-detail">
            <div className="appointment-detail-header"><div><span className={`appointment-status large ${selected.status === "已确认" ? "confirmed" : "pending"}`}>{selected.status}</span><h2>{selected.topic}</h2><p>预约编号：{selected.id}</p></div><button className="detail-more" onClick={() => toast("预约管理功能即将上线")}>···</button></div>
            <div className="appointment-facts"><div><CalendarDays size={17} /><span><small>预约日期</small><b>{selected.date}</b></span></div><div><Clock3 size={17} /><span><small>预约时段</small><b>{selected.time}</b></span></div><div><Mail size={17} /><span><small>通知方式</small><b>邮箱确认</b></span></div></div>
            <section className="appointment-section"><div className="appointment-section-title"><UserRound size={17} /><h3>导师信息</h3></div><div className="appointment-mentor"><div className="appointment-mentor-avatar" style={{ background: selected.mentorColor }}>{selected.mentorInitial}</div><div><h3>{selected.mentor}<span><Check size={12} /> 已认证</span></h3><p>{selected.mentorRole}</p><small>计算机科学研究与技术辅导</small></div><button onClick={() => toast("消息功能即将上线")}><MessageCircle size={15} /> 联系导师</button></div></section>
            <section className="appointment-section"><div className="appointment-section-title"><MessageCircle size={17} /><h3>预约问题</h3></div><div className="appointment-request">{selected.request}</div></section>
            <section className="appointment-section"><div className="appointment-section-title"><FileCode2 size={17} /><h3>已上传附件 <span>{selected.attachments.length}</span></h3><button className="download-all" onClick={() => toast("附件下载功能即将上线")}><Download size={14} /> 下载全部</button></div><div className="attachment-list">{selected.attachments.map((file) => <div className="appointment-attachment" key={file.name}><div className={`file-icon ${file.type.toLowerCase()}`}>{file.type === "PDF" ? <FileText size={16} /> : <FileCode2 size={16} />}</div><div><b>{file.name}</b><small>{file.type} · {file.size}</small></div><button aria-label={`下载 ${file.name}`} onClick={() => toast(`${file.name} 下载功能即将上线`)}><Download size={15} /></button></div>)}</div><p className="attachment-privacy"><ShieldCheck size={14} /> 附件仅用于本次咨询准备。请勿上传他人隐私、未授权数据或违反机构规定的材料。</p></section>
          </article>
        </div>
      </section>
    </main>
    <footer className="academic-footer"><div className="container academic-footer-bottom standalone-footer"><span>© 2026 K 博士工作室 · K. Research Studio</span><Link href="/">返回首页 <ArrowLeft size={14} /></Link></div></footer>
  </div>;
}
''')

css = root / 'index.css'
style = css.read_text()
insert = '''
/* Appointments / personal center */
.appointments-hero { min-height: 332px; display: flex; align-items: center; background: var(--ink); color: var(--white); }
.appointments-hero h1 { margin: 0; font-family: "Noto Serif SC", serif; font-size: clamp(40px, 5vw, 63px); line-height: 1.3; font-weight: 500; letter-spacing: -.08em; }
.appointments-hero h1 em { font-style: normal; font-weight: 500; }
.appointments-hero p:not(.academic-kicker) { max-width: 530px; margin: 20px 0 0; color: #bfccd2; font-size: 13px; line-height: 1.9; }
.appointments-content { padding-top: 82px; padding-bottom: 105px; }
.appointments-topline { display: flex; align-items: end; justify-content: space-between; gap: 25px; }
.appointments-topline h2 { margin: 0; font-family: "Noto Serif SC", serif; font-size: 36px; letter-spacing: -.08em; }
.appointments-topline p:last-child { margin: 8px 0 0; color: #78868b; font-size: 11px; }
.appointments-layout { display: grid; grid-template-columns: 295px 1fr; gap: 25px; margin-top: 34px; }
.appointment-list { align-self: start; border-top: 1px solid var(--line); }
.appointment-list-label { display: flex; align-items: center; gap: 7px; padding: 17px 0 12px; color: #667981; font-family: "DM Mono", monospace; font-size: 10px; }
.appointment-list-item { width: 100%; display: grid; grid-template-columns: 1fr auto 16px; gap: 7px; align-items: center; padding: 17px 12px; border: 0; border-bottom: 1px solid var(--line); background: transparent; color: var(--ink); text-align: left; cursor: pointer; }
.appointment-list-item:hover, .appointment-list-item.active { background: #edf0ec; }
.appointment-list-item.active { border-left: 2px solid var(--amber); }
.appointment-list-item div span, .appointment-list-item b, .appointment-list-item small { display: block; }
.appointment-list-item div span { color: var(--amber); font-family: "DM Mono", monospace; font-size: 9px; }
.appointment-list-item b { margin: 6px 0 4px; font-size: 12px; }
.appointment-list-item small { color: #89969a; font-size: 10px; }
.appointment-list-item > svg { color: #9ca6a8; }
.appointment-status { display: inline-flex; width: fit-content; padding: 4px 6px; background: #e9e9e1; color: #77847d; font-size: 9px; white-space: nowrap; }
.appointment-status.confirmed { background: #deebe1; color: #597866; }
.appointment-status.pending { background: #f2e4d5; color: #a3683b; }
.appointment-status.large { margin-bottom: 9px; font-size: 10px; }
.appointment-detail { padding: 30px 33px 25px; background: var(--paper-light); border: 1px solid var(--line); }
.appointment-detail-header { display: flex; align-items: start; justify-content: space-between; gap: 20px; }
.appointment-detail-header h2 { margin: 0; font-family: "Noto Serif SC", serif; font-size: 28px; letter-spacing: -.07em; }
.appointment-detail-header p { margin: 8px 0 0; color: #8a969a; font-family: "DM Mono", monospace; font-size: 9px; }
.detail-more { padding: 3px 6px; border: 0; background: transparent; color: #89969a; font-size: 17px; cursor: pointer; letter-spacing: 3px; }
.appointment-facts { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; margin-top: 27px; background: var(--line); border: 1px solid var(--line); }
.appointment-facts > div { display: flex; align-items: start; gap: 9px; padding: 15px; background: #eef0eb; color: var(--amber); }
.appointment-facts small, .appointment-facts b { display: block; }
.appointment-facts small { margin-bottom: 5px; color: #849196; font-size: 9px; }
.appointment-facts b { color: var(--ink); font-size: 11px; }
.appointment-section { padding-top: 27px; margin-top: 25px; border-top: 1px solid var(--line); }
.appointment-section-title { display: flex; align-items: center; gap: 8px; color: var(--ink); }
.appointment-section-title > svg { color: var(--amber); }
.appointment-section-title h3 { margin: 0; font-size: 13px; }
.appointment-section-title h3 span { display: inline-grid; place-items: center; min-width: 16px; height: 16px; margin-left: 4px; border-radius: 50%; background: #e8e9e2; color: #798580; font-family: "DM Mono", monospace; font-size: 9px; font-weight: 400; }
.appointment-mentor { display: flex; align-items: center; gap: 15px; margin-top: 17px; padding: 17px; background: #eef0eb; }
.appointment-mentor-avatar { width: 58px; height: 70px; display: grid; place-items: center; color: var(--ink); font-family: "Noto Serif SC", serif; font-size: 25px; }
.appointment-mentor h3 { margin: 0; font-family: "Noto Serif SC", serif; font-size: 16px; }
.appointment-mentor h3 span { display: inline-flex; align-items: center; gap: 3px; margin-left: 8px; color: #64806b; font-family: "DM Sans", sans-serif; font-size: 9px; font-weight: 400; }
.appointment-mentor p { margin: 6px 0 4px; font-size: 11px; }
.appointment-mentor small { color: #7d898e; font-size: 10px; }
.appointment-mentor button { display: inline-flex; align-items: center; gap: 6px; margin-left: auto; padding: 8px 10px; border: 1px solid #b7c4bd; background: #fffefa; color: var(--ink); font-size: 10px; cursor: pointer; }
.appointment-mentor button:hover { border-color: var(--amber); color: var(--amber); }
.appointment-request { margin-top: 14px; padding: 15px 17px; background: #f0eee8; color: #66767d; font-size: 12px; line-height: 1.85; }
.download-all { display: inline-flex; align-items: center; gap: 5px; margin-left: auto; padding: 4px 0; border: 0; border-bottom: 1px solid #9ba7a7; background: transparent; color: #667981; font-size: 10px; cursor: pointer; }
.download-all:hover { color: var(--amber); border-color: var(--amber); }
.attachment-list { display: grid; grid-template-columns: 1fr 1fr; gap: 9px; margin-top: 14px; }
.appointment-attachment { display: grid; grid-template-columns: 34px 1fr 20px; gap: 8px; align-items: center; padding: 11px; border: 1px solid #d5dad4; background: #fffefa; }
.file-icon { width: 32px; height: 35px; display: grid; place-items: center; color: #70867a; background: #e7eee8; }
.file-icon.pdf { color: #ae6e4a; background: #f1e5dd; }
.appointment-attachment b, .appointment-attachment small { display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.appointment-attachment b { font-size: 10px; }
.appointment-attachment small { margin-top: 4px; color: #89969a; font-family: "DM Mono", monospace; font-size: 8px; }
.appointment-attachment > button { padding: 2px; border: 0; background: transparent; color: #89969a; cursor: pointer; }
.appointment-attachment > button:hover { color: var(--amber); }
.attachment-privacy { display: flex; align-items: start; gap: 6px; margin: 14px 0 0; color: #83908e; font-size: 9px; line-height: 1.6; }
.attachment-privacy svg { flex: none; color: #6d8b76; }

@media (max-width: 920px) {
  .appointments-layout { grid-template-columns: 235px 1fr; gap: 18px; }
  .appointment-detail { padding: 24px 21px; }
  .appointment-mentor { align-items: start; flex-wrap: wrap; }
  .appointment-mentor button { margin-left: 73px; }
}
@media (max-width: 680px) {
  .appointments-hero { min-height: 320px; }
  .appointments-content { padding-top: 62px; padding-bottom: 74px; }
  .appointments-topline { align-items: start; flex-direction: column; }
  .appointments-topline h2 { font-size: 30px; }
  .appointments-layout { display: block; margin-top: 27px; }
  .appointment-list { margin-bottom: 25px; }
  .appointment-list-item { display: none; }
  .appointment-list-item.active { display: grid; }
  .appointment-detail { padding: 22px 14px; }
  .appointment-detail-header h2 { font-size: 23px; }
  .appointment-facts { grid-template-columns: 1fr; }
  .appointment-facts > div { padding: 12px; }
  .appointment-mentor { display: grid; grid-template-columns: 58px 1fr; }
  .appointment-mentor button { grid-column: 1 / -1; width: fit-content; margin-left: 0; }
  .attachment-list { grid-template-columns: 1fr; }
}
'''
marker = '/* Appointments / personal center */'
if marker not in style:
    style += '\n' + insert
css.write_text(style)
''
