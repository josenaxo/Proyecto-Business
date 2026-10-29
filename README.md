# GROUP_01 — Persistent Overtime Among Fixed-Term Staff of the SSMC

**Course:** Business Intelligence · IIB423T-1 · Universidad del Desarrollo
**Assessments:** W1 (questions worth investigating) → C1 (cleaning and EDA of the selected line) → **W2 (from exploratory analysis to credible validation)**
**Instructor:** Tomás Fontecilla Correa
**Group:** 01 · **Members:** Alessandro Lavezzi · José Saavedra
**Repository:** https://github.com/josenaxo/Proyecto-Business · W2 version: tag `W2`

## Purpose

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

## Package structure

```
GROUP_01_C1/
├── README.md
├── requirements.txt
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

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

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

## Execution status

Both W2 notebooks (`W2.ipynb`, `EDA2.ipynb`) were run from top to bottom with a restarted kernel on 23 October 2026, with no errors.
