import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'
import AdvancedNav from './AdvancedNav'


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
    <br/><br/> <br/>
    <br/><br/> <br/>

    <div className="container">
      {/* <div className="articleImage"> */}
        {/* <img src = {`data:image/jpeg;base64,${data}`} alt ="article image" width="60%" height="60%"/> */}
      {/* </div> */}

      {window.image.map((num, index) => (
            <div key={index} className="articleImage">
              {/* <form action={num[0]} method="GET" id="nameform">   "/NextResults/{window.enteredTerm}/{value}" */}
                {/* <button type="submit" name="page" value={num[0]}> */}
              <img src = {`data:image/jpeg;base64,${num}`} alt ="article image" />
              {console.log(num)}
                    {/* <p>{num[0]}</p> */}
                {/* </button> */}
                {/* </form> */}

            </div>
            ))}


      <div className="textContainer">
        <div className= "articleText">
        <div dangerouslySetInnerHTML={{__html: window.articleText}}></div>

          {/* <p>{window.articleText}</p> */}
        </div>
      </div>


      <form action={nextArticle} method="GET" id="nameform">   {/*"/NextResults/{window.enteredTerm}/{value}" */}
        <button type="submit" name="page" value="Next article">
            <p>Next article</p>
        </button>
      </form>


    </div>
    </div>

  );

}
console.log(window.image)

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
