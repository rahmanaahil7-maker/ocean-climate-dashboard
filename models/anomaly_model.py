# models/anomaly_model.py
from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df):
    """
    Uses Unsupervised Machine Learning (Isolation Forest) 
    to flag anomalous ocean conditions.
    """
    if df.empty or len(df) < 10:
        df['is_anomaly'] = False
        return df
        
    # Isolate the features we want the model to analyze
    features = df[['Temp_C', 'Wave_Height_m', 'Wind_Speed_kmh']].fillna(0)
    
    # Initialize the model assuming 5% of historical data represents extreme events
    model = IsolationForest(contamination=0.05, random_state=42)
    
    # Fit the model and predict (-1 represents an anomaly, 1 is normal)
    predictions = model.fit_predict(features)
    
    # Convert predictions to a boolean True/False column
    df['is_anomaly'] = predictions == -1
    
    return df