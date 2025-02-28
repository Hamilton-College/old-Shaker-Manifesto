import React, {Component} from 'react';


// This is a component that will be displayed in app.js

class SearchBar extends Component {
    // to convert this into a react, component, 
    // we need to give it a component state
    
    constructor(props){
        super(props)
        this.state = {
            suggestions: [],
            search: "" // initialize state property to empty. 
                        // "search" gets supplied as the value for the "value" element of the form input
                        // whenever there is a change, that new value gets taken care of by "handleSearchChange"
                        // which sets back the "search" state property to the updated value
                        // Now that the state has been set (again), the new value(string) gets set as the "value" elemt 
        }
    }
    
    suggestionSelected(value) {
        this.setState(() => ({
            search: value,
            suggestions: [],
        }))
    }
    renderSuggestions() {
        const { suggestions } = this.state;
        if(suggestions.length === 0) {
            return null;
        }
        return (
            <ul>
            {suggestions.map((item) => <li onClick={() => this.suggestionSelected(item)}> {item} </li>)}
            </ul>
        )
    }

    handleSearchChange = (e) => {
        const varString = e.target.value
        this.setState({search: varString})

        fetch("/autocomplete", {
            method:"POST",
            headers:{
                "Accept" : "application/json",
                "content_type":"application/json", // tells the app that we're going to pass over a json object
            },
            body:JSON.stringify({"txt":varString})
            }).then(response => { //do
            return response.json() // this is another promise so we have to do ".then" after
          })
          .then(array => {
            this.setState({suggestions: array})
        })
        }

        
    handleSubmit = (e) =>{
        if(this.state.value.length == 0){
            alert(`${this.state.search}`)
        }
        else{
        fetch("#", {
            method:"POST",
            headers:{
                "Accept" : "application/json",
                "contentType":"application/json", 
            },
            body:JSON.stringify(e)
            }
        ).then(response => { //do
        return response.json() 
      })
      .then(json => {
      this.setState({search: e.target.value})
      })
    }}
    render() {
        const {search} = this.state // now we don't have to type this.state when we want to edit the search property
        return(

            <div>
            <form onSubmit={this.handleSubmit} action = "#" method="POST" >
            <div className="AutoCompleteText">
                <input
                    placeholder="What are you looking for?"
                    id = "MySearchTerm" 
                    type = "text" 
                    name = "query"
                    value={search} 
                    onChange={this.handleSearchChange}
                    autoComplete="off"/> 
                {this.renderSuggestions()}
            </div>
            <button type="submit" className="searchButton">Search</button>
            </form>

           
            </div>
        )
    }
}
export default SearchBar


