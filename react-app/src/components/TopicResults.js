import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';


function TopicResults() {
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

        <img src={shakerLogo} alt="Shaker logo"width="200" height="60" class = "ShakerLogoResults" />
        <h4>Showing results for topic: {window.selectedTopic.slice(1,-1)}</h4>

        <div>
            {results.map((item, index) => (
                <div key={index}>
                  {item[0].length > 0 ? ( 
                <form action={"/ArticleResults/" + item[2]} method="GET">
                <button className="article-link" type="submit" name = "article" value={item[2]}>
                    <h3>{item[0]}</h3>
                </button>
                    <h4>{item[1]}</h4>
                    <br/>
                </form>
                    ) : (
                    <div>
                      <form action={"/ArticleResults/" + item[2]} method="GET">
                    <button className="article-link" type="submit" name = "article" value={item[2]}>
                        <h3>Title Unknown</h3>
                    </button>
                        <h4>{item[1]}</h4>
                        <br/>
                    </form>
                    </div>)}

              {/* 0: title, 1: author, 2: id */}
                </div>
            ))}
        </div>

    </div>
    </div>
  );
}
var results = window.topicResults

export default TopicResults;
