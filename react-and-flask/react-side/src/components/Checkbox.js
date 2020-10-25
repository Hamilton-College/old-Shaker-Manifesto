import React, {Component} from 'react';

// This is a component that will be displayed in app.js

class Checkbox extends Component {
    // to convert this into a react, component, 
    // we need to give it a component state
    state = {
        isCitizen : false
    }

    onChange = e =>{
        this.setState({isCitizen : e.target.checked});
    }
    
    render() {
        const {isCitizen} = this.state;
        return(
            <form>
                <h1> Are you a Citizen : {isCitizen ? "Yes" : "No"} </h1>
                <lable>
                    Are you a Citizen?
                    <input type="checkbox"
                    checked={isCitizen}
                    onChange={this.onChange}/>
                </lable>
            </form>
        )
    }
}
export default SearchBar


