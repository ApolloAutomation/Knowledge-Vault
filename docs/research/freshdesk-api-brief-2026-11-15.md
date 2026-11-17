FRESHDESK API v2 RESEARCH BRIEF (checked against the web on 2026-11-15)

Sources and confidence. Main source: developers.freshdesk.com/api, which I read in full in three passes. Other sources: Freshdesk support articles and the Hookdeck, eesel and Macha guides. Each claim carries one of these tags:
- [OFFICIAL]: Freshdesk or Freshworks documentation.
- [3P]: a third-party guide.
- [UNVERIFIED]: conflicting or only partly sourced.

== 1. AUTHENTICATION ==
- Basic auth. The username is the API key and the password can be anything (`curl -u APIKEY:X`). HTTPS only. A 401 means the Authorization header is missing or wrong; forgetting to Base64-encode it is a common cause. [OFFICIAL]
- Base URL: https://<domain>.freshdesk.com/api/v2/...
- Where to find the key: profile picture (top right) > Profile Settings > API key in the right pane. A captcha may appear before the key is shown. [OFFICIAL; captcha 3P]
- Every agent has their own key. The Sprout (free) plan has no API access. [OFFICIAL]
- Regenerating the key invalidates the old one and breaks every integration still using it. [3P citing Freshworks]
- Permissions: the key acts as that agent, so it gets the agent's role, group and ticket-scope permissions. [3P; it matches how the docs list endpoint scopes such as `freshdesk.tickets.view`, but no official sentence says it directly]
- Admin-only endpoints exist, for example `/api/v2/admin/ticket_fields`. [OFFICIAL]
- Recommendation: create a dedicated agent such as "AI Assistant" with a custom role and global ticket scope. It needs:
  - view tickets
  - reply
  - add notes
  - edit tags and fields
  - no delete and no admin rights
  This makes the bot's replies and notes clearly attributed, lets you revoke the key without touching a human's account, and keeps human agents' keys out of the bot. A bot agent usually takes up a paid seat; check whether your plan offers an occasional or day-pass option. [Seat cost UNVERIFIED]

== 2. LISTING AND EXPORTING TICKETS ==
List: GET /api/v2/tickets [OFFICIAL]
- By default it returns only tickets created in the last 30 days. Use `updated_since=YYYY-MM-DDTHH:MM:SSZ` to reach older ones.
- Filters:
  - Predefined: `filter=new_and_my_open|watching|spam|deleted`
  - By field: `requester_id`, `email`, `unique_external_id`, `company_id`
- Sorting: `order_by=created_at|due_by|updated_at|status`; `order_type=asc|desc` (default `desc`).
- `include=stats,requester,description`. Each include costs extra credits. The docs disagree on whether that is 1 or 2 per include.
  - Without `include=description`, the list does not return the ticket body.
- Pagination:
  - `page` starts at 1. `per_page` defaults to 30, maximum 100; anything above 100 is an error.
  - The `link` response header holds the next page URL and is absent on the last page.
  - Hard cap of 300 pages (30,000 tickets at 100 per page) per query. The docs also advise against going past page 500 for performance.
  - Workaround for big histories: walk time windows. Use `order_by=updated_at&order_type=asc` and move `updated_since` forward from the last record seen.
- Archived tickets: closed tickets inactive for about 120 days (depends on traffic) are archived and drop out of list and search. [OFFICIAL]
  - Read them with GET /api/v2/tickets/archived/{id} and GET /api/v2/tickets/archived/{id}/conversations.
  - There is no "list archived" endpoint in the docs, so you need the IDs from somewhere else (for example an account export). [Absence of a list endpoint: my reading]

Filter/search: GET /api/v2/search/tickets?query="..." [OFFICIAL]
- The query must be URL-encoded, wrapped in double quotes, and at most 512 characters.
- Fixed 30 results per page, at most 10 pages, so 300 results per query.
- Field names are case-sensitive. Supports AND, OR and parentheses; `:>` and `:<` work on dates and numbers; `null` matches empty fields.
- Excludes archived tickets.
- Good for "find tickets with tag X". Not suitable for bulk export.

Bulk historical export options:
a) API crawl as above. Best for structured question-and-answer extraction.
b) Admin > Account export (history at "Admin > Accounts exports"). This is the official route to full conversations and archived tickets; the "All tickets" view export explicitly leaves out conversations and archived tickets. [OFFICIAL]
   - Older Freshdesk account exports were delivered as XML, with an emailed link. [UNVERIFIED for the current Omni UI]
c) Scheduled exports: Reports (or Analytics) > Schedule Export. [OFFICIAL]
   - Frequency: hourly, daily or weekly.
   - Delivery: CSV by email or API link; ticket activities come as JSON.
   - Account admin only.
   - Ticket properties only, no conversation bodies, so useful for metadata only.

== 3. CONVERSATIONS ==
- GET /api/v2/tickets/{id}/conversations [OFFICIAL]
  - Paginated with `?page=N`, 30 per page by default.
  - Scopes: freshdesk.conversations.view and freshdesk.tickets.view.
- The ticket's FIRST message is NOT a conversation entry. It is the ticket's `description` (HTML) and `description_text` fields.
- GET /api/v2/tickets/{id}?include=conversations returns at most 10 conversations, oldest first, and costs 2 API calls. Use the conversations endpoint for complete threads. [OFFICIAL]
- Conversation fields [OFFICIAL]:
  - id, ticket_id, user_id
  - body (HTML), body_text (plain text), structured_body
  - incoming, private, source
  - support_email, from_email, to_emails, cc_emails, bcc_emails
  - attachments
  - created_at, updated_at, last_edited_at, last_edited_user_id
- Telling customer messages from agent messages:
  - `incoming=true` means it came from outside (the customer's email reply).
  - `private=true` means an internal note. Exclude these from customer-facing Q&A, but they are valuable as internal knowledge.
  - Public reply from an agent: `incoming=false`, `private=false`.
  - Most reliable: compare `user_id` against the ticket's `requester_id`, and/or check `user_id` against the agents list (GET /api/v2/agents).
  - Conversation `source` codes (from my knowledge of the docs; the reading did not cover them) [UNVERIFIED]: 0 reply, 2 note, 5 tweet, 6 survey, 7 Facebook, 8 forwarded email, 9 phone, 10 mobihelp, 11 e-commerce.
- body vs body_text: body is HTML with quoted history and signatures; body_text is the plain-text version. For training data, use body_text and strip quoted reply chains and signatures yourself; Freshdesk does not do this reliably. [Stripping advice: my inference]
- Ticket enum codes [OFFICIAL]:
  - status: 2 Open, 3 Pending, 4 Resolved, 5 Closed
  - priority: 1 Low, 2 Medium, 3 High, 4 Urgent
  - ticket source: 1 Email, 2 Portal, 3 Phone, 7 Chat, 9 Feedback Widget, 10 Outbound Email

== 4. WRITING ==
- Reply: POST /api/v2/tickets/{id}/reply [OFFICIAL]
  - `body` (HTML) is required. Optional: `from_email` (defaults to the global support email), `user_id` (post as a specific agent, such as the bot agent), `cc_emails`, `bcc_emails`, `attachments`. Attachments need multipart/form-data and the total per ticket is 20 MB.
  - A reply is a public message and is emailed to the requester (and CCs) through the ticket's channel. That is normal helpdesk behaviour, though the docs page does not state it in one sentence. There is no "draft reply" API, so a draft-for-human-review flow has to use private notes. [Email behaviour: standard, and implied]
- Note: POST /api/v2/tickets/{id}/notes [OFFICIAL]
  - `body` is required.
  - `private` defaults to TRUE ("By default, any note that you add will be private").
  - `incoming` defaults to false.
  - `notify_emails` is an array of agent emails to notify. `user_id` and `attachments` are optional.
  - A private note is NOT sent to the customer. This is the safe channel for an AI draft or suggested reply. A human copies the text, or a tag or custom field triggers the next step.
- Update a note: PUT /api/v2/conversations/{id}. Only `body` and `attachments` can change, and only on notes. Delete: DELETE /api/v2/conversations/{id}.
- Update ticket: PUT /api/v2/tickets/{id} with `status`, `priority`, `tags` (array; it REPLACES the existing tags, so read, merge, then write), `custom_fields` (object keyed by the field's API name, such as `cf_ai_confidence`), `responder_id`, `group_id`, `type`. [OFFICIAL; tag-replace behaviour from my knowledge, UNVERIFIED in this reading]
- Bulk update: POST /api/v2/tickets/bulk_update returns a job_id. [OFFICIAL]
- Discover custom fields: GET /api/v2/ticket_fields (agent-level). Creating fields needs the admin endpoints under /api/v2/admin/ticket_fields, or the UI. [OFFICIAL]
- Forward: POST /api/v2/tickets/{id}/forward. Also reply_to_forward. [OFFICIAL]

== 5. REAL-TIME TRIGGERS (WEBHOOKS) ==
- Path: Admin > Workflows > Automations. In Freshdesk Omni it is Admin Settings > Configuration and Workflows > Ticket Automations. Use the "Ticket Creation" tab (and "Ticket Updates" for customer replies), then New Rule > conditions > action "Trigger Webhook". [3P Hookdeck citing Freshdesk docs]
- Plans: Trigger Webhook on Growth, Pro and Enterprise. The separate "Trigger API" action, which can read the response back into the ticket, is Pro and above. [3P]
- Method: GET, POST, PUT, PATCH or DELETE. Encoding: JSON, XML or XML-encoded. Body: "Simple" (tick the ticket properties to send) or "Advanced" (custom JSON). [3P]
- Placeholders: Liquid-style, e.g. `{{ticket.id}}`, `{{ticket.subject}}`, `{{ticket.description}}`, `{{ticket.requester.email}}`, `{{ticket.requester.name}}`, `{{ticket.tags}}`, `{{ticket.latest_public_comment}}`, `{{Triggered event}}`.
  - In JSON bodies, string placeholders must be quoted.
  - Best practice: send only `{{ticket.id}}` (plus an event name) and fetch fresh data over the API. That avoids HTML or quote escaping breaking the JSON. [Placeholder list partly from my knowledge; best practice 3P]
- Auth options: custom headers (one `Name: value` per line; spaces can stop the trigger from running) or the "Requires authentication" toggle (API key or username/password; how it is sent is not well documented).
  - Recommended: a shared-secret custom header such as `X-Webhook-Secret`, checked by your endpoint. [3P]
  - Freshdesk does NOT sign webhooks (no HMAC). [3P]
- Retries [3P, Hookdeck citing Freshdesk; UNVERIFIED against the primary doc]:
  - Any 2xx is success. 3xx redirects are followed. Anything else fails.
  - A failure is retried once every 30 minutes, 48 attempts in total (about 24 hours). Admins get a failure email.
  - Your endpoint should return 2xx fast and do the work asynchronously.
  - Make processing idempotent, keyed on ticket id plus event, because retries can deliver duplicates.
- Webhook rate limit: 1,000 webhook calls per hour per account. Extra calls are buffered and delayed, not dropped. [3P]
  - One source says webhook calls also count against the API rate limit. [UNVERIFIED]
- Loop prevention: add a rule condition such as "Tags does not contain ai-processed", and have the bot set that tag. Also make sure the bot's own reply does not fire a "Ticket Updates" rule. [My recommendation]
- Alternative to webhooks: poll GET /api/v2/tickets?updated_since=... every 1–2 minutes. Simpler, needs no public endpoint, and the latency is acceptable for email support.

== 6. RATE LIMITS ==
- Account-wide, per minute, shared by ALL integrations and apps on the account. Invalid requests count too. Exceeding the limit returns HTTP 429. [OFFICIAL]
- Current plans [OFFICIAL table and support article 225439]:

  | Plan       | Total / min | Ticket Create / min | Tickets List / min | Contacts List / min |
  |------------|-------------|---------------------|--------------------|---------------------|
  | Trial      | 50          | -                   | -                  | -                   |
  | Growth     | 100         | 50                  | 40                 | 40                  |
  | Pro        | 400         | 160                 | 100                | 100                 |
  | Enterprise | 700         | 280                 | 200                | 200                 |

  - Ticket Update matches Ticket Create (from the legacy table: 40/80/160/280).
  - Purchasable add-ons: 1000/min (Ticket Create 400, List 300) and 2000/min (Ticket Create 800, List 400).
  - Some older guides give Growth 200/min. Treat 100 as current. [Conflict flagged]
  - Legacy plans: Blossom 100, Garden 200, Estate 400, Forest 700 per minute. A table on the same docs page is labelled "per hour" (3000/5000), which looks like an error or leftover in the docs. [Docs inconsistency]
  - Per-minute throttling was rolled out in batches; check the headers on your own account. [OFFICIAL]
- Headers [OFFICIAL]:
  - Classic: X-RateLimit-Total, X-RateLimit-Remaining, X-RateLimit-Used-CurrentRequest, and Retry-After (seconds, only on 429).
  - Newer: X-RateLimit-Account-{Total,Used,Remaining,Window-Start-At,Window-End-At,Label} and X-RateLimit-Sublimit-* (only on endpoints that have a sub-limit).
- include= parameters cost extra calls (include=conversations costs 2).
- Implications:
  - On Growth, a historical crawl gets about 40 list pages a minute (about 4,000 tickets a minute at 100 per page). The real bottleneck is the per-ticket conversation fetches, roughly 1 call per ticket per 30 messages.
  - Budget about 50–60/min for the crawl so the live bot and other apps keep headroom.

== 7. SOLUTIONS (KNOWLEDGE BASE) API ==
- Endpoints, from my knowledge of the docs; the reading did not cover this section [UNVERIFIED, though consistent with 3P sources]:
  - Categories: GET/POST /api/v2/solutions/categories; GET/PUT/DELETE /api/v2/solutions/categories/{id}
  - Folders: GET/POST /api/v2/solutions/categories/{category_id}/folders; GET/PUT/DELETE /api/v2/solutions/folders/{id}
  - Articles: GET/POST /api/v2/solutions/folders/{folder_id}/articles; GET/PUT/DELETE /api/v2/solutions/articles/{id}
  - Search: GET /api/v2/search/solutions?term=...
  - Translations: append /{language_code} to the create/update/view paths (multilingual must be enabled).
- Article `status`: 1 = draft, 2 = published. [3P, consistent]
  - The folder article list also returns drafts, so filter client-side. [3P community]
- Folder `visibility`: 1 all users, 2 logged-in users, 3 agents only, 4 selected companies. [UNVERIFIED]
- Article fields include title, description (HTML), status, tags, and seo_data (meta_title, meta_description).
- Use case: one-way sync of the public-safe part of the vault into Freshdesk Solutions. This gives a customer self-service portal and feeds Freddy, which reads Solutions natively. Store the Freshdesk article id in the vault note's frontmatter so later syncs update instead of creating duplicates. [Recommendation]

== 8. FRESHDESK NATIVE AI (BUILD VS BUY) ==
- Freddy AI Agent: an autonomous bot for chat, web widget and email. It answers from knowledge sources and can run actions.
  - Pricing: $49 per 100 sessions, after 500 free sessions. Several guides say the 500 is a one-time grant per account, not monthly. [OFFICIAL Omni pricing page plus 3P]
  - For email AI agents, each AI response counts as a session, so multi-turn threads use several. [3P]
  - CostBench lists $100 per 1,000 sessions with a different session definition. [Conflict]
- Freddy AI Copilot: for agents. Suggested replies, summaries, tone rewrite and similar.
  - About $29 per agent per month, billed annually, Pro and Enterprise only. [OFFICIAL Omni pricing page; some older sources say $49]
- Freddy Insights: analytics add-on. [Not researched]
- Knowledge sources for the AI Agent: AI Agent Studio > Build > Knowledge. [OFFICIAL, support article 50000011712]
  - Native sources: Freshdesk Solutions articles, public URLs (crawled), uploaded files, and connectors (Google Drive, SharePoint).
  - Limits are unclear; figures cited range from "10 URLs per agent, 25 per account" to "up to 3,000 pages per website source". [UNVERIFIED]
  - It CANNOT read a private Git or Obsidian vault directly. You would have to publish into Solutions, host public pages, upload files, or put the files in Drive or SharePoint.
- Trade-off:
  - Freddy: no infrastructure and native widget/email handling, but per-session cost, limited control over prompts and model, and private-repo knowledge must be exported into Freshworks.
  - Custom build (Claude via the API): full control over grounding in the vault and the past-ticket Q&A corpus, draft-as-private-note review mode, cheaper per ticket, but you own hosting, the webhook endpoint and monitoring.
  - A hybrid is possible: sync the vault into Solutions, which serves both the portal and Freddy, while building a custom drafter.

== 9. DATA / PRIVACY ==
- Tickets contain PII:
  - Requester name, email and phone (through requester and contacts).
  - Email bodies with addresses, order numbers, signatures, and sometimes home-network details.
  - Private notes may contain internal or sensitive information.
- Before adding exported tickets to the knowledge repo, redact or pseudonymise emails, phone numbers, names, street addresses, IP and MAC addresses, order numbers and serials, and strip signatures and quoted history. Store requester ids rather than emails. Keep raw exports out of git and git-ignored, and commit only the cleaned Q&A. [Recommendation]
- Consider GDPR/CCPA deletion requests: a ticket deleted in Freshdesk should also be removed from derived data. [Recommendation]
- Attachment URLs are pre-signed S3 links that expire. No official lifetime is published. [UNVERIFIED]
  - Community reports range from about 5 minutes to 24 hours. Export download links had X-Amz-Expires of 7 days.
  - The expiry is set on Freshdesk's side and cannot be changed.
  - Read the `Expires` parameter from the URL, download right away, and re-fetch the conversation to get a fresh link if it has lapsed.
  - Some developers reported 403 errors even on fresh links.
  - Do not store attachment URLs as permanent references.
- Using an LLM provider on ticket content means sending customer data to a third party. Check your privacy policy and the provider's data-retention and no-training terms. [Recommendation]
- API keys: keep them in a secret store or env var, never in the repo. One key per integration (the bot agent) so it can be rotated.

== FLAGGED / COULD NOT VERIFY ==
1. Solutions endpoint paths and folder visibility codes come from my knowledge of the docs; the docs reading did not reach that section.
2. Conversation `source` codes for conversation entries.
3. Whether PUT tags replaces or appends (I believe it replaces).
4. Webhook retry policy (48 retries at 30-minute intervals) and the 1,000 per hour webhook cap come from Hookdeck citing Freshdesk, not the primary doc.
5. Whether webhooks count against the API rate limit.
6. Account export format (XML) and exact menu path in the current Omni UI.
7. Exact lifetime of attachment URLs.
8. Freddy AI Agent knowledge-source limits, whether the 500 sessions are one-time, and regional pricing.
9. Docs inconsistencies: the "per hour" label in the rate-limit table, and 1 vs 2 credits per include.
10. Whether a bot agent needs a full paid seat.

Key sources:
- https://developers.freshdesk.com/api/
- https://support.freshdesk.com/support/solutions/articles/225439-what-are-the-rate-limits-for-the-api-calls-to-freshdesk
- https://support.freshdesk.com/support/solutions/articles/225435-where-can-i-find-my-api-key-
- https://support.freshdesk.com/support/solutions/articles/225158
- https://support.freshdesk.com/support/solutions/articles/226461-export-ticket-properties-from-your-helpdesk
- https://support.freshdesk.com/support/solutions/articles/50000011712-configure-knowledge-sources
- https://hookdeck.com/webhooks/platforms/guide-to-freshdesk-webhooks-features-and-best-practices
- https://www.freshworks.com/freshdesk/omni/pricing/2026/
- https://www.eesel.ai/blog/freshdesk-freddy-ai-pricing
- https://community.freshworks.dev/t/increase-expires-parameter-for-conversation-attachments/7959
