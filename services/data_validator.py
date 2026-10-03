# services/data_validator.py
from pydantic import BaseModel, ValidationError

class OceanObservation(BaseModel):
    Date: str
    Temp_C: float
    Wave_Height_m: float
    Wind_Speed_kmh: float

def validate_and_score(df):
    quality_scores = []
    
    for _, row in df.iterrows():
        try:
            # Enforce strict data types
            obs = OceanObservation(**row.to_dict())
            
            # Baseline perfect score
            score = 100
            
            # Deduct points for physically improbable readings
            if not (-2.0 <= obs.Temp_C <= 40.0): 
                score -= 40
            if obs.Wave_Height_m < 0 or obs.Wave_Height_m > 30: 
                score -= 30
            if obs.Wind_Speed_kmh < 0:
                score -= 30
                
            quality_scores.append(max(0, score))
            
        except ValidationError:
            # Flag corrupted or missing data payloads
            quality_scores.append(0)
            
    df['Quality_Score'] = quality_scores
    return df