---
name: inspire-me
description: Research the latest AI landscape and deliver a curated, insight-rich briefing to inspire Ody. Use when Ody says "inspire me", asks for AI news, wants content ideas, wants to explore what's happening in AI, or needs inspiration for X posts, 小红书 posts, startup ideas, or personal learning. Searches the web extensively for viral AI products, lab blog posts, technical papers, X discourse, startup launches, and draws non-obvious connections between findings.
---

# Inspire Me

Curated AI intelligence briefing for Ody. Research → Synthesize → Connect → Inspire.

## Workflow

### Phase 1: Research Sweep

Run parallel web searches across these categories. Aim for 5-8 topics total, mixing deep dives and quick hits.

**Search targets (run in parallel):**

1. **Viral AI products** — Search: "viral AI product this week", "AI tool trending Product Hunt", "new AI app blowing up"
2. **Lab blog posts** — Search each: "Anthropic blog new post", "OpenAI blog new post", "Google DeepMind blog", "Meta AI research blog", "Mistral AI blog"
3. **X/Twitter AI discourse** — Search: "AI twitter discourse this week", "viral AI tweet", "AI debate trending"
4. **AI startups & funding** — Search: "AI startup funding this week", "new AI startup launch", "YC AI company"
5. **Technical posts** — Search: "AI engineering blog post", "machine learning technical deep dive", "AI systems design"
6. **AI policy & regulation** — Search: "AI regulation news", "AI policy update"
7. **Interesting demos & use cases** — Search: "AI demo impressive", "creative AI use case"

For each interesting find, use WebFetch to read the actual source. Do not just rely on search snippets.

### Phase 2: Synthesize & Connect

This is the most important phase. Do NOT just list what you found.

For each notable find:
- Summarize what it is and why it matters
- Rate interestingness (1-5) based on: novelty, Ody's interests, content potential, learning value
- **Draw connections** — This is the key differentiator. Look for:
  - Two labs solving the same problem differently (e.g., Claude agent team vs Kimi agent swarm)
  - A product that validates/contradicts a trend
  - A technical approach that enables a new product category
  - A pattern emerging across multiple unrelated developments
  - Historical parallels (this happened before in mobile/web/crypto)

### Phase 3: Deliver the Briefing

Generate a beautiful HTML briefing using the MotherDuck-inspired template at `assets/template.html`.

**Content structure:**

1. **TL;DR** (3-5 bullet points) - Most interesting finds and connections
2. **Deep Dives** (2-3 cards) - Each card includes:
   - Topic title
   - Interest badge (5=⭐⭐⭐, 4=⭐⭐, 3=⭐)
   - **What:** What happened / what it is
   - **Why it matters:** Non-obvious significance
   - **Connection:** How it connects to other developments
   - **Content angle:** X post angle, 小红书 angle, or both
   - **Startup signal:** Product opportunity if applicable
3. **Quick Hits** (3-5 items) - Shorter cards with 2-3 sentences each
4. **Connections & Patterns** - Observations spanning multiple finds
5. **X Posts - Ready to Copy** - Actual short, copy-pasteable X posts (NOT outlines or descriptions)
   - **IMPORTANT: Single posts ONLY, NO threads**
   - Each post should be the final text ready to paste into X
   - Include copy buttons for each post
   - Show character counts
   - Keep posts concise and punchy (~600-900 characters max)
   - Make each post self-contained with a clear hook and insight
6. **Startup Signals** - Opportunities, gaps, or product ideas
7. **Sources** - All links discovered during research

**Template variables to fill:**

- `{{DATE}}` - Today's date (e.g., "February 15, 2026")
- `{{TLDR_ITEMS}}` - HTML `<li>` items for TL;DR bullets
- `{{DEEP_DIVE_CARDS}}` - HTML card blocks for deep dives
- `{{QUICK_HIT_ITEMS}}` - HTML quick hit blocks
- `{{CONNECTION_PARAGRAPHS}}` - HTML `<p>` tags for connections
- `{{CONTENT_IDEA_CARDS}}` - HTML cards with actual copy-pasteable X posts (with copy buttons), NOT descriptions
- `{{STARTUP_SIGNAL_CARDS}}` - HTML signal cards
- `{{SOURCE_LINKS}}` - HTML `<li>` items with links

**Deep dive card template:**
```html
<div class="card">
    <h3>[Topic Title]</h3>
    <div class="meta">
        <span class="badge interest-5">⭐⭐⭐ Must Read</span>
        <span class="badge">[Category]</span>
    </div>
    <div class="card-section">
        <h4>What</h4>
        <p>[Description]</p>
    </div>
    <div class="card-section">
        <h4>Why It Matters</h4>
        <p>[Significance]</p>
    </div>
    <div class="card-section">
        <h4>Connection</h4>
        <p>[How it relates to other finds]</p>
    </div>
    <div class="card-section">
        <h4>Content Angle</h4>
        <p>[Post ideas]</p>
    </div>
</div>
```

**X Post card template with copy button:**
```html
<div class="idea-card">
    <div class="post-header">
        <div>
            <span class="platform-tag x">X</span>
            <span style="font-family: 'Courier Prime', monospace; font-weight: 700;">[Post Title]</span>
        </div>
        <button class="copy-btn" onclick="copyPost(this, 'xpost1')">Copy</button>
    </div>
    <div class="post-content" id="xpost1">[Actual post text ready to copy-paste - single post only, NO threads]</div>
    <div class="post-meta">~XXX characters</div>
</div>
```

**Important:** Add copy button JavaScript before `</body>`:
```javascript
<script>
    function copyPost(btn, postId) {
        const postContent = document.getElementById(postId).innerText;
        navigator.clipboard.writeText(postContent).then(() => {
            const originalText = btn.innerText;
            btn.innerText = 'Copied!';
            btn.classList.add('copied');
            setTimeout(() => {
                btn.innerText = originalText;
                btn.classList.remove('copied');
            }, 2000);
        });
    }
</script>
```

### Phase 4: Go Deeper

After presenting the briefing, ask Ody:
- Which topics to dive deeper on
- Whether to draft any posts based on the finds
- Whether any startup ideas are worth exploring further

If Ody wants to write a post, suggest using `/x-article` or `/xhs-article` skills.

### Phase 5: Save to File

Save the HTML briefing to `~/Desktop/inspire-me/YYYY-MM-DD.html` (create directory if needed).

The HTML file should be fully self-contained and ready to open in a browser.

## Research Quality Rules

- **Go deep, not wide on the best stuff.** Read the actual blog post or article, don't just skim search results
- **Connections are king.** A briefing without connections is just a news feed. Always ask: "how does this relate to something else I found?"
- **Be opinionated.** Flag what YOU think is most interesting and why. Don't be neutral
- **Freshness matters.** Prioritize last 7 days. Flag if something is older but newly relevant
- **Ody's lens:** He cares about AI products, technical engineering, startup opportunities, and content that makes people think. Filter through this lens
- **No fluff.** Skip minor version updates, routine funding rounds under $10M, or incremental product features unless they signal something bigger
