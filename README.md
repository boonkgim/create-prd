# create-prd

**A brief is not a spec. This turns yours into one before a coding agent starts guessing —
and if you don't have a brief, it will build one with you.**

An [agent skill](https://agentskills.io) for Claude Code, Codex, and any other AI coding
agent that reads `SKILL.md`. Hand it a short problem/solution brief and it expands it into
a Product Requirements Document: lean enough to write in an hour, precise enough for an
agent to build from, and free of every tech decision. No brief yet? Say what you want to
build in a sentence and it starts round 1 of the questionnaire straight away — same gate,
same rounds, no brief required. Where there isn't enough to build from, the skill stops and
asks — in writing, in numbered rounds — until there is.

It works both ways: standing up a new product from nothing, and speccing a new feature for
a project that already exists. In the latter case it reads the project's own README and any
earlier PRDs first, so it doesn't re-ask what the project already answered.

This repo's own [commit history](https://github.com/boonkgim/create-prd/commits/main)
*is* the skill's design record: every commit that shaped it carries the real prompt that
drove the change, in order, from the first version through the two repos it was adopted
into. Read it before you install anything.

## Why you would want this

A coding agent cannot read omission. Ask for "a booking site" and the agent will invent a
currency, a cancellation policy, and a definition of "full" — usually the first plausible
thing it lands on, silently, in code you now have to find and unwind. The fix is not a
longer brief; it is a **document that cannot be written until the decisions exist**.

- **The PRD supersedes the brief.** It is self-contained — nobody who reads it needs the
  original brief, the questionnaire, or the conversation that produced it. Everything the
  user said lands in the document, in the document's own words.
- **The readiness gate is decisions, not detail.** Eight checks — money, time and
  capacity, the v1 boundary, every journey's failure path, a measurable success, identity,
  no unconfirmed guesses, the product has a name — and a thing can be *unknown* and still
  pass, as long as the unknown is written down rather than guessed. What fails the gate is
  a decision a builder would otherwise have to invent.
- **Rounds converge, they don't just continue.** Each round is strictly narrower than the
  last, never re-asks what is already answered, and carries a recommended default so
  "defaults are fine" is always a complete answer. Nothing loops forever.
- **It stays a business document.** No framework, database, language, or vendor is allowed
  in the PRD — those are a separate decision made after this one is approved. A stray tech
  preference in the brief gets moved to the assumptions section, not built into a
  requirement.
- **The brief is optional.** Nothing written down yet? Answer one question — what would you
  like to create — and the skill runs the same gate and the same rounds, just starting from
  round 1 of the questionnaire instead of a document you had to write first.
- **New product or new feature, same skill.** Point it at an existing project and it reads
  the project's own context first — README, prior PRDs — so a feature PRD only has to
  answer what's new, not re-litigate the whole product.

## Folder convention

With a brief:

```
docs/<dated-folder>/
  01-brief.md
  02-questions.md      <- round 1, the user types answers into it
  03-questions.md      <- round 2, only if needed
  04-prd.md            <- next free number once the gate passes
```

Without one:

```
docs/<dated-folder>/
  01-questions.md      <- round 1, stands in for the brief
  02-questions.md      <- round 2, only if needed
  03-prd.md            <- next free number once the gate passes
```

The PRD is one markdown file, capped at three pages. No images, no embedded scripts, no
links to files the reader might not have — it opens correctly in any text editor,
completely offline.

## Install

Paste this to your agent:

```
install the skill at https://github.com/boonkgim/create-prd
```

It clones the repo and puts `SKILL.md` and `references/` where your tool looks for
skills. To update it later, ask the same way, or `git pull` in the clone.

<details>
<summary>By hand</summary>

```bash
git clone https://github.com/boonkgim/create-prd.git

# Claude Code
ln -s "$PWD/create-prd" ~/.claude/skills/create-prd

# Codex
ln -s "$PWD/create-prd" ~/.agents/skills/create-prd
```

Symlink into a project's `.claude/skills/` instead to scope it to one repo. Other tools
read skills from their own location, and some take an upload; check yours.

</details>

A skill is instructions your agent will follow, so read `SKILL.md` before installing this
or any other. It is one file, plus two reference templates it copies from.

## Works with

`SKILL.md` follows the [Agent Skills](https://agentskills.io) open standard, so it loads
directly in any agent that reads the format — **Claude Code**, from `~/.claude/skills/`,
**OpenAI Codex**, from `~/.agents/skills/`, and any other tool with its own skills
directory. Where a tool does not read `SKILL.md` natively, paste it into the session or
drop it into the rules file that tool already reads, such as `AGENTS.md`. Nothing in it is
tool-specific — the whole skill is prose and markdown.

## Usage

Start from a short brief — a paragraph on the problem and the intended solution, saved as
`docs/<dated-folder>/01-brief.md` — or start from nothing and just say what you want to
build; the skill will ask one quick question and take it from there. Tools that support
invoking a skill by name take `/create-prd` directly; otherwise just ask for a PRD, with or
without a brief.

Works the same way for a brand-new product and for a new feature on a project you already
have open — for a feature, mention that it's an addition to the existing project and the
skill reads the project's own README and prior PRDs before asking anything.

The skill reads the folder, tests it against the readiness gate, and either writes the
next questionnaire round or writes the PRD. It never writes a partial PRD, never writes
code, and never commits on your behalf.

If this is useful, a ⭐ helps other people find it.

## When not to use this

- **The stack is already decided and you just want a spec that names it.** This skill
  refuses to name one on purpose — if that constraint does not serve you, you want a
  plainer PRD template instead.
- **You already know every answer.** The questionnaire loop earns its keep on a brief that
  is genuinely underspecified. Tell the skill to write the PRD now and it will, marking
  whatever remains as an assumption — but if nothing is actually unknown, a round is
  overhead.
- **The change is genuinely small.** A one-line tweak with no new business rule, journey, or
  edge case doesn't need a PRD at all. This skill is for a feature big enough to carry its
  own decisions — money, scope, failure paths — even when the product around it is already
  built and already documented.

## Author

Built by **Khur Boon Kgim** at [boonkgim.com](https://boonkgim.com), where I write about
practical AI for builders: AI agents, coding workflows, and shipping software.

## License

MIT. See [LICENSE](LICENSE).
