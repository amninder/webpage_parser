import React from 'react';


export default class UrlList extends React.Component{

    render(){
        return (
            <div>
                <ul>
                    {this.props.contents}
                </ul>
            </div>
        )
    }
}
