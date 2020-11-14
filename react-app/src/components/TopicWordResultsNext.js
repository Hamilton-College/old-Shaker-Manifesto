import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'
import AdvancedNav from './AdvancedNav'


function TopicWordResultsNext() { //This is the Result component

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

    <h4>Showing results for: {window.topicWord} </h4>
    <h4>In category: {window.topic} </h4>

    <form action="/ArticleResults" method="POST">
      {typeof articleItem === 'string' ? (
        <p>No results</p>
      ) : (
        articleItem.map((item, index) => (
            <div key={index}>
            <button className="article-link" type="submit">
              <h3>{item[2]}</h3>
            </button>
              <h4>{item[3]}</h4>
              <div dangerouslySetInnerHTML={{__html: item[1] }}></div>
              <br/>
              {/* 0: id, 1: preview, 2: title, 3: author */}

          </div>
        ))
      )}
      </form>

        {buttons.map((num, index) => (
            <div key={index} className="pageButton">
                 <form action={num[0]} method="GET" id="nameform">   {/*"/NextResults/{window.enteredTerm}/{value}" */}
                <button type="submit" name="page" value={num[0]}>
                    <p>{num[0]}</p>
                </button>
                </form>

            </div>
        ))}
        
    </div>
    </div>

  );

}
var articleItem = window.topicWordResults
var buttons = window.pageButtons
// var actionLink = "/TopicWordResultsNext/" + window.topic + "/" + window.topicWord  + "/"   // next page is page 2


export default TopicWordResultsNext;
