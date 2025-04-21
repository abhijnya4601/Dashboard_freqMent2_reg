
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("📊 Mentorship Hours Modeling Dashboard (with Institution Type)")
st.markdown("This dashboard summarizes model outputs explaining variation in mentorship hours by career stage, gender, race, and institutional affiliation.")

def show_image_with_text(title, img_path, desc):
    st.subheader(title)
    st.image(img_path, use_container_width=True)
    st.markdown(desc)

# Map of visuals and their interpretations
image_info = {
    "GLM Coefficient Plot": (
        "GLM_Results/GLM_Coefficient_Plot_with_EffectSize.png",
        "This plot shows log effects of predictors with 95% CI. Positive effects suggest more mentorship hours. Stars show significance: ***p<0.001, **p<0.01, *p<0.05."
    ),
    "Random Forest: Predicted vs Actual": (
        "RandomForest_LogTransformed_Results/Predicted_vs_Actual.png",
        "Points near the red line show better predictions. RF performs well for 5–30 hours, but underestimates >40 hours."
    ),
    "Random Forest: Residuals vs Predicted": (
        "RandomForest_LogTransformed_Results/Residuals.png",
        "Residuals show underestimation for high predicted hours. RF error grows past 25–30 hours."
    ),
    "Random Forest: Top Feature Importances": (
        "RandomForest_LogTransformed_Results/Top15_Feature_Importance.png",
        "Top predictors: Race_BlackAA, CareerStage_6.0, and InstitutionType_7. Career progression dominates influence."
    ),
    "XGBoost (Log): Predicted vs Actual": (
        "XGBoost_LogTransformed/Predicted_vs_Actual.png",
        "Better alignment than RF. Model fits more evenly across mid-range mentorship values."
    ),
    "XGBoost (Log): Residuals vs Predicted": (
        "XGBoost_LogTransformed/Residuals.png",
        "Tighter, more symmetric residuals. Some underestimation for high values remains, but bias reduced."
    ),
    "XGBoost (Log): Top Feature Importances": (
        "XGBoost_LogTransformed/Top15_Feature_Importance.png",
        "CareerStage_6.0 and Race_BlackAA dominate. Institutional type is still significant."
    ),
    "XGBoost (Original): Predicted vs Actual": (
        "XGBoost_Original/Predicted_vs_Actual.png",
        "Wider spread vs log-transformed version. Underestimates upper tail of mentorship hours."
    ),
    "XGBoost (Original): Residuals vs Predicted": (
        "XGBoost_Original/Residuals.png",
        "Residual spread and bias increase at high predicted values. Suggests worse generalization."
    ),
    "XGBoost (Original): Top Feature Importances": (
        "XGBoost_Original/Top15_Feature_Importance.png",
        "CareerStage_5.0 leads. Institutional types still important, though gender and race drop slightly."
    )
}

# Render each section
for title, (img, desc) in image_info.items():
    show_image_with_text(title, img, desc)

# Append full interpretation section at the end
st.markdown("---")
with st.expander("📄 Full Visual Report Summary (Narrative)", expanded=False):
    with open("model_report.md", "r") as f:
        st.markdown(f.read())
