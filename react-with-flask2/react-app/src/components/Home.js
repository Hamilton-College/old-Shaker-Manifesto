import React, {Component} from 'react';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
// This is a component that will be displayed in app.js

class Home extends Component {
    // to convert this into a react, component, 
    // we need to give it a component state
    render() {
        const {search} = this.state // now we don't have to type this.state when we want to edit the search property
        return(
            <div className="container">
            <div id="first">
                <img src={hamiltonLogo} alt="Hamilton logo"width="145" height="60" className = "HamiltonLogo" />
            </div>
        
            <div className="advancedWrapper">
                <div className="dropdownA">
                <button className="dropbtnA">Advanced Search</button>
                <div className="dropdown-contentA">
                    <a href="ArticleType">Article Type</a>
                    <a href="Author">Author</a>
                    <a href="VolumeIssue">Volume & Issue</a>
                </div>
                </div>
            </div>
        
                <br/><br/> <br/><br/> <br/>
                <img src={shakerLogo} alt="Shaker logo"width="600" height="150" className = "ShakerLogo"/>
                <div className="searchBar">
                    <p>Hola</p>
                    {this.props.children}
                {/* <SearchBar /> */}
                {/* <form action= "#" method="POST" autocomplete="off"> */}
                    {/* <input id="MySearchTerm" type="text" name="query" onkeydown="AutoComplete()"/> */}
                    {/* <input type="submit" value="search" class="searchButton"/> */}
                {/* </form> */}
                </div>   
                
            </div>
        )
    }
}
export default Home
