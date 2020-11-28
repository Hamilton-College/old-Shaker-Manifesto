import React from 'react';
import '../App.css';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import 'react-tabs/style/react-tabs.css';


function VolumeIssueResults() { 

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
    <br/>
    
    <div className="container">

      <h3>Volume {window.articleID.slice(1,3)}  Issue {window.articleID.slice(3,5)} </h3>
    
    <Tabs> 
    <TabList>
      <Tab>Image</Tab>
      <Tab>Full text of issue</Tab>
    </TabList>
 
    <TabPanel>
      <Carousel showArrows={true}>
      {window.images.map((num, index) => (
            <div key={index}>
              <img src = {`data:image/jpeg;base64,${num}`} alt ="article image"/>
            </div>
      ))}
      </Carousel>
    </TabPanel>
    
    <TabPanel>
      <br/>

      <div className="textContainer">
        <div className= "articleText">
        <div dangerouslySetInnerHTML={{__html: window.articleText}}></div>

        </div>
      </div>
    </TabPanel>
  </Tabs>


    </div>
    </div>

  );

}

export default VolumeIssueResults;
