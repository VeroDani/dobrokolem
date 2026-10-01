# Eval run · Verifier v4 · 2026-10-01

**Setup:** same 20 records, blind, separate sub-agent. Instructions v4 (status split from completeness – D-011, 5-lookup budget, undated own service page = medium-trust activity).
**Effort:** 7.4 min · 88 tool calls (~76 web lookups, 3.8 per record) · ~139k tokens. Budget exceeded on 2 records (sites blocking automated access).

## Golden set v2
Before scoring, the golden set was relabelled to the D-011 definition: 8 records whose v1 label was `verified_changed` *only* because information was missing are now `verified` with `expected_missing`. Done mechanically from the definition, in a separate commit.
To make sure the improvement isn't just the relabel, v3 was re-scored against the same golden set v2: **6 / 20**.

## Scores (all against golden set v2)
| Measure | v3 | v4 | Pass bar |
| --- | --- | --- | --- |
| Status correct | 6 / 20 | **19 / 20** ✅ | 18 / 20 |
| Key fact detected (incl. expected missing field) | – | **19 / 20** ✅ | 16 / 20 |
| Lookups per record | 7.5 | 3.8 | ≤ 5 |
| Run time | 13.1 min | 7.4 min | – |

**Result: PASS.** Verifier stays at autonomy level 1 until it also shows < 10 % PM corrections on real (non-eval) work for two weeks (D-005).

## Remaining miss
**P7-032 Ty-já-tr → `needs_check` (expected `verified`).** The stale-website rule told it to search praha7.cz, but within the 5-lookup budget it didn't find the Letenský masopust 2026 article. v3 (no budget) found it. Trade-off between cost and recall – watch on real data before changing.

## Things the PM should look at
- P7-065 Sue Ryder, P7-067 Restart Shop: `verified` on an undated shop page (allowed by v4, medium confidence). Spot-check in real work.
- P7-058 Šatník: English site says Hall 19, Czech site Hall 13 – agent chose 13. Correct, but shows sites contradict themselves.
- P7-051: organiser gmail address held back pending privacy check (R-101) – good behaviour.

## Journey so far
| Version | Change | Status score* |
| --- | --- | --- |
| v2 | Source hierarchy | 10 / 20 (golden v1) |
| v3 | + completeness checklist, stale-site rule, R-007 | 12 / 20 (golden v1) · 6 / 20 (golden v2) |
| v4 | Split status from completeness, lookup budget | **19 / 20** (golden v2) |

*Golden v1 and v2 use different definitions of `verified_changed`, so compare within a column, not across.
