import React from "react";
import Title from "./Header/Title.js";

const divTitle= {
  margin: '40px',
  border: '5px solid pink'
};

const divHeader = {
    fontSize: '15px',
    position: 'fixed',
    left: '0',
    bottom: '10',
    width: '100%',
    color: 'green',
    textAlign: 'center',
};

export default class Header extends React.Component{

    render(){
        return (
            <div>This is the Header</div>
        );
    }
}
