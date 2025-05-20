import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_and_engineer(data):
    data['Gender'] = data['Gender'].fillna('Unknown')
    data['Claim'] = data['Claim'].map({'Yes':1, 'No':0})
    data.rename(columns={'Commision (in value)': 'Commission'}, inplace=True)
    data["profit"] = data['Net Sales'] - data['Commission']
    categorical_features = ['Agency', 'Agency Type', 'Distribution Channel', 'Product Name', 'Destination', 'Gender']
    data_encoded = pd.get_dummies(data, columns=categorical_features, drop_first=True)
    return data_encoded

def train_random_forest(data_encoded):
    X = data_encoded.drop('Claim', axis=1)
    y = data_encoded['Claim']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred, output_dict=True)
    return clf, conf_matrix, class_report

def tune_model(data, preprocessor):
    param_dist = {
        'n_estimators': [50, 100, 150],
        'max_depth': [5, 10, None],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'bootstrap': [True, False]
    }
    X = data.drop('Claim', axis=1)
    y = data['Claim']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train_encoded = preprocessor.fit_transform(X_train)
    rf = RandomForestClassifier(random_state=42)
    random_search = RandomizedSearchCV(
        estimator=rf,
        param_distributions=param_dist,
        n_iter=5,
        cv=3,
        verbose=2,
        random_state=42,
        n_jobs=-1
    )
    random_search.fit(X_train_encoded, y_train)
    return random_search.best_params_, random_search.best_score_
