from pathlib import Path

root = Path('/home/ubuntu/jingxuan-store/client/src')

home = root / 'pages/Home.tsx'
s = home.read_text()
start = s.index('const services = [')
end = s.index('];', start) + 2
services = '''const services = [
  { number: "01", icon: BrainCircuit, title: "人工智能与深度学习", description: "理解模型设计、训练策略与实验评估，建立从研究假设到可复现结果的完整链路。", tags: ["深度学习", "模型训练", "实验评估"] },
  { number: "02", icon: Search, title: "计算机图像处理", description: "围绕视觉任务、图像特征与深度视觉模型，梳理数据、方法、指标和结果分析。", tags: ["视觉算法", "图像特征", "模型评估"] },
  { number: "03", icon: Code2, title: "系统与架构研究", description: "从系统架构、并发、分布式与性能优化出发，把工程实现转化为可验证的研究问题。", tags: ["系统架构", "分布式", "性能分析"] },
  { number: "04", icon: Network, title: "通信网络", description: "理解网络协议、通信系统与性能指标，支持网络实验设计、仿真分析和结果复盘。", tags: ["网络协议", "通信系统", "网络仿真"] },
  { number: "05", icon: ShieldCheck, title: "信息安全", description: "围绕安全机制、威胁建模与隐私保护，梳理实验边界、评估方法与合规研究流程。", tags: ["安全机制", "威胁建模", "隐私保护"] },
  { number: "06", icon: FlaskConical, title: "其他", description: "如果你的计算机研究方向不在以上分类中，可以先描述问题，我们会协助匹配合适的技术支持。", tags: ["问题梳理", "方向匹配", "研究方法"] },
];'''
s = s[:start] + services + s[end:]
old = '''const mentors = [
  { name: "K 博士", role: "机器学习 · 算法研究", school: "博士 / 计算机科学研究与教学", initials: "K", color: "#d9e4e5", tags: ["深度学习", "实验设计"], directions: ["机器学习", "算法研究"], availability: ["周三 19:00", "周五 14:30"] },
  { name: "陈老师", role: "系统 · 工程实践", school: "博士 / 分布式系统与性能优化", initials: "陈", color: "#e7dcc8", tags: ["系统论文", "代码复现"], directions: ["系统工程", "工程实践"], availability: ["周四 10:00", "周六 15:00"] },
  { name: "林老师", role: "论文 · 学术表达", school: "博士 / 计算机论文写作与评审", initials: "林", color: "#dce2d5", tags: ["结构梳理", "英文润色"], directions: ["论文写作", "学术表达"], availability: ["周二 20:00", "周日 10:30"] },
];'''
new = '''const mentors = [
  { name: "K 博士", role: "人工智能 · 深度学习", school: "博士 / 计算机科学研究与教学", initials: "K", color: "#d9e4e5", tags: ["深度学习", "模型训练"], directions: ["人工智能与深度学习"], availability: ["周三 19:00", "周五 14:30"] },
  { name: "陈老师", role: "系统架构 · 通信网络", school: "博士 / 分布式系统与性能优化", initials: "陈", color: "#e7dcc8", tags: ["系统架构", "网络性能"], directions: ["系统与架构研究", "通信网络"], availability: ["周四 10:00", "周六 15:00"] },
  { name: "林老师", role: "信息安全 · 研究方法", school: "博士 / 计算机安全与学术研究", initials: "林", color: "#dce2d5", tags: ["安全机制", "威胁建模"], directions: ["信息安全", "其他"], availability: ["周二 20:00", "周日 10:30"] },
];'''
if old not in s: raise SystemExit('mentor data target not found')
s = s.replace(old, new)
s = s.replace('const mentorFilters = ["全部", "机器学习", "系统工程", "论文写作"];', 'const mentorFilters = ["全部", "人工智能与深度学习", "计算机图像处理", "系统与架构研究", "通信网络", "信息安全", "其他"];')
s = s.replace('<option>算法与机器学习</option><option>系统与工程研究</option><option>计算机视觉 / NLP</option><option>软件工程 / 应用开发</option><option>其他计算机方向</option>', '<option>人工智能与深度学习</option><option>计算机图像处理</option><option>系统与架构研究</option><option>通信网络</option><option>信息安全</option><option>其他</option>')
s = s.replace('<option>研究问题与方法</option><option>论文结构与表达</option><option>代码阅读与实验复现</option><option>开题与答辩辅导</option>', '<option>研究问题与方法</option><option>代码与实验复现</option><option>实验设计与结果分析</option><option>论文结构与表达</option>')
s = s.replace('算法、系统、代码与论文表达的过程性支持', '人工智能、图像处理、系统架构、通信网络与信息安全的过程性支持')
s = s.replace('算法与机器学习</Link><Link href="/#services">系统与工程研究</Link><Link href="/#services">代码与实验复现', '人工智能与深度学习</Link><Link href="/#services">计算机图像处理</Link><Link href="/#services">系统与架构研究</Link><Link href="/#services">通信网络</Link><Link href="/#services">信息安全</Link><Link href="/#services">其他')
home.write_text(s)

process = root / 'pages/Process.tsx'
s = process.read_text()
s = s.replace('算法、系统、工程或论文表达方向', '人工智能、图像处理、系统架构、通信网络或信息安全方向')
s = s.replace('根据算法、系统、工程方向匹配', '根据六类专业方向匹配')
process.write_text(s)

mentor = root / 'pages/MentorProfile.tsx'
s = mentor.read_text()
s = s.replace('role: "机器学习 · 算法研究"', 'role: "人工智能 · 深度学习"').replace('directions: ["机器学习", "算法研究", "实验设计"]', 'directions: ["人工智能与深度学习", "实验评估"]').replace('tags: ["深度学习", "实验设计", "模型评估"]', 'tags: ["深度学习", "模型训练", "实验评估"]')
s = s.replace('role: "系统 · 工程实践"', 'role: "系统架构 · 通信网络"').replace('directions: ["系统工程", "工程实践", "分布式"]', 'directions: ["系统与架构研究", "通信网络"]').replace('tags: ["系统论文", "代码复现", "性能分析"]', 'tags: ["系统架构", "网络协议", "性能分析"]')
s = s.replace('role: "论文 · 学术表达"', 'role: "信息安全 · 研究方法"').replace('school: "博士 / 计算机论文写作与评审"', 'school: "博士 / 计算机安全与学术研究"').replace('directions: ["论文写作", "学术表达", "研究结构"]', 'directions: ["信息安全", "其他"]').replace('tags: ["结构梳理", "英文润色", "论证反馈"]', 'tags: ["安全机制", "威胁建模", "研究方法"]')
mentor.write_text(s)

# Align the records page sample tags to the same discipline vocabulary.
records = root / 'pages/Records.tsx'
s = records.read_text().replace('tag: "机器学习"', 'tag: "人工智能与深度学习"').replace('tag: "实验复现"', 'tag: "系统与架构研究"').replace('tag: "论文写作"', 'tag: "信息安全"')
records.write_text(s)
''
