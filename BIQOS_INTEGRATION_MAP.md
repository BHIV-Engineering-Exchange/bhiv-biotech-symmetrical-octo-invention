# BIQOS Integration Map — Pharmaceutical Evidence Quality



**Workstream:** Pharmaceutical Evidence Quality

**Owner:** Shyamal Jadhav

**Project:** BHIV BiotechSystem

**Date:** 16 November 2026



## 1\. Purpose



This document describes how the Pharmaceutical Evidence Quality workstream can integrate with the broader BIQOS architecture.



The objective is to connect evidence collection, provenance, structured validation, quality assessment and review outputs while maintaining traceability and scientific limitations.



## 2\. Current Workstream Assets



| Asset | Current status | Evidence |

|---|---|---|

| QC Engine | Implemented and tested | 28 automated tests passed |

| JSON Schema validation | Implemented and tested | Schema validation tests |

| Evidence Framework | Implemented as a research evidence-mapping asset | Source, evidence, claim and contradiction registers |

| Evidence Data Dictionary | Documented | EVIDENCE\_DATA\_DICTIONARY.md |

| QC Engine Rule Inventory | Documented | QC\_ENGINE\_RULE\_INVENTORY.md |

| Domain Maturity Assessment | Documented | DOMAIN\_MATURITY\_GAP\_ASSESSMENT.md |

| Evidence Packet | Assembled | Code, sample output, review packet, runtime log and screenshots |

| Dedicated formulation QC | Not demonstrated | Development gap |

| Dedicated stability QC | Not demonstrated | Development gap |



## 3\. BIQOS Component Integration



| BIQOS component | Relevant responsibility | Proposed connection to Pharmaceutical Evidence Quality | Status |

|---|---|---|---|

| TMS | Strategy and prioritization | Define evidence quality objectives and domain priorities | Proposed |

| GC | Governance and control | Define review responsibilities, approval boundaries and governance rules | Proposed |

| MDU | Data schema, provenance, lineage and semantics | Align evidence records, data dictionary, identifiers and provenance | Proposed |

| MASTERDB / Bucket | Retrieval, storage and provenance | Store and retrieve evidence records, source references and QC outputs | Proposed |

| TANTRA | Execution contracts and orchestration | Coordinate validation workflows and QC engine execution | Proposed |

| InsightFlow / Replay | Observability and replay | Track QC results, execution history, errors and reproducibility | Proposed |



**Status interpretation:** Proposed means an integration design has been identified but operational implementation has not been verified. The existing QC engine's local implementation and automated tests do not prove BIQOS integration.



## 4\. Proposed Integration Workflow



1\. Evidence sources and records are collected.

2\. The evidence framework registers sources, evidence, claims and contradictions.

3\. A unified evidence mapping layer aligns framework records with the QC engine schema.

4\. The QC engine validates records and evaluates completeness, duplicates, conflicts and review requirements.

5\. QC outputs are made available for expert review and downstream storage.

6\. Execution results and review history can be monitored and replayed through suitable BIQOS services.



## 5\. Integration Architecture



Evidence Sources

↓

Evidence Framework

(Source Register, Evidence Map, Claim Traceability, Contradiction Register)

↓

Unified Evidence Mapping Layer — Proposed

(Schema Mapping, Identifier Preservation, Provenance, Category Mapping)

↓

Pharmaceutical Evidence QC Engine — Implemented and Tested Locally

(Validation, Completeness, Classification, Duplicate Detection, Conflict Detection, Human Review)

↓

QC Review Output

↓

Proposed BIQOS Integration

(MDU, MASTERDB/Bucket, TANTRA, InsightFlow/Replay, GC and TMS)



## 6\. Important Data and Governance Requirements



The integration should preserve:



\- Original source identifiers and source references.

\- Evidence IDs, study IDs and claim IDs.

\- Original evidence categories and mapped categories.

\- Evidence limitations and contradiction status.

\- Real versus synthetic data declarations.

\- QC classification and human-review status.

\- Schema version and processing history.



The mapping layer must not silently convert one evidence category into another or remove uncertainty and limitations.



## 7\. Priority Integration Gaps



| Priority | Gap | Recommended next action |

|---|---|---|

| High | No verified unified schema mapping | Define field-level mapping between evidence framework and QC engine |

| High | No demonstrated BIQOS data exchange | Agree on input/output contracts |

| High | Formulation QC is not domain-specific | Define formulation fields and validation rules |

| High | Stability QC is not domain-specific | Define stability fields and validation rules |

| Medium | No demonstrated execution orchestration | Define TANTRA execution contract |

| Medium | No demonstrated observability/replay connection | Define InsightFlow/Replay logging requirements |

| Medium | Governance workflow not demonstrated | Define GC review and approval boundaries |



## 8\. Recommended Next Product Increment



**Unified Pharmaceutical Evidence Quality Integration Layer**



The next increment should:



1\. Map evidence framework records to the QC engine input schema.

2\. Preserve source, evidence and claim traceability.

3\. Preserve contradictions and limitations.

4\. Maintain real-versus-synthetic data declarations.

5\. Introduce formulation-specific and stability-specific QC rules.

6\. Produce structured outputs suitable for future BIQOS integration.

7\. Include automated tests using clearly labelled synthetic records.



## 9\. Scientific and Operational Boundaries



The current QC engine is a locally implemented and tested software component. No operational connection to BIQOS components is claimed by this document.



The integration design is a proposal, not evidence of deployed interoperability.



QC results support evidence organization and review. They do not independently establish biosimilarity, clinical equivalence, safety, efficacy, shelf life or regulatory compliance.
