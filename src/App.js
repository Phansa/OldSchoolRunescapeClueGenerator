import React, { Component } from 'react';
import './App.css';
import itemsJson from './data/Items.json';

class App extends Component {
  constructor(props)
  {
    super(props);
    this.randomRoll = this.randomRoll.bind(this);
    this.generateEasyClueScroll = this.generateEasyClueScroll.bind(this);
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src="/images/osrs-logo.png" width="200px" alt=""/>
          <h1 className="App-title">Osrs Clue Generator</h1>
        </header>
        <button onClick={this.generateEasyClueScroll}> Generate easy clue scroll. </button>
        <br />
        <img src="/images/all/Air rune.jpg" alt=""/>
      </div>
    );
  }

  randomRoll()
  {
    return Math.floor(Math.random * 2);
  }
  generateEasyClueScroll()
  {
    let result = this.randomRoll();
    let minRewards = 2 + this.randomRoll;
    console.log(itemsJson); 
  }
}

export default App;
