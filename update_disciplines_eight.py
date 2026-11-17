from pathlib import Path

root = Path('/home/ubuntu/jingxuan-store/client/src/pages')
home = root / 'Home.tsx'
s = home.read_text()
old = '  { number: "06", icon: FlaskConical, title: "其他", description: "如果你的计算机研究方向不在以上分类中，可以先描述问题，我们会协助匹配合适的技术支持。", tags: ["问题梳理", "方向匹配", "研究方法"] },'
new = '''  { number: "06", icon: Sparkles, title: "大数据及其挖掘", description: "围绕数据处理、特征挖掘与分析建模，梳理数据流程、方法选择与结果解释。", tags: ["数据处理", "数据挖掘", "分析建模"] },
  { number: "07", icon: Users, title: "交叉学科", description: "连接计算机技术与其他学科问题，协助梳理研究背景、技术路径与跨领域表达。", tags: ["跨领域", "方法融合", "研究设计"] },
  { number: "08", icon: FlaskConical, title: "其他", description: "如果你的计算机研究方向不在以上分类中，可以先描述问题，我们会协助匹配合适的技术支持。", tags: ["问题梳理", "方向匹配", "研究方法"] },'''
if old not in s: raise SystemExit('service other item not found')
s = s.replace(old, new)
s = s.replace('const mentorFilters = ["全部", "人工智能与深度学习", "计算机图像处理", "系统与架构研究", "通信网络", "信息安全", "其他"];', 'const mentorFilters = ["全部", "人工智能与深度学习", "计算机图像处理", "系统与架构研究", "通信网络", "信息安全", "大数据及其挖掘", "交叉学科", "其他"];')
s = s.replace('<option>信息安全</option><option>其他</option>', '<option>信息安全</option><option>大数据及其挖掘</option><option>交叉学科</option><option>其他</option>')
s = s.replace('提供人工智能、图像处理、系统架构、通信网络与信息安全的过程性支持。', '提供人工智能、图像处理、系统架构、通信网络、信息安全、大数据及其挖掘与交叉学科的过程性支持。')
s = s.replace('<Link href="/#services">信息安全</Link><Link href="/#services">其他</Link>', '<Link href="/#services">信息安全</Link><Link href="/#services">大数据及其挖掘</Link><Link href="/#services">交叉学科</Link><Link href="/#services">其他</Link>')
home.write_text(s)

process = root / 'Process.tsx'
s = process.read_text()
s = s.replace('我们根据人工智能、图像处理、系统架构、通信网络或信息安全方向匹配导师', '平台根据人工智能、图像处理、系统架构、通信网络、信息安全、大数据及其挖掘与交叉学科方向匹配导师')
process.write_text(s)

# Keep visible discipline taxonomy consistent in records/compliance copy where the six-category list appears.
for name in ['Records.tsx', 'Compliance.tsx']:
    path = root / name
    s = path.read_text()
    s = s.replace('人工智能、图像处理、系统架构、通信网络或信息安全', '人工智能、图像处理、系统架构、通信网络、信息安全、大数据及其挖掘与交叉学科')
    path.write_text(s)
''
