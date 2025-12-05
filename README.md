# Peace Agreement Success Prediction Project

## Overview

The Peace Agreement Success Prediction Project is a machine learning and natural language processing (NLP) framework designed to forecast whether a peace agreement is likely to successfully end active armed conflict. The project integrates metadata, contextual conflict characteristics, and the full text of peace agreements to build interpretable predictive models and deploy them in an interactive application.

The project uses the PA-X Peace Agreements Database created by the University of Edinburgh. 

This repository contains data preprocessing scripts, classic ML models, transformer-based classification experiments, SHAP-based explainability tools, and a deployed Streamlit app for interactive prediction.

---

## Key Objectives

- Predict success or failure of peace agreements using:
  - Metadata and contextual conflict indicators  
  - Bag-of-words and TF-IDF textual features  
  - Transformer-based language models  
- Provide interpretable explanations using SHAP values  
- Deploy an interactive peace agreement prediction tool  
- Build foundations for advanced survival analysis and generative interpretability  

---

## Project Motivation

Peace agreements are complex documents that combine legal, institutional, political, and human rights commitments. Existing political science research identifies numerous structural factors—such as negotiation stage, conflict type, or presence of enforcement mechanisms—that influence peace durability. Yet few tools leverage both structured metadata and agreement text to produce real-time predictions or explain why certain agreements fail.

This project fills that gap by merging empirical conflict research with cutting-edge NLP and ML techniques.

---

## Dataset

### PA-X Peace Agreements Database
- Over 2,000 peace agreement texts  
- Extensive metadata on:
  - Conflict type (governmental, territorial, mixed, etc.)
  - Negotiation stage (pre-negotiation, partial, ceasefire, comprehensive, etc.)
  - Institutional provisions
  - Security arrangements
  - Human rights commitments
  - Inclusion of social groups  
- Implementation status and outcome indicators  

Dataset link:  
**https://www.peaceagreements.org/**

### Feature Engineering
- Metadata encoded into binary and categorical variables  
- Provisions converted into interpretable indicators  
- Text preprocessed using:
  - Tokenization  
  - Lowercasing  
  - Stopword removal  
  - TF-IDF representation  
- Hybrid feature matrix combining textual and structural information  

---

## Modeling Approach

### 1. Baseline Machine Learning Models
Implemented using metadata + text combinations:
- Logistic Regression  
- Support Vector Machines  
- Random Forest  
- Gradient Boosting  
- AdaBoost  
- XGBoost  

**Findings:**
- Text-only classic ML performed poorly  
- Adding metadata and contextual variables significantly improved performance  
- Random Forest and Decision Trees achieved most stable results  

---

### 2. Transformer-Based Models (Hugging Face)

Fine-tuned models:
- **DistilBERT-base-uncased**  
- **DeBERTa-v3-Large**  


**Best performing model: DeBERTa-v3-Large**
- Accuracy: **0.788**  
- Precision: **0.724**  
- Recall: **0.793**  
- F1-score: **0.724**  

These results demonstrate that transformers outperform traditional ML for text classification, especially in imbalanced datasets.

---

## Explainable AI (SHAP)

The deployed Random Forest includes SHAP-based interpretability:

- Local SHAP values identify most influential features  
- Users can see why a specific agreement was predicted to succeed or fail  
- Feature contributions include:
  - Negotiation stage  
  - Conflict type  
  - International missions  
  - Human rights provisions  
  - Enforcement mechanisms  
  - Security guarantees  

Explainability allows practitioners and researchers to interpret predictions in a theory-informed way.

---

## Deployment: Streamlit App

The **Peace Agreement Success Predictor** app enables interactive exploration.

Users can:
1. Input metadata features describing an agreement  
2. See predicted outcome (SUCCESS / FAILURE)  
3. View probability estimates  
4. Explore SHAP explanations for each prediction  

Repository includes:
- `streamlit_app.py`  
- `rf_feature_model.joblib`  
- `feature_names.json`  
- `feature_descriptions.json`

---

## Future Work

### Survival Analysis
The project will extend into a survival analysis framework using:
- Cox proportional hazards model  
- Random Survival Forests  
- DeepHit and neural survival models  

This allows modeling **peace duration** instead of binary success.

### Natural-Language Explanations (OpenAI API)

A planned enhancement involves integrating the **OpenAI API** to generate human-readable explanations of model predictions. This layer will enable the system to describe:

- Why a planned agreement might fail  
- What provisions or institutions could strengthen it  
- Which components are historically associated with success  
- How a treaty could be improved before signing  

This generative interpretability extension aims to bridge the gap between quantitative prediction and actionable policy guidance.

---

## Repository Structure

```text
peace-agreement-predictor/
├── README.md
├── requirements.txt
├── environment.yml
├── LICENSE
├── .gitignore
├── streamlit_app.py
├── rf_feature_model.joblib
├── feature_names.json
├── feature_descriptions.json
│
├── data/
│   ├── raw/                             
│   └── README.md           
│
│
├── scripts/                  # scripts for experiments & training workflows
│   ├── peace.ipynb
│   └── LLMs.ipynb
