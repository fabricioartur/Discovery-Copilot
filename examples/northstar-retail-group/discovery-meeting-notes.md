# Discovery Meeting Notes - Northstar Retail Group

## Account Context

Customer: Northstar Retail Group
Industry: Retail and e-commerce
Region: Latin America
Store footprint: 420 physical stores across Brazil, Mexico, Chile, Colombia,
and Peru
Digital channels: Regional e-commerce sites, mobile app, marketplace
integrations, WhatsApp customer support, and loyalty program
Meeting type: Initial technical discovery

Northstar Retail Group operates supermarkets, pharmacies, convenience stores,
and an expanding e-commerce business across Latin America. The company grew
through acquisitions, leaving each country with different technology stacks,
integration patterns, and support processes.

## Meeting Participants

- Ana Ribeiro, VP Customer Experience
- Mateo Alvarez, Director of Digital Operations
- Sofia Mendes, Head of Enterprise Architecture
- Bruno Costa, IT Integration Manager
- Luciana Torres, Security and Compliance Lead
- Diego Salazar, Customer Support Operations Manager
- Pre-sales team: Solutions Engineer and Account Executive

## Business Goals

- Reduce customer support average handling time by at least 25%.
- Improve order visibility across store, warehouse, and e-commerce channels.
- Reduce manual reconciliation between ERP, OMS, and CRM systems.
- Standardize customer service workflows across Latin America.
- Launch a pilot within 90 days for Brazil and Mexico support teams.

## Current Environment

- ERP: SAP ECC in Brazil and Mexico; Oracle E-Business Suite in Chile and Peru.
- CRM: Salesforce Service Cloud for regional customer support teams.
- Support: Zendesk still used by acquired store brands.
- OMS: Legacy on-premises order management with nightly batch updates.
- E-commerce: Magento Brazil, custom Node.js storefront Mexico, marketplace
  connectors for regional partners.
- Identity: Microsoft Entra ID, plus local identity stores for some store apps.
- Data warehouse: Snowflake with mostly daily refreshes.
- Integration: MuleSoft APIs, point-to-point SOAP, SFTP drops, and database
  exports.
- Cloud: AWS for e-commerce, Azure for identity, VMware data centers for legacy
  retail systems.

## Pain Points

- Agents switch between Salesforce, SAP, OMS screens, Zendesk, and spreadsheets.
- Store managers receive exception reports once per day.
- Loyalty data is not consistently available during support interactions.
- Refund approvals require manual checks across ERP, payment gateway, and order
  history.
- Country teams use different case categories and escalation rules.
- Batch integrations create stale information for order status questions.
- Peak season volume causes support backlogs.

## AI and Automation Interest

Northstar wants an internal AI assistant for support agents and store operations
teams. The assistant should summarize order context, recommend next actions,
surface policy guidance, and create case notes. The assistant is not planned as
customer-facing in the first phase.

Architecture asked whether the solution could use retrieval augmented generation
over approved knowledge articles, call enterprise APIs for structured data, and
maintain audit trails for generated recommendations.

## Stated Requirements

- Integrate with Salesforce Service Cloud for case context and note updates.
- Retrieve order status from legacy OMS and selected ERP systems.
- Support Microsoft Entra ID single sign-on.
- Maintain audit trails for assistant responses and agent actions.
- Provide a Brazil and Mexico pilot within 90 days.
- Avoid direct ERP write access during phase one.
- Support Portuguese and Spanish content.
- Use approved knowledge articles and operating procedures as source material.
- Provide dashboards for pilot adoption, deflection, and handling-time impact.

## Security and Compliance Notes

- Customer data includes names, phones, addresses, payment status, loyalty IDs,
  and order history.
- PCI scope must be avoided; no full card data should be processed.
- LGPD is mandatory for Brazil.
- Data retention controls are required for prompts, responses, and audit logs.
- Role-based access must prevent cross-region exposure of sensitive notes.
- Customer asked whether model inputs can be redacted before processing.

## Integration Notes

- MuleSoft is preferred for new reusable APIs.
- Some OMS functions only expose SOAP endpoints.
- SAP data is available through existing services, but not all fields are
  API-ready.
- Zendesk migration to Salesforce will not finish before the pilot.
- Snowflake can support analytics but not real-time lookup.
- Store connectivity can be unreliable in some regions.

## Open Questions

- Exact number of pilot users was not confirmed.
- Budget owner and approved budget range were not confirmed.
- Required SLA was not defined.
- Data residency requirements were not clarified by country.
- Disaster recovery expectations were not discussed.
- Source of truth for customer identity was unclear.
- Knowledge article quality and approval status are unknown.
- Success metrics were not baselined.
- Model governance process was not explained.
- Zendesk migration timeline dependencies were not fully mapped.

## Desired Next Step

Northstar requested a follow-up technical workshop with enterprise architecture,
security, support operations, and regional IT leads. The workshop should focus
on pilot scope, integration feasibility, data access, governance, and success
metrics.
