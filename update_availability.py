from pathlib import Path

home = Path('/home/ubuntu/jingxuan-store/client/src/pages/Home.tsx')
s = home.read_text()
s = s.replace('directions: ["机器学习", "算法研究"] }', 'directions: ["机器学习", "算法研究"], availability: ["周三 19:00", "周五 14:30"] }')
s = s.replace('directions: ["系统工程", "工程实践"] }', 'directions: ["系统工程", "工程实践"], availability: ["周四 10:00", "周六 15:00"] }')
s = s.replace('directions: ["论文写作", "学术表达"] }', 'directions: ["论文写作", "学术表达"], availability: ["周二 20:00", "周日 10:30"] }')
old = '<div className="mentor-tags">{mentor.tags.map((tag) => <i key={tag}>{tag}</i>)}</div><button onClick={() => setConsultOpen(true)}>预约沟通 <ArrowRight size={15} /></button>'
new = '<div className="mentor-tags">{mentor.tags.map((tag) => <i key={tag}>{tag}</i>)}</div><div className="mentor-availability"><span>最近可约</span>{mentor.availability.map((slot) => <button key={slot} onClick={() => { toast.success(`已选择 ${mentor.name} · ${slot}`); setConsultOpen(true); }}>{slot}</button>)}</div><button onClick={() => setConsultOpen(true)}>预约沟通 <ArrowRight size={15} /></button>'
if old not in s:
    raise SystemExit('mentor card insertion target not found')
s = s.replace(old, new)
home.write_text(s)

css = Path('/home/ubuntu/jingxuan-store/client/src/index.css')
style = css.read_text()
insert = '''
/* Mentor availability */
.mentor-availability { display: flex; flex-wrap: wrap; align-items: center; gap: 5px; margin: 0 0 13px; }
.mentor-availability > span { width: 100%; margin-bottom: 1px; color: #8a9698; font-family: "DM Mono", monospace; font-size: 8px; letter-spacing: .04em; }
.mentor-availability button { min-height: 25px; padding: 0 7px; border: 1px solid #c2ccc6; background: #f7f8f4; color: #536d62; font-family: "DM Mono", monospace; font-size: 9px; cursor: pointer; transition: border-color .18s ease, background .18s ease, color .18s ease; }
.mentor-availability button:hover { border-color: var(--amber); background: #fff8ee; color: #a76736; }
'''
marker = '/* Action items dashboard */'
if '/* Mentor availability */' not in style:
    style = style.replace(marker, insert + '\n' + marker, 1)
css.write_text(style)
''
