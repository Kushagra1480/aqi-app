import React, {useState} from 'react'
import L from 'leaflet'

function AirQualityMarker({lat, lang, data, onOpenCityCard}) {
    const marker = L.marker([lat, lang], {
        icon: L.icon({
            iconUrl: '/icons/aqi-${data.aqiLevel}.png',
            iconSize: [50, 50],
        })
    })
    marker.on('click', () => openCityCard(data))
    return marker
}

export default AirQualityMarker