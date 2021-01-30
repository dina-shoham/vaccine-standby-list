import React, { Component } from "react";

export default class PatientCreated extends Component {
  constructor(props) {
    super(props);
    this.state = {
      firstName: "",
      lastName: "",
      email: "",
      age: "",
      phoneNumber: "",
      healthCareNumber: "",
      address: "",
      transportation: "",
      firstDose: false,
      occupation: "",
      riskFactors: "",
      highRiskHousehold: false,
      latitude: "",
      longitude: "",
    };
    this.patientCode = this.props.match.params.patientCode;
  }

  render() {
    return (
      <div>
        <h3>{this.patientCode}</h3>
        <p>{this.state.firstName}</p>
        <p>{this.state.lastName}</p>
        <p>{this.state.latitude}</p>
      </div>
    );
  }
}
