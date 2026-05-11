#!/usr/bin/env python3
"""Generate newspaper-style content pages for the Harvey AI deployment analysis article."""

import subprocess, os, re

DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = "/Users/odyzhou/Desktop/xhs-build/harvey"

CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1080px; height: 1800px;
  background: #f5f0e8;
  font-family: 'Songti SC','STSong',serif;
  overflow: hidden; position: relative;
}
.texture {
  position: absolute; inset: 0; opacity: 0.4; pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.15'/%3E%3C/svg%3E");
  background-size: 256px;
}
.col-line {
  position: absolute; left: 50%; top: 120px; bottom: 120px;
  width: 1px; background: rgba(0,0,0,0.05); z-index: 1;
}
.container {
  position: relative; z-index: 2; height: 100%;
  display: flex; flex-direction: column;
  padding: 48px 80px 120px;
}
.header {
  display: flex; justify-content: space-between; align-items: center;
  padding-bottom: 20px; border-bottom: 1px solid #ccc;
}
.header-left {
  font-family: Georgia,serif;
  font-size: 18px; font-weight: 700; color: #bbb;
  letter-spacing: 6px; text-transform: uppercase;
}
.header-right {
  font-family: 'PingFang SC','Hiragino Sans GB',sans-serif;
  font-size: 20px; color: #bbb;
}
.content {
  flex: 1; display: flex; flex-direction: column;
  justify-content: center; padding: 20px 0;
}
.section-title {
  font-family: 'Songti SC','STSong',serif;
  font-size: 52px; font-weight: 900; color: #111;
  line-height: 1.3; margin-bottom: 40px;
  padding-bottom: 24px; border-bottom: 2px solid #ddd;
}
p {
  font-family: 'Songti SC','STSong',serif;
  font-size: 38px; font-weight: 400; color: #333;
  line-height: 1.85; margin-bottom: 28px;
}
p:last-child { margin-bottom: 0; }
strong { font-weight: 700; color: #111; }
em.tech {
  font-style: italic;
  font-family: Georgia,serif;
  color: #b91c1c;
  font-weight: 700;
}
.footer {
  display: flex; justify-content: space-between; align-items: flex-end;
  padding-top: 20px; border-top: 1px solid #ccc;
}
.footer-left {
  font-family: 'PingFang SC','Hiragino Sans GB',sans-serif;
  font-size: 20px; color: #bbb;
}
.footer-right {
  font-family: Georgia,serif;
  font-size: 80px; font-weight: 900;
  color: rgba(0,0,0,0.04); line-height: 1;
}
/* product block */
.product-block {
  padding: 18px 0;
  border-bottom: 1px solid #ddd;
}
.product-block:last-child { border-bottom: none; }
.product-name {
  font-family: Georgia,serif;
  font-size: 32px; font-weight: 700;
  color: #b91c1c;
  margin-bottom: 8px;
  letter-spacing: 1px;
}
.product-desc {
  font-family: 'Songti SC',serif;
  font-size: 30px; line-height: 1.65; color: #333;
}
.product-desc strong { color: #111; }
/* roi tier */
.roi-tier {
  display: flex; align-items: baseline; gap: 24px;
  padding: 22px 0;
  border-bottom: 1px solid #ddd;
}
.roi-tier:last-child { border-bottom: none; }
.roi-label {
  font-family: 'PingFang SC',sans-serif;
  font-size: 26px; font-weight: 700;
  color: #b91c1c;
  min-width: 200px;
  letter-spacing: 1px;
}
.roi-detail {
  font-family: 'Songti SC',serif;
  font-size: 32px; line-height: 1.6; color: #333;
  flex: 1;
}
.roi-detail strong { color: #111; }
/* price comparison */
.price-row {
  display: flex; justify-content: space-between;
  padding: 16px 0;
  border-bottom: 1px solid #ddd;
  font-family: 'Songti SC',serif;
  font-size: 36px;
}
.price-row.harvey {
  color: #b91c1c; font-weight: 700;
}
.price-row .name { font-weight: 700; }
.price-row .price {
  font-family: Georgia,serif;
}
/* risk block */
.risk-block {
  padding: 18px 0;
  border-bottom: 1px solid #ddd;
}
.risk-block:last-child { border-bottom: none; }
.risk-name {
  font-family: 'PingFang SC',sans-serif;
  font-size: 30px; font-weight: 700;
  color: #b91c1c;
  margin-bottom: 8px;
}
.risk-desc {
  font-family: 'Songti SC',serif;
  font-size: 30px; line-height: 1.65; color: #333;
}
.risk-desc strong { color: #111; }
"""

def make_page(page_num, total, body_html, footer_left="Ody · Harvey 落地分析"):
    return f"""<!DOCTYPE html>
<html lang="zh"><head><meta charset="UTF-8"><style>{CSS}</style></head>
<body>
<div class="texture"></div>
<div class="col-line"></div>
<div class="container">
  <div class="header">
    <div class="header-left">Deep Dive</div>
    <div class="header-right">{page_num:02d} / {total:02d}</div>
  </div>
  <div class="content">{body_html}</div>
  <div class="footer">
    <div class="footer-left">{footer_left}</div>
    <div class="footer-right">{page_num:02d}</div>
  </div>
</div>
</body></html>"""

def sec(title):
    return f'<div class="section-title">{title}</div>'

def p(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return f'<p>{text}</p>'

TOTAL = 12  # cover + 11 content pages
pages = []

# Page 02 — 钩子
pages.append(make_page(2, TOTAL,
    p('2022 年 7 月 4 日上午 10 点，一位刚入职的初级律师接到一通电话。')
    + p('打来的是 <strong>Sam Altman</strong>。')
    + p('这个律师叫 <strong>Winston Weinberg</strong>，在洛杉矶一家叫 O\'Melveny 的律所做证券诉讼。')
    + p('几天前，他和室友 Gabriel Pereyra 用 GPT-3 写了一段加州房东与租客法律的回答模板，找律师朋友盲测了 100 个真实问题，结果有 <strong>86 个回答律师拿到手就能用</strong>。')
    + p('OpenAI Startup Fund 当场决定投他们。这是这只基金成立后投出去的第一家公司。')
    + p('四年后，2026 年 3 月，Harvey 估值 <strong>110 亿美元</strong>。')
))

# Page 03 — 卖给谁
pages.append(make_page(3, TOTAL,
    sec('卖给谁')
    + p('我先看了一眼 Harvey 今天的客户。')
    + p('<strong>1,300 多家机构</strong>，超过 <strong>10 万名律师</strong>在用。美国百强律所里超过一半。')
    + p('代表客户：<strong>Allen & Overy</strong>（英国最顶级律所之一，4,000 多名律师）、<strong>PwC</strong>（四大之一，4,000 多位法律专业人士）、<strong>Bridgewater</strong> 这种顶级对冲基金、<strong>T-Mobile</strong> 这种大公司的法务团队。')
    + p('全是钱多、案件量大、对错误零容忍的客户。')
))

# Page 04 — 律师到底有多贵
pages.append(make_page(4, TOTAL,
    sec('律师到底有多贵')
    + p('美国最顶尖律所合伙人计费 <strong>1,433 美元/小时</strong>，部分顶级 senior partner 已经逼近 <strong>3,000 美元/小时</strong>。一年级初级律师 600-700 美元/小时。')
    + p('<strong>77% 的美国律师报告职业倦怠</strong>。律所给初级律师定的可计费工时目标是一年 2,200 小时，实际工时常常超过 3,000 小时。')
    + p('但律师每天真正能算钱的时间，平均不到 3 小时。')
    + p('剩下的时间大量耗在文档审阅上。一桩商业诉讼里这部分能占总支出的 <strong>80% 以上</strong>。一份并购协议要逐字过 1 万页文档，错一行可能输掉整桩案子。')
))

# Page 05 — LPO 行业 + Heidi 系列回环
pages.append(make_page(5, TOTAL,
    sec('30 年的"印度后台办公室"')
    + p('过去 30 年这个工作一直在被外包出去。')
    + p('全球有一个叫 <strong>LPO</strong> 的行业，全名 Legal Process Outsourcing，法律外包。2023 年市场规模 <strong>174 亿美元</strong>，每年增长 <strong>31%</strong>。亚太地区拿走 70% 以上的钱。')
    + p('跟我上一篇讲的诊所 AI <strong>Heidi</strong> 的逻辑几乎一样：用 AI 替代医生雇的印度 scribe（远程文书）。')
    + p('法律和医疗这两个高小时费率行业，过去 30 年都靠把活外包到印度后台来压成本。Harvey 替代的是法律这一边的后台。')
))

# Page 06 — 60 倍价差 + UnitedLex 250 律师
pages.append(make_page(6, TOTAL,
    sec('60 倍价差 + 250 个律师')
    + p('印度律师审一份英文合同，给海外终端客户的报价是 <strong>25-50 美元/小时</strong>。同样一份合同在美国顶级律所，partner 收 1,433 美元，senior partner 收接近 3,000 美元。')
    + p('<strong>最大差 60 倍</strong>。')
    + p('2017 年有过一桩著名合同。美国 LPO 头部公司 <strong>UnitedLex</strong> 接下了 DXC Technology 的整个法务部，5 年合同，<strong>派 250 名律师驻场</strong>，180 天就把客户法务成本砍了 30%。')
    + p('这 250 个印度律师，就是 Harvey 现在直接对标替代的对象。')
    + p('副标题"<strong>把 250 个印度律师搬进一个 API</strong>"，是字面意思。')
))

# Page 07 — Harvey 实际怎么用
pages.append(make_page(7, TOTAL,
    sec('Harvey 实际怎么用')
    + '<div class="product-block"><div class="product-name">Assistant</div><div class="product-desc">聊天助手，集成到律师每天用的 <strong>Word</strong> 里。律师起草合同、改条款、查判例，直接在 Word 边栏对话。</div></div>'
    + '<div class="product-block"><div class="product-name">Vault</div><div class="product-desc">一次扔 <strong>1 万份文档</strong>批量审阅。一桩并购的尽调，过去要 100 个律师审一周，现在 <strong>几个小时跑完</strong>。</div></div>'
    + '<div class="product-block"><div class="product-name">Workflows</div><div class="product-desc">律所把自己的 SOP 固化成 AI 工作流。截至 2026 年 3 月，平台上跑着 <strong>25,000 个客户自定义 agent</strong>。</div></div>'
    + '<div class="product-block"><div class="product-name">Knowledge</div><div class="product-desc">2025 年 6 月跟 <strong>LexisNexis</strong> 签了内容联盟，把全美一手法律和判例数据库整进来。</div></div>'
))

# Page 08 — ROI 数据
pages.append(make_page(8, TOTAL,
    sec('ROI 数据')
    + p('底层是 <strong>多模型路由</strong>：OpenAI GPT-5、Anthropic Claude，加上自己跟 OpenAI 共建的法律自研模型（用了大约 <strong>100 亿 token</strong> 法律数据训练），三个之间动态切换。')
    + '<div class="roi-tier"><div class="roi-label">Allen &amp; Overy</div><div class="roi-detail">每位律师每周省 <strong>2-3 小时</strong>，合同审阅时间下降 <strong>30%</strong>，复杂文档分析平均省 <strong>7 小时</strong></div></div>'
    + '<div class="roi-tier"><div class="roi-label">PwC 法务</div><div class="roi-detail">案件吞吐量提升 <strong>20%</strong></div></div>'
))

# Page 09 — 钱与规模
pages.append(make_page(9, TOTAL,
    sec('钱与规模')
    + p('Harvey 累计融资超过 <strong>12 亿美元</strong>。2026 年 3 月最新一轮 <strong>2 亿美元</strong>，估值 <strong>110 亿</strong>。OpenAI Startup Fund 在 2022 种子轮第一个投，红杉一路跟到现在。')
    + p('<strong>ARR</strong>（年度经常性收入）的曲线很陡：')
    + '<div class="price-row"><span class="name">2024 年底</span><span class="price">$50M</span></div>'
    + '<div class="price-row"><span class="name">2025 年 8 月</span><span class="price">$100M</span></div>'
    + '<div class="price-row harvey"><span class="name">2026 年 1 月</span><span class="price">$195M</span></div>'
    + p('关键运营数据：<strong>167% 净留存</strong>。客户每签一年，第二年平均扩招 <strong>67% 的席位</strong>。')
    + p('定价 <strong>1,200 美元/律师/月</strong>。一家 4,000 律师的大所全员铺开，年单 <strong>5,760 万美元</strong>。')
))

# Page 10 — 风险与局限
pages.append(make_page(10, TOTAL,
    sec('我看到的下行风险')
    + '<div class="risk-block"><div class="risk-name">Thomson Reuters 反扑</div><div class="risk-desc">Westlaw 母公司 2023 年 <strong>6.5 亿美元</strong>收购 Casetext 整合进 CoCounsel。捆绑 Westlaw 卖 <strong>150-400 美元/席位</strong>，比 Harvey 便宜 <strong>3-8 倍</strong>。</div></div>'
    + '<div class="risk-block"><div class="risk-name">大律所自己造</div><div class="risk-desc">顶级律所现在普遍有工程团队，开始用 Anthropic 和 OpenAI 的 API 自己包装内部工具。直接威胁 167% 净留存这个引擎。</div></div>'
    + '<div class="risk-block"><div class="risk-name">幻觉的尾部风险</div><div class="risk-desc">Harvey 宣称错误率 <strong>0.2%</strong>。但只要出现一条"某律师因引用 Harvey 生成虚构判例被法庭处罚"的新闻，整个高端定价的信任基础会被重创。</div></div>'
))

# Page 11 — 收束 + 系列规律
pages.append(make_page(11, TOTAL,
    p('回到 2022 年 7 月 4 日上午 10 点。')
    + p('Sam Altman 那天投给 Weinberg 的，是一笔押在<strong>已经被 100 个真实问题、86 个律师验证过的回答模板</strong>上的钱。')
    + p('四年之后，这家公司估值 110 亿美元。')
    + p('有没有发现一个规律？')
    + p('目前特别成功的 B2B AI 垂直应用，都是<strong>在一个古老的商业模式里，用 AI 代替人</strong>。')
    + p('Heidi 替代的是<strong>医生雇的印度 scribe</strong>。Harvey 替代的是<strong>律所雇的印度 LPO 律师</strong>。')
    + p('下一个会是谁？')
))

# Page 12 — 参考资料
pages.append(make_page(12, TOTAL,
    sec('参考资料')
    + p('Harvey 官方 · 2026-03<br><span style="font-size:30px; color:#888;">Harvey raises at $11B valuation to scale agents</span>')
    + p('CNBC · 2026-03-25<br><span style="font-size:30px; color:#888;">Legal AI startup Harvey raises $200M at $11B valuation</span>')
    + p('TechCrunch · 2025-11-14<br><span style="font-size:30px; color:#888;">Inside Harvey: a first-year associate built one of SV\'s hottest startups</span>')
    + p('Sacra · 2026<br><span style="font-size:30px; color:#888;">Harvey AI revenue, growth, valuation analysis</span>')
    + p('Grand View Research · 2024<br><span style="font-size:30px; color:#888;">Legal Process Outsourcing (LPO) Market Report</span>')
    + p('Law.com · 2017-12-05<br><span style="font-size:30px; color:#888;">UnitedLex to support bulk of DXC Technology\'s in-house dept</span>')
    + '<div style="margin-top:40px; padding-top:30px; border-top:2px solid #ccc; font-family:PingFang SC,sans-serif; font-size:24px; color:#aaa; line-height:1.8;">'
    + '本文基于公开新闻、官网披露与客户案例整理。<br>'
    + '文中数字、案例、引文均来自公开来源。<br>'
    + '判断与立场仅代表作者个人。'
    + '</div>'
))

# ── Write & screenshot ──
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
print("Generating Harvey pages...")

for i, page_html in enumerate(pages):
    page_num = i + 2  # cover is page 01
    fname = f"_harvey-page-{page_num:02d}.html"
    fpath = os.path.join(OUT_DIR, fname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(page_html)

    out_png = os.path.join(OUT_DIR, f"harvey-page-{page_num:02d}.png")
    result = subprocess.run([
        CHROME, "--headless=new", "--disable-gpu",
        f"--screenshot={out_png}",
        "--window-size=1080,1800",
        "--force-device-scale-factor=2",
        "--hide-scrollbars",
        f"file://{fpath}"
    ], capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        print(f"✗ page {page_num}: {result.stderr[:200]}")
    else:
        print(f"✓ page {page_num}")

# Cleanup HTML files
for i in range(len(pages)):
    page_num = i + 2
    fpath = os.path.join(OUT_DIR, f"_harvey-page-{page_num:02d}.html")
    if os.path.exists(fpath):
        os.remove(fpath)

print(f"Done. {len(pages)} content pages + 1 cover = {len(pages)+1} total.")
