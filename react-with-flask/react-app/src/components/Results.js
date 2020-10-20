import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'
// import SearchBar from './components/SearchBar'

function Results() {
  return (
    <div className="container">
        
        <p>Showing results for: {window.token2}</p>
        <div class="searchBar">
            <SearchBar />
        </div>   
        <p>{window.token}</p>
        
    </div>

  );
}

export default Results;
