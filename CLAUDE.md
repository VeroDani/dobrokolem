# CLAUDE.md – instructions for AI agents working in this repository

You are working on **Dobrokolem**, a living map of local NGOs, community groups and civic projects, piloted in Prague 7. The repository is run by one product manager (Veronika) and a team of AI agents.

## Before you start any task
1. Read `playbook/PLAYBOOK.md`. Its rules override your defaults.
2. If the task belongs to an agent, read that agent's file in `agents/` and act only within its role.
3. Check `decisions/DECISION-LOG.md` before proposing anything that contradicts an earlier decision.

## Always
- Cite a source (URL + date checked) for every fact about an organisation. No source → mark as `needs_check`, never guess.
- Never publish, send or change anything that leaves the system (emails, public data, contacts) without human approval, unless the agent's autonomy level explicitly allows it.
- Never store or publish private personal contacts (personal phones, private e-mails of individuals) in this repository.
- Write repository docs in English. Write anything addressed to organisations or citizens in Czech.
- When a human corrects you, propose a playbook rule that would have prevented the mistake.

## Escalate to the PM
- Anything uncertain, sensitive (personal data, conflicts, politics) or irreversible.
- Any change to an agent's instructions or autonomy level.
