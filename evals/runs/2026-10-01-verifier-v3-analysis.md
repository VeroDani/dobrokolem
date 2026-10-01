# Eval run · Verifier v3 · 2026-10-01

**Setup:** same 20 golden-set records, blind, separate sub-agent. Instructions v3 (completeness checklist, stale-website rule, R-007).
**Effort:** 13.1 min · 158 tool calls (~150 web lookups, 7.5 per record – 2.3× more than v2) · ~204k tokens.

## Scores
| Measure | v2 | v3 | Pass bar |
| --- | --- | --- | --- |
| Status correct | 10 / 20 (11 after golden fix: 12) | **12 / 20** | 18 / 20 |
| Key fact detected | 13 / 20 | **17 / 20** ✅ | 16 / 20 |
| Lookups per record | 3.3 | 7.5 | – |

**Result: FAIL on status, PASS on findings.**

## What happened: we over-corrected
The completeness checklist fixed every v2 miss (MetroFarm, Vodárenská věž, STO•RE, Brontosaurus, Ty-já-tr all correct now) – but **no record is `verified` any more**. Guide entries are short; almost every one lacks an operator, opening hours or a contact. So the agent followed the instructions correctly and marked all 14 active records `verified_changed`.

The stale-website rule also made it stricter in three places (Šatník, Restart Shop, Nábytková banka → `needs_check`), at 2.3× the cost.

## Root cause: one field answers two questions
`status` currently mixes:
1. **Is it alive and is what we say correct?** (trust question – matters to citizens)
2. **Is the record complete?** (enrichment question – matters to us)

A record can be alive, correct *and* incomplete. Forcing both into one value means any choice of rule fails one of the two.

## Proposed change for v4 (needs PM approval)
Split the output into two fields:
- `status`: `verified` (alive, nothing we state is wrong) · `verified_changed` (alive, something we state is **wrong**) · `needs_check` · `closed` · `outside_area`
- `missing_fields`: list from the completeness checklist (operator, P7 location, contact, how to join, hours, organiser)

Also:
- Stale-website rule: an undated but working shop / service page on the organisation's own site counts as medium-trust evidence of activity.
- Budget: max 5 lookups per record; stop when the decision rule is met.

Re-scored with this split, v3's findings would give an estimated 17–18 / 20 – to be confirmed by a real v4 run.
