# Run · Verifier v4 · 2026-10-02 · first production run

**Scope:** the 51 Prague 7 records not in the golden set. Blind to the manual results of 2026-10-01.
**Setup:** 3 parallel sub-agents × 17 records, instructions v4, playbook as of 2026-10-01.
**Effort:** 37 min wall-clock (parallel) · ~190 distinct web lookups (agents reported 204; batch 2 double-counted shared lookups) · ~412k tokens.

## Output (pending PM approval)
| Status | Agent | Manual check (2026-10-01) |
| --- | --- | --- |
| verified | 11 | 0 |
| verified_changed | 2 | 12 |
| needs_check | 38 | 39 |

The manual column used the pre-D-011 definition (missing info = changed), so compare *live* (verified + verified_changed): **agent 13, manual 12.**
They disagree on 11 records: the agent found activity the manual check missed on 6 (municipal channels, school parent associations, book booths), and was stricter on 5 (sites blocking automated access; annual event whose 2026 edition it didn't find; MigAct – likely an agent miss).

## What this run taught us
1. **The bottleneck moved from reasoning to access.** 38 / 51 stayed `needs_check`, mostly because sites block automated reading (Elpida, rcletna.cz, sokol-bubenec.cz…) or the record is a Facebook-only group (14 records). More prompt rules won't fix that – outreach to organisations will.
2. **Agents surfaced risks humans missed:** private mobile numbers printed in the guide and on the municipality's site, a politically sensitive group, private persons on the map without consent.
3. **Instruction bug found by the agents themselves:** step 6 (undated service page = medium trust) conflicts with the decision rule (verified needs high trust). Two batches flagged it independently.

## Files
- `input-batch{1,2,3}.csv` – what the agents saw
- `output-batch{1,2,3}.csv` – raw agent output
- `review-queue.xlsx` – PM queue, pre-reviewed by the chief of staff (priorities A–D, notes, 4 rule proposals); PM decisions go here
- `build_queue.py` – how the queue was built
