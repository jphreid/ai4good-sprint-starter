# Eval Sprint — shared Untangle practice app

**20 minutes. No API key needed.** You just watched a PM turn requirements into
runnable tests, run them, and catch a failure. Now you do the same loop on a
shared practice app: **Untangle**, a plain-language explainer for confusing
official letters.

You're not inventing your own AI4Good project today. The app is already here and
it is not empty: `app/agent.py` contains a deliberately incomplete first draft.
The evals in `evals/test_evals.py` show what it already does and what it misses.
The synthetic sample letters in `data/untangle_letters.jsonl` give you concrete
cases to inspect or turn into extra evals. Wednesday is when you apply the same
loop to your own project.

## Setup (1 min)

```bash
git clone https://github.com/jphreid/ai4good-sprint-starter.git && cd ai4good-sprint-starter
uv run pytest evals/ -v --tb=line
```

Expected result: **3 passed, 2 failed**. The app explains the letter, gives next
steps, and stays concise. It fails to point to real help and to surface a
deadline. Those reds are the product gaps.

Open Claude Code in this folder:

```bash
claude
```

## The sprint — inspect and improve the spec

This repo ships two review-board skills in `.claude/skills/`. For this practice
sprint, the useful one is `/eval-critic`.

**1 — Read the app.** Open `app/agent.py`. Notice it is a first draft, not a
placeholder.

**2 — Read the evals.** Open `evals/test_evals.py`. Each eval has a user request,
a `# Rubric:` comment, and a deterministic check.

**3 — Pick one sample letter.** Open `data/untangle_letters.jsonl`. Choose one
case where the expected deadline, action, or risk matters.

**4 — Audit the evals with Claude Code.**

```text
/eval-critic
Audit evals/test_evals.py for Untangle. Keep it key-free. Tell me which evals
are strong, which are weak, and add or tighten one eval using one sample from
data/untangle_letters.jsonl if a bad answer could still pass.
```

**5 — Run them again.**

```bash
uv run pytest evals/ -v --tb=line
```

The goal is not to make everything green today. The goal is to understand the
loop: rubric -> eval -> red/green signal -> product decision.

## Hand it in

Paste one line in the workshop chat:

```text
Untangle: green = ___ / red = ___ / eval I would add or tighten = ___
```

> The modern PM artifact is not just a PRD. It is an eval set that makes the
> product promise checkable.
