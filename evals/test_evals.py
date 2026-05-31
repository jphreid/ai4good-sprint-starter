"""Untangle — shared practice evals for Workshop 1.

Untangle explains a confusing official letter in plain language and tells the
reader what to do next. It does not give legal advice or promise an outcome.
"""
from app.agent import respond


# Rubric: good = explains what the letter means in plain words; auto-fail = just restates jargon.
def test_explains_in_plain_language():
    out = respond("My letter says 'subject to review pending verification.' What does this mean?").lower()
    assert "means" in out or "reviewing" in out, "did not explain the letter"


# Rubric: good = a clear 'What to do next' section; auto-fail = advice buried in prose.
def test_has_a_next_steps_section():
    out = respond("Help me understand this eviction notice.").lower()
    assert "what to do next" in out or "next steps" in out, "no next-steps section"


# Rubric: good = short and plain; auto-fail = a wall of text.
def test_is_concise():
    out = respond("Explain this letter.")
    assert len(out) < 1200, "too long to be plain"


# Rubric: good = points the reader to real help; auto-fail = no pointer to where to get help.
def test_points_to_real_help():
    out = respond("Will I win my appeal?").lower()
    assert "legal aid" in out or "lawyer" in out or "legal clinic" in out, "no pointer to real help"


# Rubric: good = surfaces the actual deadline to act by; auto-fail = never names it.
def test_surfaces_the_deadline():
    out = respond("I must respond within 30 days, by March 3, or my case closes.").lower()
    assert "deadline" in out or "30 day" in out or "march 3" in out, "deadline not surfaced"
