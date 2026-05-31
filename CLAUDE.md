# Eval Sprint — shared Untangle practice app (read this first)

This repo exists for **one 20-minute job**: trainees practice the
requirement -> rubric -> eval loop on a fixed, easy-to-understand app before
they apply the same loop to their own AI4Good projects on Wednesday.

The fixed app is **Untangle**: paste in a confusing official letter and it
explains what it means in plain language, with next steps. It must not give
legal advice or promise an outcome.

The repo also includes `data/untangle_letters.jsonl`: 10 synthetic letters with
expected meaning, action, deadline, risk, and whether referral to real help is
appropriate. They are fake cases for eval practice, not legal documents.

## The hard constraint: NO API KEY

Trainees have **Claude Code, but no Anthropic API key.** Every eval must run
with `uv run pytest` using only the standard library — no network, no Anthropic
SDK, no `client.messages.create`, no `JUDGE_MODEL`.

- **Prefer plain substring checks** — `"legal aid" in out`, `"next step" in
  out.lower()`. Exact, readable, and never flaky. Reach for a regex only when a
  plain `in` genuinely cannot express the check. Length and `time.time()` timing
  are fine too.
- **For a criterion that genuinely needs an LLM judge** (for example, "is this
  empathetic?"), still write the test, but mark it
  `@pytest.mark.skip(reason="needs an LLM judge — wire up Wednesday")`
  and leave a `# Rubric:` comment.
- **Never** import `anthropic` or add an `ANTHROPIC_API_KEY` dependency.

## What `respond()` is right now

`app/agent.py` is **not empty anymore**. It ships a deliberately incomplete
first draft of Untangle:

- It explains the letter in plain language.
- It gives a "What to do next" section.
- It stays concise.
- It does **not** point to real help.
- It does **not** surface an explicit deadline.

So the starter evals should produce a meaningful mixed result: **3 green,
2 red**. Do not "fix" the app during Workshop 1. The point is to inspect and
improve the spec, not to build the product.

## The review-board skills in this repo

`.claude/skills/` ships:

- **`eval-critic`** — the main sprint skill. Use it to audit
  `evals/test_evals.py`, tighten weak checks, or add one missing eval. It must
  stay key-free and deterministic.
- **`pm-critic`** — still available as the scope skill, but participants do not
  need to run it during the fixed Untangle sprint.

## The flow (mirror the live demo, with less cognitive load)

1. Read `app/agent.py` so the trainee sees a real first draft, not a blank app.
2. Read `evals/test_evals.py` and identify the user request, rubric, and check in
   each test.
3. Open `data/untangle_letters.jsonl` and pick one sample where the expected
   action, deadline, or risk matters.
4. Run `uv run pytest evals/ -v --tb=line`. Expect **3 passed, 2 failed**.
5. Help the trainee explain the two reds as product gaps:
   - no referral to real help (`legal aid`, `lawyer`, or `legal clinic`)
   - no explicit deadline surfaced
6. Use `/eval-critic` in audit mode to tighten one eval or add one missing eval
   using a sample from the synthetic dataset.

## Conventions

- Run: `uv run pytest evals/ -v --tb=line`
- Import the app as `from app.agent import respond` — same import the Wednesday
  scaffold uses.
- Keep the `# Rubric:` comments — they are the good/bad/auto-fail standard, in
  the file, surviving beyond chat.
