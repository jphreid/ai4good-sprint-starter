# Eval Sprint — the shared Untangle practice app (read this first)

This repo exists for **one 20-minute job**: a trainee runs the full
**requirement → rubric → eval → red → green** loop themselves, on a fixed,
easy-to-understand app, before they apply the same loop to their own AI4Good
project on Wednesday.

The fixed app is **Untangle**: paste in a confusing official letter and it
explains what it means in plain language, with next steps. It must not give
legal advice or promise an outcome.

The repo also includes `data/untangle_letters.jsonl`: 10 synthetic letters with
expected meaning, action, deadline, risk, and whether referral to real help is
appropriate. They are fake cases for eval practice, not legal documents.

## The hard constraint: NO API KEY

Trainees have **Claude Code, but no Anthropic API key.** `respond()` is plain
Python with no model call, and every eval must run with `uv run pytest` using
only the standard library — no network, no Anthropic SDK, no
`client.messages.create`, no `JUDGE_MODEL`.

- **Prefer plain substring checks** — `"legal aid" in out`, `"deadline" in
  out.lower()`. Exact, readable, and never flaky. Reach for a regex only when a
  plain `in` genuinely cannot express the check. Length and `time.time()` timing
  are fine too.
- **For a criterion that genuinely needs an LLM judge** (for example, "is this
  empathetic?"), still write the test, but mark it
  `@pytest.mark.skip(reason="needs an LLM judge — wire up Wednesday")`
  and leave a `# Rubric:` comment.
- **Never** import `anthropic` or add an `ANTHROPIC_API_KEY` dependency.

## What `respond()` is right now

`app/agent.py` ships a deliberately incomplete first draft of Untangle. It is
**input-aware** (it reads the letter) and **editable** (plain Python you can
change to make a failing eval pass):

- It explains the letter in plain language.
- It gives a "What to do next" section.
- It stays concise.
- It does **not** surface the deadline named in the letter.
- It does **not** point the reader to real help (legal aid / lawyer / clinic).

The starter ships **one worked example, green** — it models the pattern (request → rubric → check).
The missing behaviours (deadline, real-help) are the gaps the trainee specifies
as their *own* eval, watches go red, and then **fixes the app to turn green**.
Editing `respond()` to close a gap is the point of this sprint — not off-limits.

## The flow — three moves, both skills, ending in green

The sprint uses **both** review-board skills and closes with a passing test.
`README.md` is the trainee-facing version of this; guide them through it:

1. **Read the app.** `app/agent.py` is a real first draft with two gaps it never
   handles (no deadline surfaced, no real-help referral).
2. **Move 1 — scope with `/pm-critic`.** Run it on Untangle to write
   `product/ai-canvas.md` + `product/one-pager.md`: the prediction, the one
   success metric, and the augment-vs-automate call. This is the spec.
3. **Move 2 — eval with `/eval-critic`.** Pick one gap, take a concrete case
   from `data/untangle_letters.jsonl`, and turn the requirement into a key-free
   eval with a `# Rubric:` comment. Run `uv run pytest evals/ -v --tb=line` — it's **red**.
4. **Move 3 — turn it green.** Edit `respond()` in `app/agent.py` to meet the
   requirement; re-run until the new eval passes without breaking the three that
   already pass. Changing the **app** to meet the test is the point — never
   loosen the eval to pass.

The Move 1 and Move 2 prompts in the README are **fill-in-the-blank templates** —
the trainee writes the prediction / the one metric / the requirement / the rubric
in their own words, on purpose (that thinking is the lesson). So when they send a
partially-filled brief: **engage with their answers** — `/pm-critic` should push
back on a thin prediction or three-metric answer; `/eval-critic` should sharpen a
vague good/bad before encoding it. Don't hand them a finished prompt or quietly
rewrite their thinking; coach it.

## The review-board skills in this repo

`.claude/skills/` ships both skills the sprint uses:

- **`pm-critic`** — Move 1. Scopes Untangle into `product/ai-canvas.md` +
  `product/one-pager.md` (the spec). Keep its markdown short and scannable.
- **`eval-critic`** — Move 2. Writes the trainee's own key-free eval from a
  requirement (or audits/tightens an existing one), then hands off to the green.

Any markdown a skill writes (e.g. `pm-critic`'s `product/*.md`) must be short
and scannable — a reviewer should be able to read and check it in under a minute.

## Conventions

- Run: `uv run pytest evals/ -v --tb=line`
- Import the app as `from app.agent import respond` — the same import shape the
  Wednesday scaffold uses.
- Keep the `# Rubric:` comments — they are the good/bad/auto-fail standard, in
  the file, surviving beyond chat.
