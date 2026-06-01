# Eval Sprint — scope it, test it, make it pass

**20 minutes.** You just watched a PM turn a requirement into a runnable test,
run it, and fix what failed. Now **you** run that loop yourself — on a shared
app so everyone starts from the same place: **Untangle**, a plain-language
explainer for confusing official letters (a benefits review, an eviction notice,
a denial).

You'll use **two review-board skills** and finish with a test you took from red
to green:

> **`/pm-critic`** (scope the spec) → **`/eval-critic`** (write one eval) →
> run it **red** → fix the app → **green**.

You are *not* inventing your own project today — that's Wednesday. Today the app
is already here, and it's deliberately incomplete so there's a real gap to close.

### The words you'll hear (plain version)

- **Eval** — a tiny automated test that checks the app's *answer*. Not ML model
  evaluation — just "did the output contain what it should?"
- **Rubric** — the standard the eval checks against, written as **good / bad /
  auto-fail**: what a right answer looks like, what a wrong one looks like, and
  the one line it must never cross.
- **Red → green** — "red" means the test is failing, "green" means it passes.
  You'll write a test that starts red, then change the app until it turns green.
- **`/pm-critic`, `/eval-critic`** — helpers you run *inside Claude Code* by
  typing their name. One helps you scope the app; one helps you write the eval.

You'll work in two places: a **terminal** (the text command window) and **Claude
Code**. You don't need to know Git or pytest — every command is written out below,
so you can copy-paste it.

---

## Setup · 2 min

Open a terminal and paste these two lines. The first downloads the app; the
second runs its tests so you can see them pass before you change anything:

```bash
git clone https://github.com/jphreid/ai4good-sprint-starter.git && cd ai4good-sprint-starter
uv run pytest evals/ -v --tb=line
```

You should see **1 passed**. That one is a *worked example* — a user request, a
`# Rubric:` comment (good / bad / auto-fail), and a check. It shows you the
shape; you'll write your own.

Now open Claude Code in this folder:

```bash
claude
```

**Read the app.** Open `app/agent.py`. It explains a letter and lists next
steps — but it has **two gaps** it never handles:

- ❌ it never **surfaces the deadline** the letter names, and
- ❌ it never **points the reader to real help** (legal aid / a lawyer / a clinic).

Those gaps are your target.

---

## Move 1 · Scope the spec with `/pm-critic` · 5 min

Before writing any test, *you* decide what Untangle should do and who stays in
control. `/pm-critic` writes the spec — but only as well as you brief it. **Don't
paste a finished description: fill the blanks in your own words first.** That
thinking *is* the PM work; the skill just turns it into the artifact.

In Claude Code, type `/pm-critic`, then complete this and send it:

```text
/pm-critic
Scope Untangle and write the AI Canvas + a one-pager. Here's my thinking —
push back where it's weak:

• What Untangle produces from a letter: _______________________________________
• The ONE thing that makes its answer "good" (something you could check): ______
• Who stays in control of the real decision — the person, or the app? _________
• The worst thing a wrong answer could cause: _________________________________
```

**How to fill each blank** — one line each, think don't copy:
- **What it produces** — not "an AI assistant." Name the actual output it hands the user.
- **The one "good" test** — resist listing three. Pick the *single* thing that, if true, means it worked — and that you could check on a fixed set of letters.
- **Who's in control** — does Untangle *decide for* the person, or *help them* decide and act? (It's high-stakes — that should point you one way.)
- **Worst wrong answer** — picture someone acting on a bad output. What's the damage?

`/pm-critic` turns your answers into **`product/ai-canvas.md`** + **`product/one-pager.md`**
and flags anything thin. Open them and read the prediction, the one success
metric, and the augment-vs-automate call.

---

## Move 2 · Write one eval with `/eval-critic` · 8 min

Now turn ONE missing behaviour into a test. The hard part isn't the code — it's
the **rubric**: saying what good and bad look like. You write that; `/eval-critic`
encodes it. **Fill the blanks** before you send — don't paste a ready-made prompt.

First, choose your target and a real case:
- **Pick one gap:** the missing **deadline**, or the missing **real-help referral**.
- Open `data/untangle_letters.jsonl` and pick a letter where it bites — the
  `benefits-review-deadline` row names a 30-day / March 3 deadline.

Then type `/eval-critic` and complete this:

```text
/eval-critic
Write me ONE key-free pytest eval — a # Rubric: comment plus a plain-substring
check. Here's my requirement and rubric:

• Requirement — what Untangle should do that it doesn't yet: __________________
• A GOOD answer must include: _________________________________________________
• A BAD answer / auto-fail (the line it can't cross): _________________________
• The letter I'm testing with (paste it, or give its id from data/): _________
```

**How to fill each blank:**
- **Requirement** — one sentence, the gap you picked (e.g. "name the deadline the letter states").
- **Good** — what must literally appear for it to pass? A date? the word "deadline"? a referral phrase? Be concrete — that's what the check looks for.
- **Bad / auto-fail** — what would a lazy-but-plausible answer look like that should still *fail*? Name it so your check catches it.
- **The letter** — a real case keeps the check honest.

Run it:

```bash
uv run pytest evals/ -v --tb=line
```

Your new eval goes **red** — the app doesn't do this yet. **That red is the
point:** the requirement is now a check the app must pass.

---

## Move 3 · Turn it green · 5 min

Open `app/agent.py` and edit `respond()` so it meets the requirement — surface
the deadline the letter names (or add a real-help referral). It's plain Python;
ask Claude Code to help if you'd like. Re-run until your eval passes **without
breaking the worked example that already passes**:

```bash
uv run pytest evals/ -v --tb=line
```

When it's green, you've closed the gap your spec identified.

---

## What you did today

In 20 minutes you ran the real loop end to end:

1. **`/pm-critic`** — scoped the spec (what good looks like, who stays in control).
2. **`/eval-critic`** — turned one requirement into a runnable test.
3. **red → green** — saw it fail, fixed the app, made it pass.

> The modern PM artifact isn't just a PRD. It's an eval set that makes the
> product promise checkable — and a loop that turns red into green.

On Wednesday you run this exact loop on a much bigger app, SymptomScout.

## What's in here

- `app/agent.py` — Untangle, a deliberately incomplete first draft (plain Python)
- `evals/test_evals.py` — one worked eval + a marked space for the one you write
- `data/untangle_letters.jsonl` — 10 synthetic letters (meaning · action · deadline · risk · whether real-help applies)
- `.claude/skills/` — the `/pm-critic` and `/eval-critic` review-board skills
