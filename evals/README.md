# Evals

An eval is a test with known answers. We run it every time an agent's instructions change, so we can see whether the change made the agent better or worse – instead of guessing.

## `verifier-golden-set.csv`
20 records from Prague 7 whose correct status was established by hand on 2026-10-01.

| Column | Meaning |
| --- | --- |
| `id` | Record ID in `data/p7-records-2026-10-01.csv` |
| `name` | Organisation |
| `expected_status` | The correct status |
| `key_fact_to_detect` | The one finding a good verifier must report |

**How to run (manual, weeks 1–2):**
1. Give the Verifier the 20 records (without the expected answers).
2. Compare its `status` with `expected_status` → status score (x / 20).
3. Check whether its `finding_cs` mentions the key fact → finding score (x / 20).
4. Record both scores, the date and the instruction version in `results.md`.

**Pass:** status ≥ 18 / 20 and finding ≥ 16 / 20.

**Note:** the real world changes. Re-check the golden set every 3 months and log any updated answers.

From week 4 the run is automated (n8n) and the chief of staff reports before / after scores.
