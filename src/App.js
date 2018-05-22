import React, { Component } from 'react';
import './App.css';
import itemsJson from './data/Items.json';
import Item from './Item.js';

class App extends Component {
  constructor(props)
  {
    super(props);
    this.randomRoll = this.randomRoll.bind(this);
    this.generateClueScroll = this.generateClueScroll.bind(this);
    this.state = {
      globalItems : [{Image:"./images/all/Air rune.jpg"}]
    };
    this.createItems = this.createItems.bind(this);
    this.createItem = this.createItem.bind(this);
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={"./images/osrs-logo.png"} width="200px" alt=""/>
          <h1 className="App-title">Osrs Clue Generator</h1>
        </header>
        <button onClick={() => {this.generateClueScroll("Easy")}}> Generate easy clue scroll. </button>
        <button onClick={() => {this.generateClueScroll("Medium")}}> Generate medium clue scroll. </button>
        <div className="Container">
          <div className="row">
            <div className="col-sm-12 text-center">
              {this.createItems(this.state.globalItems)}
            </div>
          </div>
        </div>
      </div>
    );
  }

  createItems(items)
  {
    return items.map(this.createItem);
  }
  createItem(item)
  {
    return <Item source={item['Image']}/>
  }
  randomRoll(number)
  {
    return Math.floor(Math.random() * number);
  }
  generateClueScroll(difficulty)
  {
    let roll = 0;
    if(difficulty === "Easy")
    {
      roll = 2;
    }
    else if(difficulty === "Medium")
    {
      roll = 3;
    }
    let result = this.randomRoll(roll);
    let minRewards = 2 + result;
    let rewards = [];
    let size = itemsJson[difficulty + "Unique"].length;
    let i = 0;
    for(i = 0; i < minRewards; ++i)
    {
      let reward1 = itemsJson[difficulty +"Unique"][this.randomRoll(size)];
      rewards.push(reward1);  
    }
    this.setState({globalItems: rewards});
  }
}

export default App;
