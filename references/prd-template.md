# PRD template

Copy this structure. Delete sections that genuinely do not apply; do not delete a section
because it is hard to fill in — that is usually the section that matters most.

---

```markdown
# PRD: <Product name>

Owner: <name> · Date: <YYYY-MM-DD> · Status: Draft · Source brief: <path>

## 1. Problem

3–5 sentences. What is broken today, for whom, how often it happens, and what it costs in
time or money. Concrete numbers beat adjectives. No solution talk here.

## 2. Target users

One to three personas, no more. For each:

- **<Role>** — what they are trying to get done · what they do today instead · what makes
  the current way painful for them.

## 3. Success metrics

Two to four, each numeric and time-bound.

- <Metric> — from <baseline> to <target> within <window>.
- **Counter-metric:** <what must not get worse>.

## 4. Scope

### In scope (v1)
- <capability>

### Not in scope (v1)
State positively and specifically. This section prevents over-building more than any other.
- <capability the agent must not build>

### Later / maybe
- <capability deferred to v2, recorded so it is not re-litigated>

## 5. User journeys

The core of the document. One subsection per primary flow, numbered end to end, written
from the user's point of view.

### 5.1 <Journey name>

**Happy path**
1. <step>
2. <step>

**Unhappy paths**
- <condition> → <what the user sees, what the system does>
- <condition> → <what the user sees, what the system does>

Repeat for each primary journey. Every journey needs unhappy paths.

## 6. Functional requirements

Grouped by capability, each numbered so it can be referenced in a later prompt. Each states
observable behavior, not implementation.

### 6.1 <Capability>
- **FR-1** — <observable behavior>
- **FR-2** — <observable behavior>

### 6.2 <Capability>
- **FR-3** — <observable behavior>

## 7. Business rules and edge cases

The decisions an agent cannot guess and will otherwise invent. Be exhaustive here.

- **Pricing:** <rule>
- **Cancellation / refunds:** <rule and window>
- **Timezones and hours:** <rule>
- **Currency and tax:** <rule>
- **Capacity and conflicts:** <what happens when two users want the same slot>
- **Overrides:** <what the operator can change manually, and what they cannot>

## 8. Data the business cares about

Plain-language entities only — no tables, columns, keys, or types.

- **<Entity>** — what it represents · what must be retained · how long · who can see it ·
  whether it must be exportable.

## 9. Constraints

Expressed as outcomes, never as technology choices.

- **Devices and reach:** <e.g. must work on mobile browsers, no app install>
- **Performance:** <e.g. booking page usable within 3s on a 4G connection>
- **Availability:** <e.g. can be down for maintenance overnight; must not lose a booking>
- **Privacy and compliance:** <e.g. we never hold card numbers ourselves; personal data
  deletable on request>
- **Operating limits:** <budget ceiling, who maintains it, launch date>

## 10. Acceptance criteria

Definition of done, as a checklist, grouped by journey. Each line must be verifiable by
watching the product — no judgment words.

### <Journey name>
- [ ] <criterion>
- [ ] <criterion>

## 11. Assumptions and open questions

**Assumptions made** (proceeding on these unless corrected)
- <assumption> — affects <FR references>

**Open questions** (need a decision before the affected phase is built)
- <question> — blocks <FR references>

**Stated preferences** (not requirements; input to the separate tech decision)
- <e.g. "user has an existing payment account they would prefer to reuse">

## 12. Delivery phases

Four to six phases, ordered by dependency. Each ends in something clickable and verifiable.

1. **<Phase name>** — <FR-1 … FR-6>. Verifiable when: <what the user can do at the end>.
2. **<Phase name>** — <FR-7 … FR-12>. Verifiable when: <…>.
```

---

## Filling-in notes

**Section 5 vs section 6.** Journeys are narrative and ordered; requirements are atomic and
referenceable. Both are needed — the journey gives the agent context for micro-decisions,
the requirement gives it something to check off.

**Section 7 is the one people skip.** Every rule missing here becomes an invented rule in
the codebase. If the user cannot answer a rule, it belongs in section 11 as an open
question, not silently guessed in section 6.

**Section 9 is where tech-agnosticism is won or lost.** Before writing a line here, check
that it describes what must be true for the business, not what must be installed.

**Section 12 is not a schedule.** No dates, no estimates. It is a dependency order so the
build can be prompted one verifiable chunk at a time.
