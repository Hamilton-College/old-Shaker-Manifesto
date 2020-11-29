import React from 'react';
import '../App.css';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';


function Results() { 

  return (
    <div>
      <nav className="navbar fixed-top navbar-expand-sm navbar-light"  style={{"background-color": '#003153'}}>
        <a href="http://elib.hamilton.edu/"><img src={hamiltonLogo} alt="Hamilton logo" width="130" height="60" className = "navbar-brand" /></a>
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
      <div className="pageNumber">
        <h4>page {window.pageNum} of {buttons.length}</h4>
      </div>
      <h4>Showing results for: {window.enteredTerm.slice(1,-1)}</h4>
      <br/>
      {typeof articleItem === 'string' ? ( //if it is "None"
        <h3>No results found</h3>
      ) : (
        articleItem.map((item, index) => (
            <div key={index}>
              <form action={"/ArticleResults/" + item[0]} method="GET">
              <button className="article-link" type="submit" name="article" value= {item[0]}>
                <h3>{item[2]}</h3>
              </button>
                <h4>{item[3]}</h4>
                <div dangerouslySetInnerHTML={{__html: item[1] }}></div>
                <br/>
                {/* 0: id, 1: preview, 2: title, 3: author */}
            </form>
          </div>
        ))

      )}


      {typeof articleItem === 'string' ? ( //it's a string because it's "None"
        <div></div>
        ) : ([
          <div className = "pageLabel">
          <p>Page:</p>
          </div>,
          buttons.map((num, index) => (
                <div key={index} className="pageButton">
                    <form action={num[0]} method="GET" id="nameform">   
                    <button className="pageButton" type="submit" name="page" value={num[0]}>
                        <p>{num[0]}</p>
                    </button>
                    </form>
    
                </div>
                ))]

           )}

      
        
    </div>
    </div>

  );

}
var articleItem = window.results
var buttons = window.pageButtons

export default Results;
