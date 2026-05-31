# Eval Sprint — write your product's spec as runnable evals

**20 minutes. No API key needed.** You just watched a PM turn 5 requirements into
runnable tests, run them, and catch a failure. Now do it for *your* AI4Good project.

You're not building the app today — you're writing the **spec** for it, as evals.
Run them and they go **red**. That's the point: **red is your spec.** Wednesday
you build until they turn green.

## Setup (1 min)

```bash
git clone https://github.com/jphreid/ai4good-sprint-starter.git && cd ai4good-sprint-starter
```

You have Claude Code, so let it do the work. Open Claude Code in this folder:

```bash
claude
```

## The sprint — run two skills from the review board

This repo ships two of the review-board skills in `.claude/skills/`. Invoke them by
name in Claude Code.

**1 — Scope it.** Run `/pm-critic`. It scopes your project — one user, one job, one
measurable metric, the augment-vs-automate call — and writes `product/ai-canvas.md`
+ `product/one-pager.md`. Tell it your project in a sentence and let it ask.

**2 — Spec it.** Run `/eval-critic`. It turns your requirements into runnable evals
in `evals/test_evals.py` — one per criterion (happy path · edge · values/safety ·
behavioral · UX), each with a `# Rubric:` comment. **No API key needed:** it writes
plain deterministic checks (a substring like `"next step" in out`, length, timing) and `skip`s any
genuinely-subjective eval for Wednesday.

**3 — Run them:**

```bash
uv run pytest evals/ -v --tb=line
```

(Or just ask Claude Code to run them.) Expect **mostly red**, a couple **skipped** —
your app is still a stub. Every red is a requirement.

> Prefer to drive Claude directly instead of the skills? Same loop you watched in
> the demo works too: ask it to brainstorm 5 criteria + rubrics, then "turn these
> into deterministic pytest evals against `app.agent.respond`, no API key, skip
> judge-evals for Wednesday."

## Hand it in

Commit `evals/test_evals.py`, or paste it into your team's shared doc / the
workshop Slack. **Bring it Wednesday** — it drops into the scaffold and you watch
the red turn green.

> The modern PM artifact isn't a PRD. It's an eval set.
