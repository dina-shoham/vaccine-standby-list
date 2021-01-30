import { Domain } from "@material-ui/icons";
import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class PatientForm extends Component {
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
  }

  componentDidMount() {
    navigator.geolocation.getCurrentPosition((position) =>
      this.setState({
        latitude: position.coords.latitude,
        longitude: position.coords.longitude,
      })
    );
  }

  handleChange = (event, fieldName) => {
    this.setState({ [fieldName]: event.target.value });
  };

  handleFirstDose = (event) => {
    this.setState({ firstDose: event.target.checked });
  };

  handleCheckHousehold = (event) => {
    this.setState({ highRiskHousehold: event.target.checked });
  };

  handleSubmit = (event) => {
    event.preventDefault(); //stop it from refreshing for now so we can see the console.log
    const vaccineStatus = this.state.firstDose ? "1D" : "0D";
    console.log(this.state);
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        age: this.state.age,
        firstName: this.state.firstName,
        lastName: this.state.lastName,
        phoneNumber: this.state.phoneNumber,
        email: this.state.email,
        vaccinationStatus: vaccineStatus,
        occupation: this.state.occupation,
        transport: this.state.transportation,
        highRiskHousehold: this.state.highRiskHousehold,
        healthcareNum: this.state.healthCareNumber,
        riskFactors: this.state.riskFactors,
        lat: this.state.latitude,
        lon: this.state.longitude,
      }),
    };
    fetch("/api/create-patient", requestOptions)
      .then((response) => response.json())
      .then((data) => console.log(data));
  };

  render() {
    return (
      <div>
        <h1>Covid Vaccination Waitlist: Patient Signup</h1>
        <div>
          <Link to="/">
            <button>Back to homepage</button>
          </Link>
        </div>
        <form onSubmit={this.handleSubmit}>
          <h3>Personal Information</h3>
          <div class="personal-info">
            <label for="firstName">First name: </label>
            <input
              id="firstName"
              value={this.state.firstName}
              onChange={(event) => this.handleChange(event, "firstName")}
            />
            <br></br>
            <label for="firstName">Last name: </label>
            <input
              id="lastName"
              value={this.state.lastName}
              onChange={(event) => this.handleChange(event, "lastName")}
            />
            <br></br>
            <label for="email">Email: </label>
            <input
              id="email"
              value={this.state.email}
              onChange={(event) => this.handleChange(event, "email")}
            />
            <br></br>
            <label for="age">Age: </label>
            <input
              id="age"
              value={this.state.age}
              type="number"
              max="125"
              min="18"
              onChange={(event) => this.handleChange(event, "age")}
            />
            <br></br>
            <label for="phoneNumber">Phone Number: </label>
            <input
              id="phoneNumber"
              value={this.state.phoneNumber}
              type="tel"
              minlength="10"
              maxlength="10"
              onChange={(event) => this.handleChange(event, "phoneNumber")}
            />
            <br></br>
            <label for="healthCareNumber">Health Care Number: </label>
            <input
              id="healthCareNumber"
              value={this.state.healthCareNumber}
              onChange={(event) => this.handleChange(event, "healthCareNumber")}
            />
            <div class="address">
              <label for="address">Address: </label>
              <input
                id="address"
                value={this.state.address}
                onChange={(event) => this.handleChange(event, "address")}
              />
              <br></br>
              <label for="transportation">
                What is your main mode of transportation?
              </label>
              <select
                id="transportation"
                value={this.state.transportation}
                onChange={(event) => this.handleChange(event, "transportation")}
              >
                <option default></option>
                <option value="Car">Car</option>
                <option value="Public transit">Public Transit</option>
                <option value="Walk">Walking</option>
                <option value="Bike">Biking</option>
                <option value="Other">Other</option>
              </select>
            </div>
            <h3>Covid Risk Information</h3>
            <div class="priority-info"></div>
            <label for="firstDose">
              Check if you have received your first dose of the vaccine:
            </label>
            <input
              id="firstDose"
              type="checkbox"
              checked={this.state.firstDose}
              onChange={this.handleFirstDose}
            />
            <br></br>
            <label for="occupation">
              Which of the following occupation groups do you fall under?
              <ul>
                <li>
                  Tier 1: ICU health care worker, respiratory therapist,
                  long-term care/supportive living staff
                </li>
                <li>Tier 2: Non-tier 1 health care worker</li>
                <li>Tier 3: Frontline worker </li>
              </ul>
            </label>
            <select
              id="occupation"
              value={this.state.occupation}
              onChange={(event) => this.handleChange(event, "occupation")}
            >
              <option default></option>
              <option value="Tier 1">Tier One</option>
              <option value="Tier 2">Tier Two</option>
              <option value="Tier 3">Tier Three</option>
              <option value="Tier 4">None of the above</option>
            </select>
            <br></br>
            <label for="riskFactors">
              How many of the following conditions apply to you?
              <ul>
                <li>Chronic liver disease</li>
                <li>Diabetes (Type 1 and Type 2)</li>
                <li>
                  Cardio-vascular disease (congestive heart failure, ischemic
                  heart disease, and atrial fibrillation)
                </li>
                <li>COPD</li>
                <li>Immuno-deficiency disease</li>
                <li>
                  Renal disease (chronic renal failure and end stage renal
                  disease)
                </li>
                <li>Malignant cancer (excluding non-melanoma skin cancer)</li>
                <li>Dementia</li>
              </ul>
            </label>
            <input
              id="riskFactors"
              value={this.state.riskFactors}
              type="number"
              max="8"
              min="0"
              onChange={(event) => this.handleChange(event, "riskFactors")}
            />
            <br></br>
            <label for="highRiskHousehold">
              Check if any of the above conditions apply to a member of your
              household:
            </label>
            <input
              id="highRiskHousehold"
              type="checkbox"
              checked={this.state.highRiskHousehold}
              onChange={this.handleCheckHousehold}
            />
          </div>
          <button type="submit">Sign me up!</button>
        </form>
      </div>
    );
  }
}
