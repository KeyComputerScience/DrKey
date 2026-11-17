from pathlib import Path

root = Path('/home/ubuntu/jingxuan-store/client/src')

home = root / 'pages/Home.tsx'
s = home.read_text()
for fragment in [', availability: ["周三 19:00", "周五 14:30"]', ', availability: ["周四 10:00", "周六 15:00"]', ', availability: ["周二 20:00", "周日 10:30"]']:
    s = s.replace(fragment, '')
old = '<div className="mentor-availability"><span>最近可约</span>{mentor.availability.map((slot) => <button key={slot} onClick={() => { toast.success(`已选择 ${mentor.name} · ${slot}`); setConsultOpen(true); }}>{slot}</button>)}</div>'
if old not in s: raise SystemExit('homepage availability block not found')
s = s.replace(old, '')
s = s.replace('先把技术与边界说清楚。', '先把研究目标说清楚。')
home.write_text(s)

mentor = root / 'pages/MentorProfile.tsx'
s = mentor.read_text()
s = s.replace('import { ArrowLeft, ArrowRight, CalendarDays, Check, Clock3, Mail, MessageCircle, ShieldCheck, Star, UserRound }', 'import { ArrowLeft, ArrowRight, Check, Mail, MessageCircle, ShieldCheck, Star, UserRound }')
s = s.replace('; availability: string[]', '')
for fragment in [', availability: ["周三 19:00", "周五 14:30"]', ', availability: ["周四 10:00", "周六 15:00"]', ', availability: ["周二 20:00", "周日 10:30"]']:
    s = s.replace(fragment, '')
old = '<p>选择一个合适的技术方向与时间，开始一次有记录的研究支持。</p><div className="profile-availability"><span><CalendarDays size={14} /> 最近可约</span>{mentor.availability.map((slot) => <button key={slot} onClick={() => toast.success(`已选择 ${mentor.name} · ${slot}`)}><Clock3 size={13} /> {slot}</button>)}</div><Link href="/process" className="navy-button">预约咨询 <ArrowRight size={16} /></Link>'
new = '<p>提交你的研究问题与材料，开始一次有记录的研究支持。</p><Link href="/process" className="navy-button">预约咨询 <ArrowRight size={16} /></Link>'
if old not in s: raise SystemExit('profile availability block not found')
s = s.replace(old, new)
mentor.write_text(s)

# Remove stale availability CSS while preserving other mentor and profile styles.
css = root / 'index.css'
style = css.read_text()
start = style.find('/* Mentor availability */')
if start != -1:
    end = style.find('/* Booking attachments, loading, and success state */', start)
    if end != -1:
        style = style[:start] + style[end:]
# Remove profile availability declarations from the public profile block.
for line in [
'.profile-availability { display: grid; gap: 7px; padding: 13px 0 17px; border-top: 1px solid #3a5260; }\n',
'.profile-availability > span { display: flex; align-items: center; gap: 6px; color: #c4d1ce; font-family: "DM Mono", monospace; font-size: 9px; }\n',
'.profile-availability button { display: flex; align-items: center; gap: 6px; padding: 8px 9px; border: 1px solid #506672; background: #223f50; color: #e5ece6; font-family: "DM Mono", monospace; font-size: 9px; text-align: left; cursor: pointer; }\n',
'.profile-availability button:hover { border-color: var(--amber-light); color: var(--amber-light); }\n']:
    style = style.replace(line, '')
css.write_text(style)
''
