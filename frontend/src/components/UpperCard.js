import React from "react";

function UpperCard(props) {
  return (
    <div class="trieda">
      <div class="text">{props.text}</div>

      <div class="row">
        <div class="header">
          {props.value} {props.unit}
        </div>
      </div>
    </div>
  );
}

export default UpperCard;
