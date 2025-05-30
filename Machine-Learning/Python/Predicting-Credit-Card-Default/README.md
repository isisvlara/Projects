# Predicting Default Credit Case Study

Welcome to the **Predicting Default Credit Case Study** repository! This project explores the application of machine learning techniques to predict serious credit delinquency, enabling financial institutions to better assess risk and make informed lending decisions.

---

## Introduction

Financial institutions face substantial risk when clients default on their obligations. Using a dataset of European credit card transactions, this project aims to build predictive models that identify customers at high risk of serious delinquency (over 90 days overdue) within the next two years. The dataset is highly imbalanced, with fraud cases constituting only 0.172% of all transactions.

---

## Business Problem & Hypothesis

Banks rely heavily on loan repayments for revenue. Accurately identifying borrowers likely to default allows banks to mitigate risk and refine lending practices. We hypothesize that a borrower's likelihood of serious delinquency can be effectively predicted using demographic and financial history data.

---

## Methods & Analysis

- **Dataset Overview**: The dataset includes demographic details (age, income, dependents) and credit usage metrics (debt-to-income ratio, credit utilization, delinquency counts).
- **Data Cleaning**: Addressed missing values, capped outliers, and removed inconsistent entries to ensure data quality.
- **Exploratory Data Analysis (EDA)**: Identified skewness and class imbalance, motivating data transformations and balancing techniques.
- **Feature Engineering**: Created composite indicators, balanced the dataset using up/down-sampling and SMOTE, and applied Box-Cox transformations and scaling for normalization.
- **Model Building**: Evaluated multiple supervised classifiers—including logistic regression, decision trees, Random Forest, CatBoost, and neural networks—using precision, recall, F1 score, and ROC-AUC. Hyperparameters were optimized via stratified cross-validation, and decision thresholds were tuned for optimal performance.

---

## Results

- **Random Forest** and **CatBoost** emerged as the top-performing models.
  - Random Forest provided a robust, interpretable baseline, highlighting features like combined past-due counts and credit loans.
  - CatBoost handled class imbalance effectively and identified nuanced predictors such as revolving credit utilization.
- **Interpretability**: SHAP and LIME analyses revealed that credit-line usage and delinquency history are the most influential predictors, while features like income and living situation had lesser impact.
- **Performance Metrics**:
  - Random Forest: Macro F1 Score ≈ 59.6%, Micro F1 Score ≈ 93.5%
  - CatBoost: Macro F1 Score ≈ 64.8%, Micro F1 Score ≈ 85.9%
- **Key Insights**: Middle-aged borrowers are generally less risky, and a clean payment history significantly reduces default risk, though low income and youth can still elevate risk[.

---

## Recommendations & Ethical Considerations

- **Business Use**: Deploy the model to flag high-risk applicants and design early intervention strategies.
- **Ethical Use**: Ensure transparency, avoid discriminatory biases, and use interpretability tools (SHAP/LIME) to explain decisions to stakeholders and regulators.
- **Model Maintenance**: Regularly audit and update the model to maintain fairness and accuracy as credit practices evolve.

---

## Conclusion

This case study demonstrates how machine learning, combined with careful data preprocessing and interpretability, can support banks in reducing loan defaults and fostering fair, transparent lending. Random Forest and CatBoost are recommended for their balance of accuracy and interpretability, and ongoing SHAP-based audits are advised to ensure continued fairness and efficacy.
