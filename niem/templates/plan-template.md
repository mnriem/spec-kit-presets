## NIEM Exchange Design

Complete for exchanges in scope, or state why not applicable. Resolve blockers
under the normal planning gates rather than treating these fields as defaults.

| Decision | Selected value and evidence |
|----------|-----------------------------|
| Model baseline | [Release and immutable artifact source] |
| Rules and conformance targets | [NDR edition/publication stage and applicable targets] |
| Core and domain namespaces | [Namespace URIs, versions, and ownership] |
| Model representation | [XSD or CMF; rationale] |
| Message formats | [XML, JSON, or explicitly scoped formats; applicable rules] |
| Local extensions | [Namespace owner and justified gaps, or none] |
| Compatibility | [Producer/consumer versions, evolution policy, rollback needs] |

### Design Artifacts

- `research.md`: source provenance, reuse candidates, rejected alternatives, and
  extension rationale.
- `data-model.md`: business-to-NIEM mappings using the installed
  `.specify/presets/niem/templates/niem-mapping-template.md`, plus constraints.
- `contracts/`: exchange contract, message structure, business rules, and agreed
  format/schema requirements. Distinguish design drafts from validated artifacts.
- `quickstart.md`: prerequisites and runnable scenarios for the agreed checks,
  without embedding implementation code.

### Evidence Plan

| Required claim | Applicable check / review | Tool and version or reviewer | Inputs and expected result | Evidence destination |
|----------------|--------------------------|-----------------------------|----------------------------|----------------------|
| [Claim required by spec/constitution] | [Model, schema, message, business rule, or interoperability check] | [Verified capability] | [Positive/negative scenario] | [Project-relative path] |

List unavailable sources/tools and unresolved mappings as blockers where they
prevent an agreed gate from passing. Do not install tools or claim checks ran as
part of writing this plan.
