document.addEventListener('DOMContentLoaded', () => {
    const mapElement = document.getElementById('map');
    if (mapElement) {
        const map = L.map('map').setView([10.0, 0.0], 2);
        L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
            attribution: 'Tiles &copy; Esri',
            maxZoom: 16
        }).addTo(map);

        const locationsElement = document.getElementById('locations-data');
        if (locationsElement) {
            const locations = JSON.parse(locationsElement.textContent);
            locations.forEach(site => {
                const popupContent = `<strong>${site.name}</strong><br>Temp: ${site.temp} °C`;
                L.marker([site.lat, site.lon]).addTo(map).bindPopup(popupContent);
            });
        }
    }
});