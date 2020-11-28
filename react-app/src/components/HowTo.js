import React from 'react';
import '../App.css';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';

function HowTo () { 

  return (
      <div>
        <nav className="navbar fixed-top navbar-expand-sm navbar-light"  style={{"background-color": '#003153'}}>
        <a href="http://elib.hamilton.edu/"><img src={hamiltonLogo} alt="Hamilton logo" width="130" height="60" className = "navbar-brand" /></a>
          <button className="navbar-toggler" data-toggle="collapse" data-target="#navbarMenu">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarMenu">
            <ul className="navbar-nav ml-auto"> 
              <li className="nav-item">
                <a href="/#" className="nav-link"> Basic Search</a>
              </li>
              <li className="nav-item">
                <a href="/ArticleType" className="nav-link">Article Type</a>
              </li>
              <li id="current">
                <a href="/Author" className="nav-link">Author</a>
              </li>
              <li className="nav-item">
                <a href="/VolumeIssue" className="nav-link">Volume & Issue</a>
              </li>
            </ul>
          </div>
      </nav>
      <br/>
      <br/>
    <div className="container">

        <br/><br/><br/>

        <h2>How to use the new Shake Manifesto search engine</h2> underline this
 
        <h3>Basic Search</h3>
        <p>Basic search works just like any typical search engine like Google. You can search for a single word or multiple words. Don't worry if you spell something wrong. The search function will retrieve the results for the word(s) you likely meant to type. 
            If you'd like to search for an exact phrase/sentetence, you can surround it in quotes. 
            For example: "Ye must love one another" 
        </p>
        <br/>
        <h3>Article Type</h3>
        <p>There are three ways you can use Article type search.
            1. With Article type search, you can narrow your search to a specific category. 
            2. You can see all articles of a certain category
            3. You can use it like basic search by not entering anything</p>
        <br/>
        <h3>Author</h3>
        <br/>
        <h3>Volume & Issue</h3>
          
    </div>
    </div>

  );
}

export default HowTo;
