# GROUP_01 — Persistent Overtime Among Fixed-Term Staff of the Santiago Metropolitan Health Services

**Course:** Business Intelligence · IIB423T-1 · Universidad del Desarrollo
**Instructor:** Tomás Fontecilla Correa
**Group:** 01 · Alessandro Lavezzi · José Saavedra
**Assessed version:** C3 final repository (24 November 2026). Source repository: https://github.com/josenaxo/Proyecto-Business

## Question and decision

> On 1 September 2025, using only what was known that day, can we anticipate which fixed-term (*contrata*) staff will show **persistent overtime** (overtime in at least 75% of their months) between September 2025 and August 2026?

- **Data:** monthly payrolls of fixed-term staff published by six Santiago Metropolitan Health Services on the State Transparency Portal (Law 20.285), September 2024 – August 2026. One input row is one contract-month record; analysis rows are person-months and, for the model, one person.
- **Intended decision:** help people-management units prioritize which staff groups and positions to review for staffing.
- **Route:** classification. Positive class = persistent. Model: logistic regression. Reference: "whoever was persistent last year will be persistent this year".
- **Main result (test set, 1,192 people, 204 persistent):** the model finds more persistent people than the rule (recall 0.83 vs 0.76) at the cost of more false alarms (precision 0.66 vs 0.71). F1 is practically equal (0.739 vs 0.736), so **we do not claim the model predicts better than the rule**. Past overtime is the dominant signal (odds ratio 5.9 per standard deviation).

## Reading order

| # | File | What it contains | Stage |
|---|---|---|---|
| 1 | `notebooks/W2_project.ipynb` | Data description, quality checks, preparation, sampling, leakage audit, person-level train/validation/test split | W2 |
| 2 | `notebooks/C2_classification.ipynb` | Response to W2 feedback, decision-date cohort, features, target, reference rule, logistic regression, threshold on validation, single test evaluation, interpretation | C2 |
| 3 | `notebooks/03_C3_final_views.ipynb` | The three final views, the written visual rules and where they are implemented | C3 / W3 design |
| 4 | `presentations/GROUP_01_C3_Presentations.pptx` | Presentation 1 (audience) and Presentation 2 (internal review) | C3 |

Earlier work, kept unchanged for traceability: `Analysis/EDA.ipynb` (W1/C1, Central service) and the reports and slides in `DOCS/`.

**All notebooks are executed and their outputs are saved. They can be read without running code.** The datasets are **not** included in this delivery (course rule); the notebooks show compact summary tables and plots, and the source and download dates are described below.

## Repository structure

```
README.md
requirements.txt
notebooks/
  W2_project.ipynb            data description, preparation, split
  C2_classification.ipynb     model, reference, evaluation (reuses W2 preparation and split)
  03_C3_final_views.ipynb     final views, saved with their outputs
visual_system/
  style.py                    shared visual rules (colours, text styles, helpers) imported by the final charts
figures/                      saved figures (c2_*, c3_*, W2 figures)
presentations/                both C3 presentations
Analysis/EDA.ipynb            W1/C1 analysis (unchanged)
DOCS/                         W1, C1 and C2 reports and slides (unchanged)
```

## Pipeline and traceability

`payroll CSV files (Transparency Portal)` → **W2 notebook** (read and join six services, validate, keep Sep 2024 – Aug 2026, person-months, person-level split 70/15/15, `SEED = 42`) → **C2 notebook** (cohort known on 1 Sep 2025, features from Sep 2024 – Jul 2025, gap month Aug 2025, target from Sep 2025 – Aug 2026, reference rule, model fitted on training only, threshold chosen on validation, test used once) → **C3 notebook** (draws the saved C2 numbers using `visual_system/style.py`).

| Result | Where it is computed | Saved evidence |
|---|---|---|
| People in the W2 split (16,791) | W2 notebook, section 6 | W2 notebook output |
| Cohort of 8,732 people, 8,134 labelled, 8,110 after excluding name matches across services | C2 notebook, sections 1.2–1.3 | C2 notebook output |
| Persistent in year 2: 18.3% of labelled people; test 17.1% | C2 notebook, section 1.3 | C2 notebook output |
| Reference rule vs model, test metrics and confusion matrices | C2 notebook, section 4 | C2 notebook output, `figures/c2_confusion_test.png` |
| Odds ratios | C2 notebook, section 3.2 | C2 notebook output, `figures/c3_view3_factors.png` |
| Final views | C3 notebook | saved outputs, `figures/c3_*.png` |

The C3 notebook asserts that its input numbers add up to the C2 results (1,192 test people, 204 persistent, matrices consistent with the metrics table).

## Visual system

Rules are written in the header of `visual_system/style.py` and in section 1 of `notebooks/03_C3_final_views.ipynb`, and are applied by the three final charts.

- **Colour:** blue = logistic regression; grey = reference rule, neutral context and share ramps; amber = highlight only (differences, errors, dominant factor).
- **Redundant cues (no colour needed):** the reference rule is hatched; every value is printed; circles = numeric features, diamonds = categories; error cells are named in words.
- **Text:** title states the finding; subtitle gives population, period and unit; source line at the bottom.
- **Scales:** scores 0–1 from zero (never truncated); shares 0–100% on the same scale in both panels; odds ratios on a log scale centred on 1 (a different measure, so a different scale, with the same colour meaning).
- **Highlighting:** one per view. **Layout:** title → subtitle → plot → legend → source.

**Design selection (W3).** Each of the three views was first drawn in a weaker version (rainbow colours, truncated axis, unlabelled matrix, bars in raw table order) and redesigned. The final designs were kept because each supports one task for the people-management audience: *compare* model and rule, *summarize* the errors, *identify* the dominant factor. Each view has a stated limit (hidden uncertainty, shares that make false positives look small, mixed odds-ratio scales); we kept the designs because their benefit for the task is larger than the limit, and we state the limit in the notebook.

## Decisions and development

| Stage | Decision | Reason / evidence |
|---|---|---|
| W2 → C2 (feedback) | Define the prediction date (1 Sep 2025) and a **decision-date cohort**; features only from Sep 2024 – Jul 2025 | avoids leakage: the model never sees the period it predicts (C2 notebook, section 1.1) |
| W2 → C2 (feedback) | One-month **gap** (Aug 2025) between features and target | payroll records the month paid, not the month worked; 372 contract rows (0.66% of rows with overtime) were paid after the contract ended (C2 notebook, section 1.0) |
| W2 → C2 (feedback) | **Exclude names that appear in more than one service** (24 people in the C2 data) | no national ID, so merging could join two different people (C2 notebook, sections 1.0 and 1.3) |
| Kept | 75% persistence threshold and minimum of 6 months | same definition as the KPI since C1; with fewer months the share is unstable |
| Kept | W2 person-level split, no new split | the same person is never in training and test; the test set stays the one fixed in W2 |
| C2 | Logistic regression, default L2 `C = 1`, threshold 0.35 chosen on validation by F1 | simple and explainable; default 0.5 not assumed for an 18% positive class |
| C2 | Report that the model does **not clearly beat** the reference rule | test F1 0.739 vs 0.736 is within sampling variation (about 200 persistent people) |
| W3 → C3 | Keep the three redesigned views and the shared rules | see "Visual system" above |

**Known limits.** One decision date and one year to predict; people identified only by name; payroll month is the payment month; 598 cohort people left or stayed under 6 months and cannot be evaluated; the test set was already seen descriptively in W2. A useful prediction does not prove that a staffing review would reduce overtime.

## Contributions

- **José Saavedra:** C2 dataset (features, target), reuse of the W2 split, evaluation functions, reference rule and logistic regression pipeline.
- **Alessandro Lavezzi:** response to W2 feedback (decision-date cohort, gap month, name matches), coefficients, threshold choice, test evaluation and interpretation; C3 final views and visual rules.
- Both members reviewed the whole repository and the results quoted in the presentations.

## Software

Python 3.13.7 with pandas 2.3.3, numpy 2.3.3, matplotlib 3.10.6, seaborn 0.13.2 (only for the heatmaps in the W2 figure C6), scikit-learn 1.7.2, JupyterLab 4.4.7 and nbconvert 7.16.6 (see `requirements.txt`). No installation is needed to read the notebooks.

## Data provenance

- **Source:** State Transparency Portal (Portal de Transparencia), https://www.portaltransparencia.cl/PortalPdT/. For each Metropolitan Health Service, open Active Transparency → staff payroll → *Personal a contrata*, select the month and download it as CSV.
- **Services and download dates:**

  | Service | Files | Months | Downloaded |
  |---|---|---|---|
  | Central (SSMC, code AO006) | 24 | 2024-09 to 2026-08 | Sep 15, 2026 |
  | North, East, West | 25 each | 2024-09 to 2026-09 | Oct 22, 2026 |
  | South, South-East | 85 / 25 | 2024-11 to 2026-09 / 2024-09 to 2026-09 | Oct 23, 2026 |

- **South (Sur)** publishes one file per hospital or unit from January 2025 onwards (Hospital Buin-Paine, Hospital El Peral, Hospital Lucio Córdova, Servicio Sur). It has no data for September and October 2024, and the Hospital El Peral file is missing for October 2025. The notebook reads the period from the file name and joins the units.
- **Format:** semicolon-separated, latin-1 encoding, one row per contract-month record. The files were used exactly as downloaded; **they are not part of this delivery** (course rule).
- **Analysis window:** September 2024 – August 2026 (the 24 months common to every service). September 2026 rows are loaded but excluded, and the row counts before and after are reported in §0.2.
- **Scope:** fixed-term staff only. Permanent (*planta*), fee-based and Labor Code staff are not in this payroll (see §4 of the notebook).

## Data notes

- Each row is a contract record, not a person. Records are summed into person-months.
- There is no national ID (RUT), so people are identified by (service, full name). 135 names appear in more than one service.
- Missing values are written as `-` in some amount columns, never as empty cells. `No tiene` in the overtime columns means no payment and is coded as 0.
- Known recording issues: Central has an atypical January 2025 and a staff-group error in December 2025; South's October 2025 is incomplete; South-East records holiday hours and much lower hours. The notebook flags these issues rather than deleting rows (§3).

## Privacy

The input files contain employees' full names, published under Law 20.285 on access to public information. The notebook and the reports show only aggregated counts and rates, and no individual is identified. The processed C1 table replaces names with a numeric ID.

## AI use

AI assistance (Claude, Anthropic, through Claude Code) was used for coding, translation, drafting text and building the C3 final views and presentations. We checked its output by running the notebooks from top to bottom, verifying the metric functions on a hand-calculated example (C2, section 2.1), checking that preprocessing is fitted on training data only, and comparing every number quoted in the notebooks, README and presentations with the saved outputs. The team is responsible for the choices of task, cohort, features, threshold rule, visual design and interpretation. Earlier disclosures: section 7.2 of the W2 notebook, section 6 of the C2 notebook and section 7.4 of the C1 report.
