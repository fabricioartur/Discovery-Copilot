"""Deterministic local report generator for demos and tests."""

from __future__ import annotations

import re
import textwrap


class MockDiscoveryClient:
    """Generate useful sample Markdown without calling an external API."""

    def generate_markdown(self, system_prompt: str, user_prompt: str) -> str:
        """Return deterministic Markdown for the requested report."""

        del system_prompt
        title = _extract_title(user_prompt)
        body = MOCK_REPORTS.get(title, _generic_report(title))
        return body.strip()


def _extract_title(user_prompt: str) -> str:
    match = re.search(r"Create the report named:\s*(.+)", user_prompt)
    if not match:
        return "Discovery Report"
    return match.group(1).strip()


def _generic_report(title: str) -> str:
    return textwrap.dedent(
        f"""
        # {title}

        This mock report was generated locally for demonstration purposes.

        ## Summary

        Discovery Copilot processed the provided notes and produced a structured
        report without calling the OpenAI API.

        ## Review Notes

        Replace mock mode with the OpenAI provider for full AI-generated
        analysis.
        """
    )


MOCK_REPORTS: dict[str, str] = {
    "Executive Summary": """
# Executive Summary

Northstar Retail Group is evaluating an internal AI assistant to help support
agents and store operations teams reduce manual lookups, improve order
visibility, and standardize customer service workflows across Latin America.

## Customer Context

- Large retail organization with 420 stores.
- E-commerce, mobile, marketplace, WhatsApp support, and loyalty channels.
- Fragmented environment caused by regional growth and acquisitions.

## Expected Outcomes

- Reduce average handling time.
- Improve support consistency.
- Create a focused Brazil and Mexico pilot.
- Clarify security, integration, and governance requirements before rollout.
""",
    "Customer Profile": """
# Customer Profile

## Industry

Retail and e-commerce.

## Company Size

Large enterprise with 420 stores across Latin America.

## Technical Maturity

Intermediate to advanced. Northstar has enterprise platforms such as
Salesforce, MuleSoft, Snowflake, Microsoft Entra ID, AWS, and Azure, while also
maintaining legacy ERP, OMS, SOAP, and batch integration patterns.
""",
    "Business Challenges": """
# Business Challenges

## Key Challenges

- Support agents switch between several systems to answer customer questions.
- Batch updates create stale order status information.
- Refund workflows require manual validation.
- Store managers receive operational exception reports too late.
- Country teams use inconsistent case categories and escalation rules.
""",
    "Technical Requirements": """
# Technical Requirements

## Explicit Requirements

- Integrate with Salesforce Service Cloud.
- Retrieve order status from legacy OMS and ERP systems.
- Support Microsoft Entra ID single sign-on.
- Maintain audit trails.
- Support Portuguese and Spanish.

## Implicit Requirements

- Normalize customer and order context across systems.
- Use a reusable API layer rather than direct point-to-point integrations.
- Provide measurement for pilot adoption and handling-time impact.
""",
    "Discovery Gaps": """
# Discovery Gaps

## Missing Information

- Pilot user count.
- Approved budget range and owner.
- Required SLA.
- Data residency by country.
- Disaster recovery expectations.
- Model governance process.
- Current baseline for success metrics.
""",
    "Recommended Next Questions": """
# Recommended Next Questions

## Business

- Which workflow should define pilot success?
- What handling-time reduction is required?

## Technical

- Which systems are authoritative for order and customer data?
- Which MuleSoft APIs already exist?

## Security

- What data must be redacted before model processing?
- What audit fields are mandatory?
""",
    "Customer Meeting Brief": """
# Customer Meeting Brief

## Overview

Northstar Retail Group wants to improve support productivity and order
visibility through an internal AI assistant pilot.

## Recommended Workshop Focus

- Pilot scope.
- Integration feasibility.
- Security and compliance.
- Data governance.
- Success metrics.
""",
    "Solution Recommendations": """
# Solution Recommendations

## API-First Assistant

Use MuleSoft as the approved integration layer for order, customer, case, and
loyalty data.

## Retrieval Augmented Generation

Use approved knowledge articles and operating procedures as grounded sources.

## Human-in-the-Loop Pilot

Keep agents in control of customer communication during phase one.
""",
    "Discovery Quality Score": """
# Discovery Quality Score

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
""",
    "Discovery Maturity Assessment": """
# Discovery Maturity Assessment

## Classification

Intermediate

## Rationale

The discovery captured business goals, stakeholders, systems, pain points, and
initial requirements. It still needs stronger detail around security,
integration readiness, budget, SLA, and success metrics.
""",
    "Next Steps": """
# Next Steps

## Priority 1

Confirm pilot scope and first workflow.

## Priority 2

Validate Salesforce, OMS, ERP, Zendesk, and MuleSoft integration paths.

## Priority 3

Complete security and compliance review.

## Priority 4

Baseline success metrics.

## Priority 5

Schedule a cross-functional technical workshop.
""",
}
