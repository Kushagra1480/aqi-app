import React, {useEffect, useState} from 'react'
import {Bar} from 'react-chartjs-2'
import axios from 'axios' //for fetching data

function AirQualityChart({ locationId }) {
    const [chartData, setChartData] = useState(null)
    const [isLoading, setIsLoading] = useState(null)
    const [error, setError] = useState(null)

    useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await axios.get(`/api/air-quality-data/${locationId}`); // Replace with your backend API endpoint
            const formattedData = {
              labels: response.data.labels, // Assuming labels are present in the response
              datasets: [
                {
                  label: 'AQI',
                  data: response.data.aqiValues, // Assuming AQI values are present in the response
                  backgroundColor: 'rgba(255, 99, 132, 0.2)',
                  borderColor: 'rgba(255, 99, 132, 1)',
                  borderWidth: 1,
                },
                // Add more datasets if needed for other pollutants or metrics
              ],
            };
            setChartData(formattedData);
          } catch (error) {
            setError(error);
          } finally {
            setIsLoading(false);
          }
        };
    
        fetchData();
      }, [locationId]);
    if(isLoading) {
        return <div>Loading...</div>
    }
    if(error) {
        return <div>Error: {error.message}</div>
    }
    return (
        <Bar data = {chartData} options = {{maintainAspectRatio: false}}/>
    )
}

export default AirQualityChart