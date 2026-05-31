"""Untangle — the shared practice app for the Workshop 1 eval sprint.

Untangle explains a confusing official letter in plain language and suggests
next steps. This is a deliberately incomplete first draft: useful enough to
understand, but missing important behaviours that the evals should catch.
"""


def respond(user_message: str) -> str:
    del user_message

    return (
        "Here's what this letter means, in plain language.\n\n"
        "The office is reviewing your file before they decide, and they want "
        "to confirm that you still qualify.\n\n"
        "What to do next:\n"
        "1. Gather the documents the letter asks for.\n"
        "2. Send the documents back to the office.\n"
        "3. Keep a copy of everything you send.\n\n"
        "This is general information, not legal advice."
    )
