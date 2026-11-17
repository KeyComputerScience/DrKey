from pathlib import Path

root = Path('/home/ubuntu/jingxuan-store/client/src/pages')

home = root / 'Home.tsx'
s = home.read_text().replace('Build understanding, not submission-ready work.', 'Build clarity, step by step.')
home.write_text(s)

process = root / 'Process.tsx'
s = process.read_text()
s = s.replace('<Link href="/#services">算法与机器学习</Link><Link href="/#services">系统与工程研究</Link>', '<Link href="/#services">人工智能与深度学习</Link><Link href="/#services">计算机图像处理</Link><Link href="/#services">系统与架构研究</Link><Link href="/#services">通信网络</Link><Link href="/#services">信息安全</Link><Link href="/#services">大数据及其挖掘</Link><Link href="/#services">交叉学科</Link><Link href="/#services">其他</Link>')
process.write_text(s)
''
