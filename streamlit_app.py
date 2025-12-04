import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import json
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# LOAD RANDOM FOREST + METADATA
# ---------------------------------------------------------

@st.cache_resource
def load_rf():
    rf = joblib.load("rf_feature_model.joblib")

    with open("feature_names.json", "r") as f:
        feature_names = json.load(f)

    with open("feature_descriptions.json", "r") as f:
        feature_desc = json.load(f)

    return rf, feature_names, feature_desc

rf_model, feature_names, feature_desc = load_rf()

st.title("Peace Agreement Success Predictor (Random Forest + SHAP)")

st.write("""
This tool predicts whether a peace agreement will successfully end active fighting.  
It uses metadata variables and provides **local SHAP explanations** showing why the model predicted SUCCESS or FAILURE.
""")


# ---------------------------------------------------------
# USER INPUT FORM
# ---------------------------------------------------------

st.header("1. Input Metadata Features")

inputs = {}
for feat in feature_names:
    label = feature_desc.get(feat, feat)
    inputs[feat] = st.checkbox(label, value=False)

X_input = pd.DataFrame([inputs])


# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------

st.header("2. Prediction")

if st.button("Predict"):
    pred = rf_model.predict(X_input)[0]
    prob = rf_model.predict_proba(X_input)[0][1]

    st.subheader(f"Prediction: **{'SUCCESS' if pred == 1 else 'FAILURE'}**")
    st.metric("Probability of Success", f"{prob:.2f}")

    # ---------------------------------------------------------
    # LOCAL SHAP EXPLANATION
    # ---------------------------------------------------------

    st.header("3. Local SHAP Explanation")

    explainer = shap.TreeExplainer(rf_model)

    # ALWAYS use numpy for SHAP
    X_np = X_input.values
    sv_raw = explainer.shap_values(X_np)

    # Normalize SHAP output
    if isinstance(sv_raw, list):
        sv = sv_raw[1]   # class 1 (success)
    else:
        arr = np.array(sv_raw)
        if arr.ndim == 3:
            sv = arr[:, :, 1]
        else:
            sv = arr

    human_labels = [feature_desc.get(f, f) for f in feature_names]

    # SHAP force plot
    plt.figure(figsize=(12, 4))
    shap.force_plot(
        explainer.expected_value[1],
        sv[0],
        human_labels,
        matplotlib=True
    )
    st.pyplot(plt)

    # SHAP contribution table
    st.subheader("Top Influential Features")

    shap_df = pd.DataFrame({
        "Feature": human_labels,
        "SHAP Value": sv[0]
    }).sort_values("SHAP Value", key=np.abs, ascending=False)

    st.table(shap_df)
