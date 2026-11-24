# Pharmaceutical Scientific Evidence Framework



## 1. Project Overview



This folder contains a structured scientific evidence-mapping framework developed for the BHIV Pharmaceutical Evidence Quality workstream.



The demonstration concept is **Curcuma longa L. (turmeric/curcumin) and evidence related to knee osteoarthritis**.



The framework organizes scientific information so that researchers can trace claims to evidence records and original sources, review contradictions, identify limitations and record gaps requiring further research.



## 2. Objectives



\- Register and organize scientific sources.

\- Classify evidence according to its type.

\- Link scientific claims to evidence and source records.

\- Record evidence strength and limitations.

\- Identify and preserve contradictory findings.

\- Track unknown information and unsupported claims.

\- Identify gaps between scientific evidence and future product development.



## 3. Folder Structure



| File | Purpose |

|---|---|

| `source\_register.csv` | Records source identifiers and publication details. |

| `evidence\_map.csv` | Maps evidence records to sources and scientific findings. |

| `claim\_traceability.csv` | Links claims to evidence and sources. |

| `contradiction\_register.csv` | Records conflicting evidence and resolution status. |

| `evidence\_schema.json` | Defines the evidence record structure and permitted categories. |

| `methodology.md` | Describes evidence selection, extraction, classification and quality principles. |

| `translation\_gap\_register.md` | Identifies uncertainty, further R\&D, formulation, safety and regulatory gaps. |



## 4. Current Demonstration Dataset



The current registered dataset contains:



\- 7 source records.

\- 8 evidence records.

\- 8 claim records.

\- 3 contradiction records.



These counts describe the current register contents. They do not independently establish the scientific validity of every source or claim.



## 5. Evidence Categories



The current evidence schema defines these categories:



\- `TRADITIONAL\_KNOWLEDGE`

\- `IN\_VITRO`

\- `IN\_VIVO`

\- `HUMAN\_OBSERVATIONAL`

\- `HUMAN\_RANDOMIZED`

\- `SYSTEMATIC\_REVIEW`

\- `META\_ANALYSIS`

\- `METHODOLOGY`

\- `OTHER`



Evidence strength is recorded separately from evidence category.



## 6. Quality and Traceability Principles



The framework follows these principles:



1\. Every source should have a unique source identifier.

2\. Every evidence record should have a unique evidence identifier.

3\. Every scientific claim should link to supporting evidence and its source.

4\. Evidence limitations must remain visible.

5\. Contradictory findings must not be silently removed.

6\. Missing information should be recorded as `UNKNOWN`.

7\. Traditional knowledge, preclinical evidence and human evidence must remain distinct.

8\. Evidence mapping must not be presented as proof of product efficacy, safety or regulatory approval.



## 7. Current Limitations



\- The demonstration is an evidence-mapping framework, not a formal systematic review.

\- Source and claim verification requires appropriate review of the original publications.

\- The framework does not perform formulation development or product-specific stability testing.

\- It does not independently establish clinical efficacy, safety, manufacturing suitability or regulatory approval.

\- Integration with the separate biosimilarity and preclinical QC engine remains to be demonstrated.



## 8. Future Development



The proposed next increment is a unified evidence integration layer that can:



\- Map evidence records between the framework and QC engine schemas.

\- Preserve source, evidence and claim identifiers.

\- Retain real-versus-synthetic data declarations.

\- Transfer limitations and contradiction information.

\- Support dedicated formulation and stability QC rules.

\- Produce traceable outputs for human review.



## 9. Important Scientific Boundary



This framework organizes and evaluates evidence records. It does not itself prove that a treatment works, that a product is safe, or that a product is approved.



**The objective is traceable scientific evidence, transparent uncertainty and responsible research decisions.**
