# Dobrokolem

**A living map of local good: NGOs, community groups and civic projects that stay up to date – maintained by the organisations themselves, with a team of AI agents doing the routine work.**

Pilot: Prague 7, Czech Republic · Started: October 2026 · Built by one product manager and a team of AI agents.

---

## The problem

People want to help, and local organisations need volunteers, partners and space. But the information that connects them goes stale fast.

In Prague 7, the main overview was the *Sousedský průvodce Prahou 7* (Neighbourhood Guide to Prague 7), a printed / PDF guide published by Dobrovolnické centrum Agora 7. When we checked its 71 local entries on 1 October 2026:

| Status | Entries |
| --- | --- |
| Still correct | 6 |
| Exists, but details changed | 23 |
| Could not be verified online | 40 |
| Closed | 1 |
| Outside the area | 1 |

Only **8 %** of entries were fully correct. This is the normal fate of directories: they die when the grant that funded them ends, because nobody has a reason or the capacity to keep them current.

## Two users

1. **A citizen:** "I have two hours a week and I speak English. Where near me can I help, and who do I contact?"
2. **An organisation:** "Who else works near us? Who could we partner with? Where can we send a volunteer we can't use right now?"

## The approach

- **One database, two incentives.** Organisations keep their profile current because it brings them volunteers and partners. Citizens use it because it is current.
- **AI agents do the routine work** – checking whether organisations still exist, drafting outreach, processing replies, finding new groups – under human review.
- **A chief-of-staff agent** coordinates the other agents and learns from every correction the product manager makes.
- **Trust is earned, not assumed.** Every agent starts at autonomy level 1 (everything reviewed) and earns more autonomy only by performing on a fixed evaluation set.

See [docs/operating-model.md](docs/operating-model.md).

## Repository structure

| Folder | What's inside |
| --- | --- |
| `agents/` | One instruction file per agent: role, inputs, outputs, quality bar, escalation rules |
| `playbook/` | Rules learned from human corrections – the shared memory of the team |
| `evals/` | Golden sets with known answers, used to test every agent change |
| `decisions/` | Decision log: what was decided, why, and what was rejected |
| `data/` | Data model and anonymised snapshots (no personal contacts) |
| `build-log/` | Weekly build notes – the raw material for the case study |
| `docs/` | Operating model and product documents |

## Metrics: three layers, three north stars

| Layer | North star | Why this one | Guardrails & supporting metrics |
| --- | --- | --- | --- |
| **Product** | **Live records** – organisations verified, updated or newly added in the last 90 days, split by who confirmed them (organisation / agent / PM) | Measures the core problem (data going stale). Moves from week 1, can't be inflated by repeated edits, decays on its own like reality does. | **Contact clicks** and filter use – proof that live data is actually used, by citizens *and* by staff of other NGOs looking for partners or a place to send a volunteer. Searches with no result – what people want and can't find. |
| **Agent system** | **Live records per hour of PM time** | Measures the leverage the system gives one person – not how busy the agents are. | Golden-set score ≥ 18/20 · zero errors that reached the outside world · correction rate < 10 % · cost per record (CZK) |
| **Builder (me)** | **Shipped & documented increments per week** – counts only if it runs, I can explain it, and it's logged | Measures how fast I learn to build, and fills the portfolio as a side effect. | Skills map (from "with help" to "on my own") · monthly solo build test · one public post per week |

**Pilot targets (8 weeks)**

| Metric | Baseline (2026-10-01) | Target |
| --- | --- | --- |
| Share of live records | 41 % (29 / 71) | 80 % |
| Live records confirmed by the organisation itself | 0 % | 40 % |
| New actors outside environmental topics | 0 | 30+ |
| Live records per hour of PM time | ~30 (manual, AI-assisted) | 60+ |

Website analytics are cookieless (Plausible or Umami) – no consent banner, privacy by design.

## Status

| Week | Focus | Status |
| --- | --- | --- |
| 1 | Foundations: repo, playbook, first agents, database | In progress |
| 2 | Verifier + Outreach agents with human review, first evals | Planned |
| 3 | Chief of staff: daily brief, learning loop | Planned |
| 4 | Automation (n8n), Scout agent | Planned |
| 5–6 | Public website: citizen search, organisation profiles | Planned |
| 7–8 | Metrics, evaluation of the pilot, case study | Planned |

## Language

Repository documentation is in English. The product, the data and all communication with organisations are in Czech.

## Credits

Builds on the *Sousedský průvodce* methodology by Dobrovolnické centrum Agora 7 (Nadační fond Agora 7), supported by Nadace OSF (Active Citizens Fund), the Czech Ministry for Regional Development and Nadace Via.
