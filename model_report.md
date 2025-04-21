
### 📄 Model Insights Report: Visual Interpretation Summary

#### 📊 GLM Coefficient Plot with 95% CI and Effect Sizes
- **Horizontal lines**: represent the 95% confidence interval of the estimated effect.
- **Black dots**: show the point estimate (log effect) for each factor.
- **Red dashed vertical line at 0**: indicates the no-effect line (baseline).
- **Stars (***, **, *)**: indicate the significance level (*p < 0.05, **p < 0.01, ***p < 0.001*).
- `CareerStage_5.0`, `Gender_1.0`, and `InstitutionType_1` are among the **strongest positive predictors** of mentorship.
- `CareerStage_6.0` and `Race_BlackAA` show **statistically significant negative effects**, suggesting late-career professionals and Black/African American participants reported fewer mentorship hours on average.

---

#### 🔵 Random Forest — Predicted vs Actual (Log Transformed)
- This plot compares **predicted mentorship hours** (after inverse log transform) against actual recorded hours.
- The **red dashed diagonal** indicates a perfect prediction line.
- Most data points cluster between 5–30 hours.
- **Underprediction** occurs beyond ~40 hours — the model struggles with very high mentorship hour values.

#### 🔵 Random Forest — Residuals vs Predicted
- **Residuals** are the difference between actual and predicted values.
- The blue scatter indicates variability; ideally, we want a horizontal spread centered at 0.
- A **negative curve** appears beyond 25 predicted hours — the model **underestimates high-hour mentors**.

#### 🔵 Random Forest — Top 15 Feature Importances
- The top contributing factor is `Race_BlackAA`, followed by `CareerStage_6.0`.
- Multiple **institution types** appear in the top 10, affirming their value in prediction.
- Gender variables have **lower importance** than race and career stage.

---

#### 🔶 XGBoost (Log-Transformed Target) — Predicted vs Actual
- Similar to Random Forest, but shows **slightly better alignment with the diagonal line**.
- Indicates better generalization and fewer outliers in the log-transformed model.

#### 🔶 XGBoost — Residuals vs Predicted
- Residuals are tighter and more centralized, especially in mid-ranges (10–30 hours).
- **Better residual symmetry** than Random Forest.
- Some noise persists beyond 40 hours, but bias is lower overall.

#### 🔶 XGBoost — Top 15 Feature Importances
- `CareerStage_6.0`, `Race_BlackAA`, and `InstitutionType_1` top the list.
- Shows consistent importance of **institutional affiliation** alongside race and career progression.
- Balanced mix of demographic and institutional variables.

#### 🔷 XGBoost (Original) — Predicted vs Actual
- Moderate clustering near the diagonal, but more **scatter at high actual values**.
- This version underperforms compared to log-transformed predictions.

#### 🔷 XGBoost (Original) — Residuals vs Predicted
- Visible **bias at high prediction ends** with more variance.
- Residual line shows some positive skew — errors increase with prediction.

#### 🔷 XGBoost (Original) — Top 15 Feature Importances
- `CareerStage_5.0` leads, followed by several mid-stage and early-career indicators.
- `InstitutionType_7`, `InstitutionType_6`, and `InstitutionType_1` appear strongly, confirming value of institutional breakdowns.

---

These visualizations collectively reinforce the following:
- Career stage remains the dominant predictor across all models.
- Institution types significantly improve model fit.
- Race and gender effects are observable and vary in impact.
- Log transformation improves model accuracy and interpretability across Random Forest and XGBoost.
