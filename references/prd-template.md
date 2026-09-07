<!--
PRD TEMPLATE — copy this file to the brief's folder as NN-prd.md and replace the content.
Everything in [square brackets] is a placeholder; the prose around it is guidance for
whoever writes the document, and is meant to be overwritten too.

DELETE THIS COMMENT in the copy. It is a note to the writer, not part of the PRD.

Structure rules
----------------
Delete a section that genuinely does not apply; do not delete one because it is hard to
fill in — that is usually the section that matters most. If you delete a section, delete
its contents entry too, and do not renumber the survivors: a reader referring to
"section 8" must land on business rules.

Keep this document to three pages (~1500 words) total. Cut prose to a bullet before
cutting content — see Size targets in SKILL.md for the per-section budget.

Writing notes
--------------
Section 2 is the orientation, not the spec. It exists so a reader — human or agent —
knows what is being built before hitting the detail. Keep it to what a user can do. The
moment it names a framework, database, or vendor, it has stopped being a solution summary
and become an architecture note; move that to section 12 as a stated preference.

Sections 1 and 2 must line up. Every pain named in section 1 should be visibly answered in
section 2. If a paragraph of section 2 solves nothing in section 1, it is scope creep
appearing before the scope section.

Section 6 vs section 7. Journeys are narrative and ordered; requirements are atomic and
referenceable. Both are needed — the journey gives the agent context for micro-decisions,
the requirement gives it something to check off.

Section 7 ids are load-bearing. **FR-1** is how a later prompt, a comment, or section 12
points at one requirement precisely. Number them consecutively across the whole document,
not restarting per subsection, and never reuse a number after deleting a requirement.

Section 8 is the one people skip. Every rule missing here becomes an invented rule in the
codebase. If the user cannot answer a rule, it belongs in section 12 as an open question,
not silently guessed in section 7.

Section 10 is where tech-agnosticism is won or lost. Before writing a line here, check
that it describes what must be true for the business, not what must be installed.

Section 13 is not a schedule. No dates, no estimates. It is a dependency order so the
build can be prompted one verifiable chunk at a time.

Check before reporting: every contents link jumps to the right heading, every checkbox
renders as a checkbox, and no bracketed placeholder survived.
-->

# PRD: [Product name]

Owner: [name] · Date: [YYYY-MM-DD] · Status: Draft
Supersedes: [brief and questionnaire filenames] — kept as history; this document is the
source of truth.

## Contents

1. [Problem](#1-problem)
2. [Solution summary](#2-solution-summary)
3. [Target users](#3-target-users)
4. [Success metrics](#4-success-metrics)
5. [Scope](#5-scope)
6. [User journeys](#6-user-journeys)
7. [Functional requirements](#7-functional-requirements)
8. [Business rules and edge cases](#8-business-rules-and-edge-cases)
9. [Data the business cares about](#9-data-the-business-cares-about)
10. [Constraints](#10-constraints)
11. [Acceptance criteria](#11-acceptance-criteria)
12. [Assumptions and open questions](#12-assumptions-and-open-questions)
13. [Delivery phases](#13-delivery-phases)

## 1. Problem

3–5 sentences. What is broken today, for whom, how often it happens, and what it costs in
time or money. Concrete numbers beat adjectives. No solution talk here.

Write this so it reads to someone who has never heard of the business. Do not assume the
reader knows the trade, the customers, or how the work is done today — the brief's context
lives here now, restated, not referenced.

## 2. Solution summary

**In one sentence:** [what this product is and who it is for]

3–5 sentences expanding that: what the product lets people do, how that removes the pain
in section 1, and what makes this approach the right one. Describe capability, not
construction — a reader should finish this section knowing what they would see on screen,
not what it is built with.

**Why this approach** — one or two lines on the alternative you are not taking and why,
e.g. "not adding staff to handle payments manually, because the cost scales with volume".

## 3. Target users

One to three personas, no more.

- **[Role]** — what they are trying to get done · what they do today instead · what makes
  the current way painful for them.

## 4. Success metrics

Two to four, each numeric and time-bound.

- [Metric] — from [baseline] to [target] within [window].
- **Counter-metric:** [what must not get worse].

## 5. Scope

### In scope (v1)

- [capability]

### Not in scope (v1)

State positively and specifically. This section prevents over-building more than any
other.

- [capability the agent must not build]

### Later / maybe

- [capability deferred to v2, recorded so it is not re-litigated]

## 6. User journeys

The core of the document. One subsection per primary flow, numbered end to end, written
from the user's point of view. Every journey needs unhappy paths.

### 6.1 [Journey name]

**Happy path**

1. [step]
2. [step]

**Unhappy paths**

- [condition] → [what the user sees, what the system does]
- [condition] → [what the user sees, what the system does]

### 6.2 [Journey name]

Repeat for each primary journey.

## 7. Functional requirements

Grouped by capability, each with a bold `FR-` label so it can be referenced in a later
prompt. Each states observable behavior, not implementation.

### 7.1 [Capability]

- **FR-1** — [observable behavior]
- **FR-2** — [observable behavior]

### 7.2 [Capability]

- **FR-3** — [observable behavior]

### 7.[last] Interaction feedback

Keep this subsection last and keep it short. It applies across every screen rather than to
one capability, and it is here because the alternative is that the build decides it.

- **FR-4** — [every control that changes something shows it is working until the result is
  on screen, and cannot be pressed a second time meanwhile]
- **FR-5** — [the things this business cannot be wrong about — name them, drawn from
  section 8 — are never shown as done before they are done; everything else may show its
  result immediately and correct itself if it fails]
- **FR-6** — [a failure says what went wrong, keeps what was typed, and leaves the action
  available to try again]

## 8. Business rules and edge cases

The decisions an agent cannot guess and will otherwise invent. Be exhaustive here.

- **Pricing:** [rule]
- **Cancellation / refunds:** [rule and window]
- **Timezones and hours:** [rule]
- **Currency and tax:** [rule]
- **Capacity and conflicts:** [what happens when two users want the same slot]
- **Overrides:** [what the operator can change manually, and what they cannot]

## 9. Data the business cares about

Plain-language entities only — no tables, columns, keys, or types. This doubles as the
glossary: if the business uses a word in a particular way, define it here.

- **[Entity]** — what it means in this business · what it represents · what must be
  retained · how long · who can see it · whether it must be exportable.

## 10. Constraints

Expressed as outcomes, never as technology choices.

- **Devices and reach:** [e.g. must work on mobile browsers, no app install]
- **Performance:** [e.g. booking page usable within 3s on a 4G connection]
- **Availability:** [e.g. can be down for maintenance overnight; must not lose a booking]
- **Privacy and compliance:** [e.g. we never hold card numbers ourselves; personal data
  deletable on request]
- **Operating limits:** [budget ceiling, who maintains it, launch date]

## 11. Acceptance criteria

Definition of done, grouped by journey. Each line must be verifiable by watching the
product — no judgment words.

### [Journey name]

- [ ] [criterion]
- [ ] [criterion]

## 12. Assumptions and open questions

**Assumptions made** — proceeding on these unless corrected.

- [assumption] — affects FR-1

**Open questions** — need a decision before the affected phase is built.

- [question] — blocks FR-2

**Stated preferences** — not requirements; input to the separate tech decision.

- [e.g. the user has an existing payment account they would prefer to reuse]

## 13. Delivery phases

Four to six phases, ordered by dependency. Each ends in something clickable and
verifiable.

1. **[Phase name]** — FR-1 … FR-6. Verifiable when: [what the user can do at the end].
2. **[Phase name]** — FR-7 … FR-12. Verifiable when: […].
