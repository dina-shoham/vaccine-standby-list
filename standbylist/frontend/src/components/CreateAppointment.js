import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class CreateAppointment extends Component {
  constructor(props) {
    super(props);
    this.state = {
      time: "",
      clinic: "",
      appointments: [],
    };
  }

  handleChange = (event, fieldName) => {
    this.setState({ [fieldName]: event.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault(); //stop it from refreshing for now so we can see the console.log
    console.log("SUBMITTING!");
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        time: this.state.time,
        // clinic: this.state.clinic,
      }),
    };
    fetch("/api/create-appointment", requestOptions)
      .then((response) => response.json())
      .then((response) => console.log("successful post! " + response));
  };

  getAppointments = () => {
    console.log("getting appts");
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    };
    fetch("/api/appointment", requestOptions)
      .then((response) => response.json)
      .then((response) => {
        this.setState({ appointments: response });
      });
    console.log(response);
  };

  render() {
    return (
      <div>
        <h1>Create Appointment</h1>
        <div>
          <Link to="/">
            <button>Back to homepage</button>
          </Link>
        </div>
        <form onSubmit={this.handleSubmit}>
          <label for="time">Time: </label>
          <input
            id="time"
            type="time"
            value={this.state.time}
            onChange={(event) => this.handleChange(event, "time")}
          />
          <br></br>
          <label for="clinic">Clinic: </label>
          <input
            id="clinic"
            type="clinic"
            value={this.state.clinic}
            onChange={(event) => this.handleChange(event, "clinic")}
          />
          <br></br>
          <div>
            <button type="submit">Send out notification</button>
          </div>
        </form>
        <h1>Pending Appointments</h1>
        <button onclick={this.getAppointments}>
          View pending appointments
        </button>
        <div>
          {this.state.appointments.map((appointment) => {
            return <p key={appointment.id}>{appointment.id}</p>;
          })}
        </div>
      </div>
    );
  }
}
