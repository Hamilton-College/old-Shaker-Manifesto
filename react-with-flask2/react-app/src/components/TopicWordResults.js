import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'
import AdvancedNav from './AdvancedNav'


function TopicWordResults() { //This is the Result component

  return (
    <div className="container">
        
      
      
      {/* <div class="searchBar">
          <SearchBar />
      </div>  */}
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
        
    <p>Showing results for: {window.topicWord} </p>
    <p>In category: {window.topic} </p>
    <div>
      {typeof articleItem === 'string' ? (
        <p>No results</p>
      ) : (
        articleItem.map((item, index) => (
          <div key={index}>
              <h3>{item[0]}</h3>
              <div dangerouslySetInnerHTML={{__html: item[1] }}></div>
              <p>{item[2]}</p>
          </div>
        ))
      )}
    </div>

      
    {/* <htmlDecode input = {window.token}/> */}

    {/* <p>{text}</p> */}
        
    </div>

  );

}
var articleItem = window.topicWordResults

export default TopicWordResults;
