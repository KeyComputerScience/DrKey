from pathlib import Path
import re

root = Path('/home/ubuntu/jingxuan-store/client/src')

# Rebuild the process model around the requested customer journey.
process = root / 'pages/Process.tsx'
s = process.read_text()
start = s.index('const steps = [')
end = s.index('];', start) + 2
new_steps = '''const steps = [
  { number: "01", title: "说明问题", description: "提交你的研究方向、项目背景与当前遇到的具体问题。", icon: ClipboardList, detail: "填写研究方向、问题描述与可提供的相关材料。" },
  { number: "02", title: "确认关键诉求", description: "平台整理你的重点目标、优先级与期望支持内容。", icon: MessageCircle, detail: "明确本次需求需要解决的关键问题与预期结果。" },
  { number: "03", title: "支付定金", description: "确认需求后支付定金，平台进入导师匹配流程。", icon: CheckCircle2, detail: "提交需求并完成定金支付后，开始安排匹配。" },
  { number: "04", title: "匹配导师", description: "平台根据研究方向、问题类型与导师经验进行匹配。", icon: UserRound, detail: "收到导师匹配建议后，可进一步确认支持方向。" },
  { number: "05", title: "试听交流", description: "先进行一次试听交流，了解导师的沟通方式与支持思路。", icon: MessageCircle, detail: "围绕你的问题进行初步交流，确认后续支持方式。" },
  { number: "06", title: "签署协议", description: "确认合作内容、服务范围与沟通方式后签署协议。", icon: FileCheck2, detail: "双方确认服务信息后，进入正式辅导阶段。" },
  { number: "07", title: "开始辅导", description: "围绕你的研究问题与材料展开定向辅导。", icon: Code2, detail: "按约定的方向推进讲解、反馈与问题梳理。" },
  { number: "08", title: "实时追踪", description: "平台持续记录进度、沟通重点与后续行动。", icon: ClipboardList, detail: "随时查看当前进展，并反馈新的问题与需求。" },
  { number: "09", title: "评价", description: "完成本阶段辅导后，对服务过程与沟通体验进行评价。", icon: CheckCircle2, detail: "留下你的反馈，帮助平台持续优化导师匹配与服务体验。" },
];'''
s = s[:start] + new_steps + s[end:]
# Remove restrictive or responsibility-heavy phrasing from visible workflow/form copy.
replacements = {
    '帮助你理解选择，而不是把论文或代码答案交给你。': '帮助你梳理选择，形成清晰的下一步方案。',
    '仅用于本次咨询准备，不会替代你的研究工作。': '用于本次需求整理与导师匹配。',
    '附件仅用于本次咨询准备，不会被包装为你的原创成果。': '附件用于本次需求整理与导师匹配。',
    '我已阅读并理解工作室的研究诚信边界，同意由本人完成研究、编码与写作。': '我确认已填写真实的研究方向与具体问题。',
    '我已阅读并同意研究诚信边界。': '我确认已填写真实的研究方向与具体问题。',
    '你知道下一步，也知道我们不会替你走。': '每一步都有清晰进度，平台持续跟进需求。',
    '你始终是研究与代码的作者，导师负责帮助你看见问题、理解方法，并把下一步做得更清楚。': '导师围绕你的研究方向与具体问题，提供针对性的支持与反馈。',
}
for old, new in replacements.items():
    s = s.replace(old, new)
process.write_text(s)

home = root / 'pages/Home.tsx'
s = home.read_text()
# Remove count badges from the mentor filter UI while retaining filters.
s = s.replace('{filter}<span>{filter === "全部" ? mentors.length : mentors.filter((mentor) => mentor.directions.some((direction) => direction.includes(filter))).length}</span>', '{filter}')
for old, new in replacements.items():
    s = s.replace(old, new)
# Remove FAQ copy that directly describes replacing student work if still present in source data.
s = s.replace('K 博士工作室会直接替我写论文或代码吗？', 'K 博士工作室如何提供支持？')
s = s.replace('不会。工作室提供研究方法讲解、结构反馈、代码阅读、实验设计与复现指导。论文、代码与最终提交必须由你本人完成。', '平台提供研究方法讲解、结构反馈、代码阅读、实验设计与复现指导。')
home.write_text(s)

# Update contact details site-wide.
for path in (root / 'pages').glob('*.tsx'):
    s = path.read_text()
    s = s.replace('hello@kstudio.academy', 'key.csworkG@gmail.com')
    s = s.replace('工作日 10:00 — 18:00', '9:00-18:00')
    path.write_text(s)
''
