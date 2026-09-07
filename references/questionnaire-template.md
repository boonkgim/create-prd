# Questionnaire template

Written to `NN-questions.md` in the brief's folder, where `NN` is the next free number.
The user answers **in this file**, in the answer slot under each question. Never ask for
answers in a separate file — matching them back is error-prone and loses the pairing.

---

```markdown
# Questions — round <N>

For: <product name> · Date: <YYYY-MM-DD>
Answer in the **Answer:** line under each question. Overwrite the default if it is wrong;
leave it as-is if it is fine. Write "don't know" freely — that is a useful answer.

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

Glance down this list and mark anything wrong. Silence means agreed.

| # | Assumption | Correct? |
|---|---|---|
| A1 | <assumption> | leave blank if fine, or write the correction |
| A2 | <assumption> | |

## Still open from earlier rounds

Carried forward, not yet answered. Skip if you would rather I decide.

- **Q<N-1>.4** <question> — *if unanswered, I will assume <default> and record it.*

## Out of scope for now

Noted, not asked, and deliberately deferred so this round stays short:

- <thing> — <why it can wait>
```

---

## Writing notes

**Blocking questions only, in the top section.** If a question does not block a journey,
requirement, or phase, it belongs in the assumptions table as something to confirm at a
glance — or nowhere at all. A round bloated with nice-to-knows trains the user to skim.

**The assumptions table is the pressure valve.** It is how a round stays short without the
inferences going unchecked. Anything you can reasonably guess goes here, not into a
question. Costing the user a glance instead of a sentence is the whole point.

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
