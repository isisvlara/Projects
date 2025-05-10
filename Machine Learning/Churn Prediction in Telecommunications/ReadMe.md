## Multi-level Classification ML Project: Predicting Customer Churn

This repository presents a comprehensive machine learning project focused on predicting customer churn in the telecommunications industry using multi-level classification techniques. The goal is to not only identify which customers are likely to churn but also to predict the specific category and reason for churn, enabling targeted retention strategies.

---

### **Project Overview**

Customer churn, the rate at which customers stop using a company's services, is a critical metric for telecommunication businesses. High churn can significantly impact revenue and growth. By leveraging machine learning, this project aims to:

- Predict if a customer will churn.
- Classify the churn category (e.g., service, price, support).
- Identify the specific churn reason (e.g., network issues, billing disputes).

This multi-level approach enables proactive intervention and improved customer retention.

---

### **Business Impact**

- **Increase Revenue:** Retaining customers reduces lost revenue and the need for costly acquisition campaigns.
- **Optimize Acquisition Costs:** Preventing churn lowers the cost per customer by reducing the need to win back lost users.
- **Enhance Customer Satisfaction:** Understanding churn drivers allows for targeted improvements in service and customer experience.

---

### **Project Approach**

#### **1. Data Exploration & Preprocessing**
- **Exploratory Data Analysis (EDA):** Understand data distribution, missing values, and feature relevance.
- **Handling Missing Data:** Drop or impute missing values as appropriate.
- **Feature Engineering:** Remove irrelevant features/IDs, encode categorical variables (using label encoding to avoid dimensionality explosion), and address class imbalance with SMOTE or undersampling.

#### **2. Problem Formulation**
- **Multi-class Classification:** First, predict the churn category (e.g., "Not Applicable" for non-churners).
- **Multi-label Classification:** Next, predict both the churn category and churn reason, as customers may have multiple reasons for leaving.

#### **3. Model Selection**
- **Baseline Models:** Decision Trees, Logistic Regression.
- **Ensemble Methods:** Random Forest, Bagging, Boosting (including XGBoost and Gradient Boosting).
- **Deep Learning:** Multi-layer Perceptron (MLP) using Keras for complex patterns.

#### **4. Model Training & Evaluation**
- **Supervised Learning:** Train models on labeled historical data.
- **Evaluation Metrics:** Use F1 score, recall, precision, confusion matrix, and ROC AUC to assess performance, with special attention to recall and F1-score due to class imbalance and business priorities.
- **Avoiding Data Leakage:** Ensure preprocessing is applied separately to training and test sets.

---

### **Key Concepts**

| Task Type               | Description                                                                                 | Example Algorithms                  |
|-------------------------|--------------------------------------------------------------------------------------------|-------------------------------------|
| Multi-class Classification | Assigns one label from multiple possible categories to each instance.                     | Logistic Regression, Random Forest  |
| Multi-label Classification | Assigns multiple labels (e.g., churn category and reason) to each instance.               | Neural Networks, Ensemble Methods   |

---

### **Workflow Summary**

1. **Data Exploration:** Analyze and visualize data to inform preprocessing and modeling steps.
2. **Preprocessing:** Clean data, encode features, and balance classes.
3. **Modeling:** Build and tune models for both multi-class and multi-label tasks.
4. **Evaluation:** Select models based on business-relevant metrics.
5. **Deployment (optional):** Package the best model for integration with business systems.

---

### **Tools & Libraries**

- **Python:** Core programming language for data analysis and modeling.
- **Pandas/Numpy:** Data manipulation and analysis.
- **Scikit-learn:** Traditional machine learning models and evaluation.
- **Imbalanced-learn:** SMOTE and undersampling techniques.
- **Keras/TensorFlow:** Deep learning models (MLP).
- **Matplotlib/Seaborn:** Data visualization.

---

### **How to Use This Repository**

1. **Clone the repository.**
2. **Review the Poject_one notebook** to understand the data.
3. **Run the preprocessing scripts** to prepare the data.
4. **Train models** using the provided scripts and tune hyperparameters as needed.
5. **Evaluate results** using the metrics and confusion matrices provided.
6. **Interpret model outputs** to inform business decisions on customer retention.

Note: Data set stored in zip file

---

### **Conclusion**

This project provides a robust framework for telecom companies to predict customer churn at multiple levels, offering actionable insights into both the likelihood and reasons for churn. By following the outlined approach, organizations can proactively address churn, improve customer satisfaction, and drive sustainable growth.

---

*For more details, refer to the code, notebooks, and documentation in this repository.*
