# Discovery Copilot

Discovery Copilot is a Python command-line application that helps enterprise
pre-sales teams turn raw customer discovery notes into structured technical and
business documentation.

It is designed for Pre-Sales Engineers, Solutions Engineers, Sales Engineers,
and Solution Architects who need to improve discovery quality, identify gaps,
and prepare internal briefings after customer meetings.

## Problem Statement

Customer discovery notes are often messy, incomplete, and hard to convert into
useful internal documentation. This slows down solution design, technical
validation, proof-of-concept planning, and handoff to engineering or product
teams.

Discovery Copilot uses the OpenAI API to analyze `.txt` and `.md` notes and
generate a complete set of Markdown reports that expose business context,
requirements, risks, missing information, next questions, and recommended next
steps.

## Features

- Python-only command-line workflow
- Supports `.txt` and `.md` input files
- Generates 11 structured Markdown reports
- Identifies explicit and implicit technical requirements
- Highlights discovery gaps and missing questions
- Scores discovery quality across key pre-sales dimensions
- Produces a customer meeting brief for internal teams
- Uses environment variables for API configuration
- Includes a local mock provider for demos without an API key
- Handles missing files, invalid formats, empty documents, missing API keys,
  rate limits, and API failures gracefully

## Generated Reports

Running the application creates an `output/` directory containing:

- `Executive Summary.md`
- `Customer Profile.md`
- `Business Challenges.md`
- `Technical Requirements.md`
- `Discovery Gaps.md`
- `Recommended Next Questions.md`
- `Customer Meeting Brief.md`
- `Solution Recommendations.md`
- `Discovery Quality Score.md`
- `Discovery Maturity Assessment.md`
- `Next Steps.md`

## Requirements

- Python 3.9 or newer
- OpenAI API key

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

For development and tests:

```bash
pip install -r requirements-dev.txt
```

Create your environment file:

```bash
cp .env.example .env
```

Then add your API key:

```env
OPENAI_API_KEY=your_api_key_here
```

Optional:

```env
OPENAI_MODEL=gpt-4o-mini
```

## Usage

Run the example demo locally without an API key:

```bash
python3 main.py examples/northstar_retail_group/discovery_notes.md --provider mock
```

This generates the 11 Markdown reports in `output/` using deterministic sample
content. It is the fastest way to review the project.

Run Discovery Copilot with a supported input file:

```bash
python main.py input/sample_discovery_notes.md
```

On systems where `python` is not available, use `python3`:

```bash
python3 main.py input/sample_discovery_notes.md
```

You can also use your own meeting notes:

```bash
python main.py input/customer_meeting.md
```

or:

```bash
python main.py input/discovery_notes.txt
```

Successful execution prints the list of generated reports and writes them to
`output/`.

To use the OpenAI API, configure `.env` and run the default provider:

```bash
python3 main.py input/sample_discovery_notes.md --provider openai
```

## Testing

Run the test suite:

```bash
python3 -m unittest discover
```

## Folder Structure

```text
discovery-copilot/
├── main.py
├── requirements.txt
├── requirements-dev.txt
├── README.md
├── CHANGELOG.md
├── SECURITY.md
├── .env.example
├── examples/
│   └── northstar_retail_group/
│       ├── discovery_notes.md
│       ├── discovery_report.md
│       ├── generated_outputs/
│       ├── visuals/
│       └── chart_data/
├── input/
│   └── sample_discovery_notes.md
├── output/
├── prompts/
│   ├── report_prompt.md
│   └── system_prompt.md
├── src/
│   ├── config.py
│   ├── exceptions.py
│   ├── generator.py
│   ├── input_loader.py
│   ├── mock_client.py
│   ├── openai_client.py
│   └── reports.py
├── tests/
└── utils/
    └── files.py
```

## Example Outputs

Discovery Copilot turns raw notes into executive-ready and engineering-ready
Markdown documents. Example report content includes:

- Executive summary for leadership review
- Customer profile and stakeholder map
- Explicit and inferred requirements
- Security, integration, scalability, and infrastructure requirements
- Missing discovery questions
- Recommended second-meeting questions
- Discovery quality score and maturity assessment
- Prioritized next-step action plan

## Enterprise Example: Northstar Retail Group

The repository includes a complete fictional enterprise scenario for
**Northstar Retail Group**, a large retail company with 420 stores, e-commerce
operations, customer support teams, and legacy systems across Latin America.
The example demonstrates how raw discovery notes can become structured
pre-sales documentation, architecture direction, follow-up questions, and
decision-ready internal reports.

Explore the sample package:

- [Discovery notes](examples/northstar_retail_group/discovery_notes.md)
- [Generated output reports](examples/northstar_retail_group/generated_outputs)
- [Consolidated discovery report](examples/northstar_retail_group/discovery_report.md)
- [Solution flow diagram - Mermaid](examples/northstar_retail_group/visuals/solution_flow.mmd)
- [Target architecture diagram - Mermaid](examples/northstar_retail_group/visuals/target_architecture.mmd)
- [Overview banner - PNG](examples/northstar_retail_group/visuals/overview_banner.png)
- [Discovery Copilot workflow - PNG](examples/northstar_retail_group/visuals/discovery_copilot_workflow.png)
- [Northstar target architecture - PNG](examples/northstar_retail_group/visuals/northstar_target_architecture.png)
- [Discovery scores and coverage - PNG](examples/northstar_retail_group/visuals/discovery_scores_and_coverage.png)
- [Generated output preview images](examples/northstar_retail_group/output_previews)
- [Discovery score chart data](examples/northstar_retail_group/chart_data/discovery_scores.csv)
- [Requirements coverage chart data](examples/northstar_retail_group/chart_data/requirements_coverage.csv)

### Example Usage With Northstar Notes

```bash
python3 main.py examples/northstar_retail_group/discovery_notes.md --provider mock
```

The command generates Markdown reports in `output/`. The repository also
includes prebuilt sample reports in
`examples/northstar_retail_group/generated_outputs/` so the expected output can
be inspected without running the application.

### Example Visuals

![Discovery Copilot overview banner](examples/northstar_retail_group/visuals/overview_banner.png)

![Discovery Copilot workflow](examples/northstar_retail_group/visuals/discovery_copilot_workflow.png)

![Northstar target architecture](examples/northstar_retail_group/visuals/northstar_target_architecture.png)

![Discovery scores and requirements coverage](examples/northstar_retail_group/visuals/discovery_scores_and_coverage.png)

The PNG visuals are generated by
`scripts/generate_example_images.py` and committed so the example can be
reviewed without installing extra tooling.

### Generated Output Previews

Each generated report includes a visual preview so the output set can be scanned
quickly before opening the full Markdown files.

| Report | Preview |
| --- | --- |
| [Executive Summary](examples/northstar_retail_group/generated_outputs/Executive%20Summary.md) | ![Executive Summary preview](examples/northstar_retail_group/output_previews/01_executive_summary.png) |
| [Customer Profile](examples/northstar_retail_group/generated_outputs/Customer%20Profile.md) | ![Customer Profile preview](examples/northstar_retail_group/output_previews/02_customer_profile.png) |
| [Business Challenges](examples/northstar_retail_group/generated_outputs/Business%20Challenges.md) | ![Business Challenges preview](examples/northstar_retail_group/output_previews/03_business_challenges.png) |
| [Technical Requirements](examples/northstar_retail_group/generated_outputs/Technical%20Requirements.md) | ![Technical Requirements preview](examples/northstar_retail_group/output_previews/04_technical_requirements.png) |
| [Discovery Gaps](examples/northstar_retail_group/generated_outputs/Discovery%20Gaps.md) | ![Discovery Gaps preview](examples/northstar_retail_group/output_previews/05_discovery_gaps.png) |
| [Recommended Next Questions](examples/northstar_retail_group/generated_outputs/Recommended%20Next%20Questions.md) | ![Recommended Next Questions preview](examples/northstar_retail_group/output_previews/06_recommended_next_questions.png) |
| [Customer Meeting Brief](examples/northstar_retail_group/generated_outputs/Customer%20Meeting%20Brief.md) | ![Customer Meeting Brief preview](examples/northstar_retail_group/output_previews/07_customer_meeting_brief.png) |
| [Solution Recommendations](examples/northstar_retail_group/generated_outputs/Solution%20Recommendations.md) | ![Solution Recommendations preview](examples/northstar_retail_group/output_previews/08_solution_recommendations.png) |
| [Discovery Quality Score](examples/northstar_retail_group/generated_outputs/Discovery%20Quality%20Score.md) | ![Discovery Quality Score preview](examples/northstar_retail_group/output_previews/09_discovery_quality_score.png) |
| [Discovery Maturity Assessment](examples/northstar_retail_group/generated_outputs/Discovery%20Maturity%20Assessment.md) | ![Discovery Maturity Assessment preview](examples/northstar_retail_group/output_previews/10_discovery_maturity_assessment.png) |
| [Next Steps](examples/northstar_retail_group/generated_outputs/Next%20Steps.md) | ![Next Steps preview](examples/northstar_retail_group/output_previews/11_next_steps.png) |

### Sample Discovery Score

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

### Requirements Coverage

| Area | Coverage |
| --- | ---: |
| Business Requirements | 80% |
| Technical Requirements | 69% |
| Security Requirements | 58% |
| Integration Requirements | 73% |
| Infrastructure Requirements | 56% |
| Success Metrics | 50% |
| Stakeholder Mapping | 88% |

### Why This Example Matters

This example shows practical pre-sales judgment: the tool does not only produce
summaries. It identifies gaps, separates explicit and inferred requirements,
scores discovery quality, proposes a focused pilot, and demonstrates enterprise
discovery and solution-framing ability.

## Future Roadmap

These improvements are intentionally documentation-only and are not implemented
in this version:

- PDF support
- DOCX support
- Audio transcript support
- Streamlit interface
- CRM integration
- Salesforce integration
- HubSpot integration
- Microsoft Teams integration
- Slack integration
- RAG using internal documentation
- Vector database support
- Multi-language support
- Dashboard
- Docker deployment
- Batch processing

## Design Philosophy

Discovery Copilot is not a chatbot. It is a focused productivity tool for
enterprise pre-sales work. The emphasis is on structured outputs, reasoning,
discovery quality, and practical documentation that saves time after customer
meetings.

## Author

Created by Fabricio Puliafico Artur.

- GitHub: [fabricioartur](https://github.com/fabricioartur)

## License

Copyright (c) 2026 Fabricio Puliafico Artur.

This project is released under the MIT License. See [LICENSE](LICENSE) for
details.
