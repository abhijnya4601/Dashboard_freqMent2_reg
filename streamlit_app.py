import streamlit as st
from PIL import Image
import os

# Utility to load image and caption together
def plot_with_caption(img_folder, img_filename, caption):
    try:
        img_path = os.path.join(img_folder, img_filename)
        st.image(Image.open(img_path), width=700)
        st.markdown(caption, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Image not found: {img_path}")

st.set_page_config(page_title="Mentorship Modeling Dashboard", layout="wide")
st.title("📊 Mentorship Hours Modeling Dashboard (with Institution Type)")
st.markdown("This dashboard summarizes model outputs explaining variation in mentorship hours by career stage, gender, race, and institutional affiliation.")

# === GLM Section ===
st.subheader("GLM Coefficient Plot")
plot_with_caption("GLM_Results", "GLM_Coefficient_Plot_with_EffectSize.png", """
**Interpretation**:<br>
- **Horizontal lines**: represent the 95% confidence interval of the estimated effect.<br>
- **Black dots**: show the point estimate (log effect) for each factor.<br>
- **Red dashed vertical line at 0**: indicates the no-effect line (baseline).<br>
- **Stars (*, **, ***)**: indicate significance levels (<i>p < 0.05, 0.01, 0.001</i>).<br>
- Positive effects (right of the red line) indicate increased mentorship hours.<br>
- Notable positives: <b>CareerStage_5.0</b>, <b>Gender_1.0</b>, <b>InstitutionType_1</b>.<br>
- Notable negatives: <b>CareerStage_6.0</b>, <b>Race_BlackAA</b>.
""")

# === Random Forest ===
st.subheader("Random Forest: Predicted vs Actual")
plot_with_caption("RandomForest_LogTransformed_Results", "Predicted_vs_Actual.png", """
- This plot compares predicted vs. actual mentorship hours using inverse-log-transformed values.<br>
- **Red dashed line** indicates ideal predictions.<br>
- Strong alignment below 40 hours, but poor fit for higher mentorship hours.
""")

st.subheader("Random Forest: Residuals vs Predicted")
plot_with_caption("RandomForest_LogTransformed_Results", "Residuals.png", """
- Residuals (errors) plotted against predicted values.<br>
- Most values hover around 0 (ideal).<br>
- Increasing underestimation trend visible past 25 hours.
""")

st.subheader("Random Forest: Top Feature Importances")
plot_with_caption("RandomForest_LogTransformed_Results", "Top15_Feature_Importance.png", """
- Top predictive features ranked by importance.<br>
- <b>Race_BlackAA</b> and <b>CareerStage_6.0</b> lead, followed by <b>InstitutionType_7</b>.<br>
- Institution variables contribute meaningfully to model performance.
""")

# === XGBoost Log ===
st.subheader("XGBoost (Log-Transformed): Predicted vs Actual")
plot_with_caption("XGBoost_LogTransformed", "Predicted_vs_Actual.png", """
- Higher accuracy alignment than Random Forest.<br>
- Red dashed diagonal = perfect predictions.<br>
- Performance robust for 5–30 mentorship hour range.
""")

st.subheader("XGBoost (Log): Residuals vs Predicted")
plot_with_caption("XGBoost_LogTransformed", "Residuals.png", """
- Tighter spread of residuals → less bias.<br>
- Minor skew post-30 hours, but overall improvement vs Random Forest.
""")

st.subheader("XGBoost (Log): Top Feature Importances")
plot_with_caption("XGBoost_LogTransformed", "Top15_Feature_Importance.png", """
- Top drivers: <b>CareerStage_6.0</b>, <b>Race_BlackAA</b>, <b>InstitutionType_1</b>.<br>
- Strong mix of institutional and demographic predictors.<br>
- More balanced compared to Random Forest.
""")

# === XGBoost Original ===
st.subheader("XGBoost (Original): Predicted vs Actual")
plot_with_caption("XGBoost_Original", "Predicted_vs_Actual.png", """
- Predictions scatter more than log version.<br>
- High mentorship hours are under-predicted more frequently.
""")

st.subheader("XGBoost (Original): Residuals vs Predicted")
plot_with_caption("XGBoost_Original", "Residuals.png", """
- Significant residual variance above 30 hours.<br>
- Model performs worse for mentors with high engagement.
""")

st.subheader("XGBoost (Original): Top Feature Importances")
plot_with_caption("XGBoost_Original", "Top15_Feature_Importance.png", """
- <b>CareerStage_5.0</b> dominates, followed by other career stages.<br>
- Institutional type 7 still appears high, but race/gender diminish in ranking.<br>
- Model may rely more on structural than demographic factors.
""")
