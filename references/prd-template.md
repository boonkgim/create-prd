# PRD template

The PRD is written as a single self-contained HTML file, `NN-prd.html`. Copy the skeleton
below: keep the `<style>` block as-is unless you have a reason, and replace everything
between the section tags.

Copy this structure. Delete sections that genuinely do not apply; do not delete a section
because it is hard to fill in — that is usually the section that matters most. If you delete
a section, delete its table-of-contents entry too, and do not renumber the survivors — a
reader referring to "section 8" must land on business rules.

The finished document must stand on its own. Someone who has never read the brief or the
questionnaires, and was never in the room, must be able to build from it without asking a
question you have not already answered or flagged.

---

## The stylesheet

Paste this verbatim into the `<head>`. It is deliberately plain: one accent, one font stack,
both themes, and a print block. Do not add to it — decoration is not what makes a PRD land.

```html
<style>
  :root {
    --bg: #fdfdfc;
    --fg: #1c1c1a;
    --muted: #6b6b66;
    --rule: #e2e2dd;
    --accent: #7a4b1e;
    --code-bg: #f2f2ee;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #191918;
      --fg: #e8e8e4;
      --muted: #9a9a93;
      --rule: #333331;
      --accent: #d8a271;
      --code-bg: #242422;
    }
  }
  * { box-sizing: border-box; }
  body {
    margin: 0 auto;
    padding: 3rem 1.5rem 6rem;
    max-width: 44rem;
    background: var(--bg);
    color: var(--fg);
    font: 17px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
          "Helvetica Neue", Arial, sans-serif;
    -webkit-text-size-adjust: 100%;
  }
  h1 { font-size: 1.9rem; line-height: 1.25; margin: 0 0 .5rem; letter-spacing: -.01em; }
  h2 {
    font-size: 1.25rem; line-height: 1.3; margin: 3rem 0 .75rem;
    padding-top: 1.25rem; border-top: 1px solid var(--rule); letter-spacing: -.01em;
  }
  h3 { font-size: 1.02rem; margin: 1.75rem 0 .5rem; }
  h2 .num { color: var(--accent); font-variant-numeric: tabular-nums; }
  p, li { margin: 0 0 .6rem; }
  ul, ol { padding-left: 1.4rem; margin: 0 0 1rem; }
  li > ul, li > ol { margin-top: .4rem; }
  a { color: var(--accent); }
  strong { font-weight: 600; }
  code { background: var(--code-bg); padding: .1em .35em; border-radius: 3px; font-size: .9em; }
  .meta { color: var(--muted); font-size: .9rem; margin: 0 0 .25rem; }
  .lede { font-size: 1.05rem; }
  .toc { margin: 2.5rem 0 0; padding: 1rem 1.25rem; background: var(--code-bg); border-radius: 6px; }
  .toc h2 { font-size: .8rem; text-transform: uppercase; letter-spacing: .08em;
            color: var(--muted); margin: 0 0 .5rem; padding: 0; border: 0; }
  .toc ol { margin: 0; padding-left: 1.3rem; }
  .toc li { margin: 0 0 .2rem; }
  table { border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: .95rem; }
  th, td { text-align: left; padding: .5rem .6rem; border-bottom: 1px solid var(--rule);
           vertical-align: top; }
  th { font-weight: 600; }
  .check { list-style: none; padding-left: 0; }
  .check li { padding-left: 1.75rem; text-indent: -1.75rem; }
  .check input { margin-right: .6rem; }
  @media print {
    :root { --bg: #fff; --fg: #000; --muted: #444; --rule: #ccc; --accent: #000;
            --code-bg: #fff; }
    body { padding: 0; max-width: none; font-size: 11pt; }
    .toc { border: 1px solid var(--rule); }
    h2, h3 { break-after: avoid; }
    table, li, .check li { break-inside: avoid; }
  }
</style>
```

---

## The document

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PRD: &lt;Product name&gt;</title>
<!-- stylesheet from above goes here -->
</head>
<body>

<h1>PRD: &lt;Product name&gt;</h1>
<p class="meta">Owner: &lt;name&gt; · Date: &lt;YYYY-MM-DD&gt; · Status: Draft</p>
<p class="meta">Supersedes: &lt;brief and questionnaire filenames&gt; — kept as history; this
document is the source of truth.</p>

<nav class="toc">
  <h2>Contents</h2>
  <ol>
    <li><a href="#s1">Problem</a></li>
    <li><a href="#s2">Solution summary</a></li>
    <li><a href="#s3">Target users</a></li>
    <li><a href="#s4">Success metrics</a></li>
    <li><a href="#s5">Scope</a></li>
    <li><a href="#s6">User journeys</a></li>
    <li><a href="#s7">Functional requirements</a></li>
    <li><a href="#s8">Business rules and edge cases</a></li>
    <li><a href="#s9">Data the business cares about</a></li>
    <li><a href="#s10">Constraints</a></li>
    <li><a href="#s11">Acceptance criteria</a></li>
    <li><a href="#s12">Assumptions and open questions</a></li>
    <li><a href="#s13">Delivery phases</a></li>
  </ol>
</nav>

<section id="s1">
<h2><span class="num">1.</span> Problem</h2>
<p>3–5 sentences. What is broken today, for whom, how often it happens, and what it costs in
time or money. Concrete numbers beat adjectives. No solution talk here.</p>
<p>Write this so it reads to someone who has never heard of the business. Do not assume the
reader knows the trade, the customers, or how the work is done today — the brief's context
lives here now, restated, not referenced.</p>
</section>

<section id="s2">
<h2><span class="num">2.</span> Solution summary</h2>
<p class="lede"><strong>In one sentence:</strong> &lt;what this product is and who it is
for&gt;</p>
<p>3–5 sentences expanding that: what the product lets people do, how that removes the pain
in section 1, and what makes this approach the right one. Describe capability, not
construction — a reader should finish this section knowing what they would see on screen,
not what it is built with.</p>
<p><strong>Why this approach</strong> — one or two lines on the alternative you are not
taking and why (e.g. "not adding staff to handle payments manually, because the cost scales
with volume").</p>
</section>

<section id="s3">
<h2><span class="num">3.</span> Target users</h2>
<p>One to three personas, no more.</p>
<ul>
  <li><strong>&lt;Role&gt;</strong> — what they are trying to get done · what they do today
  instead · what makes the current way painful for them.</li>
</ul>
</section>

<section id="s4">
<h2><span class="num">4.</span> Success metrics</h2>
<p>Two to four, each numeric and time-bound.</p>
<ul>
  <li>&lt;Metric&gt; — from &lt;baseline&gt; to &lt;target&gt; within &lt;window&gt;.</li>
  <li><strong>Counter-metric:</strong> &lt;what must not get worse&gt;.</li>
</ul>
</section>

<section id="s5">
<h2><span class="num">5.</span> Scope</h2>
<h3>In scope (v1)</h3>
<ul><li>&lt;capability&gt;</li></ul>
<h3>Not in scope (v1)</h3>
<p>State positively and specifically. This section prevents over-building more than any
other.</p>
<ul><li>&lt;capability the agent must not build&gt;</li></ul>
<h3>Later / maybe</h3>
<ul><li>&lt;capability deferred to v2, recorded so it is not re-litigated&gt;</li></ul>
</section>

<section id="s6">
<h2><span class="num">6.</span> User journeys</h2>
<p>The core of the document. One subsection per primary flow, numbered end to end, written
from the user's point of view.</p>

<h3 id="j-6-1">6.1 &lt;Journey name&gt;</h3>
<p><strong>Happy path</strong></p>
<ol>
  <li>&lt;step&gt;</li>
  <li>&lt;step&gt;</li>
</ol>
<p><strong>Unhappy paths</strong></p>
<ul>
  <li>&lt;condition&gt; → &lt;what the user sees, what the system does&gt;</li>
  <li>&lt;condition&gt; → &lt;what the user sees, what the system does&gt;</li>
</ul>

<p>Repeat for each primary journey. Every journey needs unhappy paths.</p>
</section>

<section id="s7">
<h2><span class="num">7.</span> Functional requirements</h2>
<p>Grouped by capability, each with an <code>id</code> so it can be linked and referenced in
a later prompt. Each states observable behavior, not implementation.</p>

<h3>7.1 &lt;Capability&gt;</h3>
<ul>
  <li id="fr-1"><strong>FR-1</strong> — &lt;observable behavior&gt;</li>
  <li id="fr-2"><strong>FR-2</strong> — &lt;observable behavior&gt;</li>
</ul>

<h3>7.2 &lt;Capability&gt;</h3>
<ul>
  <li id="fr-3"><strong>FR-3</strong> — &lt;observable behavior&gt;</li>
</ul>
</section>

<section id="s8">
<h2><span class="num">8.</span> Business rules and edge cases</h2>
<p>The decisions an agent cannot guess and will otherwise invent. Be exhaustive here.</p>
<ul>
  <li><strong>Pricing:</strong> &lt;rule&gt;</li>
  <li><strong>Cancellation / refunds:</strong> &lt;rule and window&gt;</li>
  <li><strong>Timezones and hours:</strong> &lt;rule&gt;</li>
  <li><strong>Currency and tax:</strong> &lt;rule&gt;</li>
  <li><strong>Capacity and conflicts:</strong> &lt;what happens when two users want the same
  slot&gt;</li>
  <li><strong>Overrides:</strong> &lt;what the operator can change manually, and what they
  cannot&gt;</li>
</ul>
</section>

<section id="s9">
<h2><span class="num">9.</span> Data the business cares about</h2>
<p>Plain-language entities only — no tables, columns, keys, or types. This doubles as the
glossary: if the business uses a word in a particular way, define it here.</p>
<ul>
  <li><strong>&lt;Entity&gt;</strong> — what it means in this business · what it represents ·
  what must be retained · how long · who can see it · whether it must be exportable.</li>
</ul>
</section>

<section id="s10">
<h2><span class="num">10.</span> Constraints</h2>
<p>Expressed as outcomes, never as technology choices.</p>
<ul>
  <li><strong>Devices and reach:</strong> &lt;e.g. must work on mobile browsers, no app
  install&gt;</li>
  <li><strong>Performance:</strong> &lt;e.g. booking page usable within 3s on a 4G
  connection&gt;</li>
  <li><strong>Availability:</strong> &lt;e.g. can be down for maintenance overnight; must not
  lose a booking&gt;</li>
  <li><strong>Privacy and compliance:</strong> &lt;e.g. we never hold card numbers ourselves;
  personal data deletable on request&gt;</li>
  <li><strong>Operating limits:</strong> &lt;budget ceiling, who maintains it, launch
  date&gt;</li>
</ul>
</section>

<section id="s11">
<h2><span class="num">11.</span> Acceptance criteria</h2>
<p>Definition of done, grouped by journey. Each line must be verifiable by watching the
product — no judgment words.</p>
<h3>&lt;Journey name&gt;</h3>
<ul class="check">
  <li><input type="checkbox" disabled> &lt;criterion&gt;</li>
  <li><input type="checkbox" disabled> &lt;criterion&gt;</li>
</ul>
</section>

<section id="s12">
<h2><span class="num">12.</span> Assumptions and open questions</h2>
<p><strong>Assumptions made</strong> (proceeding on these unless corrected)</p>
<ul>
  <li>&lt;assumption&gt; — affects <a href="#fr-1">FR-1</a></li>
</ul>
<p><strong>Open questions</strong> (need a decision before the affected phase is built)</p>
<ul>
  <li>&lt;question&gt; — blocks <a href="#fr-2">FR-2</a></li>
</ul>
<p><strong>Stated preferences</strong> (not requirements; input to the separate tech
decision)</p>
<ul>
  <li>&lt;e.g. "user has an existing payment account they would prefer to reuse"&gt;</li>
</ul>
</section>

<section id="s13">
<h2><span class="num">13.</span> Delivery phases</h2>
<p>Four to six phases, ordered by dependency. Each ends in something clickable and
verifiable.</p>
<ol>
  <li><strong>&lt;Phase name&gt;</strong> — FR-1 … FR-6. Verifiable when: &lt;what the user
  can do at the end&gt;.</li>
  <li><strong>&lt;Phase name&gt;</strong> — FR-7 … FR-12. Verifiable when: &lt;…&gt;.</li>
</ol>
</section>

</body>
</html>
```

---

## Filling-in notes

**Read it back cold before calling it done.** Re-read the whole thing as a stranger. Two
failure signs: a sentence that only makes sense if you were in the conversation, and a
decision that appears as a requirement without ever being stated as a rule. Both mean
knowledge stayed outside the document.

**Open it in a browser before reporting.** Rendering is the proof the file is well-formed: a
missing `</section>`, an unescaped `<`, or a broken anchor is invisible in the source and
obvious on the page. Check the contents links jump, and that no placeholder angle brackets
survive from this template.

**Section 2 is the orientation, not the spec.** It exists so a reader — human or agent —
knows what is being built before hitting the detail. Keep it to what a user can do. The
moment it names a framework, database, or vendor, it has stopped being a solution summary
and become an architecture note; move that to section 12 as a stated preference.

**Sections 1 and 2 must line up.** Every pain named in section 1 should be visibly answered
in section 2. If a paragraph of section 2 solves nothing in section 1, it is scope creep
appearing before the scope section.

**Section 6 vs section 7.** Journeys are narrative and ordered; requirements are atomic and
referenceable. Both are needed — the journey gives the agent context for micro-decisions,
the requirement gives it something to check off.

**Section 7 ids are load-bearing.** `id="fr-1"` is how a later prompt, a comment, or section
12 points at one requirement precisely. Number them consecutively across the whole document,
not restarting per subsection, and never reuse a number after deleting a requirement.

**Section 8 is the one people skip.** Every rule missing here becomes an invented rule in
the codebase. If the user cannot answer a rule, it belongs in section 12 as an open
question, not silently guessed in section 7.

**Section 10 is where tech-agnosticism is won or lost.** Before writing a line here, check
that it describes what must be true for the business, not what must be installed. The PRD
being an HTML file is a fact about the document, not a decision about the product — nothing
in section 10 may lean on it.

**Section 13 is not a schedule.** No dates, no estimates. It is a dependency order so the
build can be prompted one verifiable chunk at a time.
