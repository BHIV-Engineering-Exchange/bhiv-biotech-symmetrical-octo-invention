# Evidence and Data Dictionary



## 1\. Purpose



This document defines the fields used in the Pharmaceutical Scientific Evidence Framework. It explains how source, evidence, claim and contradiction records are structured and linked.



## 2\. Source Register — source\_register.csv



| Field | Meaning |

|---|---|

| source\_id | Unique identifier for the original source. |

| title | Title of the publication or source. |

| authors\_or\_organization | Authors or responsible organization. |

| publication\_year | Year of publication. |

| source\_type | Type of source, such as review or government information. |

| journal\_or\_organization | Journal or organization responsible for the source. |

| url\_or\_identifier | URL, DOI or other source identifier. |

| access\_date | Date the source was accessed. |

| authority\_level | Recorded assessment of source authority. |

| relevance | Relevance of the source to the research question. |

| version | Source version or publication version. |

| provenance\_note | Information about source origin and verification. |



## 3\. Evidence Map — evidence\_map.csv



| Field | Meaning |

|---|---|

| evidence\_id | Unique identifier for an evidence record. |

| source\_id | Identifier linking evidence to its source. |

| concept | Research concept or subject. |

| evidence\_category | Type of evidence, such as IN\_VITRO or SYSTEMATIC\_REVIEW. |

| study\_design | Design or type of investigation. |

| population\_or\_model | Human population or experimental model studied. |

| intervention\_or\_exposure | Intervention or exposure evaluated. |

| comparator | Comparison group or intervention, where applicable. |

| outcome | Outcome measured or evaluated. |

| main\_finding | Concise description of the reported finding. |

| evidence\_strength | Recorded evidence-strength category. |

| limitations | Important limitations of the evidence. |

| contradiction\_status | Whether contradictory findings are recorded. |

| provenance\_note | Origin and interpretation notes for the evidence record. |



## 4\. Claim Traceability — claim\_traceability.csv



| Field | Meaning |

|---|---|

| claim\_id | Unique identifier for a scientific claim. |

| evidence\_id | Evidence record supporting or relating to the claim. |

| source\_id | Original source associated with the claim. |

| claim\_text | Exact or carefully qualified claim statement. |

| evidence\_type | Evidence category associated with the claim. |

| evidence\_strength | Recorded strength of supporting evidence. |

| limitations | Limitations affecting interpretation of the claim. |

| contradiction\_status | Status of conflicting evidence. |

| provenance\_note | Explanation of the claim's source and interpretation. |



## 5\. Contradiction Register — contradiction\_register.csv



| Field | Meaning |

|---|---|

| contradiction\_id | Unique contradiction identifier. |

| claim\_id | Claim affected by the contradiction. |

| evidence\_id\_a | First related evidence record. |

| source\_id\_a | Source of the first evidence record. |

| evidence\_id\_b | Second related evidence record. |

| source\_id\_b | Source of the second evidence record. |

| conflict\_type | Nature of the disagreement. |

| position\_a | Finding or position from the first source. |

| position\_b | Finding or position from the second source. |

| possible\_explanation | Potential reasons for the disagreement. |

| resolution\_status | Whether the contradiction is open or resolved under a stated rule. |

| final\_interpretation | Current interpretation of the contradiction. |

| provenance\_note | Explanation of the origin and handling of the conflict. |



## 6\. Evidence Category Values



The current evidence schema permits:



\- TRADITIONAL\_KNOWLEDGE

\- IN\_VITRO

\- IN\_VIVO

\- HUMAN\_OBSERVATIONAL

\- HUMAN\_RANDOMIZED

\- SYSTEMATIC\_REVIEW

\- META\_ANALYSIS

\- METHODOLOGY

\- OTHER



These categories describe evidence types. They should not be confused with pharmaceutical development domains.



## 7\. Evidence Strength Values



The methodology defines:



\- HIGH

\- MODERATE

\- LOW

\- VERY LOW

\- INSUFFICIENT

\- UNKNOWN



These are structured labels. They should not be presented as a formal GRADE assessment unless the full GRADE methodology has been applied.



## 8\. Identifier Relationships



The framework uses the following traceability relationships:



**Source Register â†’ Evidence Map â†’ Claim Traceability**



The Contradiction Register links claims and two related evidence/source records.



Each identifier should remain unique within its respective register.



## 9\. Data Integrity Rules



1\. Do not create unsupported source references.

2\. Do not infer missing study information.

3\. Record unavailable information as UNKNOWN where appropriate.

4\. Preserve contradictory findings.

5\. Keep evidence category separate from evidence strength.

6\. Preserve source provenance.

7\. Do not interpret a registered claim as scientifically established without reviewing its supporting evidence.



## 10\. Scope Limitations



This dictionary describes the existing evidence-framework CSV structures. It does not establish that all fields are automatically validated by the QC engine or that the framework is fully integrated with the engine.



Dedicated formulation and stability data structures remain future development requirements.
