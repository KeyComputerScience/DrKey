from pathlib import Path

replacements = {
    '感谢你的信任。我们会在 <b>1 个工作日内</b> 回复导师匹配建议。': '感谢你的信任。我们会在 <b>1 个工作日内</b> 回复导师匹配建议。<br /><span className="customer-service-hint">请添加客服微信 <b>HawkL001</b></span>',
    '感谢你的信任。K 博士工作室会在 <b>1 个工作日内</b> 回复导师匹配建议。': '感谢你的信任。K 博士工作室会在 <b>1 个工作日内</b> 回复导师匹配建议。<br /><span className="customer-service-hint">请添加客服微信 <b>HawkL001</b></span>',
}
for path in [Path('/home/ubuntu/jingxuan-store/client/src/pages/Home.tsx'), Path('/home/ubuntu/jingxuan-store/client/src/pages/Process.tsx')]:
    s = path.read_text()
    for old, new in replacements.items():
        s = s.replace(old, new)
    path.write_text(s)

css = Path('/home/ubuntu/jingxuan-store/client/src/index.css')
s = css.read_text()
if '.customer-service-hint' not in s:
    s += '\n.customer-service-hint { display: inline-block; margin-top: 12px; padding: 8px 11px; border: 1px solid #e4c79e; background: #fff7e9; color: #8d5d2e; font-size: 13px; line-height: 1.6; }\n.customer-service-hint b { color: #6f431d; letter-spacing: .03em; }\n'
css.write_text(s)
''
