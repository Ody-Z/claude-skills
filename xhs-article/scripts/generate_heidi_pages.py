#!/usr/bin/env python3
"""Generate newspaper-style content pages for the Heidi AI deployment analysis article."""

import subprocess, os, re, base64

DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = "/Users/odyzhou/Desktop/xhs-posts/covers"
IMG_DIR = "/Users/odyzhou/Desktop/xhs-posts/covers/heidi-images"

def img_b64(filename):
    """Embed local image as base64 data URI."""
    path = os.path.join(IMG_DIR, filename)
    with open(path, 'rb') as f:
        data = base64.b64encode(f.read()).decode('ascii')
    ext = filename.rsplit('.', 1)[-1].lower()
    if ext == 'jpg':
        ext = 'jpeg'
    return f"data:image/{ext};base64,{data}"

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
/* ─ Image figure ─ */
.figure-img-wrap {
  display: flex; justify-content: center;
  margin: 24px 0;
}
.figure-img-wrap img {
  max-width: 920px; max-height: 600px;
  width: auto; height: auto;
  display: block;
  border: 1px solid #ddd;
  box-shadow: 4px 4px 0 rgba(0,0,0,0.08);
}
.figure-caption {
  font-family: 'PingFang SC','Hiragino Sans GB',sans-serif;
  font-size: 22px; color: #888;
  text-align: center; margin-top: 12px;
}
/* ─ ROI tier card ─ */
.roi-tier {
  display: flex; align-items: baseline; gap: 24px;
  padding: 20px 0;
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
/* ─ Pricing comparison row ─ */
.price-row {
  display: flex; justify-content: space-between;
  padding: 16px 0;
  border-bottom: 1px solid #ddd;
  font-family: 'Songti SC',serif;
  font-size: 36px;
}
.price-row.heidi {
  color: #b91c1c; font-weight: 700;
}
.price-row .name { font-weight: 700; }
.price-row .price {
  font-family: Georgia,serif;
}
"""

def make_page(page_num, total, body_html, footer_left="Ody · Heidi 落地分析"):
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

def figure(b64, caption):
    return f'<div class="figure-img-wrap"><img src="{b64}" alt=""></div><div class="figure-caption">{caption}</div>'

# ── Pre-load images ──
TOM_KELLY = img_b64('tom-kelly-techcrunch.jpg')
PHONE_UI = img_b64('phone-transcription.png')
TEAM = img_b64('team-rooftop.jpg')

TOTAL = 11
pages = []

# Page 02 — 钩子 + 系列定调
pages.append(make_page(2, TOTAL,
    p('一个澳洲血管外科医生，2021 年走出医院。')
    + p('31 岁，<strong>burnout</strong>，决定不再当医生。')
    + p('四年后他做的东西，每周替全球医生处理 <strong>200 万次问诊</strong>。估值 4.65 亿美元。')
    + p('他叫 Tom Kelly。公司叫 Heidi。')
    + figure(TOM_KELLY, 'Tom Kelly · Heidi 联合创始人 & CEO（来源：TechCrunch）')
))

# Page 03 — 系列定调
pages.append(make_page(3, TOTAL,
    p('我打算起一个系列，<strong>只挑有硬数据的 AI 落地案例写</strong>。')
    + p('我对 PPT 里的"赋能"、demo 视频里的概念秀没兴趣。我想看真正有医生、律师、客服在用，并且公开了具体数字的那种。')
    + p('第一篇写 Heidi，一个从澳洲跑出来的 AI 医疗初创。')
))

# Page 04 — 谁在用
pages.append(make_page(4, TOTAL,
    sec('谁在用')
    + p('Heidi 主战场不在硅谷，在英联邦：澳大利亚、英国、加拿大，加上最近发力的美国基层医疗。')
    + p('它的典型用户是 <strong>GP（家庭医生/全科医生）</strong>，主要场景是基层医疗。GP 的工作模式是一天 30+ 患者，每个 7-15 分钟，文书量恐怖。')
    + p('公开口径：<strong>116 个国家</strong>有医生在用，覆盖 <strong>110 种语言</strong>。')
    + p('英国 NHS 体系里，<strong>15+ 个 NHS Trust</strong> 已经签约。整个英国"<strong>每两个 GP 里有一个</strong>"在用 Heidi。')
))

# Page 05 — 解决什么问题
pages.append(make_page(5, TOTAL,
    sec('解决什么问题')
    + p('医生的工作时间分两段：看病人，和写病历。')
    + p('看病人是这份工作的快感来源。写病历是把快感磨掉的那个环节：SOAP 模板、转诊信、保险编码、给患者的简化版摘要。')
    + p('一个 7 分钟的诊疗，<strong>文书时间往往是 12 分钟</strong>。')
    + p('英国 BMA：GP 每周平均工作 50+ 小时，<strong>超过 1/3 在做行政文书</strong>。BMJ 调研：<strong>60% 的英国 GP 考虑过提前退休</strong>，主因是 burnout。')
))

# Page 06 — 痛到什么程度（印度外包）
pages.append(make_page(6, TOTAL,
    p('这事痛到什么程度？')
    + p('多年来美国已经有医生<strong>自己掏钱雇印度的远程 medical scribe</strong>：患者诊室里医生戴个耳麦，地球另一边的印度文员实时听诊疗对话、敲病历。')
    + p('单人 <strong>1500-3000 美元/月</strong>。这是一个上亿美元的外包行业。')
    + p('这是一个被验证过的商业模式，也是 Tom Kelly 离开医院的原因，Heidi 真正切入的市场。')
))

# Page 07 — Heidi 怎么干活 + UI 图
pages.append(make_page(7, TOTAL,
    sec('Heidi 怎么干活')
    + p('医生打开浏览器，点"开始录音"。正常和患者聊天，聊完点"结束"。')
    + p('Heidi 自动生成 SOAP 病历、转诊信、给患者的简化版摘要、保险编码建议。医生人工 review 一下，推到 Epic、Cerner 等电子病历系统。')
    + figure(PHONE_UI, 'Heidi 录音设备 + 手机端实时转录界面（来源：Heidi 官网）')
))

# Page 08 — 4 层 ROI
pages.append(make_page(8, TOTAL,
    sec('4 层 ROI')
    + '<div class="roi-tier"><div class="roi-label">个人级</div><div class="roi-detail">伦敦 George Verghese 医生，每天省 <strong>1-2 小时</strong>。原本计划提前退休，现在能继续看病人到真正退休</div></div>'
    + '<div class="roi-tier"><div class="roi-label">机构（小）</div><div class="roi-detail">英国 Modality 集团，47 个 GP × 25 天试点。诊中文书时间砍 <strong>51%</strong>，下班后行政减 <strong>61%</strong></div></div>'
    + '<div class="roi-tier"><div class="roi-label">机构（中）</div><div class="roi-detail">美国印第安纳健康集团，5 个月省下 <strong>2000 小时</strong>，折约 <strong>20 万美元</strong>临床价值，1.2 万次问诊</div></div>'
    + '<div class="roi-tier"><div class="roi-label">国家级</div><div class="roi-detail">英国 NHS。每个月 <strong>150 万+ 次诊疗</strong>用 Heidi 完成</div></div>'
))

# Page 09 — 融资规模
pages.append(make_page(9, TOTAL,
    sec('融资规模')
    + p('2025 年 10 月，Heidi 完成 <strong>B 轮 6500 万美元</strong>，由 Steve Cohen 的 <strong>Point72</strong> 领投，投后估值 <strong>4.65 亿美元</strong>。')
    + p('历史融资走的是相对安静的路线：澳洲 VC <strong>Blackbird Ventures</strong> 等长期支持。')
    + p('Point72 这种对冲基金背景的资本不投故事：他们看的就是日活、留存、付费转化。能拿到他们的钱本身就是一种数据签名。')
))

# Page 10 — 凭什么赢
pages.append(make_page(10, TOTAL,
    sec('凭什么赢同赛道')
    + p('医疗 AI 病历赛道并不空。Heidi 做了一件别人不做的事：<strong>对个人医生免费</strong>。')
    + '<div class="price-row"><span class="name">微软 Nuance DAX</span><span class="price">$600/月</span></div>'
    + '<div class="price-row"><span class="name">Suki</span><span class="price">$299/月</span></div>'
    + '<div class="price-row"><span class="name">Nabla</span><span class="price">$119/月</span></div>'
    + '<div class="price-row heidi"><span class="name">Heidi</span><span class="price">$0</span></div>'
    + p('打法核心是<strong>绕开守门人</strong>：医院 CIO 是 AI 落地的第一道墙，Heidi 让一线 GP 自己注册先用起来，再让医院来追。')
))

# Page 11 — 被质疑的点
pages.append(make_page(11, TOTAL,
    sec('Heidi 被质疑的点')
    + p('<strong>第一</strong>，没有 RCT 级别的同行评审论文。Modality 那 51% 是内部试点报告，没有顶刊数据支撑。')
    + p('<strong>第二</strong>，复杂多病种门诊（老年人 6+ 慢性病、长程心理治疗）容易把问题搅在一起，需要医生大量手动改。')
    + p('<strong>第三</strong>，数据隐私。HIPAA、GDPR、ISO 27001 合规列了一长串，但仍有医生反复关心数据训练边界。Heidi 自报"每 1000 份病历少于 1 个负面评价"，没有第三方审计。')
))

# Page 12 — 收束 + 团队照
pages.append(make_page(12, TOTAL,
    p('Tom Kelly 当年走出医院的时候是 31 岁。')
    + p('他不当医生了。')
    + p('但他现在<strong>每周辅助 200 万次诊疗</strong>。比他自己当 100 年医生还多。')
    + p('我觉得这是 AI 落地最有意思的版本：不是 AI 取代了医生，是一个被这份工作压垮的医生，做了一个让其他医生不再被压垮的东西。')
    + figure(TEAM, 'Heidi 团队（来源：Heidi 官网）')
))

# Page 13 — 系列预告
pages.append(make_page(13, TOTAL,
    sec('下一篇')
    + p('下一篇我会写 <strong>Harvey</strong>（法律 AI）。')
    + p('如果你是某个领域的从业者，知道你的垂直领域的 AI 工具有公开 ROI 数据，<strong>留言告诉我</strong>。')
    + p('我去研究。')
))

# Page 14 — 参考资料
pages.append(make_page(14, TOTAL,
    sec('参考资料')
    + p('Heidi Health 官网<br><span style="font-size:30px; color:#888;">heidihealth.com</span>')
    + p('TechCrunch · 2025-10-05<br><span style="font-size:30px; color:#888;">Heidi Health raises $65M Series B led by Point72</span>')
    + p('Bloomberg · 2025-10-06<br><span style="font-size:30px; color:#888;">AI Health Startup Heidi Gets Point72 Funds at $465M Value</span>')
    + p('CNBC · 2025-12-24<br><span style="font-size:30px; color:#888;">He left medicine to build an AI tool — now it\'s worth $460M</span>')
    + '<div style="margin-top:60px; padding-top:40px; border-top:2px solid #ccc; font-family:PingFang SC,sans-serif; font-size:26px; color:#aaa; line-height:1.8;">'
    + '本文基于公开新闻、官网披露与客户案例整理。<br>'
    + '文中数字、案例、引文均来自公开来源。<br>'
    + '判断与立场仅代表作者个人。'
    + '</div>'
))

# Update TOTAL to actual count (we have 13 content pages + cover = 14)
ACTUAL_TOTAL = 14
# Patch TOTAL in already-rendered HTML
pages = [page.replace(f'/ {TOTAL:02d}<', f'/ {ACTUAL_TOTAL:02d}<') for page in pages]

# ── Write & screenshot ──
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
print("Generating Heidi pages...")

for i, page_html in enumerate(pages):
    page_num = i + 2  # cover is page 01
    fname = f"_heidi-page-{page_num:02d}.html"
    fpath = os.path.join(OUT_DIR, fname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(page_html)

    out_png = os.path.join(OUT_DIR, f"heidi-page-{page_num:02d}.png")
    result = subprocess.run([
        CHROME, "--headless=new", "--disable-gpu",
        f"--screenshot={out_png}",
        "--window-size=1080,1800",
        "--force-device-scale-factor=2",
        "--hide-scrollbars",
        f"file://{fpath}"
    ], capture_output=True, text=True)

    os.remove(fpath)

    if os.path.exists(out_png):
        print(f"  ✓ heidi-page-{page_num:02d}.png")
    else:
        print(f"  ✗ FAILED heidi-page-{page_num:02d}: {result.stderr[:200]}")

print(f"\nDone. {len(pages)} content pages + 1 cover = {len(pages)+1} total in {OUT_DIR}.")
