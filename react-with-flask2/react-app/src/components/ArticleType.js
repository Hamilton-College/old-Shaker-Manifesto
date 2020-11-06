import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar';
import ListOfAuthors from '../AutoComplete-lists/ListOfAuthors';
import TopicSearchBar from './TopicSearchBar';


function ArticleType() {
  return (
    <div className = "container">
      <div id="first">
        <img src={hamiltonLogo} alt="Hamilton logo"width="145" height="60" className = "HamiltonLogo" />
      </div>

      <div className="advancedWrapper">
          <div className="dropdownA">
            <button className="dropbtnA">Advanced Search</button>
            <div className="dropdown-contentA">
              <a href="/ArticleType">Article Type</a>
              <a href="/Author">Author</a>
              <a href="/VolumeIssue">Volume & Issue</a>
            </div>
          </div>
          <h2> <a class="advancedSearch" href = "/"> Basic Search </a></h2>
        </div>

      <br/><br/> <br/><br/> <br/>
      <img src={shakerLogo} alt="Shaker logo"width="600" height="150" className = "ShakerLogo"/>

        <TopicSearchBar/>
        
    </div>

      
  )
};

  

export default ArticleType;
