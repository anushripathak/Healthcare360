import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(page_title="Health360 | Synthetic Demo", page_icon="🩺", layout="wide")
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "health360_synthetic_sample.csv"

st.title("Health360")
st.subheader("Comprehensive Healthcare Risk & Disease Analytics")
st.error("DISCLAIMER: This demo uses entirely fictional, synthetically generated data. It is not real patient information, is not clinically validated, and must NOT be used for diagnosis, treatment, triage, or any clinical/public-health decision.")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["observation_date"])
    return df

df = load_data()
st.caption("Learning/demo dashboard • Synthetic records only • No real patients represented")

with st.sidebar:
    st.header("Filters")
    regions = st.multiselect("Region", sorted(df["region"].unique()), default=sorted(df["region"].unique()))
    age_groups = st.multiselect("Age group", ["18–29", "30–44", "45–59", "60+"], default=["18–29", "30–44", "45–59", "60+"])
    conditions = st.multiselect("Condition category", sorted(df["condition_category"].unique()), default=sorted(df["condition_category"].unique()))
    risk_bands = st.multiselect("Illustrative demo risk band", ["Low", "Moderate", "High"], default=["Low", "Moderate", "High"])
    min_date, max_date = df["observation_date"].min().date(), df["observation_date"].max().date()
    date_range = st.date_input("Observation date range", value=(min_date, max_date), min_value=min_date, max_value=max_date)

filtered = df[
    df["region"].isin(regions) &
    df["age_group"].isin(age_groups) &
    df["condition_category"].isin(conditions) &
    df["demo_risk_band"].isin(risk_bands)
]
if isinstance(date_range, tuple) and len(date_range) == 2:
    filtered = filtered[filtered["observation_date"].dt.date.between(date_range[0], date_range[1])]

if filtered.empty:
    st.warning("No records match the selected filters. Change a filter to view the demo.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Synthetic records", f"{len(filtered):,}")
c2.metric("Average age", f"{filtered['age'].mean():.1f}")
c3.metric("Average BMI", f"{filtered['bmi_kg_m2'].mean():.1f}")
c4.metric("High demo-risk share", f"{(filtered['demo_risk_band'].eq('High').mean()*100):.1f}%")
st.caption("Metrics describe only the generated sample. 'Demo risk band' is an arbitrary illustrative label, not a medical risk score.")

left, right = st.columns(2)
with left:
    st.markdown("### Condition category")
    cond = filtered.groupby("condition_category", as_index=False).size().rename(columns={"size":"records"})
    st.altair_chart(alt.Chart(cond).mark_bar().encode(
        x=alt.X("records:Q", title="Synthetic record count"),
        y=alt.Y("condition_category:N", sort="-x", title=None),
        tooltip=["condition_category", "records"]
    ).properties(height=250), use_container_width=True)
with right:
    st.markdown("### Records by region")
    reg = filtered.groupby("region", as_index=False).size().rename(columns={"size":"records"})
    st.altair_chart(alt.Chart(reg).mark_bar().encode(
        x=alt.X("region:N", title="Region", sort="-y"),
        y=alt.Y("records:Q", title="Synthetic record count"),
        tooltip=["region", "records"]
    ).properties(height=250), use_container_width=True)

left, right = st.columns(2)
with left:
    st.markdown("### Average blood pressure by condition")
    bp = filtered.groupby("condition_category", as_index=False).agg(
        systolic=("systolic_bp_mmHg","mean"), diastolic=("diastolic_bp_mmHg","mean")
    ).melt("condition_category", var_name="measure", value_name="mmHg")
    st.altair_chart(alt.Chart(bp).mark_bar().encode(
        x=alt.X("condition_category:N", title=None, axis=alt.Axis(labelAngle=-25)),
        y=alt.Y("mmHg:Q", title="Synthetic average (mmHg)"),
        color="measure:N",
        xOffset="measure:N",
        tooltip=["condition_category","measure",alt.Tooltip("mmHg:Q",format=".1f")]
    ).properties(height=300), use_container_width=True)
with right:
    st.markdown("### Glucose distribution")
    hist = alt.Chart(filtered).mark_bar().encode(
        x=alt.X("glucose_mg_dL:Q", bin=alt.Bin(maxbins=18), title="Synthetic glucose (mg/dL)"),
        y=alt.Y("count():Q", title="Record count"),
        tooltip=[alt.Tooltip("count():Q", title="Records")]
    ).properties(height=300)
    st.altair_chart(hist, use_container_width=True)

st.markdown("### Age-group breakdown")
age = filtered.groupby("age_group", as_index=False).size().rename(columns={"size":"records"})
st.altair_chart(alt.Chart(age).mark_bar().encode(
    x=alt.X("age_group:N", sort=["18–29","30–44","45–59","60+"], title="Age group"),
    y=alt.Y("records:Q", title="Synthetic record count"),
    tooltip=["age_group","records"]
).properties(height=220), use_container_width=True)

st.markdown("### Filtered synthetic records")
st.dataframe(filtered, use_container_width=True, hide_index=True)
st.download_button("Download filtered CSV", filtered.to_csv(index=False).encode("utf-8"), "health360_filtered_synthetic.csv", "text/csv")
st.info("Reminder: all values are fictional. This demo is for analytics education only and is not for clinical use.")
