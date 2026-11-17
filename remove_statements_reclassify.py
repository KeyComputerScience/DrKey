from pathlib import Path
import re

root = Path('/home/ubuntu/jingxuan-store/client/src')

home = root / 'pages/Home.tsx'
s = home.read_text()
# Remove the top research-integrity proof bar.
s = re.sub(r'\n?\s*<div className="integrity-bar">.*?</div>', '', s, count=1, flags=re.S)
# Remove the homepage academic-responsibility commitment block.
s = re.sub(r'\s*<section className="integrity-callout-section".*?</section>', '', s, count=1, flags=re.S)
# Remove the old footer responsibility sentence and hide the research-standards link from footer only.
s = s.replace('<span>所有研究支持均以学术诚信为前提</span>', '')
s = s.replace('<Link href="/compliance">研究规范</Link>', '')
# Reclassify K 博士 as information security.
s = s.replace('role: "人工智能 · 深度学习"', 'role: "信息安全 · 安全研究"', 1)
s = s.replace('directions: ["人工智能与深度学习", "计算机图像处理"]', 'directions: ["信息安全"]', 1)
s = s.replace('tags: ["深度学习", "模型训练"]', 'tags: ["安全机制", "威胁建模"]', 1)
home.write_text(s)

mentor = root / 'pages/MentorProfile.tsx'
s = mentor.read_text()
s = s.replace('role: "人工智能 · 深度学习"', 'role: "信息安全 · 安全研究"', 1)
s = s.replace('directions: ["人工智能与深度学习", "计算机图像处理", "实验评估"]', 'directions: ["信息安全", "安全研究", "实验评估"]', 1)
s = s.replace('tags: ["深度学习", "模型训练", "实验评估"]', 'tags: ["安全机制", "威胁建模", "实验评估"]', 1)
mentor.write_text(s)

process = root / 'pages/Process.tsx'
s = process.read_text()
# Remove the technical-boundaries block that contains the old ghostwriting proof/disclaimer copy.
s = re.sub(r'\s*<section className="boundary-section".*?</section>', '', s, count=1, flags=re.S)
process.write_text(s)

# Remove the no-longer-used top-bar and removed homepage section style rules.
css = root / 'index.css'
s = css.read_text()
s = re.sub(r'\.integrity-bar[^\n]*\n', '', s)
s = re.sub(r'\.integrity-callout-section[^\n]*\n', '', s)
s = re.sub(r'\.integrity-callout[^\n]*\n', '', s)
s = re.sub(r'\.integrity-callout-icon[^\n]*\n', '', s)
s = re.sub(r'\.integrity-callout h2[^\n]*\n', '', s)
s = re.sub(r'\.integrity-callout p[^\n]*\n', '', s)
s = re.sub(r'\.integrity-callout \\.light-text-link[^\n]*\n', '', s)
css.write_text(s)
''
