# 报纸社论风格模版 (Newspaper Editorial)

确认于 2026-04-07，Ody 选定的小红书封面/正文风格。

## 设计语言
- 牛皮纸质感，权威感 + 信息感
- 衬线字体为主，无衬线用于标签/元信息
- 单色红做强调色，克制使用
- 装饰性分栏线（居中半透明竖线）

## 色彩
- 背景: `#f5f0e8`（牛皮纸色）
- 主文字: `#111`
- 次文字: `#555`
- 三级文字/meta: `#777`, `#888`, `#999`, `#aaa`
- 强调红: `#b91c1c`
- 边框线: `#ccc`
- 分栏线: `rgba(0,0,0,0.05)`
- 装饰页码: `rgba(0,0,0,0.05)`

## 字体
- 标题/正文: `'Noto Serif SC', serif`（wght 400/700/900）
- 标签/元信息: `'Noto Sans SC', sans-serif`（wght 400/700/900）
- 装饰/英文标题: `'Playfair Display', serif`（wght 700/900）
- Google Fonts import: `https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700;900&family=Noto+Sans+SC:wght@400;700;900&family=Playfair+Display:wght@700;900&display=swap`

## 封面字号（1080x1800 画布）
- 报头 DEEP DIVE: Playfair Display, 36px, 900, letter-spacing 10px
- 深度标签: Noto Sans SC, 20px, 700, 白字红底(#b91c1c)
- 来源: Noto Sans SC, 22px, #777
- 日期: Noto Sans SC, 20px, #999
- 大数字: Playfair Display, 220px, 900, #111
- 美元符号: 150px, #b91c1c
- 数据行: Noto Sans SC, 36px, 400, #777
- 主标题: Noto Serif SC, 88px, 900, #111
- 金句副标题: Noto Serif SC, 54px, 700, #333, italic
- 署名/引用来源: Noto Sans SC, 24px, #aaa
- 署名 "文": 36px, #888; 名字: 44px, 900, #333
- 装饰页码: Playfair Display, 128px, 900, rgba(0,0,0,0.05)

## 正文页字号
- 页眉: Playfair Display, 18px; 页码 Noto Sans SC, 20px
- 章节标题: Noto Serif SC, 52px, 900, #111
- 正文: Noto Serif SC, 38px, 400, #333, line-height 1.8
- 加粗: weight 700, color #111
- Pull quote: Noto Serif SC, 46px, 700, #333, italic
- 引用来源: Noto Sans SC, 22px, #aaa

## 画布与间距
- 画布: 1080 x 1800 px (9:15)
- 容器 padding: 32px top, 80px sides, 100px bottom
- 纸面纹理: SVG fractalNoise, opacity 0.4
- 分栏线: 居中竖线, top/bottom 160px margin
- 封面 header 推到顶部以便缩略图裁掉

## 截图
- Chrome headless: `--headless=new --window-size=1080,1800 --hide-scrollbars`
- 输出 PNG
