import React from 'react'
import { Line } from 'react-chartjs-2'


function LineChart() {
    
    const data = {
        labels: [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May'
        ],
        datasets: [
            {
                label: 'Co2 measurement',
                backgroundColor :'rgba(75,192,192,1)',
                borderColor: 'rgba(0,0,0,1)',
                borderWidth: 2,
                lineTension: 0.5,
                data: [3,2,2,1,5]
            }
        ]
    }

    return (
        <div>
            <Line data={data}></Line>
        </div>
    )
}



export default LineChart;   
