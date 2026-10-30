# GROUP_01 — Persistent Overtime Among Fixed-Term Staff of the Santiago Metropolitan Health Services

**Course:** Business Intelligence · IIB423T-1 · Universidad del Desarrollo
**Instructor:** Tomás Fontecilla Correa
**Group:** 01 · Alessandro Lavezzi · José Saavedra
**Current assessment:** W2 · From Exploratory Analysis to Credible Validation (due October 29, 2026)

## Project

The project studies the **persistent use of overtime** among fixed-term (*contrata*) staff, using the monthly payrolls that the health services publish under Active Transparency.

- **KPI (persistence rate):** people who received overtime (daytime + night) in at least 75% of their months on the payroll, divided by people present for at least 12 months.
- **Unit of observation:** the person-month, keyed by (service, period, full name).
- **Intended decision:** help people-management units prioritize which staff groups and positions to review for staffing.

The project has three stages:

| Stage | Scope | Main artifact |
|---|---|---|
| W1 (Sep 25, 2026) | Two candidate questions, Central service (SSMC) | `DOCS/GROUP_01_W1_Report.pdf`, `Analysis/EDA.ipynb` |
| C1 (Sep 29, 2026) | Persistence KPI, data preparation and EDA, Central service | `DOCS/GROUP_01_C1_Report.pdf`, `DOCS/GROUP_01_C1_Slides.pdf`, `Analysis/EDA.ipynb` |
| **W2 (Oct 29, 2026)** | Same KPI in six metropolitan services, data validation, sampling, leakage audit, person-level holdout | **`notebooks/W2_project.ipynb`** |

## Repository structure

```
GROUP_01_C1/
├── README.md
├── requirements.txt
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

```bash
python -m venv .venv
.venv\Scripts\activate             # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

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

## AI use

AI assistance (Claude, Anthropic) was used for coding, translation and drafting. The disclosure is in §7.2 of the W2 notebook and in §7.4 of the C1 report.
