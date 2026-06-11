# Northstar Retail Group - Consolidated Discovery Report

## Executive Summary

Northstar Retail Group is a large Latin American retail company with 420 stores,
e-commerce operations, marketplace integrations, customer support teams, and
legacy systems across multiple countries. The company is evaluating an internal
AI assistant to help support agents and store operations teams answer order,
refund, loyalty, and policy questions more quickly.

The opportunity is strongest in agent assistance rather than fully automated
customer-facing AI. Northstar has clear business pain, a measurable pilot goal,
and executive sponsorship from customer experience and digital operations.
However, the discovery still needs stronger detail around security governance,
data residency, system-of-record decisions, pilot scope, and success metrics.

## Customer Context

Northstar operates in Brazil, Mexico, Chile, Colombia, and Peru. Growth through
acquisitions created a fragmented environment with different ERP systems,
support platforms, integration approaches, and operating processes by country.

## Current Environment

| Area | Systems |
| --- | --- |
| CRM and support | Salesforce Service Cloud, Zendesk |
| ERP | SAP ECC, Oracle E-Business Suite |
| Order management | Legacy on-premises OMS |
| E-commerce | Magento, custom Node.js storefront, marketplace connectors |
| Identity | Microsoft Entra ID, local identity stores |
| Data and analytics | Snowflake |
| Integration | MuleSoft, SOAP, SFTP, database exports |
| Infrastructure | AWS, Azure, VMware data centers |

## Primary Business Challenges

- Agents switch across multiple systems to answer common order questions.
- Order and exception data is stale because of batch processing.
- Refund approvals depend on manual checks.
- Country teams use inconsistent case categories and escalation paths.
- Support volume spikes during peak seasons.
- Store managers lack timely operational exception visibility.

## Candidate Solution Direction

The recommended direction is a human-in-the-loop AI assistant supported by
approved knowledge retrieval and enterprise API access. The assistant should
summarize customer and order context, suggest next actions, generate draft case
notes, and cite approved internal sources. It should not directly modify ERP
records during phase one.

## Architecture Approach

Use Microsoft Entra ID for authentication, Salesforce for case context, MuleSoft
as the primary API gateway, and approved knowledge repositories for retrieval.
The assistant should call structured APIs for order and customer data and keep
an audit trail of prompt, response, source, and agent action metadata.

## Security and Compliance Focus

Security review should address LGPD, country-specific privacy rules, role-based
access, prompt and response retention, redaction of personal data, PCI avoidance,
and audit requirements. The assistant should minimize sensitive data sent to
model processing and enforce regional access boundaries.

## Discovery Quality Score

| Category | Score |
| --- | ---: |
| Business Understanding | 82 |
| Technical Understanding | 76 |
| Security Understanding | 68 |
| Stakeholder Mapping | 84 |
| Requirements Completeness | 71 |
| Risk Identification | 79 |
| Architecture Readiness | 74 |
| Overall Discovery Score | 76 |

## Maturity Assessment

Discovery maturity is **Intermediate**. The team captured strong business and
technical context, but the opportunity is not ready for detailed architecture or
commercial proposal until open security, integration, budget, and success metric
questions are resolved.

## Top Open Questions

1. What is the exact Brazil and Mexico pilot user count?
2. What is the approved budget and budget owner?
3. Which system is the source of truth for order, customer, and loyalty data?
4. What data residency rules apply by country?
5. What SLA and disaster recovery expectations apply?
6. Which knowledge articles are approved and current?
7. What metric threshold determines pilot success?

## Recommended Next Steps

1. Confirm pilot scope and first workflow.
2. Validate Salesforce, OMS, ERP, Zendesk, and MuleSoft integration readiness.
3. Complete security and data governance review.
4. Baseline current support metrics.
5. Schedule a cross-functional technical workshop.

## Suggested Pilot Scope

Start with order status and refund assistance for Brazil and Mexico support
agents. This workflow is high-volume, has clear business value, and can be
limited to read-heavy enterprise data access while avoiding direct ERP writes.
