import React from 'react'
import {Card, CardBody, CardTitle, CardSubtitle, CardText} from 'reactstrap'
import AirQualityChart from './AirQualityChart'

function CityCard({cityData}) {
    return (
        <Card>
            <CardBody>
                <CardTitle>
                    {cityData.name}
                </CardTitle>
                <CardSubtitle>
                    AQI: {cityData.aqi} ({cityData.aqiLevel}) | Weather : {cityData.weather}
                </CardSubtitle>
                <CardText>
                    <ul>
                        <li>
                            PM2.5: {cityData.pm25} ({cityData.pm25Level})
                        </li>
                    </ul>
                    <AirQualityChart data = {cityData.trendData} />
                    <p>

                    </p>
                </CardText>
            </CardBody>
        </Card>
    )
}

export default CityCard