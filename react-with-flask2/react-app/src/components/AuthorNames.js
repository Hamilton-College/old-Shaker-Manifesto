import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar';
import AdvancedNav from './AdvancedNav';

function AuthorNames() {
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
        
        <br/><br/> <br/>
        <img src={shakerLogo} alt="Shaker logo"width="600" height="150" className = "ShakerLogo"/>
        
        <br/>
        <p>Authors whose name begins with the letter {window.firstLetter} </p>

        <p>Results:</p>

        {/* <div>
            {window.namesOfLetter.map((user, index) => (
                <div key={index}>
                    <h3>{user[0]}</h3>
                    <p>{user[1]}</p>
                </div>
            ))}
        </div> */}
        
        {/* this needs to be attached to the part directly above */}

        {/* <div className="articleResults"> */}
        <form action="/AuthorNames" method="POST">
                {window.namesOfLetter.map((user, index) => (
                    <div className = "articleResults" key={index}>
                        
                        <button className="btn-link" type="submit" value={user[0] +" " + user[1]} name = "name">{/*look more into val and name */}
                        <h3>{user[0]} {user[1]}</h3>
                        {/* <p>{user}</p>
                        <p>{user[0]}</p>
                        <p>{user[1]}</p>
                        <p>{user[0] + user[1]}</p>
                        <p>{user.slice(0,2)}</p> */}
                        </button>
                    </div>
                ))}
        </form>
        {/* </div> */}
    </div>
    </div>

            
  );
}

export default AuthorNames;
