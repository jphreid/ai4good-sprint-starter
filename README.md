# Eval Sprint — scope it, test it, make it pass

**~20 minutes · self-paced · no API key needed.** In Workshop 1 you watched a PM
turn a product requirement into a runnable test, run it, and fix what failed. We
ran out of time to do it together — so this guide walks you through running that
loop **yourself**, start to finish, on your own machine. Nothing here needs a
facilitator; every command is written out so you can copy-paste it.

> 📊 **The Workshop 1 slides:** https://jphreid.github.io/ai4good-sprint-starter/slides/
> — skim them first if you missed the talk or want the *why* behind this sprint.

Everyone works on the same small app, so you start from the same place a room
full of trainees would: **Untangle**, a plain-language explainer for confusing
official letters (a benefits review, an eviction notice, a denial).

You'll use **two review-board skills** and finish with a test you took from red
to green:

> **`/pm-critic`** (scope the spec) → **`/eval-critic`** (turn the spec into evals) →
> run them **red** → fix the app → **green**.

You are *not* inventing your own project here — that comes in Workshop 2 (June
10). Today the app is already here, and it's deliberately incomplete so there's a
real gap to close.

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

### The review board — the skills you'll use

A **review-board skill** is a reviewer you run *inside Claude Code* by typing its
name (like `/pm-critic`). Each one bottles up a single professional practice — how
a PM scopes a product, how an eval engineer specs it — so you can run that practice
on your own project, on demand. Each skill is **dual-mode**: it can **generate** an
artifact from scratch, or **audit** one you already have and tell you what's weak.

The full board is **five** skills. This sprint uses the first two:

- **`/pm-critic`** — *Is this the right thing to build?* Scopes the app and writes
  the spec — the AI Canvas + a one-pager: the prediction, the one success metric,
  and who stays in control of the real decision.
- **`/eval-critic`** — *What do "good" and "bad" look like, in code?* Turns that
  spec into runnable tests, each with a **rubric** (good / bad / auto-fail).

You'll meet the other three in **Workshop 2** — `/eng-critic` (make it work),
`/design-critic` (make it usable), `/safety-critic` (make it safe to ship). Run on
your own forked project, the five together are a review board you can keep using
long after the Lab.

---

## Setup · 2 min

**You need:** Claude Code installed and signed in (the same one from the Lab), and
[`uv`](https://docs.astral.sh/uv/) — the Python runner the commands use — on your
machine. **No Anthropic API key is required:** the whole sprint runs offline on
plain Python, so there's nothing to pay for or sign up for.

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

**Stuck? Here's one strong fill** — make it your own:

```text
/pm-critic
Scope Untangle and write the AI Canvas + a one-pager. Here's my thinking —
push back where it's weak:

• What Untangle produces from a letter: a short action brief, in plain language —
  what the letter means, the action it requires, and the deadline to act by (and,
  when serious, where to get real help).
• The ONE thing that makes its answer "good" (something you could check): when the
  letter names a deadline, the brief surfaces that exact deadline (the date or
  "within N days") — and never invents one when the letter has none.
• Who stays in control of the real decision — the person, or the app? the person.
  Untangle explains and surfaces; it never decides, gives legal advice, or
  promises an outcome.
• The worst thing a wrong answer could cause: it drops or misstates the deadline,
  so the person misses a hearing or loses benefits.
```

`/pm-critic` turns your answers into **`product/ai-canvas.md`** + **`product/one-pager.md`**
and flags anything thin. Open them and read the prediction, the one success
metric, and the augment-vs-automate call.

---

## Move 2 · Turn the spec into evals with `/eval-critic` · 8 min

You did the thinking in Move 1. Now turn that spec into runnable tests —
`/eval-critic` **reads your `product/` spec and the labelled dataset**
(`data/untangle_letters.jsonl`) and writes the evals for the metric you named.
You don't re-type the requirement; the scoping you just did is what drives it.

In Claude Code:

```text
/eval-critic
Read my product/ spec and data/untangle_letters.jsonl, then write key-free pytest
evals for the metric I scoped. Make them data-driven over the letters — cover the
case where the behaviour should fire AND the case where it shouldn't (a letter
with no deadline must not get an invented one; a routine letter shouldn't be told
to get a lawyer). One criterion per test, a # Rubric: comment on each.
```

**Read what it wrote** — does each `# Rubric:` comment match what *you* meant by
good and bad? This is your review: tighten anything that's off, then run it:

```bash
uv run pytest evals/ -v --tb=line
```

Your new evals go **red** — the app doesn't do these yet. **That red is the
point:** the spec is now a set of checks the app must pass. Because the evals run
over the whole dataset, one red means *"the deadline is dropped across the
letters,"* not just on one example.

---

## Move 3 · Turn it green · 5 min

Open `app/agent.py` and edit `respond()` so it meets the requirement — surface
the deadline the letter names (or add a real-help referral). Because the evals
run over the whole dataset, a cheap "always print a date / always add a referral"
fix won't pass — it'd fire on the letters that *shouldn't* get one. The fix has
to be **conditional** (extract the deadline when there is one; refer only when it
matters). It's plain Python; ask Claude Code to help if you'd like. Re-run until
your evals pass **without breaking the worked example that already passes**:

```bash
uv run pytest evals/ -v --tb=line
```

When it's green, you've closed the gap your spec identified.

---

## What you did today

You just ran the real loop end to end:

1. **`/pm-critic`** — scoped the spec (what good looks like, who stays in control).
2. **`/eval-critic`** — turned that spec into runnable tests over the whole dataset.
3. **red → green** — saw them fail, fixed the app, made them pass.

> The modern PM artifact isn't just a PRD. It's an eval set that makes the
> product promise checkable — and a loop that turns red into green.

In **Workshop 2 (June 10)** you run this exact loop on a much bigger app,
SymptomScout.

## If you get stuck

You're doing this solo, so here are the snags that trip people up:

- **`uv: command not found`** → install [`uv`](https://docs.astral.sh/uv/), then
  re-run the command.
- **`/eval-critic` can't find your spec** → run `/pm-critic` (Move 1) first;
  `/eval-critic` reads the `product/` files it writes.
- **Your new eval is green on the first run (never goes red)** → the check is too
  loose — a lazy answer would pass it. Ask `/eval-critic` to tighten it until a
  bad answer would fail.
- **You can't get it green** → that's fine. Knowing exactly what's still red *is*
  the spec working. Note what's red and bring it to Workshop 2.
- **Anything else** → tell Claude Code what you ran and what you saw. It's in the
  repo with you and can read every file here.

## What's in here

- `app/agent.py` — Untangle, a deliberately incomplete first draft (plain Python)
- `evals/test_evals.py` — one worked eval + a marked space for the one you write
- `data/untangle_letters.jsonl` — 10 synthetic letters (meaning · action · deadline · risk · whether real-help applies)
- `.claude/skills/` — the `/pm-critic` and `/eval-critic` review-board skills
