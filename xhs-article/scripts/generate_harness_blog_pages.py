#!/usr/bin/env python3
"""Generate newspaper-style content pages for the harness blog article."""

import subprocess, os, re

DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = "/Users/odyzhou/Desktop/xhs-posts/covers"

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

/* ── Flow chart styles for page 06 ── */
.chart-wrap {
  display: flex; gap: 60px; padding: 0;
  align-items: stretch;
}
.chart-col {
  flex: 1; display: flex; flex-direction: column;
  align-items: center;
}
.chart-title {
  font-family: Georgia,serif;
  font-size: 30px; font-weight: 700; color: #111;
  margin-bottom: 8px;
  text-align: center;
}
.chart-subtitle {
  font-family: 'PingFang SC','Hiragino Sans GB',sans-serif;
  font-size: 22px; color: #888;
  margin-bottom: 36px;
  letter-spacing: 2px; text-transform: uppercase;
}
.flow-node {
  width: 280px;
  padding: 20px 16px;
  background: #fff;
  border: 2px solid #333;
  border-radius: 4px;
  font-family: 'PingFang SC','Hiragino Sans GB',sans-serif;
  font-size: 26px; font-weight: 700; color: #111;
  text-align: center;
  box-shadow: 4px 4px 0 rgba(0,0,0,0.08);
}
.flow-node.accent {
  border-color: #b91c1c;
  background: #fff5f5;
  color: #b91c1c;
}
.flow-arrow {
  font-family: Georgia,serif;
  font-size: 36px; color: #555;
  margin: 8px 0;
  line-height: 1;
}
.flow-arrow.curve {
  color: #b91c1c;
  font-weight: 700;
}
.cycle-wrap {
  position: relative;
  width: 380px; height: 720px;
  display: flex; flex-direction: column;
  align-items: center; justify-content: space-between;
}
.cycle-side-arrow {
  position: absolute;
  font-family: 'PingFang SC','Hiragino Sans GB',sans-serif;
  font-size: 24px; color: #b91c1c;
  font-weight: 700;
  writing-mode: vertical-rl;
  text-orientation: mixed;
  letter-spacing: 4px;
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
    <div class="footer-left">Ody · Anthropic Engineering</div>
    <div class="footer-right">{page_num:02d}</div>
  </div>
</div>
</body></html>"""

def sec(title):
    return f'<div class="section-title">{title}</div>'

def p(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    return f'<p>{text}</p>'

TOTAL = 11

pages = []

# Page 02 — 开头 + 章节1
pages.append(make_page(2, TOTAL,
    p('我在写一个叫 Compose 的深度写作软件。')
    + p('每天的状态是：让 AI 写一版交互，自己上手用，发现哪里不对，再回去剖自己的思维方式，重新定义产品该长什么样。')
    + p('1-4 句话讲清楚要做什么的产品，我手上一个都没有。')
    + p('所以三月底 Anthropic 那篇 harness blog 出来时，我看完决定不用它。')
    + p('它做得很好，只是场景不对。')
))

# Page 03 — 章节1 三 agent 架构
pages.append(make_page(3, TOTAL,
    sec('Anthropic 这套 harness 在解决什么')
    + p('文章里给了一个三 agent 的架构：<strong>Planner</strong> 把用户 1-4 句话的 prompt 扩成完整的产品 spec，<strong>Generator</strong> 按 sprint 一个 feature 一个 feature 写代码，<strong>Evaluator</strong> 用 Playwright MCP 自己点页面、跑测试、打分、写 bug。')
    + p('三个 agent 之间通过文件交接，不通过 prompt。')
))

# Page 04 — 章节1续 数字案例
pages.append(make_page(4, TOTAL,
    p('效果数字很有说服力。')
    + p('Game Maker 案例（Opus 4.5）：单 agent 跑 20 分钟花 <strong>$9</strong>，游戏跑起来了但核心是坏的，entity 出现在屏幕上点了没反应。换成完整 harness 跑 6 小时花 <strong>$200</strong>，出了能玩的版本，spec 被 Planner 扩成 16 个 feature 分 10 个 sprint。')
    + p('DAW 案例（Opus 4.6）：3 小时 50 分钟花 <strong>$124</strong>，删掉 sprint 一条 session 跑到底，能在浏览器里靠 prompt 让 agent 帮你作曲。')
    + p('v2 删掉了 sprint，因为 Opus 4.6 能 sustain agentic tasks for longer。但 Planner 和 Evaluator 没删：自己评自己宽容是结构问题，模型再强也治不了。')
))

# Page 05 — 章节2 隐藏假设
pages.append(make_page(5, TOTAL,
    sec('这套方案的隐藏假设')
    + p('读完之后我把这套方案的前提列了一下，发现有四个：')
    + p('人能用 <strong>1-4 句话讲清楚</strong>要什么。')
    + p('人愿意把 spec 的细化完全交给 Planner，<strong>不审、不改</strong>。')
    + p('人不在跑的过程中介入，<strong>全程零干预</strong>。')
    + p('成功标准是<strong>可测的</strong>，Game Maker 第 3 个 sprint 一个 contract 就有 27 条验收标准。')
    + p('这四个加在一起，说的是同一件事：<strong>spec 在执行前就已经存在</strong>，剩下的是怎么把它高质量地交付出来。')
))

# Page 06 — 章节3 概念二分文字
pages.append(make_page(6, TOTAL,
    sec('spec-execution 与<br>continuous fit-finding')
    + p('我把这套工作流叫 <strong>spec-execution</strong>：spec 已知，问题是执行。')
    + p('我自己每天做的事是另一种，<strong>continuous fit-finding</strong>：spec 是边写边浮现的，问题是发现。')
    + p('Compose 是后者。')
    + p('我得让 AI 先写出一版交互，自己上手用，才知道这条路对不对。很多时候用一下发现"不是这样"，才能反过来想清楚到底想要什么。')
))

# Page 07 — 配图：waterfall vs cycle
def flow_node(label, accent=False):
    cls = "flow-node accent" if accent else "flow-node"
    return f'<div class="{cls}">{label}</div>'

waterfall_col = (
    '<div class="chart-col">'
    '<div class="chart-title">Anthropic Harness</div>'
    '<div class="chart-subtitle">Waterfall</div>'
    + flow_node('Prompt')
    + '<div class="flow-arrow">↓</div>'
    + flow_node('Planner')
    + '<div class="flow-arrow">↓</div>'
    + flow_node('Spec')
    + '<div class="flow-arrow">↓</div>'
    + flow_node('Generator')
    + '<div class="flow-arrow">↓</div>'
    + flow_node('Evaluator')
    + '<div class="flow-arrow">↓</div>'
    + flow_node('Done')
    + '</div>'
)

cycle_col = (
    '<div class="chart-col">'
    '<div class="chart-title">My Workflow</div>'
    '<div class="chart-subtitle">Cycle</div>'
    + flow_node('AI 写功能')
    + '<div class="flow-arrow">↓</div>'
    + flow_node('我体验', accent=True)
    + '<div class="flow-arrow">↓</div>'
    + flow_node('思考 spec', accent=True)
    + '<div class="flow-arrow">↓</div>'
    + flow_node('更新 spec')
    + '<div class="flow-arrow curve">↺ 回到顶部</div>'
    + '</div>'
)

pages.append(make_page(7, TOTAL,
    sec('两种流程一眼对比')
    + f'<div class="chart-wrap">{waterfall_col}{cycle_col}</div>'
))

# Page 08 — 章节4 我的工作流
pages.append(make_page(8, TOTAL,
    sec('我自己怎么用 agent')
    + p('如果是单功能开发，<strong>Claude Code 的 Plan mode 就够用</strong>，不需要任何额外的 harness。')
    + p('如果是生产环境的产品，我现在的工作流是这样：')
    + p('第一步，用 <strong>Codex 的 Plan mode</strong>，把这个 feature 要做什么、模块怎么划、边界在哪聊清楚。聊到双方都明确了再让他动手。Codex 执行的同时做 E2E 测试：webapp 用 Playwright MCP 自己点，客户端直接 computer use 操作我的鼠标。')
))

# Page 09 — 章节4续
pages.append(make_page(9, TOTAL,
    p('第二步，<strong>我自己手动测一遍</strong>。机器测的是功能跑通了没，我测的是手感对不对、流程顺不顺。')
    + p('第三步，<strong>Claude review 代码</strong>，我把 review 结果发回给 Codex，让他选择性改进。哪些建议要采纳是我和 Codex 一起判断的，他不会全盘照单全收。')
    + p('这套用法里其实有 multi-agent，Codex 写、Claude review 是两个不同 context 的 agent 在协作。')
    + p('但和 Anthropic 的三件套不一样的地方在于，<strong>spec 始终在浮现状态，每一轮 cycle 都和 Codex 一起重新定义</strong>。Planner 一次写死 spec 的做法在这里反而是阻碍。')
))

# Page 10 — 章节5 真正的 insight + 收束
pages.append(make_page(10, TOTAL,
    sec('真正的 insight 是上下文隔离')
    + p('Anthropic 那篇文章的 insight 我觉得很到位，特别是 multi-agent 协同的部分。他们做对的事是<strong>让每个 agent 的上下文保持隔离，从而保持专注</strong>。')
    + p('Planner 不被 Generator 的实现细节污染，Evaluator 不被 Generator 的自我辩护污染。这就是为什么自评宽容是结构问题。')
    + p('这个 insight 我在用。Codex 写代码、Claude review 也是同样的逻辑：review 的 agent 不应该是写代码的那个 agent。')
    + p('我没用的是 spec-first 这一层。在 spec 已经清楚的小玩具上 Planner 是合理的；在 spec 还没浮现的产品上，Planner 会把模糊意图过早固化，扼杀掉发现的空间。')
    + p('如果你能用 1-4 句话讲清楚一个生产环境的产品，欢迎评论区告诉我，我想看看那是什么样。')
))

# Page 11 — 参考资料
pages.append(make_page(11, TOTAL,
    sec('参考资料')
    + p('Anthropic Engineering · 2026-03-24<br><span style="font-size:30px; color:#888;">Harness Design for Long-Running Application Development</span><br><span style="font-size:28px; color:#aaa;">anthropic.com/engineering/harness-design-long-running-apps</span>')
    + '<div style="margin-top:80px; padding-top:40px; border-top:2px solid #ccc; font-family:PingFang SC,sans-serif; font-size:28px; color:#aaa; line-height:1.8;">'
    + '本文基于 Anthropic 公开技术博客整理，结合作者一手 agent 工程实践。<br>'
    + '文中数字、案例、引文均来自原文。<br>'
    + '判断与立场仅代表作者个人。'
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
        "--hide-scrollbars",
        f"file://{fpath}"
    ], capture_output=True, text=True)

    os.remove(fpath)

    if os.path.exists(out_png):
        print(f"  ✓ page-{page_num:02d}.png")
    else:
        print(f"  ✗ FAILED page-{page_num:02d}: {result.stderr[:200]}")

print(f"\nDone. {len(pages)} pages generated in {OUT_DIR}.")
