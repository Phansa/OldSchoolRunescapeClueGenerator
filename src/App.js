import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src="/images/osrs-logo.png" width="200px"/>
          <h1 className="App-title">Osrs Clue Generator</h1>
        </header>
        <button onclick={this.generateEasyClueScroll}> Generate easy clue scroll. </button>
        <br />
        <img src="/images/all/Air rune.jpg"/>
      </div>
    );
  }

  generateEasyClueScroll()
  {
    
  }
}

export default App;
