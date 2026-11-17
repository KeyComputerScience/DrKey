from pathlib import Path

root = Path('/home/ubuntu/jingxuan-store/client/src/pages')

home = root / 'Home.tsx'
s = home.read_text()
s = s.replace('你知道下一步，<br />也知道我们不会替你走。', '从问题提交，<br />到持续跟进。')
s = s.replace('从需求提交到课后复盘，所有服务围绕你的真实材料展开。我们不交付可直接提交的论文或代码，而是帮助你理解、验证并完成自己的计算机研究工作。', '平台围绕你的研究方向与具体问题，完成需求确认、导师匹配、试听交流与后续辅导追踪。')
s = s.replace('<p className="academic-kicker light">A REPRODUCIBLE PROCESS</p>', '<p className="academic-kicker light">A CLEAR SUPPORT PATH</p>')
s = s.replace('提交研究或项目需求", "匹配技术方向导师", "围绕材料进行一对一会谈", "带着实验计划回到自己的工作"', '说明问题", "确认关键诉求", "支付定金", "匹配导师"')
s = s.replace('说明课程要求、研究问题或报错现象", "根据算法、系统、工程方向匹配", "获得解释、提问与结构化反馈", "继续编码、实验、分析和复盘"', '提交研究方向与具体问题", "确认重点目标与支持内容", "确认需求并完成定金支付", "平台匹配合适导师"')
home.write_text(s)

mentor = root / 'MentorProfile.tsx'
s = mentor.read_text()
old = '<div className="profile-integrity"><ShieldCheck size={17} /><p><b>研究诚信承诺</b>所有论文、代码与实验由学生本人完成，导师只提供解释、反馈与方法支持。</p></div>'
s = s.replace(old, '')
mentor.write_text(s)
''
