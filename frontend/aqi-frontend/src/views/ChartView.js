import { useState } from "react"

function ChartView() {
    const [selectedLocationIds, setSelectedLocationIds] = useState([])
    const [selectedPollutants, setSelectedPollutants] = useState([])
    const [timeframe, setTimeFrame] = useState('day')
    const [chartData, setChartData] = useState({})

    const renderChart = () => {
        if(!chartData) 
            return null
        return (
            <ChartView>
                //render chart
            </ChartView>
        )
    }
    const handleLocationSelection = (id) => {
        //setting the current location based on the user's selection
    }
    const handlePollutantSelection = (pollutant) => {
        //setting the current pollutant based on user's selection
    }
    const handleTimeFrameChange = (newTimeFrame) => {
        //set the timeframe state and fetch data 
    }
    return (
        <div className="chart-view">
            <SelectLocation onSelect = {handleLocationSelection}/>
            <SelectPollutant onSelect = {handlePollutantSelection}/>
            <TimeFrameSelector onChange = {handleTimeFrameChange}/>
            {renderChart()}
        </div>
    )
}

export default ChartView