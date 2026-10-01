# Playbook

Rules learned from real work and human corrections. Every agent reads this file before acting. Each rule has an ID, the date it was added, and the case it came from – so we can see *why* it exists and remove it if it stops being useful.

The chief-of-staff agent proposes new rules; the PM approves them.

---

## Data and verification

**R-001 · 2026-10-01 · A Facebook page alone is not proof that an organisation is active.**
Case: 10 Facebook groups in the Prague 7 guide could not be verified automatically. Status for these is `needs_check` until a human or the organisation confirms.

**R-002 · 2026-10-01 · Record where the organisation *operates*, not only its registered seat.**
Case: MetroFarm has its legal seat in Praha 4 but its garden on Císařský ostrov (Prague 7). MigAct is registered in Praha 1 but runs a project in Prague 7.

**R-003 · 2026-10-01 · Directories and aggregators (Firmy.cz, GoOut, Mapotic) are weak sources; prefer the organisation's own website or the official register.**
Case: GoOut and an older Mapotic map still list Přístav 7 at the old address Jankovcova 8b; the operator's own site shows V Přístavu 1639/24.

**R-004 · 2026-10-01 · When two official sources disagree, flag the conflict instead of picking one.**
Case: the municipality's website lists the neighbourhood-groups coordinator as Michaela Šormová on one page and Michaela Panko on others (same phone number). Report both, with URLs, and ask the PM.

**R-005 · 2026-10-01 · Placeholder text is a finding.**
Case: the guide contained "xxx", "www.xxx.cz", "(doplnit příběh)", "str. X". Report every placeholder as an issue to fix.

**R-006 · 2026-10-01 · Text copied from another locality must be flagged.**
Case: the language-courses paragraph in the Prague 7 guide was copied from the Prague 3 guide ("Na Praze 3 a v blízkém okolí…").

## Privacy

**R-101 · 2026-10-01 · Never publish private phone numbers or e-mails of individuals.**
Informal groups are often run by private people. Use a group contact or a contact form; publish a personal contact only with documented consent.

**R-102 · 2026-10-01 · Do not scrape social networks.**
Facebook and Instagram are checked manually or the organisation is asked directly.

## Communication with organisations

**R-201 · 2026-10-01 · Write to organisations in Czech, personally, one organisation per e-mail.**
No BCC mass mailings. Address the organisation by name and show the exact data we hold about them.

**R-202 · 2026-10-01 · Make replying effortless.**
Every request offers three one-word answers: "platí" (still valid) / correction / "už nepůsobíme" (no longer active).

**R-203 · 2026-10-01 · New domain: send at most 15–20 e-mails per day in the first week.**
Protects deliverability of dobrokolem.cz.
