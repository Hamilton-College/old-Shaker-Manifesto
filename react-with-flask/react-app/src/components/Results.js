import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'


function Results() { //This is the Result component

  return (
    <div className="container">
        
        <p>Showing results for: {window.token1}</p>
        <div class="searchBar">
            <SearchBar />
        </div> 
    {/* <div>{varTitle}</div> */}
    <p>{window.token2}</p>
    {/* <htmlDecode input = {window.token}/> */}

    {/* <p>{text}</p> */}
        
    </div>

  );
}

export default Results;
