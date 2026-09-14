## NIEM Component Mapping

Use this section inside the feature's existing `data-model.md`; do not create
another feature directory or duplicate the full NIEM reference model. Repeat the
record below for each information requirement with a distinct mapping decision.

**Model baseline**: [Release, artifact path/URL, immutable tag/commit or checksum]

**Applicable rules**: [NDR edition, publication stage, conformance targets]

### [Business Concept]

| Field | Mapping decision |
|-------|------------------|
| Requirement / story | [FR-### / US#] |
| Business meaning | [Meaning agreed by exchange partners] |
| Mapping status | [Verified reuse / proposed local extension / unverified candidate] |
| Component QName | [Verified prefix:local-name, or explicitly unverified candidate] |
| Namespace identity | [Full namespace URI and prefix binding] |
| Definition and provenance | [Definition summary and exact model artifact location] |
| Type / representation | [Verified type and relevant representation constraints] |
| Cardinality / presence | [Required, optional, repeated; absent/unknown/empty semantics] |
| Identity / relationships | [Identifiers, references, associations, or not applicable] |
| Values | [Code-list source/version, units, ranges, or not applicable] |
| Transformation | [Producer/consumer mapping and any intentional information loss] |
| Extension rationale | [Search evidence, gap, local owner, chosen NDR pattern; or none] |
| Contract / evidence | [Links to contract and required checks; execution status if available] |

Unverified candidates must not be presented as authoritative components or used
to claim a passed design gate. Record what evidence is missing and who must
resolve it. A local namespace proposal does not constitute an official NIEM
domain or Core addition.
