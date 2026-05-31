"""Untangle — the shared practice app for the Workshop 1 eval sprint.

Untangle reads a confusing official letter and explains it in plain language,
with next steps. It is a deliberately incomplete FIRST DRAFT: good enough to
understand, but missing behaviours your evals should catch — and that you will
fix to turn a red eval green.

There is NO API key and NO model call here on purpose: respond() is plain
Python, so every eval runs with `uv run pytest`, and you can read and edit the
logic yourself to make a failing eval pass. That edit is the whole point of the
sprint.
"""


def respond(user_message: str) -> str:
    """Explain an official letter in plain language and suggest next steps."""
    letter = user_message.strip()

    return "\n".join(
        [
            "Here's what this letter means, in plain language.",
            "",
            _explain(letter),
            "",
            "What to do next:",
            "1. Read the letter and note exactly what it is asking you for.",
            "2. Gather any documents it mentions.",
            "3. Send your response to the office and keep a copy of everything.",
            "",
            "This is general information, not legal advice.",
        ]
    )


def _explain(letter: str) -> str:
    """A rough plain-language read of the letter, based on a few keywords.

    Deliberately shallow. Notice what it does NOT do: it never surfaces the
    deadline named in the letter, and it never points the reader to real help.
    Those are the gaps your evals should catch — and the lines you would add to
    turn a red eval green.
    """
    text = letter.lower()
    if "hearing" in text:
        return ("You have a hearing scheduled. You can attend and bring evidence "
                "and someone to support you.")
    if "denied" in text or "denial" in text or "refused" in text:
        return ("A decision did not go your way. You may be able to respond to it "
                "or appeal.")
    if "review" in text or "verify" in text or "verification" in text:
        return ("An office is reviewing your file before they decide, and they "
                "want you to confirm that you still qualify.")
    return "An office needs you to act on your file before they make a decision."
