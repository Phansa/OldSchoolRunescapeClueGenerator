import React from 'react';

let Item = function statelessFunctionComponentClass(props) {
  let source = props.source
  let style = {
    margin: '10px 5px 0px 5px'
  };

  return (
    <img src={"."+source} style={style} alt=''/>
  );
};

export default Item;
