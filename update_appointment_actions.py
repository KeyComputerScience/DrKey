from pathlib import Path

page = Path('/home/ubuntu/jingxuan-store/client/src/pages/Appointments.tsx')
s = page.read_text()
s = s.replace('import { useState } from "react";', 'import { useState } from "react";')
s = s.replace('import { ArrowLeft, ArrowRight, CalendarDays, Check, ChevronRight, Clock3, Download, FileCode2, FileText, Mail, MessageCircle, ShieldCheck, UserRound } from "lucide-react";', 'import { ArrowLeft, ArrowRight, CalendarDays, Check, CheckCircle2, ChevronRight, Clock3, Download, FileCode2, FileText, Mail, MessageCircle, Send, ShieldCheck, Star, UserRound, X } from "lucide-react";')
s = s.replace('status: "已确认" | "待确认";', 'status: "已确认" | "待确认" | "已完成";')
s = s.replace('    attachments: [{ name: "system_architecture.zip", type: "ZIP", size: "4.8 MB" }],\n  },\n];', '''    attachments: [{ name: "system_architecture.zip", type: "ZIP", size: "4.8 MB" }],
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
];''')
s = s.replace('  const [selectedId, setSelectedId] = useState(appointments[0].id);\n  const selected = appointments.find((item) => item.id === selectedId) || appointments[0];', '''  const [selectedId, setSelectedId] = useState(appointments[0].id);
  const [messages, setMessages] = useState([{ from: "导师", text: "你好，收到你的材料了。我们会先从随机种子和指标记录开始排查。", time: "9 月 18 日 16:20" }]);
  const [messageText, setMessageText] = useState("");
  const [managementAction, setManagementAction] = useState<"cancel" | "reschedule" | null>(null);
  const [showReview, setShowReview] = useState(false);
  const [reviewRating, setReviewRating] = useState(0);
  const [reviewText, setReviewText] = useState("");
  const [cancelledIds, setCancelledIds] = useState<string[]>([]);
  const selected = appointments.find((item) => item.id === selectedId) || appointments[0];
  const isCancelled = cancelledIds.includes(selected.id);''')
s = s.replace('<button className="detail-more" onClick={() => toast("预约管理功能即将上线")}>···</button>', '''<div className="appointment-actions"><button onClick={() => setManagementAction("reschedule")} disabled={isCancelled || selected.status === "已完成"}><Clock3 size={14} /> 修改时间</button><button className="danger-action" onClick={() => setManagementAction("cancel")} disabled={isCancelled || selected.status === "已完成"}><X size={14} /> 取消预约</button></div>''')
s = s.replace('<section className="appointment-section"><div className="appointment-section-title"><MessageCircle size={17} /><h3>预约问题</h3></div><div className="appointment-request">{selected.request}</div></section>', '''<section className="appointment-section"><div className="appointment-section-title"><MessageCircle size={17} /><h3>预约问题</h3></div><div className="appointment-request">{selected.request}</div></section>
            {selected.status !== "已完成" && !isCancelled && <section className="appointment-section message-board-section"><div className="appointment-section-title"><MessageCircle size={17} /><h3>留言板 <span>{messages.length}</span></h3><small>预约前沟通</small></div><div className="message-board">{messages.map((message, index) => <div className={`message-bubble ${message.from === "学生" ? "student" : ""}`} key={`${message.time}-${index}`}><div><b>{message.from}</b><small>{message.time}</small></div><p>{message.text}</p></div>)}</div><form className="message-form" onSubmit={(event) => { event.preventDefault(); if (!messageText.trim()) return; setMessages((current) => [...current, { from: "学生", text: messageText.trim(), time: "刚刚" }]); setMessageText(""); toast.success("留言已发送"); }}><input value={messageText} onChange={(event) => setMessageText(event.target.value)} placeholder="给导师留一句话，例如：我已补充实验日志" aria-label="留言内容" /><button type="submit" aria-label="发送留言"><Send size={15} /></button></form><p className="message-note"><ShieldCheck size={13} /> 仅用于本次预约的简单沟通，请勿发送隐私或敏感数据。</p></section>}
            {selected.status === "已完成" && <section className="appointment-section review-section"><div className="appointment-section-title"><Star size={17} /><h3>评价本次辅导</h3></div><div className="review-panel"><p>这次辅导是否帮助你更清楚地推进了研究？</p><div className="rating-stars">{[1, 2, 3, 4, 5].map((rating) => <button key={rating} className={reviewRating >= rating ? "active" : ""} onClick={() => setReviewRating(rating)} aria-label={`${rating} 分`}><Star size={23} fill={reviewRating >= rating ? "currentColor" : "none"} /></button>)}</div><textarea value={reviewText} onChange={(event) => setReviewText(event.target.value)} placeholder="写下你对导师讲解、反馈或节奏的感受（可选）" /><button className="navy-button review-submit" disabled={!reviewRating} onClick={() => { toast.success("感谢你的评价"); setShowReview(true); }}>{showReview ? "评价已提交" : "提交评价"} <ArrowRight size={16} /></button></div></section>}''')
s = s.replace('</article>\n        </div>\n      </section>', '''</article>
        </div>
      </section>''')
# Insert management modal before main closing footer
needle = '    <footer className="academic-footer"><div className="container academic-footer-bottom standalone-footer"><span>© 2026 K 博士工作室 · K. Research Studio</span><Link href="/">返回首页 <ArrowLeft size={14} /></Link></div></footer>'
replacement = '''    <footer className="academic-footer"><div className="container academic-footer-bottom standalone-footer"><span>© 2026 K 博士工作室 · K. Research Studio</span><Link href="/">返回首页 <ArrowLeft size={14} /></Link></div></footer>
    {managementAction && <div className="simple-modal-backdrop" onClick={() => setManagementAction(null)}><div className="appointment-confirm-modal" onClick={(event) => event.stopPropagation()}><button className="modal-close-button" onClick={() => setManagementAction(null)}><X size={19} /></button><div className={`confirm-icon ${managementAction === "cancel" ? "cancel" : ""}`}>{managementAction === "cancel" ? <X size={25} /> : <Clock3 size={25} />}</div><p className="academic-kicker">{managementAction === "cancel" ? "CANCEL APPOINTMENT" : "RESCHEDULE APPOINTMENT"}</p><h2>{managementAction === "cancel" ? "确认取消这次预约？" : "选择新的预约时间"}</h2>{managementAction === "cancel" ? <p>取消后，当前时段将被释放。你仍可以稍后重新发起预约。</p> : <><p>当前时间：{selected.date} · {selected.time}</p><select className="reschedule-select" defaultValue=""><option value="" disabled>请选择新的时间</option><option>2026 年 9 月 27 日 · 19:00 — 19:50</option><option>2026 年 9 月 29 日 · 14:30 — 15:20</option><option>2026 年 10 月 1 日 · 10:00 — 10:50</option></select></>}<div className="confirm-actions"><button className="plain-cancel" onClick={() => setManagementAction(null)}>暂不操作</button><button className={`navy-button ${managementAction === "cancel" ? "danger-button" : ""}`} onClick={() => { if (managementAction === "cancel") { setCancelledIds((current) => [...current, selected.id]); toast.success("预约已取消"); } else { toast.success("修改时间申请已提交"); } setManagementAction(null); }}>{managementAction === "cancel" ? "确认取消" : "提交修改"} <ArrowRight size={16} /></button></div></div></div>}
  </div>;'''
if needle not in s:
    raise SystemExit('footer modal target not found')
s = s.replace(needle, replacement)
page.write_text(s)

css = Path('/home/ubuntu/jingxuan-store/client/src/index.css')
style = css.read_text()
insert = '''
/* Appointment message board, review, and management actions */
.appointment-actions { display: flex; align-items: center; gap: 7px; }
.appointment-actions button { display: inline-flex; align-items: center; gap: 5px; min-height: 30px; padding: 0 9px; border: 1px solid #bdc8c1; background: #fffefa; color: #5f746a; font-size: 10px; cursor: pointer; }
.appointment-actions button:hover:not(:disabled) { border-color: var(--amber); color: var(--amber); }
.appointment-actions button:disabled { cursor: not-allowed; opacity: .4; }
.appointment-actions .danger-action { color: #9b6551; }
.appointment-actions .danger-action:hover:not(:disabled) { border-color: #a96850; color: #a96850; }
.message-board-section .appointment-section-title > small { margin-left: auto; color: #89969a; font-size: 9px; }
.message-board { display: grid; gap: 9px; max-height: 175px; overflow-y: auto; padding: 13px 0 5px; }
.message-bubble { max-width: 80%; padding: 10px 12px; background: #edf1ec; }
.message-bubble.student { justify-self: end; background: #f3e8dc; }
.message-bubble > div { display: flex; align-items: center; gap: 9px; }
.message-bubble b { color: var(--ink); font-size: 10px; }
.message-bubble small { color: #99a3a4; font-family: "DM Mono", monospace; font-size: 8px; }
.message-bubble p { margin: 6px 0 0; color: #68777c; font-size: 10px; line-height: 1.65; }
.message-form { display: flex; margin-top: 7px; border: 1px solid #cbd3cd; background: #fffefa; }
.message-form input { min-width: 0; flex: 1; height: 35px; padding: 0 10px; border: 0; outline: 0; background: transparent; color: var(--ink); font-size: 10px; }
.message-form button { width: 36px; display: grid; place-items: center; border: 0; background: var(--ink); color: var(--white); cursor: pointer; }
.message-form button:hover { background: #294b62; }
.message-note { display: flex; align-items: center; gap: 5px; margin: 8px 0 0; color: #8b9899; font-size: 9px; }
.message-note svg { color: #6b8b74; }
.review-panel { margin-top: 14px; padding: 17px; background: #edf0ec; }
.review-panel > p { margin: 0; color: #63757a; font-size: 11px; }
.rating-stars { display: flex; gap: 4px; margin: 12px 0 13px; }
.rating-stars button { padding: 0; border: 0; background: transparent; color: #c9d0ca; cursor: pointer; }
.rating-stars button.active { color: var(--amber); }
.review-panel textarea { width: 100%; min-height: 68px; padding: 9px; border: 1px solid #d0d7d0; outline: 0; background: #fffefa; color: var(--ink); font-size: 10px; resize: vertical; }
.review-submit { margin-top: 11px; min-height: 34px; font-size: 10px; }
.review-submit:disabled { cursor: not-allowed; opacity: .45; }
.appointment-confirm-modal { width: min(450px, 100%); padding: 36px 32px 29px; background: var(--paper-light); box-shadow: 0 23px 65px rgba(7,25,38,.3); text-align: center; }
.confirm-icon { width: 55px; height: 55px; display: grid; place-items: center; margin: 0 auto 17px; border: 1px solid #bd9a6a; border-radius: 50%; background: #f3e9dc; color: var(--amber); }
.confirm-icon.cancel { border-color: #c9937f; background: #f3e4de; color: #a5654d; }
.appointment-confirm-modal h2 { margin: 0; font-family: "Noto Serif SC", serif; font-size: 26px; letter-spacing: -.07em; }
.appointment-confirm-modal > p:not(.academic-kicker) { margin: 12px auto 18px; color: #6d7c81; font-size: 11px; line-height: 1.8; }
.reschedule-select { width: 100%; height: 38px; padding: 0 10px; border: 1px solid #cbd3cd; background: #fffefa; color: var(--ink); font-size: 11px; outline: 0; }
.confirm-actions { display: flex; justify-content: center; gap: 9px; margin-top: 21px; }
.plain-cancel { min-height: 37px; padding: 0 13px; border: 1px solid #c2ccc6; background: transparent; color: #6d7d80; font-size: 10px; cursor: pointer; }
.plain-cancel:hover { border-color: var(--ink); color: var(--ink); }
.danger-button { background: #9b6551; }
.danger-button:hover { background: #854e3c; }
@media (max-width: 680px) {
  .appointment-actions { align-items: end; flex-direction: column; }
  .appointment-actions button { width: 88px; justify-content: center; font-size: 9px; }
  .message-bubble { max-width: 90%; }
  .appointment-confirm-modal { padding: 31px 20px 24px; }
}
'''
marker = '/* Appointments / personal center */'
if '/* Appointment message board, review, and management actions */' not in style:
    style = style.replace(marker, insert + '\n' + marker, 1)
css.write_text(style)
''
