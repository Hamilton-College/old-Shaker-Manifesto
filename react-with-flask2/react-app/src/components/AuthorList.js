import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'
import AdvancedNav from './AdvancedNav';

// We come here after entering a name in author Search
// We also come here by authorSearch -> click letter -> click name -> here

function AuthorList () { //This is the Result component

//   const authors = window.articlesList
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
      <br/>
      <br/>
    <div className="container">

        <br/><br/><br/>

        <h4>Showing results for: {window.enteredText}</h4>
 
   
        <form action="/ArticleResults" method="POST">
            {authors.map((user, index) => (
                <div key={index}>
                <button className="article-link" type="submit">
                    <h4>{user[0]}</h4>
                </button>
                    <p>{user[1]}</p>
                    <br/>
                </div>
            ))}
        </form>

    {/* <div>{loopAuthors2}</div> */}
    
    </div>
    </div>

  );
}
var authors = window.articlesList
const loopAuthors = Object.keys(authors).map(key => 
    <option value={key}>{authors[key]}</option>
)

// const loopAuthors2 = authors.map((val) =>{
//     return val;
// })
export default AuthorList;
