---
name: x-article
description: Create long-form X (Twitter) Articles for Ody. Use when Ody asks to write an X article, Twitter article, or long-form post. Guides through a 5-phase workflow: (1) Ideation & Angle, (2) Structure & Outline, (3) Writing the Draft, (4) Review & Edit, (5) Deliver & Promote. Waits for approval between phases.
---

# X Article Creation

Follow this 5-phase workflow sequentially. Wait for Ody's approval before moving to the next phase.

## Phase 1: Ideation & Angle

Before writing anything:

1. **Core thesis** - Distill topic into a single provocative claim that makes a smart person stop scrolling
2. **Framework** - Identify or create a named framework/mental model (named frameworks are sticky and shareable, e.g., "The Maslow Trap")
3. **Tension** - What's the contradiction, the thing people get wrong, or the uncomfortable truth? The article should resolve a tension
4. **Actionability** - Ensure readers get something to *do*: a framework, mental model, or process

**Present to Ody before proceeding:**
- Thesis (one sentence)
- Framework/lens
- Tension being resolved
- Suggested title (provocative, specific, curiosity-driven)
- Estimated length: post (200-500 words) or article (1000-3000 words)

## Phase 2: Structure & Outline

After angle approval:

1. **Essay arc**: Setup → Tension → Escalation → Climax → Resolution/Takeaway
2. **Section titles** - Each gets an evocative, descriptive title that works as a standalone hook
3. **Evidence per section** - At least one of: data/stats, quotation, real-world example, analogy/metaphor
4. **Web search for evidence** - Before finalizing outline, run quick web searches to verify:
   - Current product names, versions, and features (e.g., GPT-5 not GPT-4, latest Claude features)
   - Recent releases, dates, and timelines
   - Stats and data points are accurate and up-to-date
   - Examples and case studies are current and correctly attributed
   - Any quotes are real and correctly sourced
5. **Visuals** - Plan one `[VISUAL: description]` every 500-800 words. Web search for reference images, diagrams, or graphics that match each visual need — provide links Ody can use or adapt
6. **Open** - First sentence: provocation, stance, or hook (no warmup). Use bookmark-triggers: "here's how," "here's why"
7. **Close** - Plan specific device: personal story, callback to opening, mic-drop line, or provocative question
8. **Engagement** - Decide per section: confrontational (hard stance) or collaborative (invites perspective). Close always includes a question or invitation

Present full outline with verified evidence and visuals. Wait for approval.

## Phase 3: Writing the Draft

See references/style-guide.md for complete voice, formatting, and content rules.

**Key requirements:**
- Ody's voice: analytical but conversational, framework-driven, Gen Z vernacular where it fits
- Short paragraphs: 1-4 lines max, one idea per paragraph
- Bold key insights for skimmers
- Every claim needs evidence (stats, examples, quotes)
- Include 2-4 quotations, at least one personal anecdote
- Use `[VISUAL: description]` tags inline
- Make it actionable

**Ody's signature style elements:**
- → chains for causality: "Technology emerges → Incumbents dismiss → Startups win"
- Named frameworks (if you spot a pattern, title it)
- Contrast pairs with parenthetical inversions: "Consensus adoption (not dismissal)"
- Cold lines after analytical buildup: "That's the bar."
- Academic-to-casual bridge: reference Christensen then drop "lol"

## Phase 4: Review & Edit

After draft completion:

1. **Cut 20-30%** - Eliminate filler: "very," "really," "in order to," "it's important to note"
2. **Structure check** - Verify headers are compelling hooks, arc builds properly, open hooks, close punches
3. **Evidence check** - Verify all data accurate, claims supported, quotes attributed. Quick web search to double-check any facts that weren't verified in Phase 2
4. **Visual check** - One `[VISUAL]` per 500-800 words at natural break points. Ensure each has a reference link from web search
5. **Readability pass** - Read aloud, break up 4+ line paragraphs, maintain consistent tone

## Phase 5: Deliver & Promote

**Prepare promotion assets without being asked:**

1. **Teaser post** - 1-3 sentences teasing tension without revealing thesis. Use bookmark-triggers
2. **2-3 excerpt posts** - Standalone posts with key insights linking to full piece. Choose confrontational or collaborative angle for each
3. **Promotion notes:**
   - Recommend pinning for 24-72 hours
   - Flag if evergreen (can reshare during relevant news)
   - Suggest engaging with early replies

**Output to file:**

Write a markdown file to `/Users/odyzhou/Desktop/x-posts/[article-title].md` with this structure:

```markdown
# [Article Title]

## Warm-Up Posts

### Teaser Post
[teaser content]

### Excerpt Posts
[excerpt posts]

---

## Article

[full article content]

---

## Notes
- Visuals needed: [list of VISUAL tags with reference image links from web search]
- Stats to verify: [any flagged stats]
- Promotion notes: [pinning, evergreen status, engagement tips]
```

Create the `/Users/odyzhou/Desktop/x-posts/` directory if it doesn't exist. Use kebab-case for filename (e.g., `the-maslow-trap.md`).
