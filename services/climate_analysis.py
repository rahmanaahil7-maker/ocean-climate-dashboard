import numpy as np

def calculate_statistics(df):
    if df.empty:
        return {'avg': 0, 'min': 0, 'max': 0, 'anomaly': "+0.00", 'anomaly_class': 'warm-anomaly'}
    
    avg_temp = np.round(df['Temp_C'].mean(), 2)
    latest_temp = df['Temp_C'].iloc[-1]
    anomaly_val = latest_temp - avg_temp
    
    return {
        'avg': avg_temp,
        'min': df['Temp_C'].min(),
        'max': df['Temp_C'].max(),
        'anomaly': f"{anomaly_val:+.2f}",
        'anomaly_class': 'warm-anomaly' if anomaly_val > 0 else 'cold-anomaly'
    }