---
name: brief-to-prd
description: Turn a short project brief into a lean but build-ready PRD that a coding agent can implement from, asking the user numbered questionnaire rounds until the brief is decision-complete. The PRD is written as a single self-contained HTML file, supersedes the brief, and stays a business document - no tech stack, no schemas, no framework choices. Use when the user asks to write a PRD, expand a brief into requirements, answer a questionnaire round, or produce a spec before vibe coding.
---

# Brief to PRD

Expand a short problem/solution brief into a Product Requirements Document that is
**lean enough to write in an hour, precise enough for an agent to build from, and free of
technology decisions**.

## Core principle

A coding agent cannot read omission. Anything left implicit gets filled with the simplest
thing the model can invent — usually the wrong thing. So the PRD states, positively:
what is in scope, what is _not_, what the business rules are, and what "done" looks like
in observable terms.

The PRD answers **what and why**. It never answers **how**. Stack, schema, hosting, and
libraries are a separate decision made after the PRD is approved.

The PRD also **supersedes the brief**. It is the single document handed to whoever builds
this. A reader who has never seen the brief and was not present for any conversation about
it must be able to build from the PRD alone.

A brief almost never contains enough to do that. Do not paper over the gap with plausible
guesses — **ask, in writing, until the decisions exist**. The questioning is not overhead
before the real work; it is most of the work.

## Folder convention

Everything lives in the brief's folder, numbered in creation order:

```
docs/<dated-folder>/
  01-brief.md
  02-questions.md      <- round 1, markdown: the user types answers into it
  03-questions.md      <- round 2, only if needed
  04-prd.html          <- next free number once the gate passes
```

The PRD's number depends on how many rounds ran. Always use the next free number; never
overwrite or renumber an existing file.

In this repo the folder is a new dated one beside `docs/2026-08-08-setup` — never inside
it. That folder is the scaffold's plan of record and `scripts/docs-check.mjs` compares it
against the working tree file by file; a PRD dropped into it would be read as drift. Every
other folder under `docs/` is unwatched, so a new one costs nothing.

**The PRD is HTML; the questionnaires stay markdown.** The PRD is read far more often than
it is edited, and it is the document handed to other people — so it is a finished, styled
page that opens in a browser. A questionnaire is a working file the user writes into by
hand, so it stays plain markdown. Never write a questionnaire as HTML.

## Steps

1. **Read the folder, not just the brief.** Read the brief and every file in its folder in
   number order, including earlier questionnaires and everything the user wrote into them —
   answers, corrections to assumptions, and free-text comments alike. Read the comments
   first: they often invalidate a question or move something in or out of scope. Rounds may
   span sessions — the files are the memory, not the conversation. If no brief exists, ask
   the user for a paragraph on the problem and intended solution first.

2. **Test against the readiness gate** below. Record which gates pass, which fail, and for
   each failure the specific decision that is missing.

3. **If any gate fails, write a questionnaire** to the next free number
   (`NN-questions.md`) using `references/questionnaire-template.md`, and following
   _Question design_ and _Rounds_ below. Then stop and tell the
   user which file to fill in. Do not write a partial PRD, and do not write a draft PRD
   alongside the questions — a draft invites approval of guesses instead of decisions.

4. **When the user returns with answers**, start again at step 1. The folder now contains
   their answers; re-test the gate; issue a narrower round if it still fails.

5. **When every gate passes, write the PRD** to the next free number (`NN-prd.html`) by
   copying `references/prd-template.html` and replacing its content, following the rules in
   _HTML output_ below. The template is a working HTML file — open it in a browser to see
   what a finished PRD looks like. Its head comment carries the section-by-section writing
   notes and is addressed to you, not to the reader: **delete that comment from the copy.**
   Fold the brief and every answer from every round into the document itself — see
   _Self-containment_. Leave the brief and the questionnaires untouched; they stay as
   history.

6. **Open it in a browser.** Rendering is the proof the file is well-formed — a missing
   `</section>`, an unescaped `<`, or a broken anchor is invisible in the source and
   obvious on the page. Check that the contents links jump and that no bracketed
   placeholder survived. There is no build step: the copy is finished the moment it is
   written.

7. **Read it back cold.** Re-read the finished PRD as if you had never seen the brief, the
   questionnaires, or the conversation. Every question it raises that the document cannot
   answer is a gap: fill it, or record it in section 12 as an open question. Check
   specifically that every answer, correction, and comment the user wrote landed somewhere
   in the document.

8. **Report** the file path, the page count, and any open questions that remain. Say the
   file opens in a browser by double-clicking it — no server, no build step. State that the
   PRD supersedes the brief, and that it is now the user's turn to critique it. Do not start
   implementing. Once the user has approved it, building it here is the `feature` skill's
   job, one vertical slice per capability — this skill does not commit and does not write
   code.

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

The PRD replaces the brief, so everything the brief carried must survive inside it, and
nothing may point outward to context the reader lacks.

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

## HTML output

The PRD is **one file that opens by double-clicking it**. Nothing else may be needed to read
it — not a server, not a build step, not an internet connection.

- **Self-contained.** All CSS goes in a single `<style>` block in the head — take the
  template's and leave it alone unless the content needs something it lacks. No CDN links,
  no external stylesheets, no remote fonts, no images, no JavaScript. If the reader is
  offline on a plane, the document still looks right.
- **System font stacks only** — a serif for reading, a sans for labels, and a mono for
  code spans. Nothing is vendored and nothing is downloaded, so the file is small, opens
  instantly, and has no build step between writing it and reading it. The serif is what
  carries the prose: a PRD is read in long passages, and that is what a serif is for.
- **Semantic structure.** One `<h1>` for the title, one `<section>` per numbered section
  with an `id` (`id="s6"`, `id="s8"`), `<h2>` for section headings, `<h3>` for subsections.
  Journeys use `<ol>`, requirement and rule lists use `<ul>`, tables use real `<table>`.
- **Requirements are addressable.** Every functional requirement gets
  `id="fr-1"` on its list item so a later prompt or a comment can link straight to it. Same
  for journeys (`id="j-6-1"`) and acceptance criteria groups.
- **Acceptance criteria are real checkboxes** — `<input type="checkbox" disabled>` — so the
  checklist reads as a checklist rather than as prose.
- **Readable by default.** Body text is the serif at 18px, line height 1.7, measure capped
  near 70 characters. Everything that is a label rather than a sentence — the section
  number, the meta lines, table headers, the contents — is the sans, one or two steps
  smaller and muted. That split is the whole type system: if you are adding a rule, ask
  which of the two the text is, and use nothing else. Headings are separated by space
  rather than by horizontal rules — a document with a line above every heading reads as a
  form. The section number is a small muted label above its heading, not a coloured digit
  in the reading line, which keeps "section 8" findable without interrupting the sentence.
  The accent colour is for links, and nothing else.
- **The text sits on a bordered card.** `main` is a panel — card background, hairline
  border, 10px radius — on a slightly darker page. On a wide screen a bare column of text
  has no edge to sit against; the border gives the document a shape and separates it from
  the sidebar. The card is the _only_ panel: no nested cards, no callout boxes, no
  colour-coded blocks, no shadows.
- **One house style.** The stylesheet in `references/prd-template.html` is the house style;
  take it verbatim. This repo carries no companion stack document — the stack is already
  decided and lives in `CLAUDE.md` and the layer skills — so there is nothing here to keep
  in sync. If you port this skill somewhere that does have one, that pair has to be kept
  aligned by hand, one document at a time.
- **Minimal, not decorated.** This is a document to be read end to end, not a dashboard.
  No icons, no badges, no tinted highlight blocks, no borders that are not doing work.
  Where something needs separating, use space; where space is not enough, use a hairline.
  Restraint here is not austerity — it is what makes section 8 legible at the point someone
  is trying to settle an argument with it.
- **Works in both themes.** Define the palette as CSS custom properties on `:root` and
  override them inside `@media (prefers-color-scheme: dark)`. Never hard-code `color: #000`.
  If you change the stylesheet, open `references/prd-template.html` in a browser and check
  both themes there — not on a real PRD.
- **No print stylesheet.** Do not write one. These documents are read on screen, and a
  `@media print` block is not free: it drags in rules about page breaks, baseline handling
  and a second colour scheme that then get cited as reasons a diagram cannot move, cannot
  be interactive, and must be hand-placed. Nobody prints a PRD; do not pay for it.
- **Escape the content.** Business copy contains `&`, `<`, `>`, quotes, and em dashes.
  Escape entities properly — a stray `<` silently eats the rest of a paragraph in a browser,
  which is exactly the kind of loss this document exists to prevent.
- **Navigable, but not interactive.** The template's table of contents is a sticky sidebar
  above 68rem and a card at the top of the page below it — plain anchor links and a CSS
  grid, no JavaScript. Keep it. What stays out: collapsible sections, a search box, a
  progress bar, a back-to-top button, anything that needs script. A PRD is read top to
  bottom and jumped around by section number; those two behaviours are the whole navigation
  requirement, and everything past them costs the reader more than it gives. There is a
  second reason on top of the reader's: this document is also read by a coding agent that
  sees only the file's text, and anything built at runtime does not exist for it. Keeping
  the PRD scriptless is what makes the two audiences one audience.
- **No illustrations, and that is deliberate.** Unlike the stack and data-model documents
  that follow it, a PRD carries no diagrams. Its content is decisions, journeys and
  requirements — prose and lists, which a picture cannot say more precisely. Do not add an
  entity sketch, a coverage chart, a traceability matrix or a metrics dashboard. **Be
  especially wary of a figure that scores the document against itself** — how many
  requirements serve a metric, how many have a test. Those numbers require you to judge each
  requirement, they land in the document reading as the owner's own claim rather than yours,
  and the headline is usually meaningless: most requirements exist to make a product correct
  rather than to move a number. If you find a real gap in the PRD, the fix is to write the
  missing requirement or criterion, not to draw a picture of its absence.

Everything in _Writing rules_, _Self-containment_, and _Constraints_ applies unchanged. HTML
is the presentation; it does not license a longer, more decorated, or more technical
document. In particular, HTML is not a stack decision — the PRD still names no framework,
database, or vendor anywhere in its content.

## Size targets

| Section                                                 | Length                                   |
| ------------------------------------------------------- | ---------------------------------------- |
| 1–5 (problem, solution, users, metrics, scope)          | ~1–1.5 pages                             |
| 6–8 (journeys, requirements, business rules)            | the bulk — most of the detail lives here |
| 9–13 (data, constraints, acceptance, questions, phases) | ~1–1.5 pages                             |
| Total                                                   | 3–6 pages                                |

Pages here are a rough unit of reading length, not a paper measurement — roughly 500 words
each. If it runs past 6, the excess is almost always prose that should be a bullet, or
implementation detail that does not belong in a PRD.

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
