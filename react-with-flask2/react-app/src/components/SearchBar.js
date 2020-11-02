import React, {Component} from 'react';
import axios from 'axios';


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

    componentDidUpdate() {
        const varString = this.state.search
        const homeSearchPage = document.getElementById("searchHome")

        console.log(varString)
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
            console.log(array)
            homeSearchPage.innerHTML = listOfWords(array)
        })
            function listOfWords(array) {
                const autowords = array.map(array => `<li>${array}</li>`).join("\n");
                return `<ul>${autowords}</ul>`
            }
        }

    handleSearchChange = (e) => {
        this.setState({search: e.target.value})
        // console.log(e)
        // console.log(typeof e)

        // const getCircularReplacer = () => {
        //     console.log("inside getCircRep")
        //     const seen = new WeakSet();
        //     return (item) => {
        //       if (typeof item === "object" && item !== null) {
        //         if (seen.has(item)) {
        //           return;
        //         }
        //         console.log(typeof item, item)
        //         seen.add(item);
        //       }
        //       return item;
        //     };
        //   };
        // const fetchPromise = axios.post("/autocomplete", e);
        // fetchPromise.then(response => {console.log(response);})
        // .then(response => {
        //     console.log("Mira:", response)
        //     console.log(response.data)
        //     console.log(e.target.value)
        // })

        // fetch("/autocomplete", {
        //     method:"POST",
        //     headers:{
        //         "Accept" : "application/json",
        //         "content_type":"application/json", // tells the app that we're going to pass over a json object
        //     },
        //     body: {txt: String(JSON.stringify(this.state.value)).toString()}//JSON.stringify(this.state.value)
        //     })
        
        // var util = require('util')

        

        // const fetchPromise = axios.post("/autocomplete", e);
        // fetchPromise.then(response => {console.log(response);})
        // .then(response => {
        //     console.log("Mira:", response)
        //     console.log(response.data)
        //     console.log(e.target.value)
        // })

        // .then(response => { //do
        //     console.log("hello")
        //     return response.json() // get response object in json form. Response object is what is returned as a result of an api call
        //   }) 
        //   .then(data => {util.inspect(data);// .json returns a response, so now we can do whatever we want with our data 
        //   this.setState({search: e.target.value})
        //   })
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
    render() {
        const {search} = this.state // now we don't have to type this.state when we want to edit the search property
        return(
            <div>
            <form onSubmit={this.handleSubmit} action = "#" method="POST" autoComplete="off">
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
            <div id="searchHome">
            {/* The autocomplete options is going in here */}
            </div>
            </div>
        )
    }
}
export default SearchBar


