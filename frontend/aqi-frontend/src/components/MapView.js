import React, {useState, useEffect} from 'react'
import axios from 'axios'
import L from 'leaflet'

function MapView() {
    const [map, setMap] = useState(null)
    const [markers, setMarkers] = useState([])

    useEffect(() => {
        axios.get().then(response => {
            const newMarkers = response.data.map(data => ({
                lat : data.latitude,
                lng : data.longitude, 
            }))
            setMarkers(newMarkers)
        })
    }, [])
}