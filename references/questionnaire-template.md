# Questionnaire template

Written to `NN-questions.md` in the brief's folder, where `NN` is the next free number.
The user answers **in this file**, in the answer slot under each question. Never ask for
answers in a separate file — matching them back is error-prone and loses the pairing.

---

```markdown
# Questions — round <N>

For: <product name> · Date: <YYYY-MM-DD>

Write anywhere in this file — every section below has space for you, and none of it is
read-only. Answer in the **Answer:** line under each question, overwrite a default if it
is wrong, and leave it if it is fine. "Don't know" is a useful answer. So is "wrong
question" — if one is built on a false premise, say that instead of answering it; it tells
me more than an answer would.

Nothing gets built until these are settled, so a rough answer now beats a perfect one
later. There are <n> questions; most people finish in <n×1.5> minutes.

---

## Blocking — the PRD cannot be written without these

### Q<N>.1 <The question, in one line>

- **Why it matters:** <what this decides, in one line>
- **Blocks:** <journey / requirement / phase that cannot be written until this is answered>
- **Options:** <a> · <b> · <c>
- **Recommended:** <the option you would choose, and why in one clause>

**Answer:**

---

### Q<N>.2 <The question>

- **Why it matters:**
- **Blocks:**
- **Options:**
- **Recommended:**

**Answer:**

---

## Confirm — I have assumed these; correct any that are wrong

Glance down this list. Blank means you agree and I will write it into the PRD as fact.
Write the correction, a comment, or just `?` — a `?` turns it into a proper question with
options next round.

| #   | Assumption                                                                          | Correction, comment, or `?` |
| --- | ----------------------------------------------------------------------------------- | --------------------------- |
| A1  | This should feel considered, not merely correct — polish is worth real build effort |                             |
| A2  | <assumption>                                                                        |                             |
| A3  | <assumption>                                                                        |                             |

**Anything else about these assumptions:**

## Still open from earlier rounds

Carried forward, not yet answered. Skip any you would rather I decide.

### Q<N-1>.4 <question>

_If left blank, I will assume <default> and record it as an assumption in the PRD._

**Answer:**

## Out of scope for now

Noted, not asked, and deliberately deferred so this round stays short. If any of these
actually belongs in v1, say so — it is cheaper to move it now than after the PRD is
written.

- <thing> — <why it can wait>

**Move anything into v1, or add something that should be deferred:**

## Anything I did not ask about

The most useful box on the page. I only know what I have been told, so this is where the
things I could not have known belong. Prompts, if useful:

- What would surprise someone building this?
- What has gone wrong before, that this must not repeat?
- Is there anyone else — a partner, an accountant, a regulator, a big customer — whose
  requirements I should know about?
- What are you quietly worried about?

**Notes:**
```

---

## Writing notes

**Every section is writable.** A section the user can only read is a section where their
knowledge gets lost. Assumptions, deferrals, and carried-forward items all get a slot, and
the free-text boxes exist because the highest-value thing a user can tell you is the thing
you did not know to ask about.

**Blank must mean one specific thing per section, and it must be stated.** Blank on an
assumption means agreed and it goes into the PRD as fact. Blank on a carried-forward
question means the stated default gets recorded. Blank on a deferral means it stays out of
v1. If a reader cannot tell what their silence commits them to, they will answer nothing
and mean nothing by it.

**Read the free-text boxes before the answers.** They frequently invalidate a question,
move something in or out of scope, or surface a constraint that reorders the whole round.
Anything blocking that arrives this way is a legitimate new question for the next round —
it came from the user, not from something you should have asked earlier.

**Blocking questions only, in the top section.** If a question does not block a journey,
requirement, or phase, it belongs in the assumptions table as something to confirm at a
glance — or nowhere at all. A round bloated with nice-to-knows trains the user to skim.

**The assumptions table is the pressure valve.** It is how a round stays short without the
inferences going unchecked. Anything you can reasonably guess goes here, not into a
question. Costing the user a glance instead of a sentence is the whole point.

**Some assumptions are standing — put them in round 1 every time.** A few things shape a
build so broadly that nobody thinks to state them, and their silence gets read as a
preference rather than as a gap. How much polish is worth paying for is the clearest case:
left unasked, every document downstream quietly assumes build effort is a cost to minimise,
and real options get rejected on effort the user would happily have spent. It belongs in
this table rather than in a question — it costs a glance, and the correction, when it comes,
changes more of the work than most blocking answers do. Two others earn a standing row:
who besides the user has to operate this once it exists, and what they would refuse to
compromise on even if it cost time or money.

**Every question carries its default.** A user must be able to reply "defaults are fine"
and have that be a complete, usable answer to the entire round. If that reply would leave
you stuck, a default is missing.

**Name what happens if they skip.** For carried-forward questions, state the assumption you
will record instead. Skipping is then an informed choice rather than a stalled process.

**Rounds get shorter, never longer.** Round 2 asks less than round 1. If it does not, the
questions are drifting into detail that belongs in section 12 as assumptions.

**Do not attach a draft PRD.** Answering questions and critiquing a document are different
mental modes; a draft alongside the questions pulls the user into editing prose instead of
making decisions. The critique comes after the PRD is written, not during.
