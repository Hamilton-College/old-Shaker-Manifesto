import React, {Component} from 'react';
import axios from 'axios';


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
        // const suggestions2 = suggestions.slice(0,10) //this limits the autocomplete suggestions to 10. We can change this
        return (
            <ul>
            {/* <p>Here are the suggs: {suggestions}</p> */}
            {suggestions.map((item) => <li onClick={() => this.suggestionSelected(item)}> {item} </li>)}
            </ul>
        )
    }

    handleSearchChange = (e) => {
        // const value = e.target.value
        // this.setState({search: value})
        const varString = e.target.value//this.state.search
        this.setState({search: varString})

        // const homeSearchPage = document.getElementById("searchHome")

        console.log(varString)
        // console.log(this.state.search.value)
        fetch("/autocomplete", {
            method:"POST",
            headers:{
                "Accept" : "application/json",
                "content_type":"application/json", // tells the app that we're going to pass over a json object
            },
            body:JSON.stringify({"txt":varString})//varString}// JSON.stringify(varString)//{txt: String(JSON.stringify(this.state.value)).toString()}//JSON.stringify(this.state.value)
            }).then(response => { //do
            return response.json() // this is another promise so we have to do ".then" after
          })
          .then(array => {
            // console.log(array)
            this.setState({suggestions: array})
            console.log("my suggestions", this.state.suggestions)
            // homeSearchPage.innerHTML = listOfWords(array)
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
                "contentType":"application/json", // tells the app that we're going to pass over a json object
            },
            body:JSON.stringify(e)
            }
        ).then(response => { //do
            console.log(JSON.stringify(this.state.value))
        return response.json() // this is another promise so we have to do ".then" after
      })
      .then(json => {
      this.setState({search: e.target.value})
      })
    }}
    render() {
        const {search} = this.state // now we don't have to type this.state when we want to edit the search property
        return(
//             <form class="form-inline md-form mr-auto mb-4">
//   <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
//   <button class="btn aqua-gradient btn-rounded btn-sm my-0" type="submit">Search</button>
// </form>
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
            {/* <button type="submit"><i className="fa fa-search"></i>Search</button> */}
            <button type="submit" className="searchButton">Search</button>
            </form>

           
            </div>
        )
    }
}
export default SearchBar


