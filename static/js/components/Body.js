import React from "react";
import UrlList from "./UrlList";


export default class Body extends React.Component{
    constructor(){
        super();

        this.state = {
            connection: null,
            input_text: '',
            error: false,
            message: '',
            website: '',
            slug: '',
            contents: []
        }
    }

    handleChange(e){
        const title = e.target.value;
        this.setState({input_text: title});
    }

    handleClick(){
        this.props.connection.session.call(
            'com.example.saveurl',
            [this.state.input_text]
        ).then((res) => {
            if (res.error == true){
                this.setState({error: 'Error: True'});
            } else{
                this.setState({error: 'Error: False'});
                var short_url = 'http://short-url.com/' + res.data.slug;
                this.setState({slug: short_url});
            }
            this.setState({message: res.message});
            this.setState({website: res.data.website});
        });
    }

    render() {
        return (
            <div>
                <div>
                    <input onChange={this.handleChange.bind(this)}/>
                    <button onClick={this.handleClick.bind(this)}>Save</button>
                    <div>
                        <p>{this.state.error} </p>
                        <p>Message: {this.state.message} </p>
                    </div>
                    <UrlList contents={this.props.contents}/>
                </div>
            </div>
        )
    }
}
