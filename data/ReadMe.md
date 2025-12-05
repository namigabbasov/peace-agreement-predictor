# Data and Methods

## Overview

This project uses both **structured data** (metadata and contextual variables) and **unstructured data** (full-text peace agreements) to predict the effectiveness of peace agreements and identify key factors associated with their success or failure. The structured data is drawn primarily from the **UCDP Armed Conflict Dataset** and the **PA-X Peace Agreements Database**, while all textual data comes from peace agreement documents provided through PA-X.

Together, these datasets capture political, institutional, and social dimensions of peace agreements, enabling a comprehensive empirical assessment of agreement durability and implementation outcomes.

---

## Data Sources

### **1. PA-X Peace Agreements Database (University of Edinburgh)**
- Provides detailed metadata about peace agreements worldwide.  
- Includes variables on:
  - Conflict type  
  - Negotiation stage  
  - Inclusion of social groups  
  - Governance structures  
  - Human rights provisions  
  - Justice reforms  
  - Security arrangements  
  - Reconstruction efforts  
  - Transitional justice mechanisms  
  - Implementation strategies  

PA-X also provides **full text** of all peace agreements, enabling NLP-based analysis.

Dataset link:  
**https://www.peaceagreements.org/**

---

### **2. UCDP Armed Conflict Dataset (Uppsala Conflict Data Program)**  
The UCDP dataset provides the **dependent variable**, a measure of whether a peace agreement successfully halted active fighting.

---

## Dependent Variable

The dependent variable is **Effectiveness of Peace Agreement**, coded as:

- **1** → The agreement successfully stopped active fighting (fewer than 25 battle-related deaths in the following year)  
- **0** → The agreement failed to halt violence  

This measure is derived from the UCDP conflict episode dataset and aligns with conventional thresholds in conflict research.

Figures in the project notebook illustrate:
- The distribution of successful vs. unsuccessful agreements  
- Temporal patterns of agreement outcomes  

---

## Independent Variables

Independent variables include **document-level metadata** and **textual content** from peace agreements.  

### **Metadata Categories Include:**
- **Conflict Type**
- **Peace Process Stage**
- **Inclusion of Groups**
- **Governance Provisions**
- **Human Rights Commitments**
- **Justice Reform**
- **Reconstruction and Development**
- **Security Arrangements**
- **Transitional Justice**
- **Implementation Provisions**

These variables capture the institutional, political, and social features that may shape the durability and effectiveness of peace agreements.

The full text of peace agreements constitutes the **unstructured independent variable**, used for:
- Bag-of-Words and TF-IDF modeling
- Transformer-based language models (BERT, DeBERTa, RoBERTa)
- Feature extraction and semantic analysis

---

## Table 1: Datasets and Variables Used

| Dataset | Type | Category | Variables |
|--------|------|----------|-----------|
| **UCDP Armed Conflict Dataset** | Dependent | — | Effectiveness of Peace Agreement |
| **PA-X Database** | Independent | Conflict Type | Territory |
| | | | Government |
| | | | Interstate Conflict |
| | | | Mixed Conflict |
| | | | Intrastate Conflict |
| **PA-X Database** | Independent | Stage | Ceasefire |
| | | | Pre-negotiation |
| | | | Renewal |
| | | | Comprehensive |
| | | | Partial |
| **PA-X Database** | Independent | Groups | Racial/Ethnic Groups |
| | | | Religious Groups |
| | | | Refugees/Displaced Persons |
| | | | Women |
| **PA-X Database** | Independent | Governance | Political Institutions |
| | | | Elections |
| | | | Constitutional Modification |
| | | | Powersharing |
| **PA-X Database** | Independent | Human Rights | Civil and Political Rights |
| | | | Democracy |
| | | | Human Rights Protections |
| **PA-X Database** | Independent | Justice Reform | Criminal Justice |
| | | | Judiciary and Courts |
| **PA-X Database** | Independent | Reconstruction | Development |
| | | | International Funding |
| **PA-X Database** | Independent | Security | Security Guarantees |
| | | | Ceasefire Arrangements |
| | | | Police Reform |
| | | | Armed Forces Reform |
| | | | DDR (Disarmament, Demobilisation, Reintegration) |
| | | | Rebel Forces |
| | | | Withdrawal of Foreign Forces |
| **PA-X Database** | Independent | Transitional Justice | Amnesty |
| | | | Prisoner Release |
| | | | Reparations |
| | | | Reconciliation |
| **PA-X Database** | Independent | Implementation | UN Signatory |
| | | | International Mission |
| | | | Enforcement Mechanism |

---

## Notes for This Repository

- **Raw data is not included** in the repository due to licensing and size constraints.  
  Place raw files in: https://www.peaceagreements.org/
