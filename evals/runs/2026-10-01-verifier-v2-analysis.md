# Eval run · Verifier v2 · 2026-10-01

**Setup:** 20 golden-set records, blind (agent saw only id, name, guide chapter and the guide text). Run as a separate sub-agent with web search.
**Effort:** 15.4 min wall-clock · 76 tool calls (~66 web lookups, 3.3 per record) · ~130k tokens.

## Scores
| Measure | Score | Pass bar |
| --- | --- | --- |
| Status correct | **10 / 20** | 18 / 20 |
| Key fact detected | **13 / 20** | 16 / 20 |
| Errors that would reach the outside world | 0 (level 1, nothing sent) | 0 |

**Result: FAIL.** Expected for a first run – the point is to learn where the instructions are weak.

## Failure patterns
| # | Pattern | Records | Root cause |
| --- | --- | --- | --- |
| A | **Missing ≠ changed.** Marked `verified` when the guide was correct but incomplete (missing operator, P7 location, opening hours, clubhouse address). | P7-007, -009, -018, -059, -067 | Instructions say "wrong *or missing*" but the agent only compared what the guide states. No checklist of fields to look for. |
| B | **Over-strict on trust.** Real activity found only in medium-trust sources → `needs_check`. | P7-051 (flea market, Facebook only), -069 | Decision rule demands a high-trust source; organisations without a website can never be `verified`. |
| C | **Stopped searching too early.** Concluded "no activity since 2024" from the own website, missed praha7.cz / NZM pages about Letenský masopust in Jan 2026. | P7-032 | Hierarchy lists praha7.cz but the agent wasn't told to search it when the own site looks stale. |
| D | **Escalated a known conflict.** Applied R-004 correctly; the golden answer assumed the PM had already resolved it. | P7-029 | Golden set and playbook disagree – see below. |

## The agent was right and the golden set was wrong
**P7-061 Oděvní banka:** its own website (modified 11 Jun 2026) states it has become an independent NGO, no longer a project of Klub svobodných matek. The manual baseline missed this. → Golden set needs correcting; corrected status score would be **11 / 20**.

## Proposed changes (need PM approval)
1. **Verifier v3 – completeness checklist (fixes A):** for every record, check that these are present: operator, location in P7, public contact, how to get involved, opening hours (places), dates (events). Any missing → `verified_changed`.
2. **Verifier v3 – "stale own site" rule (fixes C):** if the own website shows nothing dated in 12 months, always search praha7.cz and `"<name>" 2026` before concluding.
3. **Playbook R-007 (fixes B):** for informal groups and recurring events without a website, two independent medium-trust sources showing activity in the last 12 months are enough for `verified` with `confidence: medium`.
4. **Golden set:** correct P7-061 (`verified_changed`, "now independent NGO"). For P7-029 accept `needs_check` + escalation as correct, because R-004 requires it.

## Baseline for the agent north star
Manual (PM + AI chat): ~71 records per evening ≈ 25–35 records/hour of PM time.
Agent run: 20 records in 15 min of agent time; PM review of this output ≈ 15 min → ~80 records/hour of PM time *if* quality passed. Quality did not pass yet, so this number doesn't count.
