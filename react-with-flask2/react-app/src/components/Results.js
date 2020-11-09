import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'
import AdvancedNav from './AdvancedNav'


function Results() { //This is the Result component

  return (
    <div>
      <nav className="navbar fixed-top navbar-expand-sm navbar-light"  style={{"background-color": '#e3f2fd'}}>
        <img src={hamiltonLogo} alt="Hamilton logo" width="140" height="60" className = "navbar-brand" />
          <button className="navbar-toggler" data-toggle="collapse" data-target="#navbarMenu">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarMenu">
            <ul className="navbar-nav ml-auto"> 
              <li id="current">
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

    <div className="container">

      <h4>Showing results for: {window.enteredTerm}</h4>
      {/* <div class="searchBar">
          <SearchBar />
      </div>  */}

    <form action="/ArticleResults" method="POST">
      {typeof articleItem === 'string' ? (
        <p>No results</p>
      ) : (
        articleItem.map((item, index) => (
            <div key={index}>
            <button className="article-link" type="submit">
              <h3>{item[0]}</h3>
            </button>
              <div dangerouslySetInnerHTML={{__html: item[1] }}></div>
              <br/>
              {/* <p>{item[2]}</p> this is the hit count */}
          </div>
        ))
      )}
      </form>

      
    {/* <htmlDecode input = {window.token}/> */}

    {/* <p>{text}</p> */}
        
    </div>
    </div>

  );

}
var articleItem = window.results

export default Results;
