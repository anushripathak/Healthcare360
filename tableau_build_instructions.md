# Tableau Build Instructions

## 1. Connect the data
1. Open Tableau Desktop or Tableau Public.
2. Choose **Connect → To a File → Text File**.
3. Select `data/health360_synthetic_sample.csv`.
4. Confirm `observation_date` is interpreted as a Date and numeric fields as Number (Whole/Decimal).
5. Add a dashboard title: **Health360 — Synthetic Analytics Demo**.
6. Place this disclaimer prominently at the top or bottom:
   **FICTIONAL SYNTHETIC DATA — FOR DEMONSTRATION ONLY — NOT FOR CLINICAL USE.**

## 2. Create worksheets
- **Condition Distribution:** `condition_category` on Rows; `COUNTD(record_id)` on Columns; bar chart.
- **Records by Region:** `region` on Rows; `COUNTD(record_id)` on Columns; bar chart.
- **Average BP by Condition:** `condition_category` on Rows; `AVG(systolic_bp_mmHg)` and `AVG(diastolic_bp_mmHg)` in the view; use Measure Names/Values or separate charts.
- **Glucose Distribution:** `glucose_mg_dL` on Columns; `record_id` on Rows as Count, or use a histogram.
- **Age Group Breakdown:** `age_group` on Rows; `COUNTD(record_id)` on Columns.
- **Demo Risk Band:** `demo_risk_band` on Rows; `COUNTD(record_id)` on Columns. Label it "Illustrative demo band—not clinical risk."

## 3. Add filters
Add `region`, `age_group`, `condition_category`, `demo_risk_band`, and `observation_date` to Filters. Choose **Show Filter** for each relevant worksheet and apply filters to all worksheets using this data source.

## 4. Assemble dashboard
1. Create a new dashboard, e.g. 1200 × 850.
2. Add a horizontal header with project title and disclaimer.
3. Place KPI text tiles for total records, average age, average BMI, and high demo-risk share.
4. Arrange condition, region, age, BP, and glucose worksheets.
5. Add filter controls on the left or top.
6. Add a text note: "Synthetic data; no real patients; no clinical validity."

## 5. Suggested calculated fields
- `Total Records`: `COUNTD([record_id])`
- `Average Age`: `AVG([age])`
- `Average BMI`: `AVG([bmi_kg_m2])`
- `High Demo-Risk Share`: `SUM(IIF([demo_risk_band] = "High", 1, 0)) / COUNT([record_id])`

Format share as Percentage. The "High Demo-Risk Share" is an illustrative synthetic-data statistic only.

## 6. QA checklist
- Check filter actions affect all intended views.
- Verify all axis titles include units where relevant.
- Ensure the fictional-data disclaimer is always visible in the published dashboard.
- Do not connect this demo to production clinical systems or real patient data.
