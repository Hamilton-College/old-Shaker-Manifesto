import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';


function TopicResults() {
  return (
    <div className="container">
      <div id="first">
            <a href="http://elib.hamilton.edu/">
            <img src={hamiltonLogo} alt="Hamilton logo"width="145" height="60" class = "HamiltonLogo" />
            </a>
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

        <img src={shakerLogo} alt="Shaker logo"width="200" height="60" class = "ShakerLogoResults" />
        <p>Showing results for topic: {window.selectedTopic}</p>

        <div>
            {results.map((user, index) => (
                <div key={index}>
                    <h3>{user[0]}</h3>
                    <p>{user[1]}</p>
                </div>
            ))}
        </div>
    </div>
  );
}
var results = window.topicResults

export default TopicResults;
