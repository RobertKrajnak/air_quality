import React from "react";
import LineChart from "./LineChart";

function FifthComponent() {
  return (
    <div>
      <div class="card second-chart">
        <div class="card-header">
          <h6 class="text-graph">Second Graph</h6>
        </div>

        <div className="chart">
          <LineChart></LineChart>
        </div>
      </div>
    </div>
  );
}

export default FifthComponent;
