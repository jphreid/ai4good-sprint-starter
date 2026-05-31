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

## The sprint (do what you watched)

**1 — Brainstorm 5 criteria + rubrics.** Paste this into Claude Code, filling in your project:

```
I'm working on an AI4Good project: <one sentence>.
Our users are: <who they are>.
It must NOT <the thing it should refuse — e.g. diagnose, give legal advice>.

Help me write 5 acceptance criteria — one each: happy path, edge case,
values/safety (something it must REFUSE), behavioral (how it responds),
UX (the output format). One sentence each, testable (a reader can say yes/no).
For each, give a one-line rubric: good answer / bad answer / auto-fail.
```

**2 — Turn them into runnable evals.** Then:

```
Now turn these into executable pytest evals in evals/test_evals.py, importing
respond from app.agent. One test per criterion, with a # Rubric: comment above
each. I have no API key — use deterministic checks only (substring, regex,
length, timing). If a criterion truly needs an LLM judge, write the test but
mark it @pytest.mark.skip for Wednesday.
```

**3 — Run them:**

```bash
uv run pytest evals/ -v --tb=line
```

(Or just ask Claude Code to run them.) Expect **red** (and maybe a couple
skipped) — your app is still a stub. Every red is a requirement.

## Hand it in

Commit `evals/test_evals.py`, or paste it into your team's shared doc / the
workshop Slack. **Bring it Wednesday** — it drops into the scaffold and you watch
the red turn green.

> The modern PM artifact isn't a PRD. It's an eval set.
