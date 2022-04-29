import React from "react";
import LineChart from "./LineChart";

function FourthComponent() {
  return (
    <div>
      <div class="card first-chart">
        <div class="card-header">
          <h6 class="text-graph">First Graph</h6>
        </div>

        <div className="chart">
          <LineChart></LineChart>
        </div>
      </div>
    </div>
  );
}

export default FourthComponent;
