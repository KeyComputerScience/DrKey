from pathlib import Path

root = Path('/home/ubuntu/jingxuan-store/client/src')
app = root / 'App.tsx'
s = app.read_text()
s = s.replace('import Records from "./pages/Records";', 'import Records from "./pages/Records";\nimport MentorProfile from "./pages/MentorProfile";')
s = s.replace('<Route path="/appointments" component={Appointments} />', '<Route path="/appointments" component={Appointments} /><Route path="/mentors/:slug" component={MentorProfile} />')
app.write_text(s)

home = root / 'pages/Home.tsx'
s = home.read_text()
s = s.replace('<div className="mentor-availability"><span>最近可约</span>{mentor.availability.map((slot) => <button key={slot} onClick={() => { toast.success(`已选择 ${mentor.name} · ${slot}`); setConsultOpen(true); }}>{slot}</button>)}</div><button onClick={() => setConsultOpen(true)}>预约沟通 <ArrowRight size={15} /></button>', '<div className="mentor-availability"><span>最近可约</span>{mentor.availability.map((slot) => <button key={slot} onClick={() => { toast.success(`已选择 ${mentor.name} · ${slot}`); setConsultOpen(true); }}>{slot}</button>)}</div><div className="mentor-card-actions"><Link href={`/mentors/${mentor.name === "K 博士" ? "k" : mentor.name === "陈老师" ? "chen" : "lin"}`} className="mentor-profile-link">查看个人主页 <ArrowRight size={14} /></Link><button onClick={() => setConsultOpen(true)}>预约沟通 <ArrowRight size={15} /></button></div>')
home.write_text(s)

page = root / 'pages/MentorProfile.tsx'
page.write_text('''import { ArrowLeft, ArrowRight, CalendarDays, Check, Clock3, Mail, MessageCircle, ShieldCheck, Star, UserRound } from "lucide-react";
import { Link, useRoute } from "wouter";
import { toast } from "sonner";

type Review = { name: string; date: string; rating: number; content: string; topic: string };
type Mentor = { name: string; role: string; school: string; initials: string; color: string; directions: string[]; tags: string[]; availability: string[]; bio: string; reviews: Review[] };

const mentorMap: Record<string, Mentor> = {
  k: { name: "K 博士", role: "机器学习 · 算法研究", school: "博士 / 计算机科学研究与教学", initials: "K", color: "#d9e4e5", directions: ["机器学习", "算法研究", "实验设计"], tags: ["深度学习", "实验设计", "模型评估"], availability: ["周三 19:00", "周五 14:30"], bio: "关注如何把一个模糊的研究想法，转化为可验证的算法问题与实验计划。辅导中重视假设、基线、指标与复现记录的连贯性。", reviews: [
    { name: "匿名学生 A", date: "2026.09.12", rating: 5, topic: "实验复现", content: "没有直接替我改代码，而是带我一步步定位环境、随机种子和指标记录的问题。现在我知道如何自己排查了。" },
    { name: "匿名学生 B", date: "2026.08.28", rating: 5, topic: "研究设计", content: "很擅长把复杂的模型选择讲成清楚的研究决策，讨论后实验计划具体了很多。" },
    { name: "匿名学生 C", date: "2026.07.19", rating: 4, topic: "论文方法", content: "反馈非常具体，尤其是基线与消融实验部分。希望后续能增加更多关于论文英文表达的时间。" },
  ] },
  chen: { name: "陈老师", role: "系统 · 工程实践", school: "博士 / 分布式系统与性能优化", initials: "陈", color: "#e7dcc8", directions: ["系统工程", "工程实践", "分布式"], tags: ["系统论文", "代码复现", "性能分析"], availability: ["周四 10:00", "周六 15:00"], bio: "从系统架构、并发模型和性能数据出发，帮助你把工程实现讲成可复现、可论证的研究工作。", reviews: [
    { name: "匿名学生 D", date: "2026.09.03", rating: 5, topic: "系统性能", content: "讨论后终于知道该如何设计对照实验，老师对性能瓶颈的解释特别清楚。" },
    { name: "匿名学生 E", date: "2026.08.11", rating: 4, topic: "代码复现", content: "很有耐心地帮我读懂了开源仓库的结构，也提醒了很多容易忽略的实验变量。" },
  ] },
  lin: { name: "林老师", role: "论文 · 学术表达", school: "博士 / 计算机论文写作与评审", initials: "林", color: "#dce2d5", directions: ["论文写作", "学术表达", "研究结构"], tags: ["结构梳理", "英文润色", "论证反馈"], availability: ["周二 20:00", "周日 10:30"], bio: "擅长从研究问题、方法章节到实验讨论，帮助你建立一条完整且由自己负责的论证链路。", reviews: [
    { name: "匿名学生 F", date: "2026.09.05", rating: 5, topic: "论文结构", content: "评价非常具体，不只是修改句子，而是帮我理解每一段应该承担什么论证功能。" },
    { name: "匿名学生 G", date: "2026.08.22", rating: 5, topic: "学术表达", content: "会先问清楚研究问题再给反馈，整个过程很尊重学生的判断和写作责任。" },
  ] },
};

function Rating({ value, size = 15 }: { value: number; size?: number }) { return <span className="rating-stars-static" aria-label={`${value} 分`}>{[1, 2, 3, 4, 5].map((star) => <Star key={star} size={size} fill={star <= value ? "currentColor" : "none"} />)}</span>; }

export default function MentorProfile() {
  const [, params] = useRoute("/mentors/:slug");
  const mentor = mentorMap[params?.slug || "k"] || mentorMap.k;
  const average = (mentor.reviews.reduce((sum, review) => sum + review.rating, 0) / mentor.reviews.length).toFixed(1);
  return <div className="academic-site mentor-profile-page">
    <div className="integrity-bar"><ShieldCheck size={14} /><span>研究诚信优先</span><i /><span>不代写 · 不伪造实验 · 不代替学生完成考核</span><Link href="/compliance">查看规范</Link></div>
    <header className="academic-header"><div className="container academic-header-row"><Link href="/" className="academic-brand"><span className="academic-brand-mark">K</span><span><b>K 博士工作室</b><small>K. RESEARCH STUDIO</small></span></Link><nav className="academic-nav process-nav"><Link href="/">首页</Link><Link href="/#mentors">导师团队</Link><Link href="/records">咨询记录</Link><Link href="/appointments">我的预约</Link></nav><Link href="/process" className="header-cta">预约咨询 <ArrowRight size={16} /></Link></div></header>
    <main><section className="mentor-profile-hero"><div className="container mentor-profile-hero-inner"><Link href="/#mentors" className="back-link light-link"><ArrowLeft size={15} /> 返回导师团队</Link><div className="profile-identity"><div className="profile-avatar" style={{ background: mentor.color }}>{mentor.initials}</div><div><p className="academic-kicker light">MENTOR PROFILE · VERIFIED</p><h1>{mentor.name}</h1><p>{mentor.role}</p><small>{mentor.school}</small></div></div></div></section>
      <section className="container mentor-profile-content"><div className="profile-main"><section className="profile-intro"><p className="academic-kicker">ABOUT THE MENTOR</p><h2>把技术问题，<em>讲成可行动的研究计划。</em></h2><p>{mentor.bio}</p><div className="profile-tags">{mentor.tags.map((tag) => <span key={tag}>{tag}</span>)}</div></section><section className="reviews-section"><div className="reviews-heading"><div><p className="academic-kicker">STUDENT REVIEWS</p><h2>过往学生的真实反馈</h2><p>评价来自已完成咨询的学生，内容经过匿名化处理。</p></div><div className="rating-summary"><strong>{average}</strong><Rating value={Math.round(Number(average))} size={16} /><span>基于 {mentor.reviews.length} 条评价</span></div></div><div className="review-list">{mentor.reviews.map((review) => <article className="public-review" key={`${review.name}-${review.date}`}><div className="public-review-top"><div><b>{review.name}</b><span>{review.topic}</span></div><div><Rating value={review.rating} size={13} /><small>{review.date}</small></div></div><p>“{review.content}”</p></article>)}</div></section></div><aside className="profile-sidebar"><div className="profile-booking-card"><p className="academic-kicker">BOOK A SESSION</p><h3>预约 {mentor.name}</h3><p>选择一个合适的技术方向与时间，开始一次有记录的研究支持。</p><div className="profile-availability"><span><CalendarDays size={14} /> 最近可约</span>{mentor.availability.map((slot) => <button key={slot} onClick={() => toast.success(`已选择 ${mentor.name} · ${slot}`)}><Clock3 size={13} /> {slot}</button>)}</div><Link href="/process" className="navy-button">预约咨询 <ArrowRight size={16} /></Link></div><div className="profile-facts"><div><UserRound size={16} /><span><small>研究方向</small><b>{mentor.directions.join(" · ")}</b></span></div><div><MessageCircle size={16} /><span><small>辅导方式</small><b>线上一对一沟通</b></span></div><div><Mail size={16} /><span><small>回复时间</small><b>1 个工作日内</b></span></div></div><div className="profile-integrity"><ShieldCheck size={17} /><p><b>研究诚信承诺</b>所有论文、代码与实验由学生本人完成，导师只提供解释、反馈与方法支持。</p></div></aside></section>
    </main><footer className="academic-footer"><div className="container academic-footer-bottom standalone-footer"><span>© 2026 K 博士工作室 · K. Research Studio</span><Link href="/">返回首页 <ArrowLeft size={14} /></Link></div></footer>
  </div>;
}
''')

css = root / 'index.css'
style = css.read_text()
style += '''
/* Public mentor profile and reviews */
.mentor-card-actions { display: flex; align-items: center; justify-content: space-between; gap: 9px; }
.mentor-profile-link { display: inline-flex; align-items: center; gap: 5px; color: #6e7f82; font-size: 10px; }
.mentor-profile-link:hover { color: var(--amber); }
.mentor-profile-hero { min-height: 300px; display: flex; align-items: center; background: var(--ink); color: var(--white); }
.mentor-profile-hero-inner { position: relative; }
.light-link { color: #c8d2d3; }
.light-link:hover { color: var(--amber-light); }
.back-link { display: inline-flex; align-items: center; gap: 6px; margin-bottom: 33px; font-size: 10px; }
.profile-identity { display: flex; align-items: center; gap: 21px; }
.profile-avatar { width: 96px; height: 111px; display: grid; place-items: center; color: var(--ink); font-family: "Noto Serif SC", serif; font-size: 40px; }
.profile-identity h1 { margin: 6px 0 8px; font-family: "Noto Serif SC", serif; font-size: clamp(35px, 5vw, 53px); font-weight: 500; letter-spacing: -.09em; }
.profile-identity p:not(.academic-kicker) { margin: 0 0 6px; color: #d7dfdd; font-size: 13px; }
.profile-identity small { color: #aebfc1; font-size: 11px; }
.mentor-profile-content { display: grid; grid-template-columns: minmax(0, 1fr) 310px; gap: 50px; padding-top: 82px; padding-bottom: 105px; }
.profile-intro { padding-bottom: 46px; border-bottom: 1px solid var(--line); }
.profile-intro h2 { max-width: 590px; margin: 0; font-family: "Noto Serif SC", serif; font-size: clamp(27px, 3vw, 39px); font-weight: 500; line-height: 1.45; letter-spacing: -.08em; }
.profile-intro h2 em { display: block; color: #567266; font-style: normal; }
.profile-intro > p:not(.academic-kicker) { max-width: 650px; margin: 18px 0 0; color: #6d7d81; font-size: 12px; line-height: 1.95; }
.profile-tags { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 21px; }
.profile-tags span { padding: 6px 8px; background: #e8eee9; color: #60776b; font-size: 9px; }
.reviews-section { padding-top: 44px; }
.reviews-heading { display: flex; align-items: end; justify-content: space-between; gap: 25px; }
.reviews-heading h2 { margin: 0; font-family: "Noto Serif SC", serif; font-size: 28px; letter-spacing: -.07em; }
.reviews-heading p:last-child { margin: 7px 0 0; color: #829095; font-size: 10px; }
.rating-summary { min-width: 124px; padding: 13px; background: #edf0eb; text-align: center; }
.rating-summary strong { display: block; margin-bottom: 5px; color: var(--ink); font-family: "DM Mono", monospace; font-size: 25px; }
.rating-summary span { display: block; margin-top: 5px; color: #8a9698; font-size: 9px; }
.rating-stars-static { display: inline-flex; gap: 2px; color: var(--amber); vertical-align: middle; }
.review-list { margin-top: 23px; border-top: 1px solid var(--line); }
.public-review { padding: 21px 0; border-bottom: 1px solid var(--line); }
.public-review-top { display: flex; align-items: start; justify-content: space-between; gap: 15px; }
.public-review-top > div:first-child b, .public-review-top > div:first-child span { display: block; }
.public-review-top b { font-size: 11px; }
.public-review-top > div:first-child span { margin-top: 5px; color: #9aa4a5; font-size: 9px; }
.public-review-top > div:last-child { display: flex; align-items: center; gap: 11px; }
.public-review-top small { color: #9aa4a5; font-family: "DM Mono", monospace; font-size: 8px; }
.public-review > p { max-width: 690px; margin: 12px 0 0; color: #63747a; font-size: 11px; line-height: 1.85; }
.profile-sidebar { align-self: start; }
.profile-booking-card { padding: 25px; background: var(--ink); color: var(--white); }
.profile-booking-card h3 { margin: 0; font-family: "Noto Serif SC", serif; font-size: 24px; letter-spacing: -.06em; }
.profile-booking-card > p:not(.academic-kicker) { margin: 9px 0 20px; color: #b9c9ca; font-size: 11px; line-height: 1.7; }
.profile-availability { display: grid; gap: 7px; padding: 13px 0 17px; border-top: 1px solid #3a5260; }
.profile-availability > span { display: flex; align-items: center; gap: 6px; color: #c4d1ce; font-family: "DM Mono", monospace; font-size: 9px; }
.profile-availability button { display: flex; align-items: center; gap: 6px; padding: 8px 9px; border: 1px solid #506672; background: #223f50; color: #e5ece6; font-family: "DM Mono", monospace; font-size: 9px; text-align: left; cursor: pointer; }
.profile-availability button:hover { border-color: var(--amber-light); color: var(--amber-light); }
.profile-booking-card .navy-button { width: 100%; justify-content: center; background: var(--amber); color: var(--ink); }
.profile-facts { display: grid; gap: 1px; margin-top: 17px; background: var(--line); border: 1px solid var(--line); }
.profile-facts > div { display: flex; align-items: start; gap: 9px; padding: 13px; background: #edf0eb; color: var(--amber); }
.profile-facts small, .profile-facts b { display: block; }
.profile-facts small { margin-bottom: 4px; color: #88969a; font-size: 9px; }
.profile-facts b { color: var(--ink); font-size: 10px; line-height: 1.45; }
.profile-integrity { display: flex; gap: 9px; margin-top: 17px; padding: 13px; background: #f2eee5; color: #6f7e7b; }
.profile-integrity svg { flex: none; color: #6b8b74; }
.profile-integrity p { margin: 0; font-size: 9px; line-height: 1.75; }
.profile-integrity b { display: block; margin-bottom: 3px; color: var(--ink); font-size: 10px; }
@media (max-width: 820px) { .mentor-profile-content { grid-template-columns: 1fr; gap: 35px; } .profile-sidebar { order: -1; } .profile-booking-card { max-width: 540px; } }
@media (max-width: 560px) { .mentor-profile-hero { min-height: 330px; } .profile-identity { align-items: start; flex-direction: column; gap: 15px; } .profile-avatar { width: 68px; height: 76px; font-size: 28px; } .profile-identity h1 { font-size: 38px; } .mentor-profile-content { padding-top: 60px; padding-bottom: 74px; } .reviews-heading { align-items: start; flex-direction: column; } .rating-summary { width: 100%; } .public-review-top { flex-direction: column; } .public-review-top > div:last-child { justify-content: space-between; width: 100%; } }
'''
css.write_text(style)
''
