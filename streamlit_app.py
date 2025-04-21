
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("📊 Mentorship Hours Modeling Dashboard (with Institution Type)")
st.markdown("This dashboard summarizes model outputs explaining variation in mentorship hours by career stage, gender, race, and institutional affiliation.")

def show_image_with_text(title, img_path, desc):
    st.subheader(title)
    st.image(img_path, width=650)
    st.markdown(desc)

# Map image titles to paths and updated narrative from canvas
image_info = {
    "📊 GLM Coefficient Plot with 95% CI and Effect Sizes": (
        "GLM_Results/GLM_Coefficient_Plot_with_EffectSize.png",
        "- **Horizontal lines**: 95% confidence intervals
"
        "- **Black dots**: Point estimates (log effect)
"
        "- **Red line at 0**: Baseline effect
"
        "- `CareerStage_5.0`, `Gender_1.0`, and `InstitutionType_1` are strong positive predictors.
"
        "- `CareerStage_6.0` and `Race_BlackAA` show significant negative effects."
    ),
    "🔵 Random Forest — Predicted vs Actual (Log Transformed)": (
        "RandomForest_LogTransformed_Results/Predicted_vs_Actual.png",
        "- Diagonal line = perfect predictions.
- Good alignment in 5–30 hour range.
- Underpredicts above ~40 hours."
    ),
    "🔵 Random Forest — Residuals vs Predicted": (
        "RandomForest_LogTransformed_Results/Residuals.png",
        "- Residuals ideally centered at 0.
- Curve bends down beyond 25 hours: underestimation of high-hour mentors."
    ),
    "🔵 Random Forest — Top 15 Feature Importances": (
        "RandomForest_LogTransformed_Results/Top15_Feature_Importance.png",
        "- `Race_BlackAA` and `CareerStage_6.0` dominate.
- Institution types are also influential.
- Gender variables rank lower."
    ),
    "🔶 XGBoost (Log-Transformed Target) — Predicted vs Actual": (
        "XGBoost_LogTransformed/Predicted_vs_Actual.png",
        "- Slightly better fit than RF.
- Fewer outliers, better alignment in mid-range predictions."
    ),
    "🔶 XGBoost — Residuals vs Predicted": (
        "XGBoost_LogTransformed/Residuals.png",
        "- Residuals tighter and symmetric.
- Some residual noise >40 hours but less bias than RF."
    ),
    "🔶 XGBoost — Top 15 Feature Importances": (
        "XGBoost_LogTransformed/Top15_Feature_Importance.png",
        "- `CareerStage_6.0`, `Race_BlackAA`, and `InstitutionType_1` lead.
- Balanced influence of demographic and institutional factors."
    ),
    "🔷 XGBoost (Original) — Predicted vs Actual": (
        "XGBoost_Original/Predicted_vs_Actual.png",
        "- More spread in prediction accuracy.
- Struggles with high mentorship values."
    ),
    "🔷 XGBoost (Original) — Residuals vs Predicted": (
        "XGBoost_Original/Residuals.png",
        "- Residuals show skew at higher values.
- Errors grow with higher predictions."
    ),
    "🔷 XGBoost (Original) — Top 15 Feature Importances": (
        "XGBoost_Original/Top15_Feature_Importance.png",
        "- `CareerStage_5.0` is strongest predictor.
- Mid-stage career + institutional types show consistent impact."
    )
}

for title, (img, text) in image_info.items():
    show_image_with_text(title, img, text)

# Footer section
st.markdown("---")
st.subheader("🧾 Summary Insights")
st.markdown("""
- **Career stage** is the strongest predictor across all models.
- **Institution type variables** (especially Type 1 and Type 7) improve model accuracy and add explanatory value.
- **Race** has measurable impact, particularly `Race_BlackAA`, which consistently shows reduced mentorship hours.
- **Log transformation** enhances model performance for skewed mentorship distributions.
""")
