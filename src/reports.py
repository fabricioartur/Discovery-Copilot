"""Report definitions for Discovery Copilot."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReportDefinition:
    """Metadata used to generate a single Markdown report."""

    filename: str
    title: str
    instructions: str


REPORTS: tuple[ReportDefinition, ...] = (
    ReportDefinition(
        filename="Executive Summary.md",
        title="Executive Summary",
        instructions=(
            "Generate an executive summary for leadership review. Include "
            "customer context, business goals, current environment, major pain "
            "points, and expected outcomes. Use concise executive language."
        ),
    ),
    ReportDefinition(
        filename="Customer Profile.md",
        title="Customer Profile",
        instructions=(
            "Identify industry, company size when possible, technical maturity, "
            "existing technologies, stakeholders, business priorities, and "
            "digital transformation level. Mark unknowns clearly."
        ),
    ),
    ReportDefinition(
        filename="Business Challenges.md",
        title="Business Challenges",
        instructions=(
            "Extract operational problems, technical bottlenecks, business "
            "risks, pain points, manual processes, and customer frustrations."
        ),
    ),
    ReportDefinition(
        filename="Technical Requirements.md",
        title="Technical Requirements",
        instructions=(
            "Separate findings into these sections: Explicit Requirements, "
            "Implicit Requirements, Security Requirements, Integration "
            "Requirements, Scalability Requirements, and Infrastructure "
            "Requirements. Do not invent facts; distinguish inference from "
            "directly stated requirements."
        ),
    ),
    ReportDefinition(
        filename="Discovery Gaps.md",
        title="Discovery Gaps",
        instructions=(
            "Identify missing information and weak areas in the discovery. "
            "Generate missing questions covering authentication provider, SLA, "
            "number of users, data residency, compliance, budget, timeline, "
            "integrations, and disaster recovery where relevant."
        ),
    ),
    ReportDefinition(
        filename="Recommended Next Questions.md",
        title="Recommended Next Questions",
        instructions=(
            "Generate intelligent follow-up questions grouped by Business, "
            "Technical, Security, Infrastructure, Integration, Timeline, "
            "Budget, and Success Metrics."
        ),
    ),
    ReportDefinition(
        filename="Customer Meeting Brief.md",
        title="Customer Meeting Brief",
        instructions=(
            "Create a polished internal briefing document for engineering, "
            "product, or management teams. Include executive summary, customer "
            "overview, objectives, current environment, challenges, risks, "
            "requirements, stakeholders, open questions, and recommended next "
            "steps."
        ),
    ),
    ReportDefinition(
        filename="Solution Recommendations.md",
        title="Solution Recommendations",
        instructions=(
            "Suggest high-level solution approaches that fit the scenario, such "
            "as API-first architecture, AI assistant, RAG, workflow automation, "
            "event-driven architecture, knowledge base, agentic AI, "
            "cloud-native deployment, identity federation, or microservices. "
            "Never invent vendor products. Explain why each recommendation fits."
        ),
    ),
    ReportDefinition(
        filename="Discovery Quality Score.md",
        title="Discovery Quality Score",
        instructions=(
            "Score from 0 to 100: Business Understanding, Technical "
            "Understanding, Security Understanding, Stakeholder Mapping, "
            "Requirements Completeness, Risk Identification, and Architecture "
            "Readiness. Provide an Overall Discovery Score and explain points "
            "deducted, missing information, and improvements required."
        ),
    ),
    ReportDefinition(
        filename="Discovery Maturity Assessment.md",
        title="Discovery Maturity Assessment",
        instructions=(
            "Classify discovery maturity as Poor, Basic, Intermediate, "
            "Advanced, or Enterprise Ready. Explain exactly why and provide "
            "recommendations to move to the next level."
        ),
    ),
    ReportDefinition(
        filename="Next Steps.md",
        title="Next Steps",
        instructions=(
            "Generate a prioritized action plan with Priority 1 through "
            "Priority 5. Focus on practical next actions such as confirming "
            "authentication, validating integrations, scheduling a technical "
            "workshop, preparing a proof of concept, and involving security."
        ),
    ),
)
