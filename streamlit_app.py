import streamlit as st
from PIL import Image
import os

# Utility to load image and caption together
def plot_with_caption(img_path, caption):
    try:
        st.image(Image.open(os.path.join("images", img_path)), use_container_width=True)
        st.markdown(caption, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Image not found: {img_path}")

st.set_page_config(page_title="Mentorship Modeling Dashboard", layout="wide")
st.title("📊 Mentorship Hours Modeling Dashboard (with Institution Type)")
st.markdown("This dashboard summarizes model outputs explaining variation in mentorship hours by career stage, gender, race, and institutional affiliation.")

# GLM Plot
st.header("GLM Coefficient Plot")
plot_with_caption("GLM_Coefficient_Plot_with_EffectSize.png", """
**Interpretation**:<br>
- **Horizontal lines**: represent the 95% confidence interval of the estimated effect.<br>
- **Black dots**: show the point estimate (log effect) for each factor.<br>
- **Red dashed vertical line at 0**: indicates the no-effect line (baseline).<br>
- **Stars (\*, \*\*, \*\*\*)**: indicate the significance level (<i>p < 0.05, 0.01, 0.001</i>)<br>
- <b>CareerStage_5.0, Gender_1.0, InstitutionType_1</b> are strong positive predictors.<br>
- <b>CareerStage_6.0, Race_BlackAA</b> show negative effects.
""")

# Random Forest
st.header("Random Forest: Predicted vs Actual")
plot_with_caption("RF_Predicted_vs_Actual.png", """
- Predicted mentorship hours vs. actual (after log transformation reversal).<br>
- Red dashed line = perfect prediction.<br>
- Underprediction evident > 40 hours.
""")

st.header("Random Forest: Residuals vs Predicted")
plot_with_caption("RF_Residuals_vs_Predicted.png", """
- Residuals = actual - predicted.<br>
- Curve downward above ~25 hours → underestimation for high-hour mentors.
""")

st.header("Random Forest: Top Feature Importances")
plot_with_caption("RF_Top15_Feature_Importance.png", """
- Top feature: Race_BlackAA.<br>
- CareerStage_6.0, InstitutionType_7, and Gender_2.0 also influential.
""")

# XGBoost Log
st.header("XGBoost (Log-Transformed): Predicted vs Actual")
plot_with_caption("XGB_Log_Predicted_vs_Actual.png", """
- Tighter clustering near diagonal.<br>
- Log transformation improves spread.
""")

st.header("XGBoost (Log): Residuals vs Predicted")
plot_with_caption("XGB_Log_Residuals_vs_Predicted.png", """
- Better residual symmetry 10–30 hours.<br>
- Slight upward deviation > 40 hours.
""")

st.header("XGBoost (Log): Top Feature Importances")
plot_with_caption("XGB_Log_Top15_Feature_Importance.png", """
- CareerStage_6.0, Race_BlackAA, and InstitutionType_1 dominate.<br>
- Balanced importance among race, career stage, institution types.
""")

# XGBoost Original
st.header("XGBoost (Original): Predicted vs Actual")
plot_with_caption("XGB_Original_Predicted_vs_Actual.png", """
- Less clustered than log-transformed.<br>
- Underperforms on upper range.
""")

st.header("XGBoost (Original): Residuals vs Predicted")
plot_with_caption("XGB_Original_Residuals_vs_Predicted.png", """
- Residuals skewed positive with high predictions.<br>
- More variance vs. log-transformed.
""")

st.header("XGBoost (Original): Top Feature Importances")
plot_with_caption("XGB_Original_Top15_Feature_Importance.png", """
- CareerStage_5.0 dominates, followed by InstitutionType_7.<br>
- Gender and race lower in rank here.
""")
