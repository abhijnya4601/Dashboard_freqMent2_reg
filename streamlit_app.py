import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("📊 Mentorship Hours Modeling Dashboard (with Institution Type)")
st.markdown("This dashboard summarizes model outputs explaining variation in mentorship hours by career stage, gender, race, and institutional affiliation.")

def show_image_with_text(title, img_path, desc):
    st.subheader(title)
    st.image(img_path, width=650)  # controlled size to avoid large display
    st.markdown(desc)

# Image display with interpretation under each
image_info = {
    "GLM Coefficient Plot": (
        "GLM_Results/GLM_Coefficient_Plot_with_EffectSize.png",
        "- **Black dots** represent log effect sizes.\n"
        "- **Blue error bars** = 95% CI.\n"
        "- **Red dashed line** = no effect (baseline).\n"
        "- Variables like `CareerStage_5.0`, `Gender_1.0`, and `InstitutionType_1` have strong positive effects.\n"
        "- `CareerStage_6.0` and `Race_BlackAA` show significant negative effects on mentorship hours."
    ),
    "Random Forest: Predicted vs Actual": (
        "RandomForest_LogTransformed_Results/Predicted_vs_Actual.png",
        "Predictions cluster well for 5–30 hours. Slight underprediction is seen above 40 hours."
    ),
    "Random Forest: Residuals vs Predicted": (
        "RandomForest_LogTransformed_Results/Residuals.png",
        "Residuals spread around 0, but with downward bias above 25 hours — indicating underprediction."
    ),
    "Random Forest: Top Feature Importances": (
        "RandomForest_LogTransformed_Results/Top15_Feature_Importance.png",
        "`Race_BlackAA` and `CareerStage_6.0` are the most influential predictors. Institutional types matter too."
    ),
    "XGBoost (Log): Predicted vs Actual": (
        "XGBoost_LogTransformed/Predicted_vs_Actual.png",
        "Improved prediction fit over Random Forest. More consistent around 10–30 hour ranges."
    ),
    "XGBoost (Log): Residuals vs Predicted": (
        "XGBoost_LogTransformed/Residuals.png",
        "Residuals are tightly packed and more symmetric — good model fit across the range."
    ),
    "XGBoost (Log): Top Feature Importances": (
        "XGBoost_LogTransformed/Top15_Feature_Importance.png",
        "`CareerStage_6.0`, `Race_BlackAA`, and `InstitutionType_1` show highest influence."
    ),
    "XGBoost (Original): Predicted vs Actual": (
        "XGBoost_Original/Predicted_vs_Actual.png",
        "Wider variance. Some underperformance for very high mentorship hour values."
    ),
    "XGBoost (Original): Residuals vs Predicted": (
        "XGBoost_Original/Residuals.png",
        "Bias appears in upper prediction range — residuals increase after 30 hours."
    ),
    "XGBoost (Original): Top Feature Importances": (
        "XGBoost_Original/Top15_Feature_Importance.png",
        "`CareerStage_5.0`, `2.0`, `3.0` dominate. `InstitutionType_7` also shows strong signal."
    )
}

# Render each plot and description
for title, (img_path, interpretation) in image_info.items():
    show_image_with_text(title, img_path, interpretation)

st.markdown("---")
st.caption("Dashboard generated for institutional mentorship research. Visuals include GLM, Random Forest, and XGBoost interpretations.")
