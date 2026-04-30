#!/usr/bin/env python3
"""Generate all content pages for the Kuse article in newspaper style, then screenshot."""

import subprocess, os, html

DIR = os.path.dirname(os.path.abspath(__file__))

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
  padding-bottom: 20px; border-bottom: 1px solid #ccc; margin-bottom: 0;
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
.pull-quote {
  font-family: 'Songti SC','STSong',serif;
  font-size: 46px; font-weight: 700; color: #333;
  line-height: 1.6; font-style: italic;
  padding: 32px 0; margin: 16px 0;
  border-top: 2px solid #ccc; border-bottom: 2px solid #ccc;
}
.closing-text {
  font-family: 'Songti SC','STSong',serif;
  font-size: 46px; font-weight: 700; color: #111;
  line-height: 1.7; text-align: center;
}
.closing-light {
  font-family: 'Songti SC','STSong',serif;
  font-size: 38px; font-weight: 400; color: #555;
  line-height: 1.7; text-align: center;
  margin-top: 48px;
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
"""

def make_page(page_num, total, body_html, is_closing=False):
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
    <div class="footer-left">Ody · 42章经 × Kuse CTO</div>
    <div class="footer-right">{page_num:02d}</div>
  </div>
</div>
</body></html>"""

def sec(title):
    return f'<div class="section-title">{title}</div>'

def p(text):
    # Handle **bold** markers
    import re
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return f'<p>{text}</p>'

def quote(text):
    return f'<div class="pull-quote">{text}</div>'

# ── Page definitions ──

TOTAL = 11

pages = []

# Page 2: Opening + Section 1 start
pages.append(make_page(2, TOTAL,
    p('Kuse 的 CTO 徐宇豪最近在 42 章经聊了一个数据：团队 15 个全职员工，另外还有 3-4 个 AI 员工，每月 token 成本加起来超过 2 万美金。')
    + p('一个 agent 一个月大概三四万人民币。这个价格完全能招一个不错的人。')
    + p('但他说：应该把钱花在 token 上，而不是工资上。')
    + sec('零融资跑出来的前提是敢砍')
    + p('Kuse 到现在没融资，用的是几个创始人自己的钱，大概一两百万美金。')
    + p('能用这点钱跑到千万刀 ARR，核心原因是转身够快，而且有魄力。')
    + p('产品经历了三次大转型：最早做设计 agent，后来转无限画布，最后变成他们自己戏称的"AI 网盘"。打开 Kuse，看到的就是一个文件夹。')
))

# Page 3: Section 1 continued
pages.append(make_page(3, TOTAL,
    p('每次转型都带来用户和付费的大跳水。但方向对了。')
    + p('关键洞察来自一个数据：**上传文件越多的用户，留存越高**。痛点是信息整理和理解，生成只是附带的。')
    + p('最狠的一次是放弃无限画布。当时用户画像已经从设计师变成了一人公司和高级白领，这些人对画布没概念，文件夹反而更直觉。')
    + p('我最近跟几个 YC founder 聊天，发现很多人明知方向有问题，但不敢 pivot。已经有别的 YC founder 成了客户，怕得罪 community，怕在投资人面前失去信任。')
    + p('段永平说，做对的事，把事儿做对。**Bootstrap 的好处就在这里：转身的成本只有自己承担，不用向任何人交代。**')
))

# Page 4: 固定定价
pages.append(make_page(4, TOTAL,
    sec('固定定价在 agent 时代必死')
    + p('Kuse 踩过的另一个大坑是定价。')
    + p('很长时间用的是固定价：20 美金能做多少个 task。一开始还行，但产品 agentic 化之后问题就来了。')
    + p('一个复杂任务可能跑 30 轮，但扣的积分和简单任务一样。用户完全意识不到自己在被补贴。')
    + p('你既在亏钱，又没法识别出真正有价值的客户。')
    + p('他们痛定思痛改成了 usage-based（按实际 token 消耗计费）。')
    + p('**AI 产品的成本结构和传统 SaaS 完全不同。**固定价对 SaaS 是好模式，而 agent 产品更像是传统制造业，成本随着客户数量提升。')
))

# Page 5: 10x different intro
pages.append(make_page(5, TOTAL,
    sec('AI 员工是 10x different')
    + p('Peter Thiel 在《Zero to One》里说，产品要么 10x better，要么 10x cheaper。')
    + p('AI 员工两个标准都没达到。能力还没超过人，成本也比人高。')
    + p('但 AI 员工有一个被低估的属性：**10x different。**')
    + p('它改变的是工作的维度。7×24 可用，零 onboarding，零人际摩擦，可以从头塑造，可以并行。人与人之间的摩擦很大，人与 agent 之间的摩擦小得多。')
))

# Page 6: 10x different examples
pages.append(make_page(6, TOTAL,
    p('Kuse 的销售 agent Azzurra 在掌握了所有客户和销售数据之后，自己搭了一个内部 CRM，完全贴合需求。然后 7×24 小时识别 upsell 线索，每条线索可能价值上万美金。')
    + p('徐宇豪说他一直听人说 SaaS 要完，没特别强的感受。直到看到 Azzurra 搭的这个 CRM，第一次觉得确实变天了。')
    + p('另一个 agent Rin，从做会议纪要起步，逐渐变成了项目负责人。每天早上给创始人发消息、分任务。后来甚至给了创始人一个评价：**你是瓶颈。**')
    + p('当你有很多 AI 员工时，人类确实会成为瓶颈。你的速度跟不上 agent。')
))

# Page 7: Eval + taste
pages.append(make_page(7, TOTAL,
    sec('Eval 要尽早建，发现新能力靠 taste')
    + p('产品形态绑太重，每次模型突破都要重写。这是 Kuse 反复踩的坑。')
    + p('但更大的问题是 evaluation framework（评估框架）做得不够好，模型进步之后不知道该往什么方向迭代。')
    + p('后来他们围绕核心场景搭了一套 agentic evaluation agents：模型或 agent runtime 一变，就用一组 agents 自动打分。')
    + p('但 benchmark 只能测已知场景。新模型解锁的新能力，旧 benchmark 测不出来。')
    + p('徐宇豪说这取决于**技术 taste**：能不能通过一手实践，第一时间发现模型解锁了什么。')
    + p('在 Kuse，**全员都是 agent builder**，包括销售。只有自己动手 build，才能更早发现模型到底打开了什么新空间。')
))

# Page 8: 垂类
pages.append(make_page(8, TOTAL,
    sec('垂类 C 端在变成 Skill as a Service')
    + p('徐宇豪有一个判断：agent 时代，垂类很难走通，除非有很强的合规或法律壁垒。')
    + p('逻辑很直接：通用模型能力在快速提升，垂类 agent 的领域知识壁垒会被不断侵蚀。')
    + p('C 端已经在发生这个变化。传统的垂类 SaaS 正在被拆解成一个个 skill。像 ribbi.ai 这样的产品，卖的是 AI skills：创作、发布、监控、优化。产品按能力划分，不再按行业划分。C 端 SaaS 正在变成 **Skill as a Service**。')
    + p('但 B 端垂类还有空间。核心难点是**数据和工作流的深度集成**。一个通用 agent 能写法律文书，但能不能接入律所的 case management system、理解计费规则、遵守保密特权边界？')
))

# Page 9: Agent audit
pages.append(make_page(9, TOTAL,
    sec('当 agent 成为员工，谁来审计它')
    + p('Kuse 给每个 AI 员工配了邮箱、手机号、独立机器。它们有名字，有职责，有权限边界。')
    + p('这带来了全新的问题：**身份、权限和安全。**')
    + p('他们请了白帽团队专门攻击权限系统，设计钓鱼场景测试 agent 能不能识别。Rin 和 Azzurra 知道不把用户数据泄露给任何员工，还会主动告知对方哪些能说、哪些不能说。')
    + p('徐宇豪提到一个发现：**越好的模型，越安全。**')
    + p('现在很多 agent 平台已经在把身份和权限做成原生功能。那当企业同时用多个平台的 agent 时，谁来做独立审计？')
    + p('人类世界里，公司有内审，但仍然需要四大这样的外部审计机构。Agent 世界会不会出现类似的第三方信任层？一个"KPMG for Agents"？')
    + p('只要企业用的不是单一 agent 平台，这个需求就大概率会存在。这是我正在思考和探索的方向。')
))

# Page 10: Closing
pages.append(make_page(10, TOTAL,
    '<div class="closing-text">AI 员工改变的是<br>组织运作的底层逻辑。</div>'
    + '<div class="closing-light">当 Rin 说"你是瓶颈"的时候，<br>这已经超出了工具的范畴。</div>'
    + '<div class="closing-light" style="margin-top:64px; padding-top:48px; border-top:2px solid #ccc;">零融资的 Kuse 能连续做几次<br>大跳水式转型还跑出来，<br>不需要说服投资人，<br>就没有不敢砍的东西。</div>'
    + '<div class="closing-light" style="margin-top:48px;">我相信这个时代会有越来越多的<br>bootstrap 零融资公司出现。</div>',
    is_closing=True
))

# Page 11: References
pages.append(make_page(11, TOTAL,
    sec('参考资料')
    + p('42 章经 × Kuse CTO 徐宇豪访谈<br><span style="font-size:32px; color:#888;">xueqiu.com/1948398032/381679526</span>')
    + p('Peter Thiel《Zero to One》<br><span style="font-size:32px; color:#888;">2014</span>')
    + p('ribbi.ai<br><span style="font-size:32px; color:#888;">ribbi.ai</span>')
    + '<div style="margin-top:80px; padding-top:40px; border-top:2px solid #ccc; font-family:PingFang SC,sans-serif; font-size:28px; color:#aaa; line-height:1.8;">'
    + '本文基于公开访谈内容整理，加入作者个人观点。<br>'
    + '文中提及的产品和公司信息均来自公开来源。<br>'
    + '观点仅代表作者个人，不构成任何投资建议。'
    + '</div>'
))

# ── Write HTML files ──

filenames = []
for i, page_html in enumerate(pages):
    fname = f"page-{i+2:02d}.html"
    fpath = os.path.join(DIR, fname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(page_html)
    filenames.append(fname)
    print(f"  wrote {fname}")

# ── Screenshot all ──

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
print("\nScreenshotting...")

# Also screenshot the cover
all_files = ["style-3-newspaper-v2.html"] + filenames
for fname in all_files:
    fpath = os.path.join(DIR, fname)
    page_num = fname.replace("style-3-newspaper-v2.html", "page-01").replace(".html", "")
    if "style-3" in fname:
        out = os.path.join(DIR, "page-01.png")
    else:
        out = os.path.join(DIR, fname.replace(".html", ".png"))

    result = subprocess.run([
        CHROME, "--headless=new", "--disable-gpu",
        f"--screenshot={out}",
        "--window-size=1080,1800",
        "--force-device-scale-factor=2",
        "--hide-scrollbars",
        f"file://{fpath}"
    ], capture_output=True, text=True)

    if os.path.exists(out):
        print(f"  ✓ {os.path.basename(out)}")
    else:
        print(f"  ✗ FAILED: {os.path.basename(out)}")

print(f"\nDone. {len(all_files)} pages generated.")
