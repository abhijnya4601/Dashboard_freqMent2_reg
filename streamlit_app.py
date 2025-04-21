import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Mentorship Modeling Dashboard", layout="wide")

st.title("📊 Mentorship Hours Modeling Dashboard (with Institution Type)")
st.markdown("This dashboard summarizes model outputs explaining variation in mentorship hours by career stage, gender, race, and institutional affiliation.")

def plot_with_caption(img_path, caption):
    if os.path.exists(img_path):
        st.image(Image.open(img_path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Image not found: `{img_path}`")

# === GLM Section ===
st.header("GLM Coefficient Plot")
plot_with_caption("GLM_Coefficient_Plot_with_EffectSize.png", 
"""
This plot shows GLM-estimated log effects with 95% CI. 
Positive effects (right of red line) imply higher mentorship hours. 
Stars show statistical significance.
""")

# === Random Forest Section ===
st.header("Random Forest: Predicted vs Actual")
plot_with_caption("RF_Predicted_vs_Actual.png", 
"Prediction alignment with real values. Most predictions fall under 40 hours. Strong alignment in the 5–30 hour range.")

st.header("Random Forest: Residuals vs Predicted")
plot_with_caption("RF_Residuals_vs_Predicted.png", 
"Residuals show how far predictions deviate from true values. Underestimation rises after 25 predicted hours.")

st.header("Random Forest: Top Feature Importances")
plot_with_caption("RF_Top15_Feature_Importance.png", 
"Race_BlackAA, CareerStage_6.0, and institutional types show strong predictive power.")

# === XGBoost (Log Transformed) ===
st.header("XGBoost (Log-Transformed): Predicted vs Actual")
plot_with_caption("XGB_Log_Predicted_vs_Actual.png", 
"Better alignment with diagonal, especially in the 10–30 hour range. Few high-hour outliers.")

st.header("XGBoost (Log): Residuals vs Predicted")
plot_with_caption("XGB_Log_Residuals_vs_Predicted.png", 
"Residuals mostly centered around 0. Symmetrical spread up to 40 hours.")

st.header("XGBoost (Log): Top Feature Importances")
plot_with_caption("XGB_Log_Top15_Feature_Importance.png", 
"CareerStage_6.0 and Race_BlackAA top the list. Institution types add substantial value.")

# === XGBoost (Original) ===
st.header("XGBoost (Original): Predicted vs Actual")
plot_with_caption("XGB_Original_Predicted_vs_Actual.png", 
"More scatter in high-hour mentors. Alignment weaker compared to log-transformed model.")

st.header("XGBoost (Original): Residuals vs Predicted")
plot_with_caption("XGB_Original_Residuals_vs_Predicted.png", 
"Bias appears in upper prediction range — residuals increase after 30 hours.")

st.header("XGBoost (Original): Top Feature Importances")
plot_with_caption("XGB_Original_Top15_Feature_Importance.png", 
"CareerStage_5.0, mid-career and institutional affiliation drive predictions.")

# === Report Section ===
st.markdown("### 📄 Model Insights Report")
with st.expander("Click to expand full narrative report"):
    st.markdown("""
#### ✏️ Objective
To analyze how **career stage**, **gender**, **race**, and **institution types (1, 2, 3)** influence monthly mentorship hours (`Freq_Ment2_Hours_Clean`).

#### 📊 GLM Coefficient Plot
- **Horizontal lines** = 95% confidence intervals.
- **Dots** = estimated effect (log scale).
- **Red line** = no effect.
- **Stars** = significance.
- CareerStage_5.0, Gender_1.0, InstitutionType_1 show strong positive effects.
- CareerStage_6.0, Race_BlackAA = negative effect on mentorship hours.

#### 🔵 Random Forest
- Predictions tightly clustered 5–30 hours.
- Residuals show bias at upper ranges.
- Top features: Race_BlackAA, CareerStage_6.0, multiple institution types.

#### 🔶 XGBoost (Log)
- Higher alignment with actual values.
- Residuals more balanced.
- Top features: CareerStage_6.0, Race_BlackAA, InstitutionType_1.

#### 🔷 XGBoost (Original)
- Struggles with higher mentorship predictions.
- CareerStage_5.0 and institutional variables still highly important.

---

📌 **Conclusion**:
- Career stage = dominant driver across all models.
- Institution type boosts predictive accuracy.
- Race and gender effects are nuanced and informative.
- Log transformation improves accuracy, especially for tree-based models.
""")
