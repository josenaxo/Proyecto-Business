<<<<<<< HEAD
# GROUP_01 — Persistent Overtime Among Fixed-Term Staff of the SSMC

**Course:** Business Intelligence · IIB423T-1 · Universidad del Desarrollo
**Assessments:** W1 (questions worth investigating) → C1 (cleaning and EDA of the selected line) → **W2 (from exploratory analysis to credible validation)**
**Instructor:** Tomás Fontecilla Correa
**Group:** 01 · **Members:** Alessandro Lavezzi · José Saavedra
**Repository:** https://github.com/josenaxo/Proyecto-Business · W2 version: tag `W2`
=======
# GROUP_01 — Persistent Overtime Among Fixed-Term Staff of the Santiago Metropolitan Health Services

**Course:** Business Intelligence · IIB423T-1 · Universidad del Desarrollo
**Instructor:** Tomás Fontecilla Correa
**Group:** 01 · Alessandro Lavezzi · José Saavedra
**Current assessment:** W2 · From Exploratory Analysis to Credible Validation (due October 29, 2026)
>>>>>>> avanzeRolA

## Project

<<<<<<< HEAD
The project studies overtime pay among fixed-term (*contrata*) staff of the Servicio de Salud Metropolitano Central (SSMC), using 24 monthly payrolls published under Active Transparency (September 2024 – August 2026).

| | |
|---|---|
| **Business question** | Which staff groups and positions receive overtime persistently, and how much does it weigh in their gross pay? |
| **Main KPI** | Overtime persistence rate = persons paid overtime in ≥ 75% of their payroll months / persons present ≥ 12 months |
| **Unit of observation** | Person-month (contract records summed by person and month); the KPI is computed per person |
| **Intended decision** | Prioritise which staff groups and positions should have their staffing reviewed first |

W2 keeps the same problem, KPI and unit. It adds:
- a feedback-to-action table;
- programmatic data-validation checks;
- a sampling and representativeness assessment;
- a leakage audit;
- a person-grouped chronological train/validation/test design.

It also compares the SSMC with the other five Metropolitan health services.
=======
The project studies the **persistent use of overtime** among fixed-term (*contrata*) staff, using the monthly payrolls that the health services publish under Active Transparency.

- **KPI (persistence rate):** people who received overtime (daytime + night) in at least 75% of their months on the payroll, divided by people present for at least 12 months.
- **Unit of observation:** the person-month, keyed by (service, period, full name).
- **Intended decision:** help people-management units prioritize which staff groups and positions to review for staffing.
>>>>>>> avanzeRolA

The project has three stages:

| Stage | Scope | Main artifact |
|---|---|---|
| W1 (Sep 25, 2026) | Two candidate questions, Central service (SSMC) | `DOCS/GROUP_01_W1_Report.pdf`, `Analysis/EDA.ipynb` |
| C1 (Sep 29, 2026) | Persistence KPI, data preparation and EDA, Central service | `DOCS/GROUP_01_C1_Report.pdf`, `DOCS/GROUP_01_C1_Slides.pdf`, `Analysis/EDA.ipynb` |
| **W2 (Oct 29, 2026)** | Same KPI in six metropolitan services, data validation, sampling, leakage audit, person-level holdout | **`notebooks/W2_project.ipynb`** |

**Also, we were working in Analysis/EDA2.ipynb** 
*We didn't want to drop that work even when we re-did it in W2_project.ipynb, because you could compare directly with EDA.ipynb, in the W1 and C1 work, with the same methodology.*

## Repository structure

```
GROUP_01_C1/
├── README.md
├── requirements.txt
<<<<<<< HEAD
├── GROUP_01_W1_Report.pdf            W1 report (preserved)
├── GROUP_01_C1_Report.pdf            C1 report (preserved)
├── GROUP_01_C1_Slides.pdf            C1 slides (preserved)
├── Analysis/
│   ├── W2.ipynb                      W2 submission notebook (read this first for W2)
│   ├── EDA2.ipynb                    W2 companion: same KPIs for the six Metropolitan services
│   └── EDA.ipynb                     W1/C1 notebook (preserved, Spanish, unchanged)
└── Data/
    ├── TransparenciaActiva_YYYY-MM.csv                          SSMC (Centro) payroll, 24 files
    ├── <Service>_TransparenciaActiva_YYYY-MM.csv                 Norte, Oriente, Occidente, SurOriente
    ├── Sur_TransparenciaActiva_YYYY-MM[_<Establishment>].csv     Sur (one file per establishment from Jan-2025)
    ├── figura_*.png                                              W1/C1 figures (from EDA.ipynb)
    ├── fig_w2_*.png                                              W2 figures (from W2.ipynb)
    ├── fig_eda2_*.png                                            W2 companion figures (from EDA2.ipynb)
    └── processed/
        ├── analitica_persona_mes.csv                             C1 person-month table (numeric ids, no names)
        └── w2_split_ssmc.csv                                     W2 train/test/fold assignment (numeric ids, no names)
```

## Order to open and run

1. **W2:** open `Analysis/W2.ipynb`. Its outputs are saved, so it can be read without running it. Sections follow the W2 rubric: A continuity and feedback → C validation → B revised EDA → D sampling → E leakage → F holdout design → G management summary and AI-use disclosure.
2. **Cross-service evidence:** `Analysis/EDA2.ipynb`.
3. **Earlier work:** `GROUP_01_W1_Report.pdf`, `GROUP_01_C1_Report.pdf` and `Analysis/EDA.ipynb`.

To reproduce, run each notebook from top to bottom from the `Analysis/` folder (Kernel → Restart & Run All). Each takes about 1 minute.
- They read only `../Data/` and write their figures there; `W2.ipynb` also writes `../Data/processed/w2_split_ssmc.csv`.
- Every random operation uses `SEED = 42`. The test-set fingerprint printed in W2 §F.2 (`db025253808a`) must be identical on every run.
- `EDA2.ipynb` stops with an `assert` if it does not reproduce the C1 SSMC values.

## Software and dependencies

Run with Python 3.13.7, pandas 2.3.3, NumPy 2.3.3, Matplotlib 3.10.6, seaborn 0.13.2, scikit-learn 1.7.2 and Jupyter (or VS Code with the Jupyter extension).
=======
├── notebooks/
│   └── W2_project.ipynb          W2 deliverable (English, executed, outputs saved)
├── Analysis/
│   ├── EDA.ipynb                 W1/C1 analysis of the Central service
│   └── EDA2.ipynb                W2 working draft in Spanish (superseded by notebooks/W2_project.ipynb)
├── DOCS/                         W1 and C1 reports and C1 slides (PDF)
├── Data/
│   ├── TransparenciaActiva_YYYY-MM.csv               Central (Centro), 24 files
│   ├── Norte_TransparenciaActiva_YYYY-MM.csv         North, 25 files
│   ├── Oriente_TransparenciaActiva_YYYY-MM.csv       East, 25 files
│   ├── Occidente_TransparenciaActiva_YYYY-MM.csv     West, 25 files
│   ├── Sur_TransparenciaActiva_YYYY-MM_<unit>.csv    South, 85 files (one per hospital/unit and month)
│   ├── SurOriente_TransparenciaActiva_YYYY-MM.csv    South-East, 25 files
│   ├── processed/analitica_persona_mes.csv           C1 person-month table (numeric ID, no names)
│   └── figura_*.png                                  W1/C1 figures
└── figures/                      W2 figures, written by notebooks/W2_project.ipynb
```

The W1 and C1 artifacts are kept unchanged, and their history is in git.

## How to run the W2 notebook
>>>>>>> avanzeRolA

```bash
python -m venv .venv
.venv\Scripts\activate             # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

<<<<<<< HEAD
All paths are relative to `Analysis/`. No credentials or connectors are required.

## Data provenance

- **Source:** State Transparency Portal (Portal de Transparencia), Active Transparency, fixed-term staff payroll (*Personal a contrata*) of each Metropolitan health service. Link: https://www.portaltransparencia.cl/PortalPdT/
- **SSMC (analytical dataset):** organisation code AO006, 24 monthly files, September 2024 – August 2026 (44,777 contract records). Downloaded on 15 September 2026.
- **Other services (W2 coverage and benchmark):** Norte, Oriente, Occidente and Sur Oriente (25 files each, September 2024 – September 2026), and Sur (November 2024 – September 2026; one file per establishment from January 2025, with the Hospital El Peral file missing for October 2025). They were downloaded and added to the repository on 22–23 October 2026. In total there are 209 files and 246,732 contract records.
- **Retrieval:** on the portal, search for the health service, open its Active Transparency section, go to the fixed-term staff payroll, select each month and download it as CSV. Save it as `[<Service>_]TransparenciaActiva_YYYY-MM[_<Establishment>].csv`; the SSMC files have no prefix. This is the name pattern the notebooks read.
- **Format:** semicolon-separated, latin-1 encoding, 21 columns plus an empty trailing column. Files are included unmodified, and every transformation is in the notebooks.
- **Scope:** fixed-term staff only; permanent (*planta*), fee-based (*honorarios*) and Labor Code staff are not included. Files may be updated on the portal after the download dates; the files in `Data/` are the versions used.

## Data notes

These are source characteristics, not execution errors (see W2 §C):
- Each row is a contract record, not a person. Results are aggregated per person-month.
- There is no national ID (RUT); persons are identified by full name within each service.
- In the SSMC:
  - holiday overtime has no values (other services do have them);
  - the staff-group column is misrecorded in December 2025, so the modal staff group is used;
  - January 2025 has a different format;
  - August 2025 amounts per hour are not comparable.
- `-` marks values that were not reported, and `Indefinido` marks an open-ended contract; both are kept as missing, not imputed.

## Privacy

The input files contain employees' full names, as published under Law 20.285. The notebooks display and save only aggregated results or numeric ids; no individual is identified.
=======
1. Open `notebooks/W2_project.ipynb` in JupyterLab or VS Code and run **Restart Kernel → Run All**. Alternatively, run from the command line:
   ```bash
   cd notebooks
   jupyter nbconvert --to notebook --execute --inplace W2_project.ipynb
   ```
2. The notebook reads every CSV from `../Data/` (paths are relative to `notebooks/`) and writes six figures to `../figures/`. It writes nothing to `Data/`.
3. Run time is under one minute. Every random step uses `SEED = 42` (the 25% sample in §4, the 80/20 illustration in §5 and the person-level split in §6), so results are identical on each run.

The notebook was tested with Python 3.13.7 and the versions in `requirements.txt`. It ran top to bottom with no errors before submission.

## Data provenance

- **Source:** State Transparency Portal (Portal de Transparencia), https://www.portaltransparencia.cl/PortalPdT/. For each Metropolitan Health Service, open Active Transparency → staff payroll → *Personal a contrata*, select the month and download it as CSV.
- **Services and download dates:**

  | Service | Files | Months | Downloaded |
  |---|---|---|---|
  | Central (SSMC, code AO006) | 24 | 2024-09 to 2026-08 | Sep 15, 2026 |
  | North, East, West | 25 each | 2024-09 to 2026-09 | Oct 22, 2026 |
  | South, South-East | 85 / 25 | 2024-11 to 2026-09 / 2024-09 to 2026-09 | Oct 23, 2026 |

- **South (Sur)** publishes one file per hospital or unit from January 2025 onwards (Hospital Buin-Paine, Hospital El Peral, Hospital Lucio Córdova, Servicio Sur). It has no data for September and October 2024, and the Hospital El Peral file is missing for October 2025. The notebook reads the period from the file name and joins the units.
- **Format:** semicolon-separated, latin-1 encoding, one row per contract-month record. The files are stored exactly as downloaded.
- **Analysis window:** September 2024 – August 2026 (the 24 months common to every service). September 2026 rows are loaded but excluded, and the row counts before and after are reported in §0.2.
- **Scope:** fixed-term staff only. Permanent (*planta*), fee-based and Labor Code staff are not in this payroll (see §4 of the notebook).

## Data notes

- Each row is a contract record, not a person. Records are summed into person-months.
- There is no national ID (RUT), so people are identified by (service, full name). 135 names appear in more than one service.
- Missing values are written as `-` in some amount columns, never as empty cells. `No tiene` in the overtime columns means no payment and is coded as 0.
- Known recording issues: Central has an atypical January 2025 and a staff-group error in December 2025; South's October 2025 is incomplete; South-East records holiday hours and much lower hours. The notebook flags these issues rather than deleting rows (§3).

## Privacy

The input files contain employees' full names, published under Law 20.285 on access to public information. The notebook and the reports show only aggregated counts and rates, and no individual is identified. The processed C1 table replaces names with a numeric ID.
>>>>>>> avanzeRolA

## AI use

<<<<<<< HEAD
Both W2 notebooks (`W2.ipynb`, `EDA2.ipynb`) were run from top to bottom with a restarted kernel on 23 October 2026, with no errors.
=======
AI assistance (Claude, Anthropic) was used for coding, translation and drafting. The disclosure is in §7.2 of the W2 notebook and in §7.4 of the C1 report.
>>>>>>> avanzeRolA
