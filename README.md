# Claude Code Skills

This repository contains custom skills for Claude Code.

## Skills

### x-article
Creates long-form X (Twitter) articles through a structured 5-phase workflow:
1. Ideation & Angle
2. Structure & Outline
3. Writing the Draft
4. Review & Edit
5. Deliver & Promote

### xhs-article
帮助创作小红书图文笔记/长文，遵循 4 阶段工作流：
1. 选题与切入角度
2. 结构与大纲
3. 撰写初稿
4. 审稿与打磨

### inspire-me
Researches the latest AI landscape and delivers curated, insight-rich briefings. Searches extensively for viral AI products, lab blog posts, technical papers, X discourse, and startup launches.

### skill-creator
Guide for creating effective skills. Helps create new skills or update existing ones with specialized knowledge, workflows, or tool integrations.

## Installation

These skills are automatically loaded from `~/.claude/skills/` by Claude Code.

## Structure

Each skill follows this structure:
```
skill-name/
├── SKILL.md          # Main skill definition
├── references/       # Reference materials and guides
└── assets/          # Additional assets (templates, images, etc.)
```

## Usage

Skills can be invoked in Claude Code using:
- The `/skill-name` command (e.g., `/x-article`, `/inspire-me`)
- Or by asking Claude to use the relevant skill

## Contributing

Feel free to modify and enhance these skills to better suit your workflow.
