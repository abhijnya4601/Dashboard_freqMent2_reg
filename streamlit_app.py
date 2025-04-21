import streamlit as st
from PIL import Image

st.set_page_config(page_title="Mentorship Dashboard", layout="wide")

st.title("📊 Mentorship Hours Modeling Dashboard (with Institution Type)")
st.markdown("This dashboard summarizes model outputs explaining variation in mentorship hours by career stage, gender, race, and institutional affiliation.")

# Function to load and display image with explanation
def plot_with_caption(img_path, caption):
    st.image(Image.open(img_path), use_column_width=True)
    st.markdown(caption)

# 1. GLM Coefficient Plot
st.subheader("📊 GLM Coefficient Plot")
plot_with_caption("GLM_Coefficient_Plot_with_EffectSize.png", """
**Interpretation:**  
- Horizontal lines = 95% confidence intervals  
- Dots = log effect estimate  
- Stars = significance (*p* < 0.05, **p* < 0.01, ***p* < 0.001)  
- Positive log values imply increased mentorship hours  
- `CareerStage_5.0`, `Gender_1.0`, and `InstitutionType_1` show strong positive effects  
- `CareerStage_6.0`, `Race_BlackAA` indicate negative impact
""")

# 2. Random Forest
st.subheader("🌲 Random Forest: Predicted vs Actual")
plot_with_caption("Predicted_vs_Actual_RF.png", """
**Interpretation:**  
- Most values fall under 40 hours  
- Red diagonal = ideal predictions  
- Model underpredicts very high mentorship hours
""")

st.subheader("🌲 Random Forest: Residuals vs Predicted")
plot_with_caption("Residuals_RF.png", """
**Interpretation:**  
- Residuals ideally hover around 0  
- Slight negative slope after 25 predicted hours — indicates underestimation for higher ranges
""")

st.subheader("🌲 Random Forest: Top 15 Feature Importances")
plot_with_caption("Top15_Feature_Importance_RF.png", """
**Interpretation:**  
- `Race_BlackAA` and `CareerStage_6.0` dominate  
- Institution types (`InstitutionType_1`, etc.) matter  
- Gender has lesser predictive power
""")

# 3. XGBoost - Log Transformed
st.subheader("⚡ XGBoost (Log): Predicted vs Actual")
plot_with_caption("Predicted_vs_Actual_XGB_Log.png", """
**Interpretation:**  
- Tighter clustering along diagonal  
- Better performance in 10–30 hour range  
- Slight bias at very high actual values
""")

st.subheader("⚡ XGBoost (Log): Residuals vs Predicted")
plot_with_caption("Residuals_XGB_Log.png", """
**Interpretation:**  
- Residuals more symmetric  
- Outliers reduced in comparison to RF  
- Slight bias above 40 predicted hours
""")

st.subheader("⚡ XGBoost (Log): Top 15 Feature Importances")
plot_with_caption("Top15_Feature_Importance_XGB_Log.png", """
**Interpretation:**  
- `CareerStage_6.0`, `Race_BlackAA`, `InstitutionType_1` top the chart  
- Shows good mix of career stage, race, and institution-based predictors
""")

# 4. XGBoost - Original Target
st.subheader("🔷 XGBoost (Original): Predicted vs Actual")
plot_with_caption("Predicted_vs_Actual_XGB_Orig.png", """
**Interpretation:**  
- Higher scatter at upper actual values  
- Underperforms compared to log version
""")

st.subheader("🔷 XGBoost (Original): Residuals vs Predicted")
plot_with_caption("Residuals_XGB_Orig.png", """
**Interpretation:**  
- Bias increases after ~30 predicted hours  
- Positive skew indicates consistent underprediction
""")

st.subheader("🔷 XGBoost (Original): Top 15 Feature Importances")
plot_with_caption("Top15_Feature_Importance_XGB_Orig.png", """
**Interpretation:**  
- `CareerStage_5.0`, `2.0`, and `3.0` dominate  
- `InstitutionType_7` and `6` also rank high  
- Gender and race have moderate influence
""")

# 5. Full Interpretive Report
with st.expander("📄 Full Analysis Summary and Interpretation Report"):
    st.markdown(open("full_analysis_report.txt").read())

