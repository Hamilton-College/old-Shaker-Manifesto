import Search from 'react-search'
import ReactDOM, { render } from 'react-dom'
import React, { Component, PropTypes } from 'react'
// import useForm from 'react-hook-form';
import {  useForm, Controller } from "react-hook-form";
import 'react-bootstrap-typeahead/css/Typeahead.css';
import axios from 'axios';
import '../App.css';


// class AutoComplete2 extends Component {
    // state = {value: ''};

    // render(){
    // var Typeahead = require('react-typeahead').Typeahead;
    // return(
    // <Typeahead
    //     options={['John', 'Paul', 'George', 'Ringo']}
    //     maxVisible={2}
    //     // name = "query" 
    // />
    // );
    
    // }}

    // class AutoComplete2 extends Component {
    //     constructor(props){
    //         super(props)
    //         this.state = {
    //             search: "" // initialize state property to empty. 
    //                         // "search" gets supplied as the value for the "value" element of the form input
    //                         // whenever there is a change, that new value gets taken care of by "handleSearchChange"
    //                         // which sets back the "search" state property to the updated value
    //                         // Now that the state has been set (again), the new value(string) gets set as the "value" elemt 
    //         }
    //     }
    //     handleSearchChange = (event) => {
    //         this.setState({
    //             search: event.target.value // sets the "search" state property to whatever has been typed
    //         })
    //     }
    //     handleSubmit = (event) =>{
    //         axios.post("/", this.state.search).then(response => {
    //             console.log(response)
    //         })
    //         .catch(error => {
    //             console.log(error)
    //         })
    //         // console.log(event.target)
    //         console.log(typeof event.target)
    //         console.log(event.target)
    //         alert(`${this.state.search}`)

    //         // console.log(typeof JSON.parse(data))
    //         // console.log(data)
    //         // fetch("/", {
    //         //     method:"POST",
    //         //     headers:{
    //         //         "content_type":"application/json", // tells the app that we're going to pass over a json object
    //         //     },
    //         //     body:JSON.stringify(this.state.search)//this.state.value)
    //         //     }
    //         // )//.then(response => { //do
        
    //     //     return response.json() // this is another promise so we have to do ".then" after
    //     //   })
    //     //   .then(json => {
        
    //     //   this.setState({search: event.target.value})
    //     //   })
    //     }
    //     render(){
    //         var Typeahead = require('react-typeahead').Typeahead;
    //         return(
    //         <div>
    //         <form onSubmit={this.handleSubmit} action = "#" method="POST">
    //             <Typeahead
    //                 options={['John', 'Paul', 'George', 'Ringo', "Billy", "Will"]}
    //                 maxVisible={5}
    //                 name = "query" 
    //                 // value = {this.state.search}
    //                 // onChange={this.handleSearchChange}
    //             />
    //             <button type="submit" className="searchButton">Search</button>
    //         </form>
    //         </div>
    //         );
    //     }}

    // const AutoComplete2 = (props) => {
    //     const { register, handleSubmit, errors, control } = useForm();
    //     const onSubmit = (data) => {
    //         console.log(data)
    //         var data = JSON.stringify(data)
    //         console.log(typeof data)
    //         console.log(data)
    //         alert(`${data}`)
    //         // console.log(typeof JSON.parse(data))
    //         // console.log(data)
    //         fetch("#", {
    //             method:"POST",
    //             headers:{
    //                 "Accept" : "application/json",
    //                 "content_type":"application/json", // tells the app that we're going to pass over a json object
    //             },
    //             body:{data} //JSON.stringify(data.target.name)
    //             })
    //             // ).then(response => { //do
    //             //     console.log(response)
    //             // return response.json() // this is another promise so we have to do ".then" after
    //             // })
    //             // .then(json => {
            
    //             // this.setState({search: event.target.value})
    //             // })
    //     };
    //     // render(){
    //     const mydata = [ "one", "two", "three" ];

    //     return(
    //         <>
    //         <form onSubmit={handleSubmit(onSubmit)} action = "/" method="POST">
    //             <div className="form-group">
    //             <input 
    //                 type="text" 
    //                 className="form-control" 
    //                 name="query" 
    //                 ref={register({ required: true })} />
    //             </div>
    //             <div className = "form-group mb-0">
    //                 <Controller
    //                 as={Typeahead}
    //                     control={control}
    //                     name="query"
    //                     rules={{ required: true }}
    //                     id="multiple-typeahead"
    //                     clearButton
    //                     // multiple
    //                     options={mydata}
    //                     defaultValue=""
    //                 />
    //                 </div>
    //             <button type="submit" className="searchButton">Search</button>
    //         </form>
    //         </>
    //     );
    // };


class AutoComplete2 extends Component {
    constructor(props){
        super(props)
        this.state = {
            suggestions: [],
            text: ""
        };
    }

    handleSubmit = (e) => {
        // console.log(typeof JSON.parse(data))
        // console.log(data)
        // axios.post("/", this.state.text.value).then(response => {
        //                 console.log(response)
        //             })
        //             .catch(error => {
        //                 console.log(error)
        //             })
        fetch("#", {
            method:"POST",
            headers:{
                "Accept" : "application/json",
                "content_type":"application/json", // tells the app that we're going to pass over a json object
                "Authorization" : "query"
            },
            body:JSON.stringify(this.state.text.value)//this.state.value)
            }
        ).then(response => { //do
            return response.json() // this is another promise so we have to do ".then" after
          })
          .then(json => {
          this.setState({search: e.target.value})
          })
    }

    onTextChanged = (e) => {
        const { items } = this.props;
        const value = e.target.value;
        let suggestions = [];
        if(value.length > 0) {
            const regex = new RegExp(`^${value}`, 'i');
            suggestions = items.sort().filter(v => regex.test(v));
        }
        this.setState(() => ({ suggestions, text: value }));
    }
    suggestionSelected(value) {
        this.setState(() => ({
            text: value,
            suggestions: [],
        }))
    }
    renderSuggestions() {
        const { suggestions } = this.state;
        if(suggestions.length === 0) {
            return null;
        }
        const suggestions2 = suggestions.slice(0,10) //this limits the autocomplete suggestions to 10. We can change this
        return (
            <ul>
            {suggestions2.map((item) => <li onClick={() => this.suggestionSelected(item)}> {item} </li>)}
            </ul>
        )
    }

    render () {
        const { text } = this.state;
        return (
            <div className = "AutoCompleteText">
                <form onSubmit={this.handleSubmit} action = "#" method="POST">
                    <input value={text} onChange= {this.onTextChanged} type ="text" name = "query" autoComplete="off"/>
                    {this.renderSuggestions()}

                    <button type="submit" className="searchButton">Search</button>
                </form>
            </div>
        )
    }
}



    
export default AutoComplete2
// ReactDOM.render( <AutoComplete2 />, document.getElementById('root'))