# Security Policy

## Supported Versions

Discovery Copilot is currently an open-source example project. Security fixes
are applied to the `main` branch.

## Reporting a Vulnerability

If you find a security issue, please open a private report through GitHub's
security advisory flow or contact the repository owner directly.

Do not include real customer discovery notes, API keys, personal data, payment
data, credentials, or proprietary system details in public issues.

## Data Handling Notes

Discovery Copilot processes local `.txt` and `.md` files and sends prompt
content to the selected provider when using the OpenAI mode. Review and redact
sensitive customer data before processing real discovery notes.

For demos, use:

```bash
python3 main.py examples/northstar_retail_group/discovery_notes.md --provider mock
```

Mock mode runs locally and does not call the OpenAI API.
