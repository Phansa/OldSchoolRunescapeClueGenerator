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
      globalItems : [{Image:"/images/all/Air rune.jpg"}]
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
        <button onClick={() => {this.generateClueScroll("Easy")}}> Generate an easy clue scroll. </button>
        <br />
        <button onClick={() => {this.generateClueScroll("Medium")}}> Generate a medium clue scroll. </button>
        <br />
        <button onClick={() => {this.generateClueScroll("Hard")}}> Generate a hard clue scroll. </button>
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
  //1/5 chance of getting onto rare drop table. Else common.
  generateClueScroll(difficulty)
  {
    let roll = 0;
    let minimum = 0;
    if(difficulty === "Easy")
    {
      roll = 2;
      minimum = 2;
    }
    else if(difficulty === "Medium")
    {
      roll = 3;
      minimum = 3;
    }
    else if(difficulty === "Hard")
    {
      roll = 3;
      minimum = 4;
    }
    let result = this.randomRoll(roll);
    let minRewards = minimum + result;
    let rewards = [];
    let reward = "";
    let i = 0;
    for(i = 0; i < minRewards; ++i)
    {
      let rareDrop = Math.floor(Math.random() * 4);
      if(rareDrop === 4)
      {
        reward = itemsJson[difficulty +"Unique"][this.randomRoll(itemsJson[difficulty + "Unique"].length)];
      }
      else
      {
        let commonDrop = Math.floor(Math.random()*2);
        if(commonDrop === 1)
        {
          reward = itemsJson[difficulty +"Common"][this.randomRoll(itemsJson[difficulty +"Common"].length)];
        }
        else
        {
          reward = itemsJson["All"][this.randomRoll(itemsJson["All"].length)]
        }
      }
      rewards.push(reward);  
    }
    this.setState({globalItems: rewards});
  }
}

export default App;
