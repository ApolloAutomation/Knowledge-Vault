BRIEF: Best practices for a Claude support agent grounded in a small markdown KB plus historical tickets (Nov 2026)

Most sources are vendor and practitioner blogs. Treat their numbers as rules of thumb, not benchmarks. The Anthropic, Freshdesk and Langfuse sources and the EMNLP paper carry the most weight.

1. RETRIEVAL: SKIP VECTOR RAG. LOAD THE WHOLE VAULT AND CACHE IT.
- Anthropic's own guidance: a knowledge base under 200k tokens (about 500 pages) can go into the prompt whole, without RAG. Prompt caching cuts latency by more than 2x and cost by up to 90%. About 40 notes and fewer than 1k lines is roughly 10-20k tokens, far below that limit.
- Build the prompt in this order: system rules, then the full vault (each note wrapped with its path and title), with a cache breakpoint after the vault. Put the ticket text last. Because the cache key changes only when the vault changes (a git commit), the hit rate stays high.
- For citations, pass each note as a `search_result` content block (source = `kb://<note-path>`, title = note title) with `citations.enabled: true`. Claude then returns citations at block level. Use these to check grounding: a draft with no citation is not allowed to auto-send. Gotcha: enabling citations together with structured output (`output_config.format`) returns a 400 error. Get the routing decision (confidence, category) in a separate call or with a tool call.
- When to switch: past about 50-100k tokens of KB plus distilled ticket Q&A, or once noise starts hurting accuracy. The next step is Anthropic Contextual Retrieval (contextual chunk prefixes plus BM25 plus embeddings plus rerank). Until then, a cheap middle step is to always load the core notes and add the top-k Q&A notes from simple keyword or BM25 search.
- Opinion: do not stand up a vector DB now. It adds infrastructure and failure modes and gives this corpus no accuracy gain.

2. TURNING HISTORICAL TICKETS INTO KNOWLEDGE
- Pipeline: (1) export through the Freshdesk API v2. `GET /api/v2/tickets` returns metadata only, so the message thread needs a separate `GET /tickets/{id}/conversations` call, which is paginated. (2) Apply quality filters. (3) Scrub PII. (4) Extract Q&A pairs. (5) Cluster them. (6) Distill them into canonical notes. (7) Have a human review the notes, then merge them into git.
- Quality filters: status Resolved or Closed; the final public reply was written by an agent (not the customer or a bot); no reopen within about 14 days; CSAT is good or missing; drop spam, auto-replies, order-only and shipping-status tickets; prefer recent tickets so stale firmware or product answers drop out.
- PII: scrub in code before any LLM sees the text. Remove names, emails, phones, addresses, order numbers and serials, MAC/IP addresses, Home Assistant URLs and tokens, and signatures. Use regex plus an NER pass (for example Presidio), then a sampled manual check. Keep ticket IDs only in a private mapping, outside the vault.
- Distill, do not dump. The EMNLP 2025 industry paper ("AI Knowledge Assist") extracts Q&A pairs from transcripts, clusters similar pairs, and builds one representative pair per cluster. The same approach suits this vault. Store canonical notes such as `FAQ/<product>/<topic>.md` with frontmatter: products, symptoms, firmware versions, source ticket count, last_verified, confidence. Do not put raw transcripts in the prompt. They are noisy, repeat each other, carry PII leakage risk, and contain old answers that contradict current docs. If raw tickets are useful, keep them scrubbed in a separate archive used for evals.
- Clustering: at a small company's ticket volume (hundreds to low thousands), have Claude assign a topic label per ticket against a growing taxonomy, then group by label. Embeddings plus HDBSCAN are optional.
- Staleness: an FAQ distilled from old tickets can contradict later firmware changes. Add a `last_verified` field and a periodic re-validation pass.

3. SAFETY
- Default to drafting into a Freshdesk private note (`POST /tickets/{id}/notes` with `private: true`). Public replies are a separate endpoint (`/tickets/{id}/reply`), which makes it easy to keep the auto-send path physically separate and switched off at first.
- Tiered gating: high confidence plus at least one citation plus an allowed category leads to auto-reply, but only after shadow mode proves it. Medium confidence leads to a private-note draft for an agent to approve. Low confidence, or any hard category, leads to no draft (or a triage summary only) plus a tag or group assignment.
- Do not gate on model self-reported confidence alone. Practitioners report high confidence on wrong answers. Combine it with signals the system can check: the draft cites a KB note, the category classifier result, sentiment, and keyword rules.
- Always escalate these, whatever the confidence: refunds, chargebacks and billing; RMA, warranty and replacement; order changes, cancellations and address changes; shipping lost or damaged; safety (overheating, burning smell, battery, electrical, mains wiring); legal or compliance and data deletion; angry or threatening customers, or anyone who asks for a human; repeat contacts or reopened tickets; VIP/B2B and wholesale accounts; tickets with attachments the model cannot interpret.
- Hallucination controls: the system prompt says "answer only from the provided notes; if the notes don't cover it, say so and escalate". Require citations and reject any uncited factual sentence in post-processing. Never invent part numbers, prices, ship dates, firmware versions or URLs. Use a whitelist of URLs that appear in the vault. Make "I don't know" the expected outcome when coverage is missing: escalate with a note saying "KB gap: <topic>".
- Prompt injection from customer email (the "lethal trifecta": private data plus untrusted input plus outbound communication): wrap the ticket body in delimiters and label it untrusted data. Give the drafting model no tools; it only produces text. Never let the model change ticket status, priority or assignee, issue refunds, or look up other customers. Deterministic code makes all Freshdesk writes from a fixed allowlist. Strip or flag hidden HTML text and instructions in email bodies. Log every input and output. Prompt-level defenses are probabilistic, so the guarantee comes from limiting what the system can do, not from the prompt.

4. EVALUATION
- Eval set: 100-300 scrubbed historical tickets stratified by product and category, plus about 30 adversarial ones (escalation-required cases, injection attempts, out-of-KB questions). The gold answer is the agent's final reply. Each item also gets a label for whether it should escalate.
- Metrics:
  - Offline (before launch): an LLM-judge "resolution match" (does the draft recommend the same fix as the human reply? Binary), as in Langfuse's support example. Faithfulness: every claim traces to a cited note. Escalation precision and recall, where recall on hard categories must be about 100%. Wrong-action count.
  - Online (shadow mode and pilot): draft acceptance rate (the share sent with no or minor edits; one pilot plan targets 70% with a 60% floor). Edit distance between the draft and the sent reply, as normalized token-level Levenshtein. No published source used this, but it is cheap and objective, so pair it with an LLM label for the type of edit (tone, correction, addition, as Langfuse does). Time to first response. Reopen or re-contact rate within 7-14 days. CSAT on AI-assisted tickets compared with others.
  - Deflection compared with resolution: track true resolution (closed with no human and no reopen), not "deflection", which inflates the figure.
- Judge hygiene: calibrate the judge against about 50 human-graded cases. Keep the judge model and rubric fixed across versions. Re-run the full set on every KB or prompt change, which is easy as a CI job on the git repo.
- Rollout:
  - Phase 0: offline eval.
  - Phase 1: shadow mode. Drafts are logged or written as private notes that agents can see but nothing is sent, for 2-4 weeks.
  - Phase 2: agent-assist. Agents send edited drafts.
  - Phase 3: auto-send for one or two narrow, high-acceptance categories (for example setup and Wi-Fi onboarding FAQs, firmware update how-to), using a kill switch and a sampled human audit.

5. FEEDBACK LOOP
- When a ticket is resolved, compare the AI private note with the agent's sent public reply. Store the pair: draft, final, cited notes, edit-type label.
- A weekly batch job has Claude cluster heavy edits and "KB gap" escalations, then propose vault diffs (a new FAQ note or a correction to an existing note) as a git PR for human review. Never auto-merge into the KB.
- Tag the root cause of each escalation (KB gap, policy, judgement, angry customer) to decide what to document next.
- Promoted edits also become new eval cases (regression tests).

6. FRESHDESK SPECIFICS
- Trigger on ticket create using a Freshdesk automation webhook to your service. The service fetches the conversations, calls Claude, and posts a private note plus tags (for example `ai-drafted`, `ai-escalate:<reason>`).
- Rate limits apply account-wide and are shared with every other integration. Reported figures conflict (about 100-700 per minute depending on plan), so check the limit on your own plan. Throttle bulk historical exports and respect `Retry-After`.
- One community report says a ticket accepts at most about 400 notes. Not verified, and unlikely to matter here.
- Use a dedicated API key on a dedicated "AI Assistant" agent seat with minimal role permissions, so its actions are attributable and easy to revoke.

Sources:
- [Anthropic: Contextual Retrieval (the under-200k-tokens guidance and caching)](https://www.anthropic.com/engineering/contextual-retrieval)
- [Claude docs: search result blocks](https://platform.claude.com/docs/en/build-with-claude/search-results)
- [Claude docs: citations](https://platform.claude.com/docs/en/build-with-claude/citations)
- [DEV: when not to use RAG, Claude support bot](https://dev.to/vitalii-nosov/when-not-to-use-rag-lessons-from-building-a-claude-powered-support-bot-433b)
- [EMNLP 2025 Industry: AI Knowledge Assist (Q&A extraction and clustering from transcripts)](https://aclanthology.org/anthology-files/pdf/emnlp/2025.emnlp-industry.130.pdf)
- [eesel: PII redaction in support transcripts](https://www.eesel.ai/blog/how-to-use-ai-to-redact-pii-in-support-transcripts)
- [Deskpro: help desk tickets should inform your AI](https://www.deskpro.com/blog/knowledge-is-power-your-help-desk-tickets-should-inform-your-ai)
- [Fini: building a KB from tickets](https://www.usefini.com/guides/ai-knowledge-base-build-help-center-from-tickets)
- [eesel: confidence thresholds](https://eesel.ai/blog/setting-confidence-thresholds-for-ai-responses)
- [eesel: AI escalation management](https://eesel.ai/blog/ai-escalation-management)
- [Parloa: human-in-the-loop best practices](https://www.parloa.com/knowledge-hub/best-practices-human-in-the-loop/)
- [tianpan: escalation protocol](https://tianpan.co/blog/2026/04/10/escalation-protocol-agent-to-human-handoffs)
- [tianpan: prompt injection in agentic pipelines](https://tianpan.co/blog/2026/04/18/prompt-injection-agentic-pipelines-defense)
- [Robylon: lethal trifecta in email support](https://www.robylon.ai/blog/lethal-trifecta-email-support)
- [SwiftCase: prompt injection arrives by email](https://swiftcase.co.uk/2026/06/09/prompt-injection-arrives-by-email)
- [Langfuse: customer support chatbot evals](https://langfuse.com/academy/examples/customer-support-chatbot.md)
- [Richpanel: evaluating AI support agents before launch](https://www.richpanel.com/learn/evaluating-ai-support-agents-before-launch)
- [Gyde: AI support copilot evaluation plan](https://amitsinghbhadoria.github.io/gyde-pod-delivery-docs/engagement/evaluation-plan)
- [Voiceflow: AI agent evaluation](https://www.voiceflow.com/blog/ai-agent-evaluation.md)
- [Freshdesk API v2 reference](https://developer.freshdesk.com/api/)
- [Freshworks community: private note compared with reply](https://community.freshworks.dev/t/sending-a-conversation-as-private/14312)
- [Truto: Freshdesk API 2026 guide (rate limits)](https://truto.one/blog/how-to-integrate-with-the-freshdesk-api-2026-engineering-guide/)
- [eesel: Freshdesk Conversations API](https://www.eesel.ai/blog/freshdesk-conversations-api)