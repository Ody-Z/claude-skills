# Platform: X (Twitter)

X platform spec + writing constraints. Layered on top of [[voice]], does not duplicate voice rules.

When `/x-article` is built, it must Read this file before execution.

---

## Platform DNA

- **Character limits**: 280 per tweet (links count as 23 chars). Long-form tweets up to 25,000, sweet spot 1,000-2,000
- **Tempo**: fast, opinion-driven, scrollable. Users have ~0.5 seconds to be hooked. First line is everything
- **Algorithm**: engagement rate (replies > retweets > likes) + dwell time. **Replies are the highest signal** — early reply velocity decides whether a post takes off
- **Ody's audience here skews [[builders]]**: indie hackers, AI engineers, founders, independent researchers. The [[casual]] layer is nearly absent on X
- **Language strategy**: English-first. Ody's X target is the international AI builder community. Chinese only when explicitly addressing the (small) Chinese X niche

---

## Content Rules

- **Read [[voice]] first**: hard rules apply unchanged on X — no emoji, no exclamation marks, no em-dashes, no "不是 X 是 Y" patterns, no guru voice. The platform vibe is more casual but Ody's three cores (judgment sharpness / humble observer / information density) don't loosen
- **Register can be looser**: X allows more colloquial phrasing than voice.md's default. But **not the all-lowercase aesthetic** (the Naval / dril path doesn't fit Ody's builder-consultant positioning) — keep normal capitalization
- **No hashtags. Ever.** They read as spammy on X
- **Links in a reply to your own post, never in the main tweet** — the algorithm penalizes external links in the main body
- **Line breaks between every thought**. Don't write dense paragraphs in tweets
- **First line is everything**: in a 280-char tweet, if line one doesn't hook them, the rest is wasted

---

## Formats That Work

Ranked by fit with Ody's content types + X algorithm preference:

1. **Step-by-Step Thread** (most reliable) — "Here are N things I learned building X:" + 5-7 numbered tweets. Fits Ody's methodology-sharing and battle-report prototypes
2. **Proof Post** (high conversion) — "[before metric] → [after metric] in [timeframe]" + the breakdown. Fits the AI-product-landing analysis prototype condensed into a single data-driven thread
3. **Contrarian Short Take** (2-4 lines) — bold claim + one-line context + punchline. Fits the thinking-notes prototype, but the judgment has to be sharp. Soft critique falls flat
4. **Resource Drop** (high value) — "Just found [thing] — [why it matters]" + a one-line personal take. **Personal judgment is mandatory.** Pure retweets have no Ody in them
5. **Long-Form Tweet** (1-2x/week max) — 1,000-2,000 chars, deep breakdown of one idea. Use when deriving from `articles/`

---

## Posting Strategy

Industry defaults below — Ody's actual cadence to be calibrated after a few months of real posting:

- **Frequency**: 5-7 tweets/week (1-2/day). Below this, the algorithm down-weights you
- **Best times** (target audience timezone): 8-9am, 12-1pm, 5-6pm. Ody's English audience is mostly US West / East — Australia timezone requires staggered scheduling
- **30-minute rule**: spend the first 30 min after posting actively replying to your timeline. Early reply velocity is decisive
- **High-leverage list**: pick 10-20 accounts with 10-100x your follower count in your space. One or two substantive comments/day (not flattery — additions or pushback)

---

## Audience on X

- **Primary**: [[builders]] — indie hackers, AI engineers, SaaS founders, independent researchers
- **What they want**:
  - Actionable content (a playbook they can run today)
  - Real numbers (revenue, metrics, cost, time saved)
  - Tool recommendations (with when + why, not just "use this tool")
  - First-hand builder perspective (what you're building, what broke, what you decided)
- **What they don't want**:
  - Motivational quotes with no substance
  - "AI is changing the world" grand-narrative takes
  - Marketing voice, course pitches, signup CTAs
  - "I think AI will XXX" claims with no numbers
- **How to address them**: direct "you", peer energy (building alongside them), never coach energy ("Let me teach you")

---

## Repurposing Notes

Ody uses X in two modes:

### Mode A: X-first short content
Same-day hot takes, news reactions, build progress, tool discoveries — X is the starting point.
- After posting on X, expand into [[linkedin]] long-form (add narrative + professional framing)
- Multiple X tweets can aggregate into a weekly digest (if Ody runs a newsletter)

### Mode B: Derived from articles/
When Ody finishes a deep long-form piece (battle-report / product-thinking / AI-product-analysis prototype), extract a tweet thread.
- 1 hook tweet: the most counter-intuitive judgment from the long-form + a first-hand detail
- 3-5 expansion tweets: each a standalone observation, readable without context
- 1 closing tweet with the long-form link (link goes in a reply, not the main tweet)
- Full flow in [[repurpose]] phase C

### Cross-platform rewriting
- Chinese builder-circle context (e.g. "卡兹克路线", "同频读者", "AI 大厂") → rewrite with English builder-circle analogs readers can actually parse
- Keep judgment sharpness; adjust terminology and cultural reference points; **don't soften the position**
- Don't copy-paste long-form paragraphs — X needs new rhythm

---

## To fill in (after 3-5 months of real posting)

- Which hook patterns perform best on Ody's account (with specific metrics)
- The actual high-leverage account list (recalibrate monthly)
- Comment-quote trigger library (which accounts discussing which topics are worth quoting back into)
- Which prototypes travel best on X (working hypothesis: technical-blog analysis and thinking-notes > AI-product analysis, since the latter is more naturally a long-form / image post)
- Ody's optimal posting times (balancing Australia + US West/East audiences)
