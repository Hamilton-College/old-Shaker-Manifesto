import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar'
import AdvancedNav from './AdvancedNav';

// We come here after entering a name in author Search
// We also come here by authorSearch -> click letter -> click name -> here

function AuthorList () { //This is the Result component

//   const authors = window.articlesList
  return (
    <div className="container">
        <div class="searchBar">
            <SearchBar />
        </div> 
        <div id="first">
            <a href="http://elib.hamilton.edu/">
            <img src={hamiltonLogo} alt="Hamilton logo"width="145" height="60" class = "HamiltonLogo" />
            </a>
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



        <img src={shakerLogo} alt="Shaker logo"width="200" height="60" class = "ShakerLogoResults" />
        <p>Showing results for: {window.enteredText}</p>
        
    {/* <div>{varTitle}</div> */}
    {/* <p>{window.name}</p> */}
    
    {/* <script>
        function loop(){
            
            console.log(window.articlesList),
            console.log(typeof window.articlesList)
        }
    </script> */}

    {/* <div>
        {Object.keys(authors).map((key)=>(
            <p>{authors[`${key}`]}</p>
        ))}
    </div> */}
    
    {/* <div>
        {authors.forEach(function (item, index) {
            // console.log(item, index)

        })}
        
    </div> */}
        <div>
            {authors.map((user, index) => (
                <div key={index}>
                    <h3>{user[0]}</h3>
                    <p>{user[1]}</p>
                    {/* <p>{user[1]}</p> */}
                </div>
            ))}
        </div>
    {/* <div>{loopAuthors2}</div> */}
    
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
