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

        <div className="howToHeader">
        <h2>How to use the new Shake Manifesto search engine</h2> 
        </div>
        <br/>

        <h3>Basic Search</h3>
        <p>Basic search works just like any typical search engine like Google. You can search for a single word or multiple words. Don't worry if you spell something wrong. The search function will retrieve the results for the word(s) you likely meant to type. 
            If you'd like to search for an exact phrase/sentetence, you can surround it in quotes. 
            <br/>
            For example: "Ye must love one another" 
            <br/>
            You can even combine an exact phrase with another word.
            <br/>
            For example: "house of" happiness 
        </p>
        <br/>
        <h3>Article Type</h3>
        <p>There are three ways you can use Article type search:
            <br/>
            1. You can search for words within articles of a specific article type by selecting a category and entering the word(s) you're looking for. 
            <br/>
            2. You can view all articles of a certain category by selecting a category and clicking "search" without typing anything into the search bar.
            <br/>
            3. You can use it like basic search by not selecting a category and just entering words into the search box.</p>
        <br/>
        <h3>Author</h3>
        <p>On Author search, you can browse all of the authors by their last name by clicking on one of the letters of the alphabet.
        <br/>
        If you know the author you're looking for, feel free to type their name right into the search bar.</p>

        <br/>
        <h3>Volume & Issue</h3>
          <p>On the Volume & Issue page, you can browse The Shaker Manifesto according to volume and issue</p>
    </div>
    </div>

  );
}

export default HowTo;
