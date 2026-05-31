"""Untangle — practice evals for the Workshop 1 eval sprint.

Every eval is three things:
  1. a user request — the letter someone pastes in,
  2. a `# Rubric:` comment — what GOOD looks like, what BAD looks like, what
     AUTO-FAILS (the line that can never be crossed),
  3. a deterministic check that applies the rubric — plain Python, no model call.

The one eval below already PASSES. It's a worked example — the shape to copy,
nothing more.

Your job in the sprint:
  • write the eval that actually matters and is still MISSING, then
  • watch it go RED, then
  • edit app/agent.py until it turns GREEN.

Untangle has two real gaps to aim at (pick one):
  • it never surfaces the DEADLINE named in the letter, and
  • it never points the reader to REAL HELP (legal aid / a lawyer / a clinic).

Use a sample letter from data/untangle_letters.jsonl as the input.
"""
from app.agent import respond


# ── Worked example (this one passes) — copy this shape for your own eval ──
# Rubric: good = explains what the letter means in plain words;
#         bad = just repeats the jargon; auto-fail = says nothing about meaning.
def test_explains_in_plain_language():
    out = respond("My letter says 'subject to review pending verification.' What does this mean?").lower()
    # "reviewing" comes from the explanation, not the fixed intro line — so this
    # fails if the app stops actually explaining the letter.
    assert "reviewing" in out, "did not explain the letter"


# ──────────────────────────────────────────────────────────────────────────
# Your eval goes below. Write it with /eval-critic, run pytest, watch it go
# RED, then edit app/agent.py until it turns GREEN. Keep the `# Rubric:`
# comment so the standard lives in the file, not just in chat.
# ──────────────────────────────────────────────────────────────────────────
