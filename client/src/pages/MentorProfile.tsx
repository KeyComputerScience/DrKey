import { ArrowLeft, ArrowRight, Check, Mail, MessageCircle, ShieldCheck, Star, UserRound } from "lucide-react";
import { Link, useRoute } from "wouter";
import { toast } from "sonner";

type Review = { name: string; date: string; rating: number; content: string; topic: string };
type Mentor = { name: string; role: string; school: string; initials: string; color: string; directions: string[]; tags: string[]; bio: string; reviews: Review[] };

const mentorMap: Record<string, Mentor> = {
  k: { name: "K 博士", role: "信息安全 · 安全研究", school: "博士 / 计算机科学研究与教学", initials: "K", color: "#d9e4e5", directions: ["信息安全", "安全研究", "实验评估"], tags: ["安全机制", "威胁建模", "实验评估"], bio: "关注如何把一个模糊的研究想法，转化为可验证的算法问题与实验计划。辅导中重视假设、基线、指标与复现记录的连贯性。", reviews: [
    { name: "匿名学生 A", date: "2026.09.12", rating: 5, topic: "实验复现", content: "没有直接替我改代码，而是带我一步步定位环境、随机种子和指标记录的问题。现在我知道如何自己排查了。" },
    { name: "匿名学生 B", date: "2026.08.28", rating: 5, topic: "研究设计", content: "很擅长把复杂的模型选择讲成清楚的研究决策，讨论后实验计划具体了很多。" },
    { name: "匿名学生 C", date: "2026.07.19", rating: 4, topic: "论文方法", content: "反馈非常具体，尤其是基线与消融实验部分。希望后续能增加更多关于论文英文表达的时间。" },
  ] },
  chen: { name: "陈老师", role: "系统架构 · 通信网络", school: "博士 / 分布式系统与性能优化", initials: "陈", color: "#e7dcc8", directions: ["系统与架构研究", "通信网络"], tags: ["系统架构", "网络协议", "性能分析"], bio: "从系统架构、并发模型和性能数据出发，帮助你把工程实现讲成可复现、可论证的研究工作。", reviews: [
    { name: "匿名学生 D", date: "2026.09.03", rating: 5, topic: "系统性能", content: "讨论后终于知道该如何设计对照实验，老师对性能瓶颈的解释特别清楚。" },
    { name: "匿名学生 E", date: "2026.08.11", rating: 4, topic: "代码复现", content: "很有耐心地帮我读懂了开源仓库的结构，也提醒了很多容易忽略的实验变量。" },
  ] },
  lin: { name: "林老师", role: "信息安全 · 研究方法", school: "博士 / 计算机安全与学术研究", initials: "林", color: "#dce2d5", directions: ["信息安全", "其他"], tags: ["安全机制", "威胁建模", "研究方法"], bio: "擅长从研究问题、方法章节到实验讨论，帮助你建立一条完整且由自己负责的论证链路。", reviews: [
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
    <header className="academic-header"><div className="container academic-header-row"><Link href="/" className="academic-brand"><span className="academic-brand-mark">K</span><span><b>K 博士工作室</b><small>K. RESEARCH STUDIO</small></span></Link><nav className="academic-nav process-nav"><Link href="/">首页</Link><Link href="/#mentors">导师团队</Link><Link href="/records">咨询记录</Link><Link href="/appointments">我的预约</Link></nav><Link href="/process" className="header-cta">预约咨询 <ArrowRight size={16} /></Link></div></header>
    <main><section className="mentor-profile-hero"><div className="container mentor-profile-hero-inner"><Link href="/#mentors" className="back-link light-link"><ArrowLeft size={15} /> 返回导师团队</Link><div className="profile-identity"><div className="profile-avatar" style={{ background: mentor.color }}>{mentor.initials}</div><div><p className="academic-kicker light">MENTOR PROFILE · VERIFIED</p><h1>{mentor.name}</h1><p>{mentor.role}</p><small>{mentor.school}</small></div></div></div></section>
      <section className="container mentor-profile-content"><div className="profile-main"><section className="profile-intro"><p className="academic-kicker">ABOUT THE MENTOR</p><h2>把技术问题，<em>讲成可行动的研究计划。</em></h2><p>{mentor.bio}</p><div className="profile-tags">{mentor.tags.map((tag) => <span key={tag}>{tag}</span>)}</div></section><section className="reviews-section"><div className="reviews-heading"><div><p className="academic-kicker">STUDENT REVIEWS</p><h2>过往学生的真实反馈</h2><p>评价来自已完成咨询的学生，内容经过匿名化处理。</p></div><div className="rating-summary"><strong>{average}</strong><Rating value={Math.round(Number(average))} size={16} /><span>基于 {mentor.reviews.length} 条评价</span></div></div><div className="review-list">{mentor.reviews.map((review) => <article className="public-review" key={`${review.name}-${review.date}`}><div className="public-review-top"><div><b>{review.name}</b><span>{review.topic}</span></div><div><Rating value={review.rating} size={13} /><small>{review.date}</small></div></div><p>“{review.content}”</p></article>)}</div></section></div><aside className="profile-sidebar"><div className="profile-booking-card"><p className="academic-kicker">BOOK A SESSION</p><h3>预约 {mentor.name}</h3><p>提交你的研究问题与材料，开始一次有记录的研究支持。</p><Link href="/process" className="navy-button">预约咨询 <ArrowRight size={16} /></Link></div><div className="profile-facts"><div><UserRound size={16} /><span><small>研究方向</small><b>{mentor.directions.join(" · ")}</b></span></div><div><MessageCircle size={16} /><span><small>辅导方式</small><b>线上一对一沟通</b></span></div><div><Mail size={16} /><span><small>回复时间</small><b>1 个工作日内</b></span></div></div></aside></section>
    </main><footer className="academic-footer"><div className="container academic-footer-bottom standalone-footer"><span>© 2026 K 博士工作室 · K. Research Studio</span><Link href="/">返回首页 <ArrowLeft size={14} /></Link></div></footer>
  </div>;
}
