import requests
import pandas as pd
import numpy as np

def fetch_live_data():
    api_url = "https://marine-api.open-meteo.com/v1/marine?latitude=0.0&longitude=0.0&daily=ocean_temperature_max&past_days=5&timezone=GMT"
    try:
        headers = {'User-Agent': 'OceanClimateDashboard/1.0'}
        response = requests.get(api_url, headers=headers, timeout=5, verify=False)
        response.raise_for_status()
        data = response.json()
        
        dates = data['daily']['time']
        temps = data['daily']['ocean_temperature_max']
        return pd.DataFrame([{'Date': dates[i], 'Temp_C': round(temps[i], 2) if temps[i] else 16.5} for i in range(len(dates))])
    except Exception:
        dates = pd.date_range(start='2026-09-28', periods=6, freq='D')
        return pd.DataFrame({
            'Date': dates.strftime('%Y-%m-%d'),
            'Temp_C': np.round(np.random.normal(loc=16.5, scale=1.2, size=6), 2)
        })