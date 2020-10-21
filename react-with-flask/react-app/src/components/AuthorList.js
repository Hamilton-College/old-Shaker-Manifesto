import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'


function AuthorList () { //This is the Result component

  return (
    <div className="container">
        <div class="searchBar">
            <SearchBar />
        </div> 
        <div id="first">
            <a href="http://elib.hamilton.edu/">
            <img src={hamiltonLogo} alt="Hamilton logo"width="145" height="60" class = "HamiltonLogo" />
            </a>
        </div>
        <img src={shakerLogo} alt="Shaker logo"width="200" height="60" class = "ShakerLogoResults" />
        <p>Showing results for: {window.enteredText}</p>
        
    {/* <div>{varTitle}</div> */}
    {/* <p>{window.name}</p> */}
    <p>{window.articleDict}</p>
    {/* <htmlDecode input = {window.token}/> */}

    {/* <p>{text}</p> */}
        
    </div>

  );
}

export default AuthorList;
