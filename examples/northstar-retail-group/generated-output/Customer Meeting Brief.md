# Customer Meeting Brief

## Executive Summary

Northstar Retail Group wants to improve customer support productivity and order
visibility across 420 stores and digital channels in Latin America. The customer
is exploring an internal AI assistant for support agents and store operations,
with a Brazil and Mexico pilot targeted within 90 days.

## Customer Overview

Northstar operates physical retail, e-commerce, marketplace integrations, mobile
channels, WhatsApp support, and a loyalty program. Its technology landscape is
fragmented due to regional operations and prior acquisitions.

## Objectives

- Reduce average handling time by at least 25%.
- Improve access to order, refund, and loyalty context.
- Reduce manual reconciliation across support and back-office systems.
- Standardize support workflows while respecting country-level differences.
- Measure pilot adoption and business impact.

## Current Environment

- Salesforce Service Cloud and Zendesk for support.
- SAP ECC and Oracle E-Business Suite for ERP.
- Legacy OMS with batch updates.
- MuleSoft, SOAP, SFTP, and database exports for integration.
- Snowflake for analytics.
- Microsoft Entra ID for corporate identity.
- AWS, Azure, and VMware-based data centers.

## Challenges

- Agents perform manual lookups across several systems.
- Store exception reporting is delayed.
- Knowledge and case categories vary by country.
- Batch updates create stale order data.
- Privacy and governance requirements must be clarified.

## Risks

- Integration complexity could exceed the 90-day pilot window.
- Unclear data residency and retention requirements may delay security approval.
- Poor knowledge quality could reduce trust in AI recommendations.
- Zendesk migration dependencies may complicate pilot scope.

## Requirements

- Entra ID single sign-on.
- Salesforce case context and note integration.
- OMS and ERP read access.
- Audit trails for responses and actions.
- Portuguese and Spanish support.
- Approved knowledge source retrieval.
- Dashboards for adoption and impact.

## Stakeholders

- Customer Experience
- Digital Operations
- Enterprise Architecture
- IT Integration
- Security and Compliance
- Support Operations
- Regional IT

## Open Questions

- What is the approved budget and budget owner?
- How many pilot users will participate?
- What SLA and DR requirements apply?
- What data must remain in-country?
- Which knowledge articles are approved for AI use?
- What metrics will determine pilot success?

## Recommended Next Steps

Schedule a technical workshop focused on pilot scope, integration feasibility,
security governance, data access, and success metrics. The workshop should
produce a pilot architecture, use-case matrix, data classification summary, and
implementation plan.
