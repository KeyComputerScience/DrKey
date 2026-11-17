from pathlib import Path

p = Path('/home/ubuntu/jingxuan-store/client/src/pages/Process.tsx')
s = p.read_text()
s = s.replace('好的技术支持不是把你带到提交按钮，而是让你理解为什么这样设计、如何验证，以及下一步如何继续。', '平台从需求确认开始，持续跟进导师匹配、试听交流与后续辅导进度。')
s = s.replace('每一步都有明确边界，也都有你需要完成的技术动作。', '每一步都有清晰进度，平台持续跟进需求。')
p.write_text(s)

p = Path('/home/ubuntu/jingxuan-store/client/src/pages/Home.tsx')
s = p.read_text()
s = s.replace('但不会替你伪造实验结果或提交不可验证的结论。', '并分析结果差异与下一步改进方向。')
p.write_text(s)
''
