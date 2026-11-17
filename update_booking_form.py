from pathlib import Path

home = Path('/home/ubuntu/jingxuan-store/client/src/pages/Home.tsx')
s = home.read_text()
s = s.replace('import { useState } from "react";', 'import { useRef, useState } from "react";')
s = s.replace('import { ArrowRight, BrainCircuit, Check, ChevronDown, Code2, FileCode2, FlaskConical, GraduationCap, Menu, Network, Search, ShieldCheck, Sparkles, Users, X } from "lucide-react";', 'import { ArrowRight, BrainCircuit, Check, CheckCircle2, ChevronDown, Code2, FileCode2, FileUp, FlaskConical, GraduationCap, Loader2, Menu, Network, Search, ShieldCheck, Sparkles, Users, X } from "lucide-react";')
s = s.replace('  const [consultOpen, setConsultOpen] = useState(false);\n  const [mentorFilter', '  const [consultOpen, setConsultOpen] = useState(false);\n  const [consultSubmitting, setConsultSubmitting] = useState(false);\n  const [consultSuccess, setConsultSuccess] = useState(false);\n  const [attachmentName, setAttachmentName] = useState("");\n  const attachmentInputRef = useRef<HTMLInputElement>(null);\n  const [mentorFilter')
old = '<form onSubmit={(event) => { event.preventDefault(); toast.success("已收到你的预约意向，我们会尽快联系你"); setConsultOpen(false); }}><label>你的研究方向<select required defaultValue=""><option value="" disabled>请选择技术方向</option><option>算法与机器学习</option><option>系统与工程研究</option><option>计算机视觉 / NLP</option><option>软件工程 / 应用开发</option><option>其他计算机方向</option></select></label><label>你希望获得哪类支持<select required defaultValue=""><option value="" disabled>请选择支持方向</option><option>研究问题与方法</option><option>论文结构与表达</option><option>代码阅读与实验复现</option><option>开题与答辩辅导</option></select></label><label>一句话描述你的问题<textarea required placeholder="例如：论文方法看懂了，但无法复现实验结果"></textarea></label><label className="consent-line"><input type="checkbox" required /> <span>我已阅读并理解工作室的研究诚信边界，同意由本人完成研究、编码与写作。</span></label><button className="amber-button full" type="submit">提交预约意向 <ArrowRight size={17} /></button></form>'
new = '<form onSubmit={(event) => { event.preventDefault(); setConsultSubmitting(true); window.setTimeout(() => { setConsultSubmitting(false); setConsultOpen(false); setConsultSuccess(true); toast.success("预约意向已提交"); }, 1000); }}><label>你的研究方向<select required defaultValue=""><option value="" disabled>请选择技术方向</option><option>算法与机器学习</option><option>系统与工程研究</option><option>计算机视觉 / NLP</option><option>软件工程 / 应用开发</option><option>其他计算机方向</option></select></label><label>你希望获得哪类支持<select required defaultValue=""><option value="" disabled>请选择支持方向</option><option>研究问题与方法</option><option>论文结构与表达</option><option>代码阅读与实验复现</option><option>开题与答辩辅导</option></select></label><label>一句话描述你的问题<textarea required placeholder="例如：论文方法看懂了，但无法复现实验结果"></textarea></label><div className="attachment-field"><div className="attachment-label"><span>附加材料 <small>可选</small></span><span>PDF / ZIP / TXT · 最大 20MB</span></div><input ref={attachmentInputRef} type="file" accept=".pdf,.zip,.txt,.md,.py,.js,.ts,.java,.cpp,.ipynb" onChange={(event) => setAttachmentName(event.target.files?.[0]?.name || "")} /><button type="button" className="attachment-picker" onClick={() => attachmentInputRef.current?.click()}><FileUp size={16} /> {attachmentName || "选择代码片段或项目文档"}</button>{attachmentName && <button type="button" className="attachment-remove" onClick={() => { setAttachmentName(""); if (attachmentInputRef.current) attachmentInputRef.current.value = ""; }}>移除附件</button>}<p>附件仅用于本次咨询准备，不会被包装为你的原创成果。</p></div><label className="consent-line"><input type="checkbox" required /> <span>我已阅读并理解工作室的研究诚信边界，同意由本人完成研究、编码与写作。</span></label><button className="amber-button full" type="submit" disabled={consultSubmitting}>{consultSubmitting ? <><Loader2 className="spin" size={17} /> 正在提交预约…</> : <>提交预约意向 <ArrowRight size={17} /></>}</button></form>'
if old not in s:
    raise SystemExit('Home form target not found')
s = s.replace(old, new)
old_end = '    {consultOpen && <div className="consult-modal-backdrop" onClick={() => setConsultOpen(false)}><div className="consult-modal" role="dialog" aria-modal="true" onClick={(event) => event.stopPropagation()}>'
# Add a success overlay after the existing consult modal block by targeting the final closing around the component ending.
needle = '</div></div>}\n  </div>;\n}'
replacement = '</div></div>}\n    {consultSuccess && <div className="success-modal-backdrop" onClick={() => setConsultSuccess(false)}><div className="success-modal" role="dialog" aria-modal="true" onClick={(event) => event.stopPropagation()}><div className="success-icon"><CheckCircle2 size={30} /></div><p className="academic-kicker">REQUEST RECEIVED</p><h2>预约意向已提交</h2><p>感谢你的信任。K 博士工作室会在 <b>1 个工作日内</b> 回复可预约时段和导师匹配建议。</p>{attachmentName && <div className="success-attachment"><FileUp size={15} /> 已附加：{attachmentName}</div>}<div className="success-next"><Check size={15} /> 你可以先准备论文 PDF、代码仓库或实验日志</div><button className="navy-button" onClick={() => { setConsultSuccess(false); setAttachmentName(""); }}>好的，我知道了 <ArrowRight size={17} /></button></div></div>}\n  </div>;\n}'
if needle not in s:
    raise SystemExit('Home success insertion target not found')
s = s.replace(needle, replacement, 1)
home.write_text(s)

process = Path('/home/ubuntu/jingxuan-store/client/src/pages/Process.tsx')
s = process.read_text()
s = s.replace('import { useState } from "react";', 'import { useRef, useState } from "react";')
s = s.replace('import { ArrowRight, CalendarDays, Check, ClipboardList, Code2, FileCheck2, MessageCircle, ShieldCheck, UserRound, X } from "lucide-react";', 'import { ArrowRight, CalendarDays, Check, CheckCircle2, ClipboardList, Code2, FileCheck2, FileUp, Loader2, MessageCircle, ShieldCheck, UserRound, X } from "lucide-react";')
s = s.replace('  const [formOpen, setFormOpen] = useState(false);', '  const [formOpen, setFormOpen] = useState(false);\n  const [submitting, setSubmitting] = useState(false);\n  const [submitted, setSubmitted] = useState(false);\n  const [attachmentName, setAttachmentName] = useState("");\n  const fileRef = useRef<HTMLInputElement>(null);')
old = '<form onSubmit={(event) => { event.preventDefault(); toast.success("已收到预约意向，我们会在工作日内回复"); setFormOpen(false); }}><input required placeholder="你的称呼" /><input required type="email" placeholder="邮箱地址" /><textarea required placeholder="你的技术问题、论文方向或实验现象"></textarea><label><input type="checkbox" required /> 我已阅读并同意研究诚信边界。</label><button className="navy-button" type="submit">提交预约意向 <ArrowRight size={17} /></button></form>'
new = '<form onSubmit={(event) => { event.preventDefault(); setSubmitting(true); window.setTimeout(() => { setSubmitting(false); setFormOpen(false); setSubmitted(true); toast.success("预约意向已提交"); }, 1000); }}><input required placeholder="你的称呼" /><input required type="email" placeholder="邮箱地址" /><textarea required placeholder="你的技术问题、论文方向或实验现象"></textarea><div className="attachment-field compact"><div className="attachment-label"><span>附加材料 <small>可选</small></span><span>PDF / ZIP / TXT · 最大 20MB</span></div><input ref={fileRef} type="file" accept=".pdf,.zip,.txt,.md,.py,.js,.ts,.java,.cpp,.ipynb" onChange={(event) => setAttachmentName(event.target.files?.[0]?.name || "")} /><button type="button" className="attachment-picker" onClick={() => fileRef.current?.click()}><FileUp size={16} /> {attachmentName || "选择代码片段或项目文档"}</button>{attachmentName && <button type="button" className="attachment-remove" onClick={() => { setAttachmentName(""); if (fileRef.current) fileRef.current.value = ""; }}>移除附件</button>}<p>仅用于本次咨询准备，不会替代你的研究工作。</p></div><label><input type="checkbox" required /> 我已阅读并同意研究诚信边界。</label><button className="navy-button" type="submit" disabled={submitting}>{submitting ? <><Loader2 className="spin" size={17} /> 正在提交…</> : <>提交预约意向 <ArrowRight size={17} /></>}</button></form>'
if old not in s:
    raise SystemExit('Process form target not found')
s = s.replace(old, new)
needle = '</div></div>}\n  </div>;\n}'
replacement = '</div></div>}\n    {submitted && <div className="success-modal-backdrop" onClick={() => setSubmitted(false)}><div className="success-modal" role="dialog" aria-modal="true" onClick={(event) => event.stopPropagation()}><div className="success-icon"><CheckCircle2 size={30} /></div><p className="academic-kicker">REQUEST RECEIVED</p><h2>预约意向已提交</h2><p>感谢你的信任。我们会在 <b>1 个工作日内</b> 回复可预约时段和导师匹配建议。</p>{attachmentName && <div className="success-attachment"><FileUp size={15} /> 已附加：{attachmentName}</div>}<div className="success-next"><Check size={15} /> 下一步：准备与你问题相关的代码、论文或实验材料</div><button className="navy-button" onClick={() => { setSubmitted(false); setAttachmentName(""); }}>好的，我知道了 <ArrowRight size={17} /></button></div></div>}\n  </div>;\n}'
if needle not in s:
    raise SystemExit('Process success insertion target not found')
s = s.replace(needle, replacement, 1)
process.write_text(s)

css = Path('/home/ubuntu/jingxuan-store/client/src/index.css')
style = css.read_text()
insert = '''
/* Booking attachments, loading, and success state */
.consult-modal form .attachment-field, .simple-booking-modal form .attachment-field { display: block; padding: 10px; border: 1px dashed #c7cfca; background: #f6f7f3; }
.attachment-field > input[type="file"] { position: absolute; width: 1px; height: 1px; opacity: 0; pointer-events: none; }
.attachment-label { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 7px; color: #65777c; font-size: 10px; font-weight: 700; }
.attachment-label small { color: #9aa4a5; font-weight: 400; }
.attachment-label > span:last-child { color: #9aa5a7; font-family: "DM Mono", monospace; font-size: 8px; font-weight: 400; }
.attachment-picker { width: 100%; display: flex; align-items: center; gap: 7px; min-height: 32px; padding: 0 9px; border: 1px solid #c9d1cc; background: #fffefa; color: #5f766b; font-size: 10px; text-align: left; cursor: pointer; }
.attachment-picker:hover { border-color: var(--amber); color: #a76736; }
.attachment-field > p { margin: 7px 0 0; color: #8a9698; font-size: 9px; line-height: 1.5; }
.attachment-remove { margin-top: 6px; padding: 0; border: 0; background: transparent; color: #a76736; font-size: 9px; cursor: pointer; }
.attachment-field.compact { margin-top: 1px; }
.amber-button:disabled, .navy-button:disabled { cursor: wait; opacity: .78; }
.spin { animation: spin .8s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.success-modal-backdrop { position: fixed; inset: 0; z-index: 100; display: grid; place-items: center; padding: 20px; background: rgba(12,30,44,.52); animation: fade-in .2s ease; }
.success-modal { width: min(430px, 100%); padding: 37px 34px 31px; background: var(--paper-light); box-shadow: 0 23px 65px rgba(7,25,38,.3); text-align: center; animation: modal-in .28s cubic-bezier(.23,1,.32,1); }
.success-icon { width: 59px; height: 59px; display: grid; place-items: center; margin: 0 auto 19px; border: 1px solid #7a9a82; border-radius: 50%; background: #e4efe6; color: #5b8065; }
.success-modal h2 { margin: 0; font-family: "Noto Serif SC", serif; font-size: 28px; letter-spacing: -.07em; }
.success-modal > p:not(.academic-kicker) { margin: 13px auto 17px; color: #6e7c82; font-size: 12px; line-height: 1.8; }
.success-attachment, .success-next { display: flex; align-items: center; gap: 7px; padding: 10px 11px; margin-top: 8px; background: #edf1ec; color: #60746a; font-size: 10px; text-align: left; }
.success-attachment { color: #8c6b49; background: #f3eee5; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.success-attachment svg { flex: none; }
.success-next svg { flex: none; color: #65856c; }
.success-modal .navy-button { width: 100%; margin-top: 21px; }
'''
marker = '/* Mentor availability */'
if '/* Booking attachments, loading, and success state */' not in style:
    style = style.replace(marker, insert + '\n' + marker, 1)
css.write_text(style)
''
