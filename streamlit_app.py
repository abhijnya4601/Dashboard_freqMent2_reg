import streamlit as st
from PIL import Image
import os

# Utility to load image and caption together
def plot_with_caption(img_folder, img_filename, caption):
    try:
        img_path = os.path.join(img_folder, img_filename)
        st.image(Image.open(img_path), use_container_width=True)
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
- **Stars (*, **, ***)**: indicate significance levels (<i>p < 0.05, 0.01, 0.001</i>)<br>
- <b>CareerStage_5.0</b>, <b>Gender_1.0</b>, <b>InstitutionType_1</b> → Strong positive predictors.<br>
- <b>CareerStage_6.0</b>, <b>Race_BlackAA</b> → Significant negative effects.
""")

# === Random Forest ===
st.subheader("Random Forest: Predicted vs Actual")
plot_with_caption("RandomForest_LogTransformed_Results", "RF_Predicted_vs_Actual.png", """
- Predicted vs actual mentorship hours (inverse log transformed).<br>
- **Red dashed diagonal** = ideal predictions.<br>
- Model underestimates values > 40 hours.
""")

st.subheader("Random Forest: Residuals vs Predicted")
plot_with_caption("RandomForest_LogTransformed_Results", "RF_Residuals_vs_Predicted.png", """
- Residual = actual - predicted.<br>
- Negative residual curve beyond ~25 hrs shows underestimation.
""")

st.subheader("Random Forest: Top Feature Importances")
plot_with_caption("RandomForest_LogTransformed_Results", "RF_Top15_Feature_Importance.png", """
- Top: <b>Race_BlackAA</b>, <b>CareerStage_6.0</b>, <b>InstitutionType_7</b>.<br>
- Institutional data adds substantial predictive power.
""")

# === XGBoost Log ===
st.subheader("XGBoost (Log-Transformed): Predicted vs Actual")
plot_with_caption("XGBoost_LogTransformed", "XGB_Log_Predicted_vs_Actual.png", """
- More accurate alignment with the diagonal.<br>
- Log transformation helps mitigate outlier influence.
""")

st.subheader("XGBoost (Log): Residuals vs Predicted")
plot_with_caption("XGBoost_LogTransformed", "XGB_Log_Residuals_vs_Predicted.png", """
- Residuals concentrated 10–30 hours → tighter fit.<br>
- Less bias vs. Random Forest.
""")

st.subheader("XGBoost (Log): Top Feature Importances")
plot_with_caption("XGBoost_LogTransformed", "XGB_Log_Top15_Feature_Importance.png", """
- Dominant: <b>CareerStage_6.0</b>, <b>Race_BlackAA</b>, <b>InstitutionType_1</b>.<br>
- Strong mix of institutional + demographic drivers.
""")

# === XGBoost Original ===
st.subheader("XGBoost (Original): Predicted vs Actual")
plot_with_caption("XGBoost_Original", "XGB_Original_Predicted_vs_Actual.png", """
- Moderate scatter.<br>
- Log version performs better on upper values.
""")

st.subheader("XGBoost (Original): Residuals vs Predicted")
plot_with_caption("XGBoost_Original", "XGB_Original_Residuals_vs_Predicted.png", """
- Residuals increase sharply > 30 hours.<br>
- Bias in high-prediction zone.
""")

st.subheader("XGBoost (Original): Top Feature Importances")
plot_with_caption("XGBoost_Original", "XGB_Original_Top15_Feature_Importance.png", """
- Leading: <b>CareerStage_5.0</b>, <b>InstitutionType_7</b>.<br>
- Gender/race less dominant than in log version.
""")
