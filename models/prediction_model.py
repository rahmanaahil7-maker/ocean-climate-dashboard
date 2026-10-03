# models/prediction_model.py
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from datetime import timedelta

def forecast_temperature(df, days_ahead=7):
    """
    Uses Linear Regression to forecast future ocean temperatures.
    """
    if df.empty or len(df) < 5:
        return []
        
    # Convert dates to numerical indices for the regression model
    df['Day_Index'] = np.arange(len(df))
    X = df[['Day_Index']]
    y = df['Temp_C']
    
    # Train the model on the historical trend
    model = LinearRegression()
    model.fit(X, y)
    
    # Generate future indices and predict their temperatures
    future_indices = np.arange(len(df), len(df) + days_ahead).reshape(-1, 1)
    future_temps = model.predict(future_indices)
    
    # Format the output dates and predictions
    last_date = pd.to_datetime(df['Date'].iloc[-1])
    forecast = []
    
    for i in range(days_ahead):
        forecast_date = (last_date + timedelta(days=i+1)).strftime('%Y-%m-%d')
        forecast.append({
            'Date': forecast_date,
            'Predicted_Temp_C': round(future_temps[i], 2)
        })
        
    return forecast