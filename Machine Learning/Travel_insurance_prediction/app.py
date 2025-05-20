import streamlit as st
import pandas as pd
from Streamlit_insurance import load_data, clean_and_engineer, train_random_forest, tune_model

st.title("Travel Insurance Claim Prediction")

# File uploader
uploaded_file = st.file_uploader("Upload your travel_insurance.csv file", type="csv")

if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.write("Raw Data Preview:")
    st.dataframe(data.head())

    # Data cleaning and feature engineering
    data_encoded = clean_and_engineer(data)
    st.write("Processed Data Preview:")
    st.dataframe(data_encoded.head())

    # Model training
    if st.button("Train Random Forest Model"):
        clf, conf_matrix, class_report = train_random_forest(data_encoded)
        st.write("Confusion Matrix:")
        st.write(conf_matrix)
        st.write("Classification Report:")
        st.json(class_report)

    # Model tuning (optional)
    if st.button("Tune Model (RandomizedSearchCV)"):
        from sklearn.preprocessing import OneHotEncoder
        from sklearn.compose import ColumnTransformer
        categorical_columns = ['Agency', 'Agency Type', 'Distribution Channel', 'Product Name', 'Gender', 'Destination']
        preprocessor = ColumnTransformer(transformers=[
            ('onehot', OneHotEncoder(sparse=False, handle_unknown='ignore'), categorical_columns)
        ], remainder='passthrough')
        best_params, best_score = tune_model(data, preprocessor)
        st.write(f"Best Parameters: {best_params}")
        st.write(f"Best Cross-Validation Score: {best_score:.2f}")
