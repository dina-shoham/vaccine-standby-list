import React, { Component } from "react";
import PatientForm from "./PatientForm";
import ClinicSignUp from "./ClinicSignUp";
import ClinicLogin from "./ClinicLogin";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <p>HOMEPAGE</p>
          </Route>
          <Route path="/signup" component={PatientForm}></Route>
          <Route path="/clinic/signup" component={ClinicSignUp}></Route>
          <Route path="/clinic/login" component={ClinicLogin}></Route>
        </Switch>
      </Router>
    );
  }
}
