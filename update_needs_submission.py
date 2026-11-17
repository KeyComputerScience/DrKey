from pathlib import Path
import re

root = Path('/home/ubuntu/jingxuan-store/client/src')

home = root / 'pages/Home.tsx'
s = home.read_text()
# Remove FAQ-only state/import and delete the complete FAQ section.
s = s.replace(', ChevronDown', '')
s = s.replace('  const [faqOpen, setFaqOpen] = useState<number | null>(0);\n', '')
faq_start = s.find('      <section className="section-shell faq-section"')
if faq_start == -1:
    raise SystemExit('homepage FAQ section not found')
faq_end = s.find('</section>', faq_start) + len('</section>')
s = s[:faq_start] + s[faq_end:]
# Change primary CTAs and modal language to a platform-routed needs submission.
s = s.replace('预约一次咨询', '提交研究需求')
s = s.replace('预约相关支持', '提交研究需求')
s = s.replace('预约沟通', '提交需求')
s = s.replace('预约前置沟通', '研究需求提交')
s = s.replace('留下你的专业方向、研究阶段与主要问题，我们会在工作日内回复适合的导师方向。', '填写你的专业方向与具体问题，平台会根据需求为你匹配合适的导师。')
s = s.replace('提交预约意向', '提交研究需求')
s = s.replace('预约意向已提交', '研究需求已提交')
s = s.replace('预约意向', '研究需求')
s = s.replace('可预约时段和导师匹配建议', '导师匹配建议')
s = s.replace('好的，我知道了', '好的，知道了')
# Replace the specific modal form intro text if the previous copy differs.
s = s.replace('留下你的专业方向、研究阶段与主要问题', '填写你的专业方向与具体问题')
home.write_text(s)

process = root / 'pages/Process.tsx'
s = process.read_text()
s = s.replace('预约咨询', '提交研究需求')
s = s.replace('预约前置沟通', '研究需求提交')
s = s.replace('我们会根据你的技术方向与问题，回复适合的导师方向和时段。', '平台会根据你的专业方向与具体问题，匹配合适的导师。')
s = s.replace('预约意向已提交', '研究需求已提交')
s = s.replace('预约意向', '研究需求')
s = s.replace('可预约时段和导师匹配建议', '导师匹配建议')
s = s.replace('提交预约意向', '提交研究需求')
s = s.replace('开始预约', '提交需求')
process.write_text(s)

# Keep the global appointment page actions meaningful after the terminology change.
appointments = root / 'pages/Appointments.tsx'
s = appointments.read_text()
s = s.replace('发起新预约', '提交新需求')
appointments.write_text(s)
''
