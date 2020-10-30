import React, {Component} from 'react';

// This is a component that will be displayed in app.js

class SearchBar extends Component {
    // to convert this into a react, component, 
    // we need to give it a component state
    constructor(props){
        super(props)
        this.state = {
            search: "" // initialize state property to empty. 
                        // "search" gets supplied as the value for the "value" element of the form input
                        // whenever there is a change, that new value gets taken care of by "handleSearchChange"
                        // which sets back the "search" state property to the updated value
                        // Now that the state has been set (again), the new value(string) gets set as the "value" elemt 
        }
    }
    handleSearchChange = (event) => {
        this.setState({
            search: event.target.value // sets the "search" state property to whatever has been typed
        })
    }
    handleSubmit = (event) =>{
        // alert(`${this.state.search}`)
        fetch("#", {
            method:"POST",
            headers:{
                "Accept" : "application/json",
                "contentType":"application/json", // tells the app that we're going to pass over a json object
            },
            body:JSON.stringify(this.state.value)
            }
        ).then(response => { //do
            console.log(JSON.stringify(this.state.value))
        return response.json() // this is another promise so we have to do ".then" after
      })
      .then(json => {
      this.setState({search: event.target.value})
      })
    }
    render() {
        const {search} = this.state // now we don't have to type this.state when we want to edit the search property
        return(
            <form onSubmit={this.handleSubmit} action = "#" method="POST">
                <div>
                <input
                    id = "MySearchTerm" 
                    type = "text" 
                    name = "query"
                    value={search} 
                    onChange={this.handleSearchChange}/> 
                </div>
                <button type="submit" className="searchButton">Search</button>
            </form>
        )
    }
}
export default SearchBar


