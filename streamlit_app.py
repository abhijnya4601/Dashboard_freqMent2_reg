
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("📊 Mentorship Hours Modeling Dashboard (with Institution Type)")
st.markdown("This dashboard summarizes model outputs explaining variation in mentorship hours by career stage, gender, race, and institutional affiliation.")

def show_image_with_text(title, img_path, desc):
    st.subheader(title)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(img_path, use_column_width=True)
    with col2:
        st.markdown(desc)

image_info = {
    "GLM Coefficient Plot": (
        "GLM_Results/GLM_Coefficient_Plot_with_EffectSize.png",
        "This plot shows GLM-estimated log effects with 95% CI. Positive effects (right of red line) imply higher mentorship hours. Stars show statistical significance."
    ),
    "Random Forest: Predicted vs Actual": (
        "RandomForest_LogTransformed_Results/Predicted_vs_Actual.png",
        "Prediction alignment with real values. Most predictions fall under 40 hours. Strong alignment in the 5–30 hour range."
    ),
    "Random Forest: Residuals vs Predicted": (
        "RandomForest_LogTransformed_Results/Residuals.png",
        "Residuals (errors) spread around zero, but higher predictions show underestimation bias."
    ),
    "Random Forest: Top Feature Importances": (
        "RandomForest_LogTransformed_Results/Top15_Feature_Importance.png",
        "Top predictors include Race_BlackAA, CareerStage_6.0, and InstitutionType_7."
    ),
    "XGBoost (Log): Predicted vs Actual": (
        "XGBoost_LogTransformed/Predicted_vs_Actual.png",
        "Better prediction alignment than Random Forest. Very high mentorship hours still underpredicted."
    ),
    "XGBoost (Log): Residuals vs Predicted": (
        "XGBoost_LogTransformed/Residuals.png",
        "Residuals tighter and more symmetric. Model handles mid-range values (10–30) effectively."
    ),
    "XGBoost (Log): Top Feature Importances": (
        "XGBoost_LogTransformed/Top15_Feature_Importance.png",
        "CareerStage_6.0, Race_BlackAA, and InstitutionType_1 dominate the model's decision-making."
    ),
    "XGBoost (Original): Predicted vs Actual": (
        "XGBoost_Original/Predicted_vs_Actual.png",
        "Slightly more error and scatter than log-transformed version, especially for extreme values."
    ),
    "XGBoost (Original): Residuals vs Predicted": (
        "XGBoost_Original/Residuals.png",
        "Residuals more variable than log version. Greater bias with higher predictions."
    ),
    "XGBoost (Original): Top Feature Importances": (
        "XGBoost_Original/Top15_Feature_Importance.png",
        "CareerStage_5.0, CareerStage_2.0, and InstitutionType_7 stand out. Race and gender matter less."
    )
}

for title, (img, desc) in image_info.items():
    show_image_with_text(title, img, desc)


# Narrative Report Section
st.markdown("---")
with st.expander("📄 Model Insights Report (Click to Expand)", expanded=False):
    with open("model_report.md", "r") as f:
        st.markdown(f.read())
