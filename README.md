# Health360 — Healthcare Risk & Disease Analytics (Demo)

Health360 is a learning/demo project for exploring synthetic population-level health indicators with a lightweight interactive dashboard and Tableau-ready dataset.

## Important disclaimer
**All records and values in this project are fictional and synthetically generated. They do not describe real people, are not validated medical data, and must not be used for diagnosis, treatment, triage, clinical decisions, or public-health decisions.** The `demo_risk_band` is an illustrative rule-based label created only to demonstrate dashboard filtering; it is not a medical risk score.

## Contents
- `dashboard/app.py` — Streamlit interactive dashboard
- `data/health360_synthetic_sample.csv` — 500 synthetic records
- `data_dictionary.md` — field definitions and caveats
- `tableau/tableau_build_instructions.md` — Tableau setup and suggested worksheets
- `requirements.txt` — Python dependencies
- `run_dashboard.bat` / `run_dashboard.sh` — launch helpers

## Run locally
Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
streamlit run dashboard/app.py
```

Open the local URL shown by Streamlit (usually http://localhost:8501).

## Dashboard features
- KPI cards for records, average age, average BMI, and high demo-risk share
- Filters for region, age group, condition category, and demo risk band
- Charts for condition distribution, blood pressure by condition, glucose distribution, and age-group counts
- Filtered data table and CSV export

## Notes
- This dataset is intentionally synthetic and contains no real patient identifiers.
- The demo risk band is generated from simple arbitrary rules, not clinically validated thresholds.
- Do not upload real patient information into this demo without appropriate security, governance, consent, and legal review.
