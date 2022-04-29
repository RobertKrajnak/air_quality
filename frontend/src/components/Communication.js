import React, { Component } from "react";
import UpperCard from "./UpperCard.js";
import FourthComponent from "./fourthComponent.js";
import FifthComponent from "./fifthComponent.js";

class Communication extends Component {
  constructor(props) {
    super(props);
    this.state = {
      light: undefined,
      nh3: undefined,
      oxidised: undefined,
      pm1: undefined,
      pm10: undefined,
      pm25: undefined,
      pressure: undefined,
      reduced: undefined,
      temperature: undefined,
    };
    this.loadData = this.loadData.bind(this);
  }
  loadData() {
    const currentRoute = window.location.href + "api";
    fetch(currentRoute)
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          light: data.light,
          nh3: data.nh3,
          oxidised: data.oxidised,
          pm1: data.pm1,
          pm10: data.pm10,
          pm25: data.pm25,
          pressure: data.pressure,
          reduced: data.reduced,
          temperature: data.temperature,
        });
      });
  }
  componentDidMount() {
    this.loadData();
    setInterval(this.loadData, 5000);
  }

  render() {
    var {
      light,
      nh3,
      oxidised,
      pm1,
      pm10,
      pm25,
      pressure,
      reduced,
      temperature,
    } = this.state;
    return (
      <div>
        <div class="container-fluid">
          <div class="row upperCards">
            <UpperCard value={light} unit="lux" text="Light:" />
            <UpperCard value={nh3} unit="kO" text="Nh3:" />
            <UpperCard value={oxidised} unit="kO" text="Oxidised:" />
            <UpperCard value={pm1} unit="ug/m^3" text="Pm1:" />
            <UpperCard value={pm10} unit="ug/m" text="Pm10:" />
            <UpperCard value={pm25} unit="ug/m" text="Pm25:" />
            <UpperCard value={pressure} unit="hPa" text="Pressure:" />
            <UpperCard value={reduced} unit="kO" text="Reduced:" />
            <UpperCard value={temperature} unit="°C" text="Temperature:" />
          </div>
          <div class="row">
            <FourthComponent></FourthComponent>
            <FifthComponent></FifthComponent>
          </div>
        </div>
      </div>
    );
  }
}
export default Communication;
