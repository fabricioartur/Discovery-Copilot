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
Meeting date: Fictional sample scenario

Northstar Retail Group is a large retail organization operating supermarkets,
pharmacies, convenience stores, and an expanding e-commerce business across
Latin America. The company has grown through acquisitions, leaving each country
with different technology stacks, integration patterns, and operating models.

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
- Provide store managers with faster access to operational exceptions.
- Standardize customer service workflows across Latin America.
- Launch a pilot within 90 days for Brazil and Mexico support teams.
- Improve customer satisfaction scores during peak shopping seasons.

## Current Environment

Northstar operates a fragmented technology environment:

- ERP: SAP ECC in Brazil and Mexico, Oracle E-Business Suite in Chile and Peru.
- CRM: Salesforce Service Cloud used by regional customer support teams.
- Customer support: Zendesk is still used by acquired store brands.
- Order management: Legacy on-premises OMS with nightly batch updates.
- E-commerce: Magento for Brazil, custom Node.js storefront in Mexico, and
  marketplace connectors for regional partners.
- Identity: Microsoft Entra ID for corporate users; local identity stores still
  exist for some store applications.
- Data warehouse: Snowflake for consolidated reporting, refreshed mostly in
  daily batches.
- Integration: Mix of MuleSoft APIs, point-to-point SOAP integrations, SFTP
  drops, and scheduled database exports.
- Cloud: AWS for e-commerce workloads, Azure for productivity and identity,
  VMware-based data centers for legacy retail systems.

## Pain Points Discussed

- Support agents switch between Salesforce, SAP, OMS screens, Zendesk, and
  spreadsheets to answer simple order questions.
- Store managers receive exception reports once per day, which is too late for
  same-day fulfillment issues.
- Loyalty data is not consistently available during support interactions.
- Refund approvals require manual checks across ERP, payment gateway, and order
  history.
- Country teams use different case categories and escalation rules.
- Batch integrations create stale information for customers asking about order
  status.
- Peak season volume causes support backlogs and inconsistent responses.
- Architecture team is concerned about adding another isolated tool without a
  reusable integration layer.

## AI and Automation Interest

The customer is interested in an internal AI assistant for support agents and
store operations teams. The initial idea is not customer-facing. Northstar wants
the assistant to summarize order context, recommend next actions, surface policy
guidance, and create case notes.

The architecture team asked whether the solution could use retrieval augmented
generation over approved knowledge articles, return structured data from
enterprise APIs, and maintain audit trails for generated recommendations.

Security emphasized that the assistant must not expose customer personal data
outside approved boundaries and must respect role-based access controls.

## Stated Requirements

- Integrate with Salesforce Service Cloud for case context and case note
  updates.
- Retrieve order status from the legacy OMS and selected ERP systems.
- Support Microsoft Entra ID single sign-on for corporate users.
- Maintain an audit trail of assistant responses and agent actions.
- Provide a pilot for Brazil and Mexico within 90 days.
- Avoid direct write access to ERP during the first phase.
- Support Portuguese and Spanish content for the pilot teams.
- Use approved knowledge articles and operating procedures as source material.
- Provide dashboards for pilot adoption, deflection, and handling-time impact.

## Security and Compliance Notes

- Northstar handles customer names, phone numbers, addresses, payment status,
  loyalty identifiers, and order history.
- PCI scope must be avoided; the assistant should not process full card data.
- LGPD is mandatory for Brazil. Mexico and Chile privacy requirements were
  mentioned but not detailed.
- Security wants data retention controls for prompts, responses, and audit logs.
- Role-based access must prevent store users from viewing sensitive customer
  support notes outside their region.
- The customer asked whether model inputs can be redacted before processing.

## Integration Notes

- MuleSoft is the preferred API gateway for new reusable services.
- Some OMS functions only expose SOAP endpoints.
- SAP data is available through existing integration services but not all
  required fields are API-ready.
- Zendesk migration into Salesforce is planned but will not be complete before
  the pilot.
- Snowflake can be used for analytics but is not suitable for real-time order
  lookup.
- Store systems have unreliable connectivity in some regions.

## Open Questions From Meeting

- Exact number of pilot users was not confirmed.
- Budget owner and approved budget range were not confirmed.
- Required service-level agreement was not defined.
- Data residency requirements were mentioned but not clarified by country.
- Disaster recovery expectations were not discussed.
- Exact source of truth for customer identity was unclear.
- It is unknown whether all knowledge articles are current and approved.
- Success metrics were discussed directionally but not baselined.
- The customer's model governance process was not explained.
- Timeline dependencies on Zendesk migration were not fully mapped.

## Risks Mentioned

- Integration complexity across multiple ERP and OMS systems.
- Incomplete or stale knowledge articles could reduce assistant trust.
- Data privacy review may delay the pilot.
- Store network reliability could affect operational use cases.
- Country-specific processes may make standardization difficult.
- Pilot expectations may be too broad for a 90-day window.

## Desired Next Step

Northstar requested a follow-up technical workshop with enterprise architecture,
security, support operations, and regional IT leads. The workshop should focus
on pilot scope, integration feasibility, data access, governance, and success
metrics.
