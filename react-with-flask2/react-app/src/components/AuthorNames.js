import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar';
import AdvancedNav from './AdvancedNav';

function AuthorNames() {
  return (
    <div className="container">
        <div id="first">
            <img src={hamiltonLogo} alt="Hamilton logo"width="145" height="60" className = "HamiltonLogo" />
        </div>

        <div className="advancedWrapper">
            <div className="dropdownA">
            <button className="dropbtnA">Advanced Search</button>
            <div className="dropdown-contentA">
                <a href="ArticleType">Article Type</a>
                <a href="Author">Author</a>
                <a href="VolumeIssue">Volume & Issue</a>
            </div>
            </div>
        <h2> <a class="advancedSearch" href = "/"> Basic Search </a></h2>
        </div>

        <br/><br/> <br/><br/> <br/>
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

            
  );
}

export default AuthorNames;
