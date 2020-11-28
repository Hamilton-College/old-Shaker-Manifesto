import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';

function AuthorNames() {
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
    <br/><br/> <br/>

        <div className="container">
        
        <br/>
        <img src={shakerLogo} alt="Shaker logo"width="600" height="150" className = "ShakerLogo"/>
        
        <br/><br/> <br/>
        <br/><br/> <br/>
        <br/><br/> <br/>
        <h3>Authors whose last name begins with {window.firstLetter} </h3>

        <form action="/AuthorNames" method="POST">
                {window.namesOfLetter.map((user, index) => (
                    <div className = "articleResults" key={index}>
                        <button className="btn-link" type="submit" value={user[0]+user[1]} name = "name">
                        <h3>{user[0]} {user[1]}</h3>
                        
                        </button>
                    </div>
                ))}
        </form>
    </div>
    </div>

            
  );
}

export default AuthorNames;
