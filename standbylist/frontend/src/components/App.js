import React, { Component } from "react";
import { render } from "react-dom";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return <h1>react app!! let's go</h1>;
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
