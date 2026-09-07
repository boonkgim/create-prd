---
name: brief-to-prd
description: Turn a short project brief into a lean but build-ready PRD that a coding agent can implement from. The PRD stays a business document - no tech stack, no schemas, no framework choices. Use when the user asks to write a PRD, expand a brief into requirements, or produce a spec before vibe coding.
---

# Brief to PRD

Expand a short problem/solution brief into a Product Requirements Document that is
**lean enough to write in an hour, precise enough for an agent to build from, and free of
technology decisions**.

## Core principle

A coding agent cannot read omission. Anything left implicit gets filled with the simplest
thing the model can invent — usually the wrong thing. So the PRD states, positively:
what is in scope, what is *not*, what the business rules are, and what "done" looks like
in observable terms.

The PRD answers **what and why**. It never answers **how**. Stack, schema, hosting, and
libraries are a separate decision made after the PRD is approved.

## Steps

1. **Read the brief.** Find it in `docs/` (most recent dated folder) unless the user names
   a file. Also read any sibling notes in the same folder. If no brief exists, ask the user
   for a paragraph on the problem and the intended solution before going further.

2. **Draft silently first.** Fill in everything the brief already answers or that has one
   obvious sensible answer. Do not ask about things you can reasonably infer.

3. **Ask the gaps — once, in a batch.** Collect every genuine unknown and ask them
   together (see *Interview* below). Do not drip-feed questions across several turns. If
   the user declines to answer, write the PRD anyway under stated assumptions and list them
   in section 11.

4. **Write the PRD** to `docs/<same-folder-as-brief>/02-prd.md` using the structure in
   `references/prd-template.md`. Keep the brief file untouched.

5. **Report** the file path, the page count, and the open questions that still need the
   user's decision. Do not start implementing.

## Interview

Ask only what you cannot infer. These are the questions that most often decide the build
and that nobody can guess for the user:

- **Money** — who pays, how much, when. Deposit or full amount? Refunds? Cancellation
  window? Currency? Tax?
- **Time** — timezones, business hours, lead time, capacity/availability limits, what
  happens on a double-booking.
- **Identity** — do users need accounts? Guest checkout allowed? What can they see about
  their own history?
- **Failure** — what should happen when the unhappy path hits: payment declined, no-show,
  customer wants to reschedule, admin needs to override.
- **Scale and stakes** — roughly how many users/transactions, and what breaking would
  actually cost the business.
- **Boundaries** — what they explicitly do *not* want in v1.

Group them, number them, and give a recommended default for each so the user can answer
"defaults are fine."

## Writing rules

**Requirements are observable.** Every functional requirement describes behavior a person
could watch happen. Number them `FR-1`, `FR-2` … so the user can reference them in later
prompts.

**Acceptance criteria are checkable.** No judgment words. Translate:

| Don't write | Write |
|---|---|
| "Checkout should be fast" | "Confirmation screen appears within 5s of payment authorization" |
| "Intuitive booking flow" | "A returning customer reaches paid confirmation in ≤3 screens" |
| "Handles errors gracefully" | "A declined card returns the user to payment with the booking held for 10 minutes" |

**Non-goals are stated positively.** Never rely on omission. Write "Not in scope: refunds,
staff roles, email reminders, multi-location" — not silence.

**Constraints are outcomes, not technologies.** This is what keeps the document
business-side while still constraining the build correctly:

| Don't write | Write |
|---|---|
| "Use Stripe" | "Customers pay by card; we never hold card numbers ourselves" |
| "Postgres" | "Booking and payment history is retained indefinitely and exportable to CSV" |
| "Next.js, server-rendered" | "Works on mobile browsers; booking page usable within 3s on 4G" |
| "Deploy on Vercel" | "One person can run this without a sysadmin; hosting under $50/month" |

**Unhappy paths get equal billing.** For every journey in section 5, write the failure
branches. This is where agents improvise worst.

**Phase the work.** Section 12 orders delivery into 4–6 phases by dependency, each ending
in something the user can click and verify. Keep each phase to roughly 30–50 requirements
— beyond ~150–200 instructions in one pass, agents start dropping them.

## Size targets

| Section | Length |
|---|---|
| 1–4 (problem, users, metrics, scope) | ~1 page |
| 5–7 (journeys, requirements, business rules) | the bulk — most of the detail lives here |
| 8–12 (data, constraints, acceptance, questions, phases) | ~1–1.5 pages |
| Total | 3–6 pages |

If it runs past 6 pages, the excess is almost always prose that should be a bullet, or
implementation detail that does not belong in a PRD.

## Constraints

- **Never name a framework, language, database, library, cloud, or vendor** in the PRD.
  If the brief names one, move it to section 11 as a stated preference for the tech
  decision that follows, not as a requirement.
- **No schemas, endpoints, file layouts, or pseudo-code.** Section 8 describes entities in
  plain business language only.
- Never invent a business rule and present it as settled. Inferred rules go in section 11
  as assumptions, flagged for confirmation.
- Do not write code, scaffold a project, or pick a stack as part of this skill. Producing
  the PRD is the whole deliverable.
- Do not modify the source brief.
