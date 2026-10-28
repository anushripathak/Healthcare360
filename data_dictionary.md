# Health360 Data Dictionary

**Dataset:** `data/health360_synthetic_sample.csv`  
**Rows:** 500 synthetic records  
**Purpose:** Dashboard / analytics demonstration only.

> **Disclaimer:** All values are fictional. This is not real patient data, a validated clinical dataset, or a clinical decision-support tool. Do not use for clinical or public-health decisions.

| Field | Type | Description | Notes |
|---|---|---|---|
| `record_id` | String | Synthetic row identifier | Generated ID; not a real patient ID |
| `observation_date` | Date (ISO 8601) | Fictional observation date in 2025 | Randomly generated |
| `age` | Integer | Fictional age in years | Randomly generated, 18–85 |
| `age_group` | String | Age band derived from `age` | 18–29, 30–44, 45–59, 60+ |
| `sex` | Category | Fictional demographic category | Not based on actual individuals |
| `region` | Category | Fictional broad region | North, South, East, West, Central |
| `condition_category` | Category | Illustrative condition grouping | Not a diagnosis |
| `systolic_bp_mmHg` | Integer | Synthetic systolic blood pressure value | Demonstration only |
| `diastolic_bp_mmHg` | Integer | Synthetic diastolic blood pressure value | Demonstration only |
| `bmi_kg_m2` | Decimal | Synthetic body mass index | Demonstration only |
| `glucose_mg_dL` | Decimal | Synthetic glucose value | Demonstration only |
| `visits_last_12_months` | Integer | Fictional visit count | Randomly generated, 0–12 |
| `demo_risk_band` | Category | Illustrative rule-based band | Not validated; not a medical risk score |
| `data_source` | String | Dataset origin marker | Always `SYNTHETIC_DEMO` |

## Suggested checks
- Confirm row count and inspect nulls before building visuals.
- Treat categorical fields as dimensions and numeric measures as measures in Tableau.
- Avoid drawing clinical conclusions from any chart.
