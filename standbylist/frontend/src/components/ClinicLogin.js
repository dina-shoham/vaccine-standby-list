import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class ClinicLogin extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <div>
          <Link to="/">
            <button>Back to homepage</button>
          </Link>
        </div>
        <p>clinic login</p>;
      </div>
    );
  }
}
