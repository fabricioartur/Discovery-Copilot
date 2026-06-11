# Technical Requirements

## Explicit Requirements

- Integrate with Salesforce Service Cloud for case context and case note updates.
- Retrieve order status from the legacy OMS and selected ERP systems.
- Support Microsoft Entra ID single sign-on.
- Maintain audit trails for assistant responses and agent actions.
- Deliver a Brazil and Mexico pilot within 90 days.
- Avoid direct ERP write access during phase one.
- Support Portuguese and Spanish.
- Use approved knowledge articles and operating procedures as source material.
- Provide dashboards for adoption, deflection, and handling-time impact.

## Implicit Requirements

- Provide real-time or near-real-time access to order information.
- Normalize inconsistent regional support processes.
- Add a reusable integration layer instead of point-to-point AI integrations.
- Provide confidence indicators or source citations for generated guidance.
- Support phased rollout by country, role, and channel.

## Security Requirements

- Enforce Microsoft Entra ID authentication.
- Apply role-based access controls by region and job function.
- Redact sensitive personal data before model processing where possible.
- Avoid PCI scope by excluding full card data.
- Maintain prompt, response, and action audit logs.
- Define retention policies for AI interaction data.
- Support LGPD obligations for Brazil and clarify other country requirements.

## Integration Requirements

- Salesforce Service Cloud integration.
- Zendesk coexistence during migration.
- MuleSoft as preferred API gateway.
- OMS data retrieval, including SOAP-backed functions.
- SAP ECC and Oracle E-Business Suite read access through approved services.
- Snowflake analytics for reporting and measurement.

## Scalability Requirements

- Handle support volume spikes during peak retail seasons.
- Support multi-country rollout after the pilot.
- Isolate pilot scope while preserving a path to enterprise reuse.
- Provide monitoring for latency, API errors, usage, and adoption.

## Infrastructure Requirements

- Operate across AWS, Azure, and on-premises systems.
- Respect unreliable store connectivity in some regions.
- Avoid direct writes to ERP in the first phase.
- Provide secure access to enterprise APIs and approved knowledge repositories.
