# QC Engine Rule Inventory

**Workstream:** Pharmaceutical Evidence Quality

**Project:** BHIV BiotechSystem

**Engine:** Biosimilarity \& Preclinical Evidence QC Engine

**Version:** 1.0.0

**Verification status:** Implemented and automated tests passed



## 1. Purpose



The QC Engine performs structured quality checks on pharmaceutical and preclinical evidence records. It identifies missing information, invalid records, duplicate identifiers, conflicting study information and records requiring human review.



The engine supports evidence quality assessment. It does not independently establish biosimilarity, clinical equivalence, safety, efficacy or regulatory validity.



## 2. Implemented QC Rules



| No. | QC rule | Engine function | Implementation status |

|---|---|---|---|

| 1 | JSON Schema validation | `get\_schema\_validator()` | Implemented |

| 2 | Required-field validation | `validate\_record()` | Implemented |

| 3 | Evidence status validation | `validate\_record()` | Implemented |

| 4 | Completeness assessment | `completeness()` | Implemented |

| 5 | Duplicate evidence ID detection | `detect\_duplicates()` | Implemented |

| 6 | Duplicate study ID detection | `detect\_duplicates()` | Implemented |

| 7 | Conflicting study information detection | `detect\_conflicts()` | Implemented |

| 8 | Evidence quality classification | `classify\_record()` | Implemented |

| 9 | Human-review requirement identification | `human\_review\_required()` | Implemented |

| 10 | Dataset-level QC processing | `process\_dataset()` | Implemented |

| 11 | Synthetic/real data declaration validation | `validate\_record()` | Implemented |

| 12 | Candidate/reference comparison function | `compare\_candidate\_reference()` | Function present; detailed rule verification pending |



## 3. Evidence Quality Classification



The engine uses five evidence-quality states:



\- **VERIFIED:** Record meets the engine's applicable QC requirements.

\- **PARTIAL:** Evidence has limitations or incomplete review status.

\- **NEEDS REVIEW:** Additional review is required.

\- **CONFLICTING:** Inconsistent evidence values have been identified.

\- **INSUFFICIENT:** Required evidence information is incomplete or inadequate.



These are software QC classifications, not scientific conclusions.



## 4. Validation and Review Controls



The engine checks:

\- Required evidence identifiers and study information.

\- Source and protocol references.

\- Experimental conditions and measurement methods.

\- Method validation and raw-data availability.

\- Missing data, deviations and statistical reporting.

\- Reproducibility and limitations.

\- Evidence category and review status.

\- Synthetic-data declaration.

\- JSON Schema compliance.



Conflicting values are retained and flagged rather than silently resolved.



## 5. Automated Test Evidence



**Latest reported test result: 28 passed.**



The automated test suite covers:

\- Evidence tracker operations.

\- JSON Schema validation.

\- Complete and invalid evidence records.

\- Missing information and invalid status values.

\- Duplicate identifiers.

\- Conflict detection.

\- Evidence classification.

\- Human-review requirements.

\- Dataset processing and repeatability.

\- Synthetic-data declaration preservation.

\- Prevention of unsupported scientific conclusions.



## 6. Current Domain Coverage and Gaps



| Domain | Current coverage | Remaining gap |

|---|---|---|

| Biosimilarity | General evidence QC and candidate/reference comparison function | Dedicated scientific biosimilarity assessment and domain-specific acceptance criteria |

| Preclinical | Evidence validation, completeness, conflicts and review controls | Dedicated study-design and preclinical domain rules |

| Formulation | General evidence-record QC | Dedicated formulation attributes and acceptance criteria |

| Stability | General evidence-record QC | Dedicated stability parameters, time-point checks and acceptance criteria |



Formulation and stability are not demonstrated as dedicated QC modules in the inspected engine functions.



## 7. Data Integrity and Limitations



The engine supports explicit data declarations:

\- `SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING`

\- `REAL / SOURCE-VERIFIED`



Synthetic records must remain identified as synthetic. Automated validation does not independently authenticate real-world source documents or verify scientific truth.



## 8. Recommended Next Development Increment



Develop a unified Pharmaceutical Evidence Quality Integration Layer to connect the evidence framework with the QC engine.



Priority improvements:

1\. Map evidence framework records to QC engine records while preserving original categories.

2\. Preserve source IDs, evidence IDs, claim IDs and provenance.

3\. Introduce dedicated formulation QC rules.

4\. Introduce dedicated stability QC rules.

5\. Add synthetic test records for new domain-specific rules.

6\. Verify integration through automated tests.



## 9. Overall Assessment



The existing QC engine provides a tested foundation for structured pharmaceutical and preclinical evidence quality control. Its current strengths are record validation, completeness assessment, duplicate and conflict detection, evidence classification, human-review identification and schema validation.



Further domain-specific development is required before claiming dedicated formulation and stability QC coverage.



**Scientific boundary:** The engine is a software quality-control and evidence-review support tool. It does not replace expert scientific assessment, laboratory verification or regulatory review.
