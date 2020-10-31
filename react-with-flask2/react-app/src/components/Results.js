import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'
import AdvancedNav from './AdvancedNav'


function Results() { //This is the Result component

  return (
    <div className="container">
        
        <p>Showing results for: {window.enteredTerm}</p>
        {/* <div class="searchBar">
            <SearchBar />
        </div>  */}
        <p>{testVar}</p>
        <br/>
        {testVar}
        <div className="advancedWrapper">
            <div className="dropdownA">
            <button className="dropbtnA">Advanced Search</button>
            <div className="dropdown-contentA">
                <a href="ArticleType">Article Type</a>
                <a href="Author">Author</a>
                <a href="VolumeIssue">Volume & Issue</a>
            </div>
            </div>
            <h2> <a class="advancedSearch" href = "/"> Basic Search </a></h2>
        </div>
        
    {/* <div>{varTitle}</div> */}
    {/* {window.results} */}
    {articleItem.map((item, index) => (
                <div key={index}>
                    <h3>{item[0]}</h3>
                    <p>{item[1]}</p>
                    <p>{item[2]}</p>
                </div>
            ))}
    {/* <htmlDecode input = {window.token}/> */}

    {/* <p>{text}</p> */}
        
    </div>

  );

}
var articleItem = window.results
var testVar = "Hello <b>there</b>"


export default Results;
