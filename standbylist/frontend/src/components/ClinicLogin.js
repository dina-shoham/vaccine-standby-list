import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class ClinicLogin extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
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
        username: this.state.username,
        password: this.state.password,
      }),
    };
    fetch("/api/login-clinic", requestOptions)
      .then((response) => response.json())
      .then((data) => this.props.history.push("/create-appointment/"));
  };

  render() {
    return (
      <div>
        <h1>Clinic Login</h1>
        <div>
          <Link to="/">
            <button>Back to homepage</button>
          </Link>
          <div>
            <Link to="/clinic/signup">
              <button>Clinic signup</button>
            </Link>
          </div>
        </div>
        <form onSubmit={this.handleSubmit}>
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
          <button type="submit">Log in</button>
        </form>
      </div>
    );
  }
}
