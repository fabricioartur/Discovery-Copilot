# Discovery Copilot

**Turn raw customer discovery notes into 11 structured pre-sales reports in under 60 seconds — powered by the OpenAI API.**

Built for Pre-Sales Engineers, Solutions Engineers, Sales Engineers, and Solution Architects who need to improve discovery quality, close gaps, and hand off clean documentation to engineering and product teams.

---

## The Problem It Solves

After a customer discovery call, a senior SE typically spends **2–4 hours** converting messy notes into:

- An executive summary for leadership
- A requirements document for engineering
- Gap analysis and missing questions
- A follow-up brief for the next meeting

Discovery Copilot automates the entire documentation layer in one command, so SEs can focus on the conversation — not the paperwork.

**Measured impact:** 2–4 hours of post-meeting documentation → under 60 seconds.

---

## What It Generates

One command produces 11 structured Markdown reports:

| # | Report | Purpose |
|---|--------|---------|
| 1 | Executive Summary | Leadership review — business goals, pain points, expected outcomes |
| 2 | Customer Profile | Industry, maturity, stakeholders, existing tech, digital transformation level |
| 3 | Business Challenges | Operational problems, bottlenecks, manual processes, risks |
| 4 | Technical Requirements | Explicit, implicit, security, integration, scalability, and infrastructure requirements |
| 5 | Discovery Gaps | What's missing — and why it matters before solution design |
| 6 | Recommended Next Questions | Intelligent follow-ups grouped by Business, Technical, Security, Budget, and Timeline |
| 7 | Customer Meeting Brief | Polished internal briefing for engineering, product, or management handoff |
| 8 | Solution Recommendations | Architecture patterns that fit the scenario, with reasoning |
| 9 | Discovery Quality Score | 0–100 score across 7 dimensions with gap explanation |
| 10 | Discovery Maturity Assessment | Poor → Enterprise Ready classification with next-level roadmap |
| 11 | Next Steps | Prioritized action plan (P1–P5) for the SE and account team |

---

## Quick Start

```bash
# Clone and install
git clone https://github.com/fabricioartur/Discovery-Copilot.git
cd Discovery-Copilot
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Run the demo instantly — no API key needed
python main.py examples/northstar_retail_group/discovery_notes.md --provider mock

# Run with your own notes
cp .env.example .env          # add your OPENAI_API_KEY
python main.py input/my_notes.md
```

---

## Model Selection

Discovery Copilot supports three OpenAI models. The right model depends on the account complexity and your goals:

| Model | Cost (input / output per MTok) | Use When |
|-------|-------------------------------|----------|
| `gpt-5.4-mini` *(default)* | $0.75 / $4.50 | Routine discovery, daily use — fast and cost-efficient |
| `gpt-5.4` | $2.50 / $15.00 | Complex enterprise accounts and final deliverables |
| `gpt-5.5` | $5.00 / $30.00 | Strategic accounts, board-level reports, highest output quality |

```bash
# Default (fast, cost-efficient)
python main.py input/notes.md

# Complex enterprise account
python main.py input/notes.md --model gpt-5.4

# Strategic account — highest quality
python main.py input/notes.md --model gpt-5.5
```

The model can also be set via environment variable:

```env
OPENAI_MODEL=gpt-5.4
```

### Reasoning Effort

GPT-5 models support a `--reasoning` flag that controls how deeply the model thinks before producing output. This is the same parameter exposed in Codex.

| Level | Use When |
|-------|----------|
| `low` | Fast summaries and routine notes — lowest cost |
| `medium` | Balanced quality for standard enterprise accounts |
| `high` | Complex accounts, technical architecture, compliance-heavy scenarios |
| `extra_high` | Strategic accounts, board-level deliverables, maximum output quality |

```bash
# High-quality reasoning for a complex enterprise account
python main.py input/notes.md --model gpt-5.4 --reasoning high

# Maximum depth for a strategic account
python main.py input/notes.md --model gpt-5.5 --reasoning extra_high
```

> **Note:** When `--reasoning` is set, `temperature` is disabled — reasoning models control their own sampling internally.

---

## CLI Reference

```
usage: discovery-copilot [-h] [--provider {openai,mock}] [--model MODEL]
                         [--reasoning LEVEL] [--output DIR] [--verbose]
                         input_file

positional arguments:
  input_file            Path to a .txt or .md discovery notes file.

options:
  --provider {openai,mock}
                        'mock' runs locally without an API key. (default: openai)
  --model MODEL         gpt-5.4-mini | gpt-5.4 | gpt-5.5 (default: gpt-5.4-mini)
  --reasoning LEVEL     low | medium | high | extra_high — reasoning effort for
                        GPT-5 models. Higher effort = deeper analysis, higher cost.
  --output DIR          Directory for generated reports. (default: ./output)
  --verbose             Enable debug logging for API calls.
```

---

## Architecture

```
input (.txt / .md)
       │
       ▼
┌─────────────────────┐
│   input_loader.py   │  validates format, encoding, emptiness
└─────────────────────┘
       │
       ▼
┌─────────────────────┐   ┌──────────────────────────┐
│    generator.py     │──▶│  prompts/system_prompt.md │
│  ThreadPoolExecutor │   │  prompts/report_prompt.md │
│   (4 threads)       │   └──────────────────────────┘
└─────────────────────┘
       │ 11 parallel API calls
       ▼
┌──────────────────────────────────────┐
│        ReportGenerationClient        │
│  (Protocol — pluggable by design)    │
│                                      │
│  DiscoveryOpenAIClient               │
│  • timeout: 60s                      │
│  • retry: 3x with exponential backoff│
│  • temperature: 0.2 (deterministic)  │
│                                      │
│  MockDiscoveryClient                 │
│  • no API key required               │
│  • deterministic output for demos    │
└──────────────────────────────────────┘
       │
       ▼
  output/ (11 Markdown files)
```

### Architecture Decisions

**Why `temperature=0.2`?**
Pre-sales documentation must be factual and consistent. Low temperature suppresses hallucination and keeps output reproducible across runs. Creative temperature settings are appropriate for copy or brainstorming — not for compliance matrices and technical requirements.

**Why parallel report generation?**
Each report is an independent prompt. Sequential generation wastes ~50 idle seconds waiting for API responses. `ThreadPoolExecutor(max_workers=4)` keeps OpenAI rate limits comfortable while cutting wall-clock time by ~4x.

**Why a Protocol for the client interface?**
The `ReportGenerationClient` Protocol (not a base class) allows switching providers — OpenAI, Azure OpenAI, a local model, or the mock — without touching the orchestration logic. This is the same pluggable-client pattern you'd recommend to a customer building their own LLM integration.

**Why separated prompt templates?**
Keeping prompts in `.md` files instead of Python strings lets non-engineers edit and version them independently. It also makes prompt engineering visible in git history — a best practice for any production LLM application.

**Why retry with exponential backoff?**
Enterprise deployments often hit OpenAI rate limits during burst usage. The client retries up to 3 times (2s → 4s → 8s delays) before failing. This is the standard resilience pattern for any API-dependent service.

---

## Project Structure

```
discovery-copilot/
├── main.py                          # CLI entrypoint
├── pyproject.toml                   # Package config, ruff, mypy
├── requirements.txt
├── requirements-dev.txt
├── .env.example
├── .github/
│   └── workflows/ci.yml             # GitHub Actions: test + lint + type-check
├── prompts/
│   ├── system_prompt.md             # SE persona and output rules
│   └── report_prompt.md             # Per-report template
├── src/
│   ├── config.py                    # Settings, model registry
│   ├── client_protocol.py           # Pluggable client Protocol
│   ├── openai_client.py             # OpenAI wrapper (timeout, retry, logging)
│   ├── mock_client.py               # Local demo client (no API key)
│   ├── generator.py                 # Parallel orchestration
│   ├── input_loader.py              # Validation and loading
│   ├── reports.py                   # 11 report definitions
│   └── exceptions.py                # Exception hierarchy
├── tests/
│   ├── test_input_loader.py
│   ├── test_mock_generation.py
│   └── test_openai_client.py        # Error path tests (rate limit, timeout, retry)
├── utils/
│   └── files.py
├── input/
│   └── sample_discovery_notes.md
├── output/                          # Generated reports (git-ignored)
└── examples/
    └── northstar_retail_group/      # Full enterprise scenario
```

---

## Enterprise Example: Northstar Retail Group

The repository includes a complete fictional enterprise scenario: **Northstar Retail Group**, a large retailer with 420 stores, e-commerce, WhatsApp support, and legacy systems across Latin America — a realistic complex-account discovery scenario.

### Run the example

```bash
python main.py examples/northstar_retail_group/discovery_notes.md --provider mock
```

### Sample Discovery Quality Score

| Category | Score |
|----------|------:|
| Business Understanding | 82 |
| Technical Understanding | 76 |
| Security Understanding | 68 |
| Stakeholder Mapping | 84 |
| Requirements Completeness | 71 |
| Risk Identification | 79 |
| Architecture Readiness | 74 |
| **Overall Discovery Score** | **76** |

### Requirements Coverage

| Area | Coverage |
|------|--------:|
| Business Requirements | 80% |
| Technical Requirements | 69% |
| Security Requirements | 58% |
| Integration Requirements | 73% |
| Infrastructure Requirements | 56% |
| Success Metrics | 50% |
| Stakeholder Mapping | 88% |

### Example Visuals

![Discovery Copilot overview banner](examples/northstar_retail_group/visuals/overview_banner.png)

![Discovery Copilot workflow](examples/northstar_retail_group/visuals/discovery_copilot_workflow.png)

![Northstar target architecture](examples/northstar_retail_group/visuals/northstar_target_architecture.png)

![Discovery scores and requirements coverage](examples/northstar_retail_group/visuals/discovery_scores_and_coverage.png)

### Generated Output Previews

| Report | Preview |
|--------|---------|
| [Executive Summary](examples/northstar_retail_group/generated_outputs/Executive%20Summary.md) | ![](examples/northstar_retail_group/output_previews/01_executive_summary.png) |
| [Customer Profile](examples/northstar_retail_group/generated_outputs/Customer%20Profile.md) | ![](examples/northstar_retail_group/output_previews/02_customer_profile.png) |
| [Business Challenges](examples/northstar_retail_group/generated_outputs/Business%20Challenges.md) | ![](examples/northstar_retail_group/output_previews/03_business_challenges.png) |
| [Technical Requirements](examples/northstar_retail_group/generated_outputs/Technical%20Requirements.md) | ![](examples/northstar_retail_group/output_previews/04_technical_requirements.png) |
| [Discovery Gaps](examples/northstar_retail_group/generated_outputs/Discovery%20Gaps.md) | ![](examples/northstar_retail_group/output_previews/05_discovery_gaps.png) |
| [Recommended Next Questions](examples/northstar_retail_group/generated_outputs/Recommended%20Next%20Questions.md) | ![](examples/northstar_retail_group/output_previews/06_recommended_next_questions.png) |
| [Customer Meeting Brief](examples/northstar_retail_group/generated_outputs/Customer%20Meeting%20Brief.md) | ![](examples/northstar_retail_group/output_previews/07_customer_meeting_brief.png) |
| [Solution Recommendations](examples/northstar_retail_group/generated_outputs/Solution%20Recommendations.md) | ![](examples/northstar_retail_group/output_previews/08_solution_recommendations.png) |
| [Discovery Quality Score](examples/northstar_retail_group/generated_outputs/Discovery%20Quality%20Score.md) | ![](examples/northstar_retail_group/output_previews/09_discovery_quality_score.png) |
| [Discovery Maturity Assessment](examples/northstar_retail_group/generated_outputs/Discovery%20Maturity%20Assessment.md) | ![](examples/northstar_retail_group/output_previews/10_discovery_maturity_assessment.png) |
| [Next Steps](examples/northstar_retail_group/generated_outputs/Next%20Steps.md) | ![](examples/northstar_retail_group/output_previews/11_next_steps.png) |

---

## Testing

```bash
# Full test suite
python -m unittest discover -v

# Lint
ruff check .

# Type check
mypy src/ utils/ main.py --ignore-missing-imports
```

Test coverage includes:
- Input validation (missing file, unsupported format, empty document, encoding errors)
- Full mock report generation pipeline
- OpenAI client error paths: rate limit with retry, connection error, API status errors, empty response, unexpected exceptions

---

## Design Philosophy

Discovery Copilot is not a chatbot. It is a focused productivity tool for enterprise pre-sales work.

The emphasis is on **structured outputs**, **discovery quality**, and **practical documentation** that saves time after customer meetings — the same principles that should guide any LLM application built for enterprise B2B workflows.

---

## Requirements

- Python 3.9+
- OpenAI API key (not required for `--provider mock`)

---

## License

Copyright (c) 2026 Fabricio Artur. Released under the MIT License. See [LICENSE](LICENSE) for details.
