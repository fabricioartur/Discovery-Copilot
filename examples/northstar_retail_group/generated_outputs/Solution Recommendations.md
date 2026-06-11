# Solution Recommendations

## 1. API-First Assistant Architecture

Northstar should avoid direct point-to-point connections between the AI assistant
and core systems. MuleSoft should expose approved APIs for order, case, loyalty,
and customer context where possible. This fits the architecture team's concern
about reusable integration and reduces long-term technical debt.

## 2. Retrieval Augmented Generation Over Approved Knowledge

The assistant should use approved knowledge articles and operating procedures as
retrieval sources. This reduces the risk of unsupported guidance and gives
agents traceable answers. Knowledge readiness should be assessed before pilot.

## 3. Human-in-the-Loop Case Assistance

The first phase should assist agents rather than automate customer-facing
responses. Recommended actions, summaries, and case notes should remain under
agent review. This matches the customer's first-phase intent and lowers risk.

## 4. Security and Redaction Layer

Sensitive customer data should be minimized and redacted before model
processing where possible. Role-based access, audit logging, and retention
controls should be designed before production rollout.

## 5. Pilot-Focused Workflow Automation

The pilot should focus on a narrow workflow such as order status and refund
support for Brazil and Mexico. This makes a 90-day delivery more realistic and
allows measurable comparison against baseline handling time.

## 6. Analytics and Quality Dashboard

Use Snowflake or a reporting layer to measure adoption, handling-time impact,
answer quality, escalation trends, and agent feedback. Dashboards should support
pilot governance and expansion decisions.
