import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'
import AdvancedNav from './AdvancedNav'


function ArticleResults() { //This is the Result component

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
    <br/><br/> <br/>

    <div className="container">
      <div className="textContainer">
        <div className= "articleText">
          <p>{window.articleText}</p>
        </div>
      </div>

      <form action={nextArticle} method="GET" id="nameform">   {/*"/NextResults/{window.enteredTerm}/{value}" */}
        <button type="submit" name="page" value="Next article">
            <p>Next article</p>
        </button>
      </form>


    </div>
    </div>

  );

}
// var articleItem = window.results
var lastDigit = window.articleID.slice(-2,-1)
var lastDigit = lastDigit.slice(0,1)

var incDigit = parseInt(lastDigit) +1
var nextArticle = window.articleID.slice(1, -2) + (incDigit.toString())  //+ JSON.stringify(value)


export default ArticleResults;
