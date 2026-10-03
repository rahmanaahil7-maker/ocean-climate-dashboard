document.addEventListener('DOMContentLoaded', () => {
    const dataElement = document.getElementById('climate-data');
    if (dataElement) {
        const climateData = JSON.parse(dataElement.textContent);
        
        // Extract data arrays
        const labels = climateData.map(row => row.Date);
        const temps = climateData.map(row => row.Temp_C);
        const waves = climateData.map(row => row.Wave_Height_m);
        const winds = climateData.map(row => row.Wind_Speed_kmh);

        Chart.defaults.color = '#94a3b8';
        Chart.defaults.borderColor = '#1e293b';

        new Chart(document.getElementById('tempChart'), {
            type: 'line',
            data: { 
                labels, 
                datasets: [{ label: 'Temperature', data: temps, borderColor: '#ef4444', backgroundColor: 'rgba(239, 68, 68, 0.1)', fill: true, tension: 0.4 }] 
            },
            options: { 
                responsive: true, 
                maintainAspectRatio: false, 
                plugins: { 
                    legend: { display: false }, 
                    title: { display: true, text: 'Sea Surface Temp (°C)', color: '#f8fafc' } 
                } 
            }
        });

        new Chart(document.getElementById('waveChart'), {
            type: 'bar',
            data: { 
                labels, 
                datasets: [{ label: 'Wave Height', data: waves, backgroundColor: '#06b6d4', borderRadius: 4 }] 
            },
            options: { 
                responsive: true, 
                maintainAspectRatio: false, 
                plugins: { 
                    legend: { display: false }, 
                    title: { display: true, text: 'Wave Height (m)', color: '#f8fafc' } 
                } 
            }
        });

        new Chart(document.getElementById('windChart'), {
            type: 'line',
            data: { 
                labels, 
                datasets: [{ label: 'Wind Speed', data: winds, borderColor: '#3b82f6', borderDash: [5, 5], tension: 0.1 }] 
            },
            options: { 
                responsive: true, 
                maintainAspectRatio: false, 
                plugins: { 
                    legend: { display: false }, 
                    title: { display: true, text: 'Wind Speed (km/h)', color: '#f8fafc' } 
                } 
            }
        });
    }
});