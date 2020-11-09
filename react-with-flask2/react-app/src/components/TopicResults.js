import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';


function TopicResults() {
  return (
      <div>
        <nav className="navbar fixed-top navbar-expand-sm navbar-light"  style={{"background-color": '#e3f2fd'}}>
        <img src={hamiltonLogo} alt="Hamilton logo" width="140" height="60" className = "navbar-brand" />
          <button className="navbar-toggler" data-toggle="collapse" data-target="#navbarMenu">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarMenu">
            <ul className="navbar-nav ml-auto"> 
              <li className="nav-item">
                <a href="/#" className="nav-link"> Basic Search</a>
              </li>
              <li id="current">
                <a href="/ArticleType" className="nav-link">Article Type</a>
              </li>
              <li className="nav-item">
                <a href="/Author" className="nav-link">Author</a>
              </li>
              <li className="nav-item">
                <a href="/VolumeIssue" className="nav-link">Volume & Issue</a>
              </li>
            </ul>
          </div>
      </nav>
      <br/><br/> <br/>
      <br/><br/> <br/>

        <div className="container">

        <img src={shakerLogo} alt="Shaker logo"width="200" height="60" class = "ShakerLogoResults" />
        <h4>Showing results for topic: {window.selectedTopic}</h4>

        <div>
            {results.map((user, index) => (
                <div key={index}>
                    <h3>{user[0]}</h3>
                    <p>{user[1]}</p>
                </div>
            ))}
        </div>
    </div>
    </div>
  );
}
var results = window.topicResults

export default TopicResults;
