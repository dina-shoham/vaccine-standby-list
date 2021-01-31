import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class ClinicSignUp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "",
      email: "",
      address: "",
      username: "",
      password: "",
      lat: "",
      lon: "",
    };
  }

  componentDidMount() {
    navigator.geolocation.getCurrentPosition((position) =>
      this.setState({
        lat: position.coords.latitude,
        lon: position.coords.longitude,
      })
    );
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
        name: this.state.name,
        email: this.state.email,
        address: this.state.address,
        username: this.state.username,
        password: this.state.password,
        lat: this.state.lat,
        lon: this.state.lon,
      }),
    };
    fetch(requestOptions)
      .then((response) => response.json())
      .then((response) => console.log(response))
      .catch((error) => console.log(error));
  };

  render() {
    return (
      <div>
        <h1>Clinic Sign Up</h1>
        <div>
          <Link to="/">
            <button>Back to homepage</button>
          </Link>
          <div>
            <Link to="/clinic/login">
              <button>Clinic login</button>
            </Link>
          </div>
        </div>
        <form onSubmit={this.handleSubmit}>
          <label for="name">Clinic Name: </label>
          <input
            id="name"
            value={this.state.name}
            onChange={(event) => this.handleChange(event, "name")}
          />
          <br></br>
          <label for="email">Clinic Email: </label>
          <input
            id="email"
            value={this.state.email}
            onChange={(event) => this.handleChange(event, "email")}
          />
          <br></br>
          <label for="address">Address: </label>
          <input
            id="address"
            value={this.state.address}
            onChange={(event) => this.handleChange(event, "address")}
          />
          <br></br>
          <label for="username">Username: </label>
          <input
            id="username"
            value={this.state.username}
            onChange={(event) => this.handleChange(event, "username")}
          />
          <br></br>
          <label for="password">Password: </label>
          <input
            id="password"
            type="password"
            value={this.state.password}
            onChange={(event) => this.handleChange(event, "password")}
          />
          <br></br>
          <Link to="/clinic/login">
            <button type="submit">Sign up!</button>
          </Link>
        </form>
      </div>
    );
  }
}
