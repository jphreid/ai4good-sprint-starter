# Eval Sprint — starter repo (read this first)

This repo exists for **one 20-minute job**: a team turns its AI4Good project
idea into **runnable acceptance evals** — the same move they just watched in the
Workshop-1 live demo, now on *their own* project.

## The hard constraint: NO API KEY

Trainees have **Claude Code, but no Anthropic API key.** So every eval you write
**must run with `uv run pytest` using only the standard library** — no network,
no Anthropic SDK, no `client.messages.create`, no `JUDGE_MODEL`.

- **Write deterministic checks only:** substring (`"911" in out`), regex
  (a URL / citation pattern), length, `time.time()` timing, simple language
  heuristics. These are exact and never flaky — they ARE the contract.
- **For a criterion that genuinely needs an LLM judge** (e.g. "is this
  empathetic?"), still write the test, but mark it
  `@pytest.mark.skip(reason="LLM-judge eval — wire up Wednesday with the scaffold + API key")`
  and leave a `# Rubric:` comment. It's captured for Wednesday, and it won't
  error today for lack of a key.
- **Never** import `anthropic` or add an `ANTHROPIC_API_KEY` dependency.

## What `respond()` is right now

`app/agent.py` ships a **stub** `respond()` that returns a placeholder. That's on
purpose: today the team writes the *spec*, not the app. So the deterministic
evals will go **RED** against the stub — **red is the deliverable.** Do not
"fix" the stub to make tests pass; the reds are the requirements the team builds
to green on Wednesday.

## The flow (mirror the live demo)

1. Help the team write **5 acceptance criteria** for their project — one each:
   happy path · edge case · values/safety (must REFUSE) · behavioral · UX. One
   sentence each, testable (a reader can say yes/no).
2. For each, write a **one-line rubric**: good answer / bad answer / auto-fail.
   Push back on vague ones — "helpful"/"safe" aren't rubrics until they say what
   that means here.
3. Turn the five into **executable pytest** in `evals/test_evals.py`, importing
   `from app.agent import respond`. One `def test_…()` per criterion, a
   `# Rubric:` comment above each (good / bad / auto-fail), a short assert
   message so a red test explains itself. Deterministic where possible; skip +
   comment where it truly needs a judge.
4. Run them: `uv run pytest evals/ -v --tb=line`. Expect **red** (and some
   skipped). That's the spec, working.

## Conventions

- Run: `uv run pytest evals/ -v --tb=line`  (you can run this for the team)
- Import the app as `from app.agent import respond` — same import the Wednesday
  scaffold uses, so the team's `evals/test_evals.py` drops straight in.
- Keep the `# Rubric:` comments — they're the good/bad/auto-fail standard, in the
  file, surviving to Wednesday instead of living only in chat.
