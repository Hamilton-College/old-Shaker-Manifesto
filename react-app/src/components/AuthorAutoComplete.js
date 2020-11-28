import React, { Component } from 'react'


class AuthorAutoComplete extends Component {
    constructor(props){
        super(props)
        this.state = {
            suggestions: [],
            search: ""
        };
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

        fetch("/autocomplete2", {
            method:"POST",
            headers:{
                "Accept" : "application/json",
                "content_type":"application/json", // tells the server that we're going to pass over a json object
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
        fetch("#", {
            method:"POST",
            headers:{
                "Accept" : "application/json",
                "contentType":"application/json", 
            },
            body:JSON.stringify(e)
            }
        ).then(response => { //do
        return response.json() // this is another promise so we have to do ".then" after
      })
      .then(json => {
      this.setState({search: e.target.value})
      })
    }

    render () {
        const { search } = this.state;
        return (
            <div>
            <form onSubmit={this.handleSubmit} action = "#" method="POST" >
            <div className="AutoCompleteText2">
                <input value={search} id="MySearchTerm" onChange= {this.handleSearchChange} type ="text" name = "query" autoComplete="off" placeholder="Search by author..."/>

                {this.renderSuggestions()}
            </div>
            <button type="submit" className="searchButton2">Search</button>
            </form>

            </div>
        )
    }
}
    
export default AuthorAutoComplete