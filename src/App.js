import React, { Component } from 'react';
import './App.css';
import itemsJson from './data/Items.json';
import Item from './Item.js';

class App extends Component {
  constructor(props)
  {
    super(props);
    this.randomRoll = this.randomRoll.bind(this);
    this.generateEasyClueScroll = this.generateEasyClueScroll.bind(this);
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
          <img src="/images/osrs-logo.png" width="200px" alt=""/>
          <h1 className="App-title">Osrs Clue Generator</h1>
        </header>
        <button onClick={this.generateEasyClueScroll}> Generate easy clue scroll. </button>
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
  generateEasyClueScroll()
  {
    let result = this.randomRoll(2);
    let minRewards = 2 + result;
    let rewards = [];
    let size = itemsJson["EasyUnique"].length;
    let i = 0;
    for(i = 0; i < minRewards; ++i)
    {
      let reward1 = itemsJson["EasyUnique"][this.randomRoll(size)];
      rewards.push(reward1);  
    }
    this.setState({globalItems: rewards});
  }
}

export default App;
