import React from 'react';
import './App.css';
import shakerLogo from './images/shaker-manifesto-logo.PNG';
import hamiltonLogo from './images/hamilton-lib-logo.PNG';
import SearchBar from './components/SearchBar'
import AdvancedNav from './components/AdvancedNav';
import ArticleType from './components/ArticleType';
import Author from './components/Author';
import VolumeIssue from './components/VolumeIssue';
import Results from './components/Results';
import AuthorList from './components/AuthorList';
import TopicResults from './components/TopicResults';
import TopicWordResults from './components/TopicWordResults';
import AuthorNames from './components/AuthorNames';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import AutoComplete2 from './components/autocomplete2';


function App() {
  return (
    <div className="container">

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
          </Switch>
        
      </Router>
      <div className= "footer">
          <p> <a className = "footer" href="http://elib.hamilton.edu/"> ©2020 Hamilton College</a> </p>
      </div>
    </div>

  );
}
//This is just another component. Our landing page
const Home = () => (
  <div className="container">
    <div id="first">
      <img src={hamiltonLogo} alt="Hamilton logo"width="145" height="60" className = "HamiltonLogo" />
    </div>

    <div className="advancedWrapper">
      <div className="dropdownA">
        <button className="dropbtnA">Advanced Search</button>
        <div className="dropdown-contentA">
          <a href="/ArticleType">Article Type</a>
          <a href="/Author">Author</a>
          <a href="/VolumeIssue">Volume & Issue</a>
        </div>
      </div>
    </div>

      <br/><br/> <br/><br/> <br/>
      <img src={shakerLogo} alt="Shaker logo"width="600" height="150" className = "ShakerLogo"/>
      <div className="searchBar">
        <SearchBar />
        {/* <form action= "#" method="POST" autocomplete="off"> */}
          {/* <input id="MySearchTerm" type="text" name="query" onkeydown="AutoComplete()"/> */}
          {/* <input type="submit" value="search" class="searchButton"/> */}
        {/* </form> */}
      </div>   
      
    </div>
)

export default App;
