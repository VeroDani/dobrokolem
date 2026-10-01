# Decision log

Each decision: what we decided, why, what we rejected, and when to revisit. Newest first.

---

## D-009 · 2026-10-01 · Source hierarchy for the Verifier; dobrovolnik.cz as partner, not competitor
**Decision:** The Verifier weighs sources by what they actually prove (existence vs. activity). Added dobrovolnik.cz, the municipal grants list and fundraising platforms as activity signals; GlobalGiving Atlas and Mapa neziskovek as existence-only sources (useful for the Scout to find candidates).
**Why:** A register entry proves an organisation exists, not that it is active – the most likely wrong conclusion for an agent.
**Competitive note:** dobrovolnik.cz (HESTIA + dobrokruh) already serves part of use case 1 nationally. Our edge is local depth, informal groups and organisation-to-organisation connections. Treat them as a potential partner (link to their calls, offer our verified local data).
**Check before reuse:** licence of GlobalGiving Atlas data before storing it in this public repository.

## D-008 · 2026-10-01 · Three north stars: product, agent system, builder
**Decision:**
- Product: **live records** (verified, updated or added in the last 90 days), split by who confirmed them. Guardrail: contact clicks on the website.
- Agent system: **live records per hour of PM time**.
- Builder: **shipped & documented increments per week**.

**Why:**
- The core problem is stale data, so the product north star measures freshness directly. A stock ("how many records are live now") rather than a flow ("how many updates") cannot be inflated by repeated edits and decays naturally.
- A perfectly fresh database nobody uses would be worthless, so contact clicks act as the guardrail. They cover both use cases: a click can come from a citizen or from a staff member of another NGO looking for a partner or a place to send a volunteer – we don't need to tell them apart.
- Agent metrics measure leverage, not activity, so they don't double-count the product metric.

**Rejected:**
- "Connections made" (citizen ↔ organisation and organisation ↔ organisation) – the organisation-to-organisation part cannot be measured reliably, and the metric would sit at zero until the website launches in week 5.
- Number of updates – easy to inflate.
- Quarterly survey of organisations about partnerships – redundant, contact clicks already capture NGO staff using the site.

**Revisit:** after the pilot (week 8), when we have real usage data.

## D-007 · 2026-10-01 · Repository in English, product in Czech
**Decision:** Docs, agent instructions and code comments in English; data, UI and all communication with organisations in Czech.
**Why:** The repository doubles as a portfolio for international AI companies; users are Czech.
**Rejected:** Czech-only repo (limits portfolio reach).

## D-006 · 2026-10-01 · Start with 3 agents, grow to 8
**Decision:** Weeks 1–2 run only Verifier, Outreach writer and Chief of staff. New agents are added only after a task has been done manually three times.
**Why:** Each agent needs instructions, an eval set and review time. Too many at once = no real quality control.
**Rejected:** Launching all 8 agents in week 1.

## D-005 · 2026-10-01 · Agents earn autonomy through measured performance
**Decision:** Three autonomy levels (1 = everything reviewed, 2 = sample reviewed, 3 = exceptions only). Promotion requires < 10 % correction rate for two weeks and passing the golden set. Only the PM approves promotions.
**Why:** Trust must be earned and measurable; this is also the core skill to demonstrate as an AI PM.

## D-004 · 2026-10-01 · Airtable first, Supabase later
**Decision:** Start the database in Airtable.
**Why:** The PM is learning the technical side; Airtable gives forms, views and a review queue without code. Migrate to Supabase when we need geo-queries and a public API.
**Revisit:** Week 5 (public website).

## D-003 · 2026-10-01 · Domains: dobrokolem.cz (platform) + sousedskypruvodce.cz (methodology / brand protection)
**Why:** "Dobrokolem" ("good around you") covers NGOs, groups and projects, not only neighbourhood life; easy to say aloud. "Sousedský průvodce" is an existing brand used by six localities – kept as the name of printed/PDF outputs generated from the database.
**Rejected:** mapadobra.cz (taken, used by Linka bezpečí), dobroprojekt.cz ("project" sounds temporary), zivesousedstvi.cz (too narrow).
**Owner of domains:** should be Nadační fond Agora 7, not a private person.

## D-002 · 2026-10-01 · Build a living database, not a new directory silo
**Decision:** One verified database that other platforms (municipality website, Mapotic, Praha lidem) can embed or consume.
**Why:** Prague already has several partial lists; adding another silo would make the problem worse.

## D-001 · 2026-10-01 · Pilot in Prague 7, measure organisation response rate first
**Decision:** The key pilot metric is the share of organisations that confirm or correct their record within 30 days of being asked.
**Why:** If organisations don't respond, no technology will keep the data alive. ≥ 40 % → scale; < 20 % → fix incentives first.
