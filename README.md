# 🌊 Ocean Climate Intelligence Platform

**Abstergo Industries Research Division**  
**Operator:** AK_007

An enterprise-grade web application engineered to monitor, validate, and predict global oceanic telemetry. Built as a comprehensive final-year system, this platform integrates real-time geospatial mapping, unsupervised machine learning anomaly detection, automated predictive regression forecasting, and dynamic PDF reporting within a custom "Dark Ocean" glassmorphism UI.

## 🚀 Key Features

### Intelligence & Machine Learning
* **Predictive Forecasting:** 7-day sea surface temperature projections powered by Scikit-Learn Linear Trend Regression.
* **Anomaly Detection:** Unsupervised learning (Isolation Forest) isolates extreme environmental patterns in real-time.
* **Data Validation:** Pydantic-based schemas score and validate incoming sensor data to ensure physical realism.

### Interactive Telemetry & UI
* **Geospatial Mapping:** Live tracking of global ocean monitoring stations (Gulf of Guinea, North Atlantic Drift, etc.) via Leaflet.js.
* **Dynamic Visualizations:** Responsive Chart.js telemetry graphs for temperature, wave height, and wind speed.
* **Premium Interface:** Custom CSS grid layout featuring a video-animated background and glassmorphism translucent panels.

### Enterprise Functionality
* **User Authentication:** Secure session management with Flask-Login and Werkzeug password hashing.
* **Automated Reporting:** Instant generation of downloadable PDF analytics reports using ReportLab.
* **Threshold Alerts:** Configurable user settings that trigger automated email notifications when oceanic temperatures exceed safety bounds.
* **Data Export:** Direct CSV exports for localized machine learning or offline analysis.

## 🛠️ Technology Stack

**Backend System**
* **Framework:** Python / Flask
* **Database:** SQLite (Relational telemetry and user storage)
* **Data Science:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn

**Frontend Design**
* **Styling:** Custom CSS (Dark Theme, Glassmorphism, Responsive)
* **Visualization:** Chart.js, Leaflet.js (Interactive Maps)
* **Assets:** HTML5 Video Backgrounds

## ⚙️ Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/ocean-climate-dashboard.git](https://github.com/YOUR-USERNAME/ocean-climate-dashboard.git)
   cd ocean-climate-dashboard
