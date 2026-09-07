---
name: create-prd
description: Turn a short project brief - or, if there is none, a one-line answer to "what would you like to create?" - into a lean but build-ready PRD that a coding agent can implement from, asking the user numbered questionnaire rounds until it is decision-complete. Works both for standing up a new product and for adding a feature to a project that already exists. The PRD is written as a single self-contained Markdown file, supersedes the brief and questionnaires, and stays a business document - no tech stack, no schemas, no framework choices. Use when the user asks to write a PRD, expand a brief into requirements, start a PRD with no brief at all, spec out a new feature for an existing project, answer a questionnaire round, or produce a spec before vibe coding.
license: MIT
---

# Create PRD

Expand a short problem/solution brief — or, with no brief at all, a discovery
questionnaire built from a single question — into a Product Requirements Document that is
**lean enough to write in an hour, precise enough for an agent to build from, and free of
technology decisions**.

## Core principle

A coding agent cannot read omission. Anything left implicit gets filled with the simplest
thing the model can invent — usually the wrong thing. So the PRD states, positively:
what is in scope, what is _not_, what the business rules are, and what "done" looks like
in observable terms.

The PRD answers **what and why**. It never answers **how**. Stack, schema, hosting, and
libraries are a separate decision made after the PRD is approved.

The PRD also **supersedes the brief and every questionnaire**, including a round 1 that
stood in for a missing brief. It is the single document handed to whoever builds this. A
reader who has never seen any of it and was not present for any conversation about it must
be able to build from the PRD alone.

A brief — when there is one — almost never contains enough to do that, and a one-line
answer to "what would you like to create?" contains even less. Do not paper over the gap
with plausible guesses — **ask, in writing, until the decisions exist**. The questioning is
not overhead before the real work; it is most of the work.

## Folder convention

Everything lives in one dated folder, numbered in creation order. The first file depends on
whether a brief exists.

**With a brief:**

```
docs/<dated-folder>/
  01-brief.md
  02-questions.md      <- round 1, the user types answers into it
  03-questions.md      <- round 2, only if needed
  04-prd.md            <- next free number once the gate passes
```

**Without a brief** — nothing has been written down yet, just an idea:

```
docs/<dated-folder>/
  01-questions.md      <- round 1, stands in for the brief
  02-questions.md      <- round 2, only if needed
  03-prd.md            <- next free number once the gate passes
```

The PRD's number depends on how many rounds ran. Always use the next free number; never
overwrite or renumber an existing file.

`<dated-folder>` is `yyyy-mm-dd-<slug>`, e.g. `2026-09-08-loyalty-points`. Take the slug
from the brief's subject, or, when there is no brief, from the user's one-line answer to
"what would you like to create?".

If the project has its own convention for where dated docs live and what a tool checks
against them, use that convention instead — the requirement is only that the folder is
new, and that nothing else in the project reads it as drift.

**The PRD and the questionnaires — round 1 included, whether or not it followed a brief —
are all markdown, but not the same kind of file.** A questionnaire is a working file the
user edits by hand — numbered questions with blanks. The PRD is the finished document that
replaces the brief and every questionnaire round. Never let PRD content leak into a
questionnaire, or vice versa.

## Steps

1. **Work out what this is for.** Two situations are both in scope, and the rest of this
   skill applies to either:
   - **A feature for a project that already exists on disk.** Before asking anything, look
     for context the project already carries — a root `README`, `CLAUDE.md`/`AGENTS.md`,
     and any earlier PRDs under `docs/`. Absorb what they already establish (product name,
     users, constraints, house conventions) instead of re-asking for it. The questionnaire
     and PRD only need to cover what is new about this feature; say where an established
     fact came from instead of asking the user to restate it.
   - **A new product with nothing built yet.** There is no existing context to read, so
     every gate question in this skill is live.

2. **If a brief exists, read the folder, not just the brief.** Read the brief and every
   file in its folder in number order, including earlier questionnaires and everything the
   user wrote into them — answers, corrections to assumptions, and free-text comments
   alike. Read the comments first: they often invalidate a question or move something in or
   out of scope. Rounds may span sessions — the files are the memory, not the conversation.

3. **If no brief exists, do not ask for one.** A brief is a convenience, not a requirement.
   Ask the user a single quick question — "What would you like to create?" — one sentence
   is enough. Then create `docs/<dated-folder>/01-questions.md` from
   `references/questionnaire-template.md` and go straight to the readiness gate below to
   work out what round 1 needs to ask. This first round does the job the brief would have
   done: problem, users, and scope get written down for the first time in the user's own
   answers, not in prose you invented on their behalf. Expect it to run longer than a normal
   round, since nothing is decided yet — the ~10-question guideline in _Rounds_ still
   applies; anything past it overflows to round 2.

4. **Test against the readiness gate** below. Record which gates pass, which fail, and for
   each failure the specific decision that is missing. In feature mode, a gate already
   settled by the existing project (commonly G8, the product name, or G6, the identity
   model) passes immediately — note where you found the answer rather than asking again.

5. **If any gate fails, write a questionnaire** to the next free number (`NN-questions.md`)
   using `references/questionnaire-template.md`, and following _Question design_ and
   _Rounds_ below. Then stop and tell the user which file to fill in. Do not write a partial
   PRD, and do not write a draft PRD alongside the questions — a draft invites approval of
   guesses instead of decisions.

6. **When the user returns with answers**, start again at step 2 (or step 1 if the project
   context may have changed). The folder now contains their answers; re-test the gate; issue
   a narrower round if it still fails.

7. **When every gate passes, write the PRD** to the next free number (`NN-prd.md`) by
   copying `references/prd-template.md` and replacing its content, following the rules in
   _Markdown output_ below. The template's head comment carries the section-by-section
   writing notes and is addressed to you, not to the reader: **delete that comment from the
   copy.** Fold the brief (if any) and every answer from every round into the document
   itself — see _Self-containment_. Leave the brief and the questionnaires untouched; they
   stay as history.

8. **Check the rendered file.** Open it in a markdown viewer and confirm the contents links
   jump to the right section, the checkboxes render as checkboxes, and no bracketed
   placeholder survived. There is no build step: the copy is finished the moment it is
   written.

9. **Report** the file path, its length, and any open questions that remain. Say the
   file opens in any text editor or markdown viewer — no server, no build step. State that
   the PRD supersedes the brief and questionnaires, and that it is now the user's turn to
   critique it. Do not start implementing. Once the user has approved it, building it is a
   separate step — this skill does not commit and does not write code.

## Readiness gate

The gate is about **decisions, not detail**. A thing can be unknown and the gate still
passes, provided the unknown is recorded and nothing in the build depends on guessing it.
What fails the gate is a decision a builder would otherwise have to invent.

Write the PRD only when all of these hold:

- **G1 — Money is decided.** Every point where money changes hands has a stated rule: who
  pays, how much, when, and what happens when it fails or must be reversed. If no money
  moves in v1, that is itself stated. "How much" includes the **currency, named by the
  user** (and how tax appears in displayed prices) — a builder must never default to one.
- **G2 — Time and capacity are decided.** Anything scheduled, limited, or expiring has a
  rule: timezone, operating hours, lead time, duration, how many at once, and what happens
  when two people want the same thing.
- **G3 — The v1 boundary is drawn and the user has seen it.** There is an explicit
  not-in-scope list, and it was shown to the user rather than assumed by you.
- **G4 — Every journey has an ending, including the bad ones.** Each primary flow has a
  defined outcome for its main failure — not just the happy path.
- **G5 — Success is measurable.** At least one numeric, time-bound metric with a baseline,
  so someone can later tell whether this worked.
- **G6 — Identity and visibility are decided.** Whether accounts are required, what a
  person can see of their own history, and what the operator can see or change.
- **G7 — Nothing rests on an unconfirmed guess.** Every inference you made is either
  confirmed by the user or written down as an assumption the user has read.
- **G8 — The product is named.** The business/site has a name the user typed — a working
  name is fine if flagged as such, but a builder must never invent one: an invented brand
  leaks into page titles, mock data, and copy, and reads as fact.

A gap is **blocking** if a builder would have to invent a business rule to proceed, or if
getting it wrong means rework rather than adjustment. Blocking gaps must be asked.
Non-blocking gaps become assumptions in section 12 — do not spend a round on them.

**In feature mode**, apply every gate to the feature, not to the whole product. G3's
boundary is this feature's scope, not a new product's. G8 passes immediately from the
product name the existing project already carries. A gate the existing project has already
settled for the whole product (say, G6's identity model) passes immediately too — cite
where you found it instead of asking.

## Rounds

There is no fixed number of rounds. Keep going until the gate passes — but every round
must **converge**, not merely continue:

- **Each round is strictly narrower than the last.** Fewer questions, and only about what
  remains undecided.
- **Never re-ask an answered question.** Follow up only where an answer was ambiguous,
  incomplete, or contradicted another answer — and when you do, quote what they said and
  ask the narrow thing that is still open.
- **New questions only from what the user gave you.** A later round may introduce a
  question only if an answer, a corrected assumption, or a free-text comment opened a
  genuinely blocking gap. It may not introduce something you should have asked in round 1.
- **An assumption marked `?` becomes a question.** If the user queries an assumption rather
  than correcting it, promote it to a proper question with options and a default.
- **Carry unanswered questions forward**, marked as still open, so nothing is silently
  dropped.
- **Blocking first.** If only non-blocking gaps remain, stop asking: write the PRD and
  record them as assumptions.
- **If a round returns no new information** — skipped, or the same answers restated — do
  not reissue it. Convert what is left into assumptions, write the PRD, and say plainly
  which decisions were made on the user's behalf.
- **The user can end it at any time.** If they say to write it now, write it, with every
  remaining gap marked as an assumption in section 12.

Keep a single round to what someone can answer in one sitting — roughly ten questions.
Overflow goes to the next round, highest-consequence first.

## Question design

**Interrogate the decisions, not the description.** A question that merely fills a blank in
your template is a bad question. A good question forces the user to decide something they
have not yet decided — and they will often discover, while answering, that they had not
thought about it at all. That discovery is the point.

Every question must satisfy all of these:

- **One decision per question.** If it contains "and", split it.
- **Closed where possible.** Offer the realistic options rather than an open field. People
  choose faster and more accurately than they compose.
- **States what it blocks.** Name the journey, requirement, or phase that cannot be
  written until this is answered. A question that blocks nothing does not belong in a
  round.
- **Carries a recommended default.** Give the answer you would choose and why, so the user
  can reply "defaults are fine" and be done. This does more to shorten the process than
  anything else you can do.
- **Answerable in one line.** If it needs a paragraph, it is really several questions.
- **Written in the user's business language.** Ask about deposits, no-shows, and slots —
  never about records, states, or endpoints.

Never ask:

- what the brief already answers, or what you can reasonably infer — put the inference in
  the questionnaire as an assumption to confirm instead, which costs the user a glance
  rather than an essay;
- what was answered in an earlier round;
- what only matters after v1 ships.

Aim questions at where things go wrong. The happy path is the part the user has already
thought through and described; the value is in the conflict, the reversal, the exception,
and the boundary. Money, time, capacity, identity, failure, and the edge of scope are where
briefs are silent and builds go wrong.

## Self-containment

The PRD replaces the brief and every questionnaire (round 1 included, whether or not it
followed a brief), so everything they carried must survive inside it, and nothing may point
outward to context the reader lacks.

- **Absorb, don't cite.** Restate the brief's and questionnaires' content in the PRD's own
  words in the right sections. Never write "as described in the brief", "see
  `02-questions.md`", "per our discussion", or "as we agreed" — the reader has none of
  those.
- **Everything the user wrote becomes document content.** Answers, corrected assumptions,
  and free-text comments must each land in a numbered section, not just quietly shape a
  requirement. A deposit percentage belongs in business rules; a capacity limit belongs in
  business rules and in an acceptance criterion; a worry mentioned in a comment box belongs
  in constraints, non-goals, or section 12. If something the user wrote changed your
  thinking but appears nowhere in the text, it is lost.
- **Define the domain terms.** Any word the business uses in a particular way — slot,
  service, no-show, session, credit — gets defined at first use or in section 9. Do not
  assume the reader knows the trade.
- **No unexplained proper nouns.** If the PRD names a person, team, tool, or system the
  business already uses, say in one clause what it is and why it matters.
- **Assumptions are visible.** Anything you inferred rather than were told goes in section
  12, so a reader can tell fact from inference without asking you.

**In feature mode**, absorb only what this feature needs — you do not have to restate the
whole product's history or every existing capability. But anything this feature's own
requirements, journeys, or rules depend on must still be spelled out in the PRD itself, the
same as if there were no existing project: a domain term this feature introduces, a rule it
changes, a journey it adds. "The existing product already handles this" is fine as a fact
absorbed into a sentence; it is not fine as a reason to leave a requirement unwritten.

## Writing rules

**Lead with the solution, in capability terms.** Section 2 tells a reader what is being
built before they hit the detail — one sentence, then a short paragraph on what people can
do with it and how that removes the pain in section 1. It is the section most likely to
leak a stack, so check it: if it names a framework, database, or vendor, rewrite it as
what the user sees and move the choice to section 12.

**Requirements are observable.** Every functional requirement describes behavior a person
could watch happen. Number them `FR-1`, `FR-2` … so the user can reference them in later
prompts.

**Acceptance criteria are checkable.** No judgment words. Translate:

| Don't write                 | Write                                                                              |
| --------------------------- | ---------------------------------------------------------------------------------- |
| "Checkout should be fast"   | "Confirmation screen appears within 5s of payment authorization"                   |
| "Intuitive booking flow"    | "A returning customer reaches paid confirmation in ≤3 screens"                     |
| "Handles errors gracefully" | "A declined card returns the user to payment with the booking held for 10 minutes" |

**Non-goals are stated positively.** Never rely on omission. Write "Not in scope: refunds,
staff roles, email reminders, multi-location" — not silence.

**Constraints are outcomes, not technologies.** This is what keeps the document
business-side while still constraining the build correctly:

| Don't write                | Write                                                                        |
| -------------------------- | ---------------------------------------------------------------------------- |
| "Use Stripe"               | "Customers pay by card; we never hold card numbers ourselves"                |
| "Postgres"                 | "Booking and payment history is retained indefinitely and exportable to CSV" |
| "Next.js, server-rendered" | "Works on mobile browsers; booking page usable within 3s on 4G"              |
| "Deploy on Vercel"         | "One person can run this without a sysadmin; hosting under $50/month"        |

**Unhappy paths get equal billing.** For every journey in section 6, write the failure
branches. This is where agents improvise worst.

**Waiting is a state, and it gets written down.** Every product with a save button has a
moment between the press and the result, and a PRD that never mentions it gets a build where
that moment is whatever the framework did by default. Give section 7 a short subsection —
three requirements is usually enough — covering: every control that changes something shows
it is working and cannot be pressed twice; a failure keeps what was typed and stays
retryable; and, for the handful of things the business cannot be wrong about, nothing is
shown as done before it is done. That last one is the one to write carefully. Showing a
result optimistically and correcting it later is good practice for a list of favourites and
a liability for a seat, a payment or a balance, so name which is which rather than stating a
blanket rule — section 8 has usually already decided the list. These belong in section 7 as
numbered requirements with acceptance criteria in section 11, not as a line in section 10,
because they are testable and because every one of them will otherwise be argued about
during the build.

**Phase the work.** Section 13 orders delivery into 4–6 phases by dependency, each ending
in something the user can click and verify. Keep each phase to roughly 30–50 requirements
— beyond ~150–200 instructions in one pass, agents start dropping them.

## Markdown output

The PRD is **one file that opens in any text editor or markdown viewer**. Nothing else may
be needed to read it — not a server, not a build step, not an internet connection.

- **Self-contained.** No images, no embedded scripts, no links to external files. If the
  reader is offline on a plane, the document still reads exactly as written.
- **Standard markdown only.** One `#` for the title, `##` per numbered section
  (`## 6. User journeys`), `###` for subsections. Journeys use numbered lists, requirement
  and rule lists use bullets, tables use real markdown tables. Nothing that needs a
  non-standard extension or a renderer plugin.
- **Requirements are addressable by name.** Give every functional requirement a bold label
  — `**FR-1**` — at the start of its line, numbered consecutively across the whole
  document, never reused after a requirement is deleted. Later sections and later prompts
  reference it as "FR-1" in prose; markdown has no reliable cross-file anchor, so do not
  build a link that depends on one.
- **Acceptance criteria are real checkboxes** — `- [ ] criterion` — so the checklist reads
  as a checklist rather than as prose.
- **A contents list at the top**, one line per section, linking to the heading's generated
  anchor (`[User journeys](#6-user-journeys)`). Match the heading text exactly, including
  the number, since the anchor is derived from it.
- **Escape the content.** Business copy contains `*`, `_`, `|`, and `#`. Escape or wrap in
  backticks anything that would otherwise be read as markdown syntax — especially inside
  table cells, where a stray `|` silently breaks the row.
- **No illustrations.** A PRD carries no diagrams, coverage charts, or figures that score
  the document against itself. Its content is decisions, journeys, and requirements — prose
  and lists say them more precisely than a picture. If you find a real gap, write the
  missing requirement, not a picture of its absence.

Everything in _Writing rules_, _Self-containment_, and _Constraints_ applies unchanged.
Markdown is the presentation; it does not license a more technical document. In
particular, the file format is not a stack decision — the PRD still names no framework,
database, or vendor anywhere in its content.

## Length

**There is no page or word cap.** The PRD is as long as the decisions it carries and no
longer. A document that drops a business rule to save a paragraph has failed at the only
job it has — an omitted rule does not disappear, it gets invented during the build.

What that does not license is padding. Length must come from content, not prose:

- **Cut prose to a bullet before cutting content**, never the reverse.
- **Sections 6–8 are the bulk.** Journeys, requirements and business rules are what a
  builder actually reads. Sections 1–5 orient and should stay tight; 9–13 are reference.
- **Say each thing once.** A rule stated in section 8 need not be restated in section 7 —
  point at it by requirement id instead.
- **Detail belonging to the later stack decision goes in section 12**, as a line, not
  expanded in the body.

Long documents get skimmed, so let the structure carry the reader: the contents list, the
`FR-` ids and the phases in section 13 all exist so nobody has to read end to end to find
one decision. If a PRD is long enough that a single build pass would start dropping
requirements, that is a phasing problem rather than a length problem — see _Phase the work_.

## Constraints

- **Never name a framework, language, database, library, cloud, or vendor** in the PRD.
  If the brief names one, move it to section 12 as a stated preference for the tech
  decision that follows, not as a requirement.
- **No schemas, endpoints, file layouts, or pseudo-code.** Section 9 describes entities in
  plain business language only.
- Never invent a business rule and present it as settled. Inferred rules go in section 12
  as assumptions, flagged for confirmation.
- **No dangling references.** The PRD may not depend on the brief, a questionnaire, this
  conversation, a chat thread, or anything the reader cannot open. Provenance in the header
  is a courtesy, not a dependency.
- Do not write code, scaffold a project, or pick a stack as part of this skill. Producing
  the PRD is the whole deliverable.
- Do not modify or delete the brief or any earlier questionnaire. They are superseded, not
  replaced on disk.
