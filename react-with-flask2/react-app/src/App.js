import React from 'react';
import './App.css';
import shakerLogo from './images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from './images/hamilton-lib-logo.PNG';
import SearchBar from './components/SearchBar'
import ArticleType from './components/ArticleType';
import Author from './components/Author';
import VolumeIssue from './components/VolumeIssue';
import Results from './components/Results';
import ArticleResults from './components/ArticleResults';
import AuthorList from './components/AuthorList';
import TopicResults from './components/TopicResults';
import TopicWordResults from './components/TopicWordResults';
import AuthorNames from './components/AuthorNames';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import {NavLink} from 'react-router-dom';
import AutoComplete2 from './components/autocomplete2';


function App() {
  return (
    <div>
      <Router>
          {/* <AdvancedNav />  always display nave component */}
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/ArticleType" component={ArticleType}/>
            <Route path="/AuthorList" component={AuthorList}/>
            <Route path="/Author" exact component={Author}/>
            <Route path="/VolumeIssue" component={VolumeIssue}/>
            <Route path="/Results" component={Results}/>
            <Route path="/AuthorNames" component={AuthorNames}/>
            <Route path="/TopicResults" component={TopicResults}/>
            <Route path="/TopicWordResults" component={TopicWordResults}/>
            <Route path="/ArticleResults" component={ArticleResults}/>
          </Switch>
        
      </Router>
      <br/>
      <br/>
      <a className = "pClass" href="http://elib.hamilton.edu/"> ©2020 Hamilton College</a>
    </div>

  );
}
//This is just another component. Our landing page
const Home = () => (
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
      <div className="container">

      <br/><br/> <br/>
      <br/><br/> <br/>
      <img src={shakerLogo} alt="Shaker logo"width="600" height="150" className = "ShakerLogo"/>
      {/* <div className="searchBar"> */}
      <br/>
      <br/>
      <SearchBar />
        {/* <form action= "#" method="POST" autocomplete="off"> */}
          {/* <input id="MySearchTerm" type="text" name="query" onkeydown="AutoComplete()"/> */}
          {/* <input type="submit" value="search" class="searchButton"/> */}
        {/* </form> */}
      {/* </div>    */}
      </div>
    </div>
)

export default App;
