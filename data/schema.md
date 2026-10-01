# Data model

One record = one actor (organisation, community group, informal group, community place, recurring event). Needs (volunteers, items, space) and events are separate tables linked to a record.

Values are in Czech (the product language); field names are in English.

## `records`
| Field | Type | Filled by | Notes |
| --- | --- | --- | --- |
| `id` | text | system | `P7-001` … stable ID |
| `name` | text | source / organisation | |
| `type` | single select | agent proposes, PM approves | NGO, spolek, informal group, community place, municipal programme, social enterprise, charity shop, event, online group |
| `ico` | text | source | Czech company ID; empty for informal groups; key for matching with the register |
| `categories` | multi select | agent proposes | Sousedství, Komunitní místa, Zahrady a zeleň, Děti a rodiny, Mládež, Senioři, Migrace a inkluze, Sociální pomoc, Re-use a cirkularita, Jídlo, Kultura, Sport, Vzdělávání, Dobrovolnictví, Životní prostředí, Info kanály |
| `description_cs` | text ≤ 280 chars | agent proposes, organisation approves | |
| `how_to_join_cs` | text | organisation | volunteering, membership, donations |
| `location` | text | source | where it **operates**, not only the registered seat (playbook R-002) |
| `lat`, `lng` | number | system (geocoding) | |
| `area` | single select | system | Holešovice, Letná, Bubeneč, Troja; later: municipality |
| `website`, `facebook`, `instagram` | URL | source / organisation | |
| `contact_email` | e-mail | organisation | **private**, used only for update requests; never in this repo |
| `public_contact` | text | organisation | only with consent |
| `status` | single select | Verifier / PM | verified, verified_changed, needs_check, closed, outside_area |
| `verified_on` | date | system | last confirmation by organisation or PM |
| `freshness_score` | 0–100 | system | see below |
| `gdpr_consent` | yes/no + date | organisation | required for informal groups |
| `sources` | list | system | where the record came from |

## Freshness score
Starts at 100 on every confirmation and decreases:
| Signal | Effect |
| --- | --- |
| Each month since last verification | −3 |
| Website down twice in a row | −30 |
| Register shows liquidation | set to 0, escalate |
| No reply 30 days after a request | −20 |
| New event or need posted by the organisation | +15 (max 100) |
| Confirmation by organisation or PM | reset to 100 |

Displayed: 60–100 active · 30–59 unverified (shown with a label and date) · < 30 archived (hidden).

## Linked tables
- `needs` – type (volunteers, items, space, partners), description, valid until.
- `events` – date, place, link.
- `changes` – who, when, what, source. Audit trail and training data for the learning loop.
