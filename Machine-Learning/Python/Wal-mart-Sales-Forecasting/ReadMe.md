# Sales Forecasting Using Walmart Stores

Welcome to the repository for the project: **Sales Forecasting Using Walmart Stores**. This project leverages machine learning to improve sales forecasting accuracy for Walmart, supporting better inventory management, staffing, and operational efficiency across thousands of stores.

---

## Overview

Sales forecasting is crucial for large retailers like Walmart, where accurate predictions help maintain optimal inventory, reduce costs, and enhance customer satisfaction. By applying data science and machine learning, we aim to uncover trends and patterns in historical sales data, integrate external factors (like weather and holidays), and generate precise weekly sales forecasts at the store and department level.

---

## Business Problem & Hypothesis

Walmart operates over 10,000 stores in 24 countries, each affected by unique seasonal, promotional, and regional factors. Inaccurate forecasts can lead to overstocking (increased costs) or understocking (lost sales and dissatisfied customers). Our hypothesis: **Integrating machine learning techniques with historical sales, holiday, promotion, and location data will significantly improve weekly sales forecast accuracy compared to traditional statistical methods**.

---

## Methods & Analysis

Our workflow included:

- **Data Loading & Integration**: Combined historical sales with store metadata, weather, promotions, and holiday calendars.
- **Data Cleaning & Preprocessing**: Converted data types, imputed missing values, removed duplicates, and ensured consistency.
- **Exploratory Data Analysis (EDA)**: Used visualizations (histograms, boxplots, heatmaps) to identify trends, correlations, and outliers.
- **Feature Engineering**: Created new features (week number, year, holiday flags, lagged sales) to capture seasonality and temporal effects.
- **Data Splitting**: Divided data into training and testing sets based on time, preventing data leakage.
- **Model Training & Evaluation**: Compared Linear Regression, Decision Tree, and Random Forest regressors using MAE and RMSE metrics.
- **Prediction**: Deployed the best-performing model (Random Forest) to forecast weekly sales on test data.

---

## Results

- **Random Forest Regression** outperformed other models, achieving the lowest RMSE and MAE on validation and test sets.
- Visualizations showed strong alignment between predicted and actual sales, especially for larger stores.
- Feature importance analysis highlighted store size, department, and temporal features as key predictors.

| Model             | RMSE (Val) | MAE (Val) | RMSE (Test) | MAE (Test) |
|-------------------|------------|-----------|-------------|------------|
| Linear Regression | 7731.06    | 2829.84   | 5128.54     | 2514.60    |
| Decision Tree     | 8490.61    | 2426.67   | 6109.89     | 2918.42    |
| Random Forest     | 6082.37    | 1920.15   | 4221.75     | 2142.02    |

---

## Recommendations & Ethical Considerations

- **Model Maintenance**: Retrain models regularly to adapt to changing sales patterns.
- **Data Quality**: Address outliers and missing values for robust predictions.
- **Advanced Models**: Explore time series models (e.g., ARIMA, Prophet) for further improvements.
- **Ethics**: Ensure human oversight in staffing decisions influenced by forecasts, and align improvements with sustainability goals (e.g., reducing waste).

---

## Data Dictionary

**sales_data.csv**  
- Store: Store number (categorical)  
- Dept: Department number (categorical)  
- Date: Date of sales (datetime)  
- Weekly_Sales: Weekly sales (numerical, target)  
- IsHoliday: Holiday week flag (binary)  

**stores.csv**  
- Store: Store number (categorical)  
- Type: Store type (categorical)  
- Size: Store size in sq ft (numerical)  

**features.csv**  
- Store: Store number (categorical)  
- Date: Date (datetime)  
- Temperature, Fuel_Price, CPI, Unemployment: Regional indicators (numerical)  
- MarkDown1-5: Promotional markdowns (numerical)  
- IsHoliday: Holiday week flag (binary)  

---

## Conclusion

This project demonstrates the value of machine learning in retail sales forecasting, with Random Forest models providing significant accuracy gains. Ongoing model updates and ethical considerations are essential for sustained impact and responsible use.

---

*Explore the code, data, and notebooks in this repository to learn more about our approach and findings!*
