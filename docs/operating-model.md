# Operating model

One product manager, one chief-of-staff agent, and eight specialised agents in four teams.

```
                Veronika (PM) – goals, priorities, approvals
                              │
              Chief of staff – routes, reviews, learns
                              │
   ┌──────────────┬───────────┴───────┬──────────────────┐
  DATA       COMMUNICATION          BUILD              STORY
  Scout        Outreach writer      Builder            Chronicler
  Verifier     Inbox triage         Tester             Analyst
```

## Five rules
1. **An agent is created only after a task has been done manually three times.** First do it with Claude, then write it down, then give it to an agent.
2. **Every agent has one instruction file** (`agents/`): purpose, input, output, quality bar, escalation.
3. **Nothing leaves the system without PM approval** until the agent has proven itself on the eval set.
4. **Every correction is logged.** Corrections teach the agents and the chief of staff – and they are the most valuable data for the case study.
5. **Cost and benefit are measured.** Cost per verified record, PM hours saved, correction rate.

## Agents
| Agent | Team | Starts | Does |
| --- | --- | --- | --- |
| Chief of staff | – | week 1 | Daily brief, review against playbook, evening learning loop, autonomy proposals |
| Verifier | Data | week 1 | Checks whether organisations still exist and what changed |
| Outreach writer | Communication | week 1 | Personal Czech e-mails asking organisations to confirm their data |
| Inbox triage | Communication | week 3 | Reads replies, proposes record updates |
| Scout | Data | week 4 | Finds missing actors in registers, municipality sites, community maps |
| Builder | Build | week 5 | Builds website, map, forms (Claude Code) |
| Tester | Build | week 5 | Tests the site as a citizen and as an organisation; runs evals |
| Analyst | Story | week 7 | Weekly metrics report |
| Chronicler | Story | week 1 (light) | Weekly build notes, posts, case study drafts |

## Autonomy levels
| Level | PM reviews | Promotion condition |
| --- | --- | --- |
| 1 | Every output | – (start here) |
| 2 | 20 % random sample | < 10 % corrections for 2 weeks + eval passed |
| 3 | Exceptions only | Level 2 stable for 4 weeks; never for anything sent to people outside |

## Tools
Claude (Max plan, Claude Code) · Airtable · n8n Cloud · Claude API · Google Workspace / e-mail on dobrokolem.cz · GitHub · Vercel or Netlify.

## Metrics
Three layers, each with one north star – see the Metrics section of the [README](../README.md) and decision D-008.

| Layer | North star |
| --- | --- |
| Product | Live records (verified, updated or added in the last 90 days) – guardrail: contact clicks |
| Agent system | Live records per hour of PM time |
| Builder | Shipped & documented increments per week |
