import React from "react";
import ReactJson from "react-json-view";


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
            contents: [],
            data: [],
        }
    }

    handleChange(e){
        const title = e.target.value;
        this.setState({input_text: title});
    }

    handleClick(){
        this.props.connection.session.call(
            'com.example.requestcount',
            [this.state.input_text]
        ).then((res) => {
            if (res.error == true){
                this.setState({error: 'True'});
            } else{
                this.setState({error: 'False'});
            }
            this.setState({message: res.message});
            this.setState({data: res.data})
        });
    }

    render() {
        const styles = {
            fontFamily: 'sans-serif',
            textAlign: 'center',
        };
        return (
            <div>
                <div>
                    <div style={styles}>
                        <h2>Webpage Parser</h2>
                        <input
                            onChange={this.handleChange.bind(this)}
                            style={{width: '470px'}}
                        />
                        <button onClick={this.handleClick.bind(this)}>Save</button>
                    </div>
                    <div style={styles}>
                        <p>Error: {this.state.error} </p>
                        <p>Message: {this.state.message} </p>
                    </div>
                    <ReactJson src={this.state.data} theme='hopscotch' />
                </div>
            </div>
        )
    }
}
