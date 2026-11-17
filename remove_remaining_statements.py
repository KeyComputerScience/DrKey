from pathlib import Path
import re

root = Path('/home/ubuntu/jingxuan-store/client/src')

for filename in ['Home.tsx', 'Process.tsx', 'MentorProfile.tsx']:
    path = root / 'pages' / filename
    s = path.read_text()
    # Remove any remaining visible integrity proof bar.
    s = re.sub(r'\s*<div className="integrity-bar">.*?</div>', '', s, flags=re.S)
    # Remove residual footer responsibility wording.
    s = s.replace('<span>所有研究支持均以学术诚信为前提</span>', '')
    path.write_text(s)

home = root / 'pages/Home.tsx'
s = home.read_text()
s = s.replace('边界清晰', '研究导向', 1)
s = s.replace('只做辅导，不做代写', '围绕真实问题提供支持', 1)
home.write_text(s)

process = root / 'pages/Process.tsx'
s = process.read_text()
s = s.replace('逐步形成自己的研究判断，最终由你完成论文、代码、提交与答辩。', '逐步形成自己的研究判断，围绕研究问题完成分析与验证。')
s = s.replace('工作室不提供可直接提交的代写论文、代写代码或伪造实验结果。', '围绕你的研究材料提供方法讲解、结构反馈与实验复盘。')
s = s.replace('研究规范</Link>', '')
process.write_text(s)

# Remove the now-unused boundary section responsive styling.
css = root / 'index.css'
s = css.read_text()
s = re.sub(r'\.boundary-section[^\n]*\n', '', s)
css.write_text(s)
''
