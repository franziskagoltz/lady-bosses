import React, { Component } from 'react';
import './App.css';
import fetch from 'isomorphic-fetch'


class App extends Component {
  getData() {
    fetch("http://localhost:5000/businesses.json").then(response => {
      return response.json();
    }).then(data => console.log(data) );
  }

  render() {
    return (
      <div >
      <button onClick={() => this.getData()}>Get Business Info</button>
      </div>
          
    );
  }
}

export default App;
