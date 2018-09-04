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
            broadcasted_item: [],
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
        const input_styles = {
            width: '100%',
            padding: '12px 20px',
            margin: '8px 0',
            display: 'inline-block',
            border: '1px solid #ccc',
            borderRadius: '4px',
            boxSizing: 'border-box',
            textAlign: 'center',
            fontSize: '30px',
            color: '#4CAF50',
        };
        const button_styles = {
            backgroundColor: '#4CAF50',
            border: 'none',
            color: 'white',
            padding: '20px',
            textAlign: 'center',
            textDecoration: 'none',
            display: 'inline-block',
            fontSize: '16px',
            margin: '4px 2px',
            cursor: 'pointer',
            borderRadius: '8px',
        };
        const result_div = {
            width: '50%',
            height: '100%',
            float: 'left',
        };
        const broadcast_div = {
            width: '50%',
            height: '100%',
            float: 'right',
        };
        return (
            <div>
                <div>
                    <div style={styles}>
                        <h2>Webpage Parser</h2>
                        <input
                            onChange={this.handleChange.bind(this)}
                            style={input_styles}
                        />
                        <button
                            onClick={this.handleClick.bind(this)}
                            style={button_styles}
                        >Generate</button>
                    </div>
                    <div style={styles}>
                        <p>Error: {this.state.error} </p>
                        <p>Message: {this.state.message} </p>
                    </div>
                    <div style={result_div}>
                        <h2>Result</h2>
                        <ReactJson src={this.state.data} />
                    </div>
                    <div style={broadcast_div}>
                        <h2>Broadcasted Message</h2>
                        <ReactJson src={this.props.broadcasted_item} />
                    </div>
                </div>
            </div>
        )
    }
}
