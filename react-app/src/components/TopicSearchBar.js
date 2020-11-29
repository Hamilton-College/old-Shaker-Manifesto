import React, { Component } from 'react'
import 'react-bootstrap-typeahead/css/Typeahead.css';
import '../App.css';
import {withRouter} from 'react-router';


class TopicSearchBar extends Component {
    constructor(props){
        super(props)
        this.state = {
            checkbox: null,
            label: "None",
            suggestions: [],
            search: ""
        }
    }
  
     
  
    componentDidMount() { // This is to clear the radio button when back is pressed
        window.addEventListener('unload', function(event) {
            document.getElementById("radioForm").reset();
           }, false);

    }

    handleCheckbox = (e) => {
        this.setState({checkbox: e.target.value.slice(0, e.target.value.indexOf(";"))})
        this.setState({label: e.target.id})

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
                "content_type":"application/json", 
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
        ).then(response => {
        return response.json() 
      })
      .then(json => {
      })
    }

    render () {
        const { search, checkbox, label } = this.state;
        return (
            
                <form onSubmit={this.handleSubmit} action = "#" method="POST" id="radioForm">
                    <div id="dropdownWrapper">
                    <div className="dropdown">
                        <label className="dropbtn">Literature</label>
                        <div className="dropdown-content">
                                {/* I send over the value with the ":id" part so that the displayed category on the results page is the same as it is on this page  */}
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "editorial"} id="Editorials" name = "checkbox" value="editorial;Editorials"  />
                            <label for="vehicle1"> Editorials</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "poem"} id="Poetry" name = "checkbox" value="poem;Poetry"/>
                            <label for="vehicle2"> Poetry</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox==="letter"} id="Letter" name="checkbox" value="letter;Letter"/> 
                            <label for="vehicle3"> Letter</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox==="biography"} id="Biography" name="checkbox" value="biography;Biography"/> 
                            <label for="vehicle4"> Biography</label><br/> 
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox==="quote"} id="Quote" name="checkbox" value="quote;Quote"/>
                            <label for="vehicle5"> Quote</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox==="fiction"} id="Fiction" name="checkbox" value="fiction;Fiction"/>
                            <label for="vehicle6"> Fiction</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox==="note"} id="Notes" name="checkbox" value="note;Notes"/> 
                            <label for="vehicle7"> Notes</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox==="story"} id="Story" name="checkbox" value="story;Story"/> 
                            <label for="vehicle8"> Story</label><br/> 
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox==="publication"} id="Publication" name="checkbox" value="publication;Publication"/> 
                            <label for="vehicle9"> Publication</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox==="book"} id="Book" name="checkbox" value="book;Book"/> 
                            <label for="vehicle10"> Book</label><br/> 
                        </div>
                    </div>
                    <div className="dropdown">
                        <label className="dropbtn">News & Events</label>
                        <div className="dropdown-content">
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "shaker-history"} id="Shaker History" name="checkbox" value="shaker-history;Shaker History"/>
                            <label for="vehicle1"> Shaker History</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "shaker-report"} id="Shaker Community Reports" name="checkbox" value="shaker-report;Shaker Community Reports"/>
                            <label for="vehicle2"> Community Reports</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "shaker-press"} id="Shakers in the Press" name="checkbox" value="shaker-press;Shakers in the Press"/>
                            <label for="vehicle3"> Shakers in the Press</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "national-news"} id="National News" name="checkbox" value="national-news;National News"/>
                            <label for="vehicle4"> National News</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "world-news"} id="World News" name="checkbox" value="world-news;World News"/>
                            <label for="vehicle5"> World News</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "history"} id="Historical Events" name="checkbox" value="history;Historical Events"/>
                            <label for="vehicle6"> Historical Events</label><br/>
                        </div>
                    </div>
                    <div className="dropdown">
                        <label className="dropbtn">Food & Home</label>
                        <div className="dropdown-content">
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "food"} id="Food" name="checkbox" value="food;Food"/>
                            <label for="vehicle1"> Food</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "recipe"} id="Recipes" name="checkbox" value="recipe;Recipes"/>
                            <label for="vehicle2"> Recipes</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "livestock"} id="Livestock" name="checkbox" value="livestock;Livestock"/>
                            <label for="vehicle3"> Livestock</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "equipment"} id="Equipment" name="checkbox" value="equipment;Equipment"/>
                            <label for="vehicle4"> Equipment</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "farmind"} id="Farming" name="checkbox" value="farming;Farming"/>
                            <label for="vehicle5"> Farming</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "crops"} id="Crops" name="checkbox" value="crops;Crops"/>
                            <label for="vehicle6"> Crops</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "house"} id="House" name="checkbox" value="house;House"/>
                            <label for="vehicle7"> House</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "health"} id="Health" name="checkbox" value="health;Health"/>
                            <label for="vehicle8"> Health</label><br/>
                        </div>
                    </div>
                    <div className="dropdown">
                        <label className="dropbtn">Arts</label>
                        <div className="dropdown-content">
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "music"} id="Music" name="checkbox" value="music;Music"/>
                            <label for="vehicle1"> Music</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "dance"} id="Dance" name="checkbox" value="dance;Dance"/>
                            <label for="vehicle2"> Dance</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "hymn"} id="Hymn" name="checkbox" value="hymn;Hymn"/>
                            <label for="vehicle3"> Hymn</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "humor"} id="Humor" name="checkbox" value="humor;Humor"/>
                            <label for="vehicle4"> Humor</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "figure"} id="Illustrations" name="checkbox" value="figure;Illustrations"/>
                            <label for="vehicle5"> Illustrations</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "saying"} id="Sayings" name="checkbox" value="saying;Sayings"/>
                            <label for="vehicle6"> Sayings</label><br/>
                        </div>
                    </div>
                    <div className="dropdown">
                        <label className="dropbtn">Miscellaneous</label>
                        <div className="dropdown-content">
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "lecture"} id="Lecture" name="checkbox" value="lecture;Lecture"/>
                            <label for="vehicle1"> Lecture</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "science"} id="Science" name="checkbox" value="science;Science"/>
                            <label for="vehicle2"> Science</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "ann lee"} id="Ann Lee" name="checkbox" value="ann lee;Ann Lee"/>
                            <label for="vehicle3"> Ann Lee</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "obituary"} id="Obituary" name="checkbox" value="obituary;Obituary"/>
                            <label for="vehicle4"> Obituary</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "instruction"} id="Instruction" name="checkbox" value="instruction;Instruction"/>
                            <label for="vehicle5"> Instructions</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "lesson"} id="Lessons" name="checkbox" value="lesson;Lessons"/>
                            <label for="vehicle6"> Moral lessons</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "juvenile"} id="Juvenile" name="checkbox" value="juvenile;Juvenile"/>
                            <label for="vehicle7"> Juvenile</label><br/>
                            <input type="radio" onChange={this.handleCheckbox} checked = {this.state.checkbox === "other"} id="Other" name="checkbox" value="other;Other"/>
                            <label for="vehicle8"> Other</label><br/>
                        </div>
                    </div>
                </div>
                    <br/> 
                    
                    <div className="pClass">
                    <p>Current topic is: {label}</p>
                    </div>
                    <br/>
                    <div className = "AutoCompleteText2">
                        <input
                            placeholder="What are you looking for?"
                            id = "MySearchTerm" 
                            type = "text" 
                            name = "query"
                            value={search} 
                            onChange={this.handleSearchChange}
                            autoComplete="off"
                        /> 
                    {this.renderSuggestions()}
                    </div>
                    <button type="submit" className="searchButton2">Search</button>

                </form>
        )
    }
}

export default TopicSearchBar