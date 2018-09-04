import React from "react";
import Title from "./Header/Title.js";

const divFooter = {
    fontSize: '5px',
    position: 'fixed',
    left: '0',
    bottom: '0',
    width: '100%',
    color: 'green',
    textAlign: 'left',
};

const pStyle = {
    fontSize: '15px',
    textAlign: 'center',
    bottom: '0',
};

export default class Footer extends React.Component{

    render(){
        return (
            <div style={divFooter}>
               <Title title={this.props.title} />
            </div>
        );
    }
}
