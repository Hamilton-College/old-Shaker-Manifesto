import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import 'react-tabs/style/react-tabs.css';


function ArticleResults() { //This is the Result component

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
    
    <Tabs> {/* defaultIndex={0} >*/}
    <TabList>
      <Tab>Image</Tab>
      <Tab>Full text of issue</Tab>
    </TabList>
 
    <TabPanel>
      <Carousel selectedItem={parseInt(window.startPage)} showArrows={true}>
      {window.images.map((num, index) => (
            <div key={index}>
              <img src = {`data:image/jpeg;base64,${num}`} alt ="article image"/>
            </div>
      ))}
      </Carousel>
    </TabPanel>
    {/* <TabPanel>
      <div className="thumbWrapper">
        {window.thumbs.map((num, index) => (
            <div key={index} className="thumb">
              <img src = {`data:image/jpeg;base64,${num}`} alt ="article thumbnail" />
              
                <p> page {index+1} </p>
              

            </div>
            ))}
        </div>
    </TabPanel> */}
    <TabPanel>
      <br/>

      <div className="pClass">
        <a href="#target"><b>Click here</b></a> to jump to the selected article
      </div>

      <div className="textContainer">
        <div className= "articleText">
        <div dangerouslySetInnerHTML={{__html: window.articleText}}></div>

          {/* <p>{window.articleText}</p> */}
        </div>
      </div>
    </TabPanel>
  </Tabs>
      {/* <div className="articleImage"> */}
        {/* <img src = {`data:image/jpeg;base64,${data}`} alt ="article image" width="60%" height="60%"/> */}
      {/* </div> */}

      
      {/* <form action={nextArticle} method="GET" id="nameform">  
        <button type="submit" name="page" value="Next article">
            <p>Next article</p>
        </button>
      </form> */}


    </div>
    </div>

  );

}
console.log(window.image)
console.log(window.startPage)

// var i;
// for (i = 0; i < window.image.length; i++) {
//   for (var j=0; j < window.image[i].length; j++) {
//     if(Array.isArray(window.image[i][j])){ // WE SHOULD DO A WHILE
//       window.image[i].splice(j,1) // remove the item
//       j--
//     }
//     else{ // if it's the string
//       window.image[i][j] = (window.image.slice(1,-1));
//     }
//   console.log(window.image[i])
//   } 
// }
// var data = window.image
// data.reduce((acc, val) => acc.concat(val), []);

//var data = window.image//[].concat.apply([], [window.image]);
// function flattenDeep(arr1) {
//   return arr1.reduce((acc, val) => Array.isArray(val) ? acc.concat(flattenDeep(val)) : acc.concat(val), []);
// }


// var data = (window.image.slice(1,-1))
// var data = `data:image/jpeg;base64,${window.image}`
// console.log(data)

// const Example = {data}  => <img src={`data:image/jpeg;base64,${data}`} />

// var articleItem = window.results
var lastDigit = window.articleID.slice(-2,-1)
var lastDigit = lastDigit.slice(0,1)

var incDigit = parseInt(lastDigit) +1
var nextArticle = window.articleID.slice(1, -2) + (incDigit.toString())  //+ JSON.stringify(value)


export default ArticleResults;
