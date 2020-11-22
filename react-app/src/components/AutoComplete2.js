import React, { Component } from 'react'


class AutoComplete2 extends Component {
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
        fetch("/autocomplete2", {
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
        // alert(`${this.state.search}`)
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
    }

    render () {
        const { search } = this.state;
        return (
            <div>
            <form onSubmit={this.handleSubmit} action = "#" method="POST" >
            <div className="AutoCompleteText2">
                <input value={search} id="MySearchTerm" onChange= {this.handleSearchChange} type ="text" name = "query" autoComplete="off" placeholder="Search by author..."/>

                {/* <input
                    placeholder="Search"
                    id = "MySearchTerm" 
                    type = "text" 
                    name = "query"
                    value={search} 
                    onChange={this.handleSearchChange}
                    autoComplete="off"/>  */}
                {this.renderSuggestions()}
            </div>
            {/* <button type="submit"><i className="fa fa-search"></i>Search</button> */}
            <button type="submit" className="searchButton2">Search</button>
            </form>

{/*            
            </div>
            <div className = "AutoCompleteText">
                <form onSubmit={this.handleSubmit} action = "#" method="POST">
                    <input value={text} onChange= {this.onTextChanged} type ="text" name = "query" autoComplete="off"/>
                    {this.renderSuggestions()}

                    <button type="submit" className="searchButton">Search</button>
                </form> */}
            </div>
        )
    }
}



    
export default AutoComplete2
// ReactDOM.render( <AutoComplete2 />, document.getElementById('root'))