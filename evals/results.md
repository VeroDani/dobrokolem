# Eval results

| Date | Agent | Version | Status score | Finding score | Run time | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-01 | (manual baseline) | – | 20 / 20 | 20 / 20 | one evening (71 records) | Answers established by hand – the reference. |
| 2026-10-01 | Verifier | v2 | 10 / 20 | 13 / 20 | 15.4 min | **Fail.** Missing info not flagged; over-strict on trust; found an error in the golden set (P7-061). See `runs/2026-10-01-verifier-v2-analysis.md`. |
| 2026-10-01 | Verifier | v3 | 12 / 20 | 17 / 20 ✅ | 13.1 min | **Fail on status.** Over-corrected: completeness check marks every active record as changed. Root cause: `status` mixes "correct?" and "complete?". See `runs/2026-10-01-verifier-v3-analysis.md`. |
| 2026-10-01 | Verifier | v4 | **19 / 20** ✅ | **19 / 20** ✅ | 7.4 min | **Pass** (golden set v2, D-011). Half the lookups of v3. One miss: Ty-já-tr (budget vs recall). v3 re-scored on golden v2: 6/20. See `runs/2026-10-01-verifier-v4-analysis.md`. |
