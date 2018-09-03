import React from "react";

import Header from "./Header";
import Footer from "./Footer";
import Body from "./Body"

var autobahn = require('autobahn');


export default class Layout extends React.Component{
    constructor(){
        super();

        const connection = new autobahn.Connection({
            url: "ws://127.0.0.1:8080/ws",
            realm: 'realm1'
        });


        this.state = {
            title: "Welcome to Url Shortner",
            connection: connection,
            session: null,
            ws_status: 'Disconnected',
            contents: null,
            broadcasted_item: '',
        }


        connection.onopen = (session) => {
            this.setState({ws_status: 'Connected', session: session})

            this.state.session.call(
                'com.example.requesttoloadcontents'
            ).then((res) => {
                const listItems = res.map((data, idx) => {
                    return <li key={idx}>
                        <a href={data.data.website} target="_blank">http://url-shortner/{data.data.slug}</a>
                    </li>
                });
                console.log(listItems)
                this.setState({
                    contents: listItems,
                    connection: connection
                });
            });

            session.subscribe('com.example.broadcastsave', (args) => {
                console.log('Broadcast Event: ', args[0]);
                const appendItem = [args[0]];
                const broadcastItem = appendItem.map((data, idx) => {
                    return <li key={idx}>
                        <a href={data.data.website} target="_blank">http://url-shortner/{data.data.slug}</a>
                    </li>
                });
                this.state.contents.push(broadcastItem);
                this.setState({broadcasted_item: broadcastItem});
            });
        }
        connection.onclose = this.onCloseEvent.bind(this)
        connection.open();
    }

    onCloseEvent(reason, detail){
        this.setState({ws_status: 'Disconnected'})
    }

    render(){

        return (
            <div>
                <Body
                    connection={this.state.connection}
                    contents={this.state.contents}/>
                <Footer title={this.state.ws_status} />
            </div>
        );
    }
}
