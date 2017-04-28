import React, { Component } from 'react';
import './App.css';
import Business from "./Business"
import Navbar from "./Navbar"
import CategorySelect from "./CategorySelect"
// import Places from "./GoogleMaps"


class App extends Component {

  render() {

    return (
      <div>
        <Navbar />
        <CategorySelect />
        <Business />
      </div>
    );
  }
}

export default App;
