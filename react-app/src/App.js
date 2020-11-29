import React from 'react';
import './App.css';
import shakerLogo from './images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from './images/hamilton-lib-logo.PNG';
import lomas from './images/manifesto-office-lomas.jpg';
import articleGroup from './images/article-group.png';
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
import VolumeIssueResults from './components/VolumeIssueResults';
import HowTo from './components/HowTo';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';



function App() {
  return (
    <div>
      <Router>
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
            <Route path="/VolumeIssueResults" component={VolumeIssueResults}/>
            <Route path="/HowTo" component={HowTo}/>
          </Switch>

      </Router>
      <br/>
      <br/>
      <a href="/HowTo" className="pClass"> ⓘ How to use</a>
      <br/>
      <a className = "pClass" href="http://elib.hamilton.edu/"> ©2020 Hamilton College</a>

    </div>

  );
}
//This is just another component. Our landing page
const Home = () => (
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
      <div className="container">

      <br/><br/> <br/>
      <br/><br/>

      <img src={shakerLogo} alt="Shaker logo" width="700" height="250" className = "ShakerLogo"/>

      <img src={articleGroup} alt="Lomas" width="210" height="335" className = "lomasL"/>
      <img src={lomas} alt="Lomas" width="230" height="250" className = "lomasR"/>
      <br/>
      <br/>
      <br/>
      <br/>
      <br/>
      <SearchBar />
      <br/>
      <br/>
      <br/>
      <br/>

      </div>
    </div>
)

export default App;
