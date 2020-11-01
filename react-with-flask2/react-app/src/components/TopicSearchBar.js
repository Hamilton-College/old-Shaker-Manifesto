import Search from 'react-search'
import ReactDOM, { render } from 'react-dom'
import React, { Component, PropTypes } from 'react'
// import useForm from 'react-hook-form';
import {  useForm, Controller } from "react-hook-form";
import 'react-bootstrap-typeahead/css/Typeahead.css';
import axios from 'axios';
import '../App.css';


class TopicSearchBar extends Component {
    constructor(props){
        super(props)
        this.state = {
            checkbox: false,
            suggestions: [],
            text: ""
        };
    }

    handleCheckbox = (e) => {
        this.setState({checkbox: e.target.checked})
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
            body:JSON.stringify(e)//this.state.value)
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
        const checkState = this.state.checkbox.checked
        console.log(checkState)
        let suggestions = [];
        if(value.length > 0) {
            const regex = new RegExp(`^${value}`, 'i');
            suggestions = items.sort().filter(v => regex.test(v));
        }
        // this.setState(() => ({checkbox: checkbox.checked}))
        this.setState({checkbox: this.state.checkbox.checked})
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

                    <div id="dropdownWrapper">
                    <div className="dropdown">
                        <button className="dropbtn">Literature</button>
                        <div className="dropdown-content">
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle1" name="checkbox" value="editorial"/>
                        <label for="vehicle1"> Editorials</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle2" name="checkbox" value="poem"/>
                        <label for="vehicle2"> Poetry</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle3" name="checkbox" value="letter"/> 
                        <label for="vehicle3"> Letter</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle4" name="checkbox" value="biography"/> 
                        <label for="vehicle4"> Biography</label><br/> 
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle5" name="checkbox" value="quote"/>
                        <label for="vehicle5"> Quote</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle6" name="checkbox" value="fiction"/>
                        <label for="vehicle6"> Fiction</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle7" name="checkbox" value="note"/> 
                        <label for="vehicle7"> Notes</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle8" name="checkbox" value="story"/> 
                        <label for="vehicle8"> Story</label><br/> 
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle9" name="checkbox" value="publication"/> 
                        <label for="vehicle9"> Publication</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle10" name="checkbox" value="book"/> 
                        <label for="vehicle10"> Book</label><br/> 
                        </div>
                    </div>
                    <div className="dropdown">
                        <button className="dropbtn">News & Events</button>
                        <div className="dropdown-content">
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle1" name="checkbox" value="shaker-history"/>
                        <label for="vehicle1"> Shaker History</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle2" name="checkbox" value="shaker-report"/>
                        <label for="vehicle2"> Shaker Community Reports</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle3" name="checkbox" value="shaker-press"/>
                        <label for="vehicle3"> Shakers in the Press</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle4" name="checkbox" value="national-news"/>
                        <label for="vehicle4"> National News</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle5" name="checkbox" value="world-news"/>
                        <label for="vehicle5"> World News</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle6" name="checkbox" value="history"/>
                        <label for="vehicle6"> Historical Events</label><br/>
                        </div>
                    </div>
                    <div className="dropdown">
                        <button className="dropbtn">Food & Home</button>
                        <div className="dropdown-content">
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle1" name="checkbox" value="food"/>
                        <label for="vehicle1"> Food</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle2" name="checkbox" value="recipe"/>
                        <label for="vehicle2"> Recipes</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle3" name="checkbox" value="livestock"/>
                        <label for="vehicle3"> Livestock</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle4" name="checkbox" value="equipment"/>
                        <label for="vehicle4"> Equipment</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle5" name="checkbox" value="farming"/>
                        <label for="vehicle5"> Farming</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle6" name="checkbox" value="crops"/>
                        <label for="vehicle6"> Crops</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle7" name="checkbox" value="house"/>
                        <label for="vehicle7"> House</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle8" name="checkbox" value="health"/>
                        <label for="vehicle8"> Health</label><br/>
                        </div>
                    </div>
                    <div className="dropdown">
                        <button className="dropbtn">Arts</button>
                        <div className="dropdown-content">
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle1" name="checkbox" value="music"/>
                        <label for="vehicle1"> Music</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle2" name="checkbox" value="dance"/>
                        <label for="vehicle2"> Dance</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle3" name="checkbox" value="hymn"/>
                        <label for="vehicle3"> Hymn</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle4" name="checkbox" value="humor"/>
                        <label for="vehicle4"> Humor</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle5" name="checkbox" value="figure"/>
                        <label for="vehicle5"> Illustrations</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle6" name="checkbox" value="saying"/>
                        <label for="vehicle6"> Sayings</label><br/>
                        </div>
                    </div>
                    <div className="dropdown">
                        <button className="dropbtn">Miscellaneous</button>
                        <div className="dropdown-content">
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle1" name="checkbox" value="lecture"/>
                        <label for="vehicle1"> Lecture</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle2" name="checkbox" value="science"/>
                        <label for="vehicle2"> Science</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle3" name="checkbox" value="ann lee"/>
                        <label for="vehicle3"> Ann Lee</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle4" name="checkbox" value="obituary"/>
                        <label for="vehicle4"> Obituary</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle5" name="checkbox" value="instruction"/>
                        <label for="vehicle5"> Instructions</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle6" name="checkbox" value="lesson"/>
                        <label for="vehicle6"> Moral lessons</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle7" name="checkbox" value="juvenile"/>
                        <label for="vehicle7"> Juvenile</label><br/>
                        <input type="radio" onChange={this.handleCheckbox.bind(this)} checked = {this.state.checkbox} id="vehicle8" name="checkbox" value="other"/>
                        <label for="vehicle8"> Other</label><br/>
                        </div>
                    </div>
                    </div>
                                
                    <input value={text} onChange= {this.onTextChanged} type ="text" name = "query" autoComplete="off"/>
                    {this.renderSuggestions()}

                    <button type="submit" className="searchButton">Search</button>
                </form>
            </div>
        )
    }
}



    
export default TopicSearchBar
// ReactDOM.render( <AutoComplete2 />, document.getElementById('root'))