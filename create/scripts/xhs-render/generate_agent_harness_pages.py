#!/usr/bin/env python3
"""Generate newspaper-style content pages for the OpenAI/Anthropic agent harness packaging article."""

import subprocess, os, re, base64

DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = "/Users/odyzhou/Desktop/xhs-build/agent-harness"

def img_data_uri(filename):
    """Read image file and return as base64 data URI (avoids Chrome file:// sub-resource issues)."""
    path = os.path.join(OUT_DIR, filename)
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return f"data:image/png;base64,{b64}"

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
ul.bullets {
  list-style: none; padding: 0; margin-bottom: 28px;
}
ul.bullets li {
  font-family: 'Songti SC','STSong',serif;
  font-size: 34px; font-weight: 400; color: #333;
  line-height: 1.7; margin-bottom: 18px;
  padding-left: 28px; position: relative;
}
ul.bullets li::before {
  content: '·';
  position: absolute; left: 0; top: 0;
  color: #b91c1c; font-weight: 900;
  font-size: 38px;
}
.quote-box {
  font-family: Georgia,serif;
  font-style: italic;
  font-size: 32px; line-height: 1.5;
  color: #111;
  padding: 28px 32px;
  border-left: 4px solid #b91c1c;
  background: rgba(185,28,28,0.04);
  margin-bottom: 28px;
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

/* ── Figure page styles ── */
.figure-title {
  font-family: 'Songti SC','STSong',serif;
  font-size: 38px; font-weight: 900;
  color: #111;
  text-align: center;
  margin-bottom: 28px;
  line-height: 1.35;
}
.figure-img-wrap {
  display: flex; justify-content: center;
  margin-bottom: 28px;
}
.figure-img-wrap img {
  width: 100%; max-width: 920px;
  height: auto;
  background: #fff;
  padding: 16px;
  border: 1px solid #ddd;
  box-shadow: 4px 4px 0 rgba(0,0,0,0.06);
}
.figure-caption {
  font-family: 'Songti SC','STSong',serif;
  font-size: 30px; font-weight: 400;
  color: #333; line-height: 1.65;
  margin-bottom: 20px;
}
.figure-source {
  font-family: 'PingFang SC','Hiragino Sans GB',sans-serif;
  font-size: 22px; color: #999;
  text-align: center;
  font-style: italic;
}

/* ── Chart B: Timeline + Layers ── */
.timeline-wrap {
  display: flex; justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 48px;
  position: relative;
}
.timeline-wrap::before {
  content: '';
  position: absolute; top: 18px; left: 60px; right: 60px;
  height: 2px; background: #333;
  z-index: 0;
}
.timeline-event {
  flex: 1; display: flex; flex-direction: column;
  align-items: center; position: relative; z-index: 1;
}
.timeline-dot {
  width: 36px; height: 36px;
  background: #b91c1c; border: 4px solid #f5f0e8;
  border-radius: 50%;
  margin-bottom: 12px;
}
.timeline-date {
  font-family: Georgia,serif;
  font-size: 22px; font-weight: 700;
  color: #b91c1c;
  margin-bottom: 6px;
}
.timeline-label {
  font-family: 'PingFang SC','Hiragino Sans GB',sans-serif;
  font-size: 18px; color: #333;
  text-align: center;
  line-height: 1.4;
  width: 200px;
}
.layers-wrap {
  display: flex; flex-direction: column-reverse;
  gap: 8px;
}
.layer-row {
  display: flex; align-items: center;
  padding: 16px 24px;
  border: 2px solid #ccc;
  background: #fff;
  font-family: 'PingFang SC','Hiragino Sans GB',sans-serif;
}
.layer-name {
  flex: 1;
  font-size: 22px; font-weight: 700;
  color: #111;
}
.layer-examples {
  flex: 2;
  font-size: 16px; color: #666;
}
.layer-tag {
  flex: 0 0 auto;
  padding: 6px 12px;
  font-size: 16px; font-weight: 700;
  border-radius: 4px;
}
.layer-row.lab {
  background: #f0f0f0; border-color: #999;
}
.layer-row.sandbox {
  background: #fff5f5; border-color: #b91c1c;
}
.layer-row.sandbox .layer-name { color: #b91c1c; }
.layer-row.sandbox .layer-tag {
  background: #b91c1c; color: #fff;
}
.layer-row.framework {
  background: #fffbe6; border-color: #d4a017;
}
.layer-row.framework .layer-tag {
  background: #d4a017; color: #fff;
}
.layer-row.workflow {
  background: #f0f9f0; border-color: #0a7a2f;
}
.layer-row.workflow .layer-tag {
  background: #0a7a2f; color: #fff;
}
.chart-title-bar {
  font-family: Georgia,serif;
  font-size: 26px; font-weight: 700;
  color: #111;
  text-align: center;
  margin-bottom: 24px;
  letter-spacing: 1px;
}
"""

def make_page(page_num, total, body_html):
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
    <div class="footer-left">Ody · Anthropic + OpenAI</div>
    <div class="footer-right">{page_num:02d}</div>
  </div>
</div>
</body></html>"""

def sec(title):
    return f'<div class="section-title">{title}</div>'

def p(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return f'<p>{text}</p>'

def figure_page(title, img_filename, caption, source):
    """OpenAI 官方图作为独立的 figure page。图片用 base64 data URI 内联。"""
    data_uri = img_data_uri(img_filename)
    return (
        f'<div class="figure-title">{title}</div>'
        f'<div class="figure-img-wrap"><img src="{data_uri}" /></div>'
        f'<div class="figure-caption">{caption}</div>'
        f'<div class="figure-source">— {source}</div>'
    )

TOTAL = 14

pages = []

# Page 02 — 开头
pages.append(make_page(2, TOTAL,
    p('我硅谷一个做 agent infra 的朋友，3 月前就从这个赛道撤退了，现在还在探索下一步方向。')
    + p('当时他给我的理由很短：<strong>agent 是大厂头部集中的游戏</strong>。')
    + p('我当时没太理解。直到 4 月初这两周，Anthropic 和 OpenAI 一周内出招，我看明白他说的事。')
))

# Page 03 — 4 月时间线
pages.append(make_page(3, TOTAL,
    sec('4 月这两周到底发生了什么')
    + p('<strong>2026 年 2 月</strong>：OpenAI 给 Responses API 加了 container_auto，托管 Debian 12 容器，预装 Python / Node / Java / Go / Ruby。')
    + p('<strong>4 月 8 日</strong>：Anthropic 发布 Managed Agents，把 brain / harness / sandbox 三件套全部托管。')
    + p('<strong>4 月 15 日</strong>：OpenAI Agents SDK 加 native sandbox harness，一口气接入 9 个 sandbox provider，再配 Codex 风格的 filesystem tools 和 apply_patch。')
    + p('两家做了同一件事：<strong>把 agent harness 这一层全部打包</strong>。')
))

# Page 04 — 新增：OpenAI 图 2（SDK packaging）
pages.append(make_page(4, TOTAL,
    figure_page(
        '"打包"长这样',
        'openai-arch-sdk-small.png',
        'OpenAI 自己画的"打包"动作。左边是你自己拼 agent loop / tool integrations / components，右边是 SDK 包圆，开发者只剩配置。',
        'OpenAI Engineering Blog · 2026-04'
    )
))

# Page 05 — Anthropic 三抽象
pages.append(make_page(5, TOTAL,
    sec('Anthropic 的方案：<br>把整套托管掉')
    + p('Managed Agents 把一个 agent 拆成三个抽象。')
    + p('<strong>Session</strong>：一条 append-only 的事件日志，所有发生过的事都记在这。')
    + p('<strong>Harness</strong>：调 Claude 加路由 tool call 的循环。')
    + p('<strong>Sandbox</strong>：执行环境，统一接口 <code>execute(name, input) → string</code>，下面挂容器、手机、模拟器都行。')
))

# Page 06 — Anthropic 架构变化 + 数据
pages.append(make_page(6, TOTAL,
    p('关键变化在架构。')
    + p('旧版本三件套塞在一个容器里，需要小心维护，挂掉一个 session 全没。')
    + p('新版本 harness 把 sandbox 当 tool 调，容器死了就是一次 tool call 报错，Claude 自己决定要不要 retry，挂了重新起一个。')
    + p('代价收益：<strong>p50 TTFT 降 60%，p95 降 90%</strong>。')
    + p('原因很简单。旧架构每个 session 都付完整容器启动开销；新架构 inference 立刻起跑，容器按需 provision。')
    + '<div class="quote-box">We\'re opinionated about the shape of these interfaces, not about what runs behind them.</div>'
    + p('只定义接口，下面跑什么由他们随时换。')
))

# Page 07 — OpenAI 方案
pages.append(make_page(7, TOTAL,
    sec('OpenAI 的方案：<br>把 sandbox 给别人卷')
    + p('2 月的 container_auto 已经把"hosted Debian 12 容器"这个能力做出来。后来又加了 Agent <strong>Skills</strong>（SKILL.md manifest 加文件 bundle）和完整 shell tool。')
    + p('4 月 15 日的 Agents SDK 升级是这条路线的关键一步。')
    + p('<strong>9 家 sandbox provider 全部接入 SDK</strong>：Unix-local、Docker、Blaxel、Cloudflare、Daytona、E2B、Modal、Runloop、Vercel。要本地、要云、要哪家都行，OpenAI 不挑。')
    + p('表面看是开放，实际是 commoditize。9 家 partner 互相卷价格，OpenAI 只收 token 钱。')
))

# Page 08 — 新增：OpenAI 图 1（harness separate from compute）
pages.append(make_page(8, TOTAL,
    figure_page(
        'sandbox 那一栏，<br>OpenAI 自己列了 5 家',
        'openai-arch-harness-separate.png',
        '左边是旧架构：harness、agent loop、tools、filesystem 全塞 sandbox 一个容器。右边是新架构：harness 从 compute 拆出来，sandbox 列出 OpenAI / E2B / Cloudflare / Vercel / Modal 五家 logo。secrets 留在 harness 一侧，sandbox 拿不到。Runs anywhere: Temporal / AWS / Azure。',
        'OpenAI Engineering Blog · 2026-04'
    )
))

# Page 09 — 包圆 vs 抽水 + Joel Spolsky
pages.append(make_page(9, TOTAL,
    sec('包圆 vs 抽水：<br>二十年前的剧本')
    + p('Joel Spolsky 2002 年写过一篇 Strategy Letter V，核心一句话：<strong>互补品越商品化，主品越值钱</strong>。')
    + p('微软当年把 PC 硬件商品化（让 OEM 互相卷），Windows 利润最大化。IBM 推 Linux 让操作系统商品化，自己卖咨询和服务器。')
    + p('OpenAI 用同样的剧本：主品 = token，互补品 = sandbox。<strong>把 sandbox 卷成商品，token 才更值钱</strong>。')
    + p('Anthropic 走包圆路线：brain + harness + sandbox 全部我来跑，垂直整合换 latency 和集成度。')
    + p('他们做的是同一件事：<strong>抢 agent infra 的接口定义权</strong>。谁定义了 session、harness、sandbox 这三个抽象，谁就拥有下一代 agent 应用的入口。')
))

# Page 10 — 我们独家：时间轴 + 层级图
chart_b = '''
<div class="chart-title-bar">2026 年 4 月：agent infra 战定盘</div>
<div class="timeline-wrap">
  <div class="timeline-event">
    <div class="timeline-dot"></div>
    <div class="timeline-date">2 月</div>
    <div class="timeline-label">OpenAI<br>container_auto</div>
  </div>
  <div class="timeline-event">
    <div class="timeline-dot"></div>
    <div class="timeline-date">4 / 8</div>
    <div class="timeline-label">Anthropic<br>Managed Agents</div>
  </div>
  <div class="timeline-event">
    <div class="timeline-dot"></div>
    <div class="timeline-date">4 / 15</div>
    <div class="timeline-label">OpenAI Agents SDK<br>+ 9 sandbox providers</div>
  </div>
</div>
<div class="layers-wrap">
  <div class="layer-row lab">
    <div class="layer-name">Lab</div>
    <div class="layer-examples">OpenAI / Anthropic</div>
    <div class="layer-tag" style="background:#999;color:#fff;">接口定义权</div>
  </div>
  <div class="layer-row sandbox">
    <div class="layer-name">Sandbox infra</div>
    <div class="layer-examples">E2B / Modal / Daytona / Runloop / Blaxel</div>
    <div class="layer-tag">被夹击 · 18 个月</div>
  </div>
  <div class="layer-row framework">
    <div class="layer-name">Harness framework</div>
    <div class="layer-examples">LangGraph / CrewAI</div>
    <div class="layer-tag">需转 multi-model</div>
  </div>
  <div class="layer-row workflow">
    <div class="layer-name">AI workflow</div>
    <div class="layer-examples">Dify / n8n</div>
    <div class="layer-tag">空白市场</div>
  </div>
  <div class="layer-row">
    <div class="layer-name">垂直应用</div>
    <div class="layer-examples">Heidi / 法律 / 医疗 / 金融</div>
    <div class="layer-tag" style="background:#eee;color:#666;">数据为王</div>
  </div>
</div>
'''
pages.append(make_page(10, TOTAL, chart_b))

# Page 11 — sandbox 公司 18 个月（3 理由）
pages.append(make_page(11, TOTAL,
    sec('为什么 sandbox 公司<br>可能撑不过 18 个月')
    + p('18 个月这个时间是我推断的，不是公开数据。原因有三个。')
    + p('<strong>第一，降低延迟需要垂直整合</strong>。lab 把 inference 和 sandbox 放在同一张网里能拿到 p50 -60%、p95 -90%。E2B 在 AWS、Modal 在自己机房，跨网调用永远追不上。')
    + p('<strong>第二，经济模型只有 lab 能玩</strong>。lab 用 token margin 补贴 runtime，第三方 sandbox 必须直接收容器钱。一份 token 的钱 vs token 加 sandbox 双份钱，价格永远不可能赢。')
    + p('<strong>第三，distribution</strong>。Claude Code、Codex CLI 默认用自家 runtime。开发者第一次接触就被锁定。')
    + p('三个加在一起，<strong>E2B、Modal、Daytona、Runloop、Blaxel 大概率撑不过 18 个月</strong>。最好的出路是被 lab 收编做 acquihire。')
))

# Page 12 — 分层
pages.append(make_page(12, TOTAL,
    sec('分层来看，<br>没有那么粗暴')
    + p('不是所有跟 agent 相关的公司都被打了。')
    + p('<strong>受冲击</strong>：sandbox-as-a-service。E2B、Modal、Daytona、Runloop、Blaxel，他们卖的就是被 lab 内置的能力。')
    + p('<strong>不受影响</strong>：AI workflow（Dify、n8n）。在更高的业务编排层，agent runtime 商品化对他们是利好。')
    + p('<strong>有空间的几条</strong>：')
    + '<ul class="bullets">'
    + '<li>multi-model framework：OpenAI 和 Anthropic 必然分裂，"跨 GPT 和 Claude"是真需求</li>'
    + '<li>企业部署 + 安全合规：SOC2 不是 lab 特权</li>'
    + '<li>垂直应用：法律 / 医疗 / 金融 agent，比如澳洲跑出来的诊所 AI 助手 Heidi</li>'
    + '<li>本地部署 / 隐私敏感场景</li>'
    + '</ul>'
))

# Page 13 — 创业公司站哪一层 + 收尾
pages.append(make_page(13, TOTAL,
    sec('创业公司应该<br>站哪一层')
    + p('<strong>agent infra 这一战已经是大厂游戏，没有创业公司的位置</strong>。')
    + p('真正的空白市场在 workflow 那一层。Dify、n8n 那种把 agent 能力包成业务流程的公司，护城河是场景理解和数据集成，不是 runtime 能力。')
    + p('我给中小企业落地 AI 时，客户要的从来不是"用了什么 sandbox"，是"我这个流程能不能省人"。理解场景和业务比理解 infra 重要得多。')
    + p('<strong>agent infra 越商品化，做 workflow 的人越值钱</strong>。')
    + p('我朋友 3 月前撤退的时候，agent infra 还远没到现在这种格局。他看的不是事件，是趋势。')
    + p('（怪不得人家在硅谷融资百万呢。）')
))

# Page 14 — 参考资料
pages.append(make_page(14, TOTAL,
    sec('参考资料')
    + p('Anthropic Engineering · 2026-04-08<br><span style="font-size:30px; color:#888;">Managed Agents</span><br><span style="font-size:26px; color:#aaa;">anthropic.com/engineering/managed-agents</span>')
    + p('OpenAI Engineering · 2026-02 / 04<br><span style="font-size:30px; color:#888;">Equipping the Responses API with a computer environment</span><br><span style="font-size:26px; color:#aaa;">openai.com/index/equip-responses-api-computer-environment</span>')
    + p('VentureBeat · 2026-04-15<br><span style="font-size:30px; color:#888;">OpenAI Agents SDK + agent skills + complete terminal shell</span>')
    + p('Joel Spolsky · 2002<br><span style="font-size:30px; color:#888;">Strategy Letter V — Commoditize Your Complement</span><br><span style="font-size:26px; color:#aaa;">joelonsoftware.com/2002/06/12/strategy-letter-v</span>')
    + '<div style="margin-top:36px; padding-top:28px; border-top:2px solid #ccc; font-family:PingFang SC,sans-serif; font-size:22px; color:#aaa; line-height:1.7;">'
    + '本文基于两家公开技术博客整理，结合作者一手 builder 视角。<br>'
    + 'Page 04 / 08 架构图来自 OpenAI Engineering Blog · 2026-04，仅作分析引用。<br>'
    + '"18 个月窗口" 是作者推断，非公开数据。判断与立场仅代表作者个人。'
    + '</div>'
))

# ── Write & screenshot ──

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
print("Generating pages...")

for i, page_html in enumerate(pages):
    page_num = i + 2
    fname = f"_page-{page_num:02d}.html"
    fpath = os.path.join(OUT_DIR, fname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(page_html)

    out_png = os.path.join(OUT_DIR, f"page-{page_num:02d}.png")
    result = subprocess.run([
        CHROME, "--headless=new", "--disable-gpu",
        f"--screenshot={out_png}",
        "--window-size=1080,1800",
        "--force-device-scale-factor=2",
        "--hide-scrollbars",
        "--allow-file-access-from-files",
        f"file://{fpath}"
    ], capture_output=True, text=True, timeout=180)

    os.remove(fpath)

    if os.path.exists(out_png):
        print(f"  ✓ page-{page_num:02d}.png")
    else:
        print(f"  ✗ FAILED page-{page_num:02d}: {result.stderr[:200]}")

print(f"\nDone. {len(pages)} pages generated in {OUT_DIR}.")
