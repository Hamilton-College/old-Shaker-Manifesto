import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar';
import ListOfAuthors from '../AutoComplete-lists/ListOfAuthors';
import TopicSearchBar from './TopicSearchBar';


function ArticleType() {
  return (
    <div className = "container">
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
          <h2> <a class="advancedSearch" href = "/"> Basic Search </a></h2>
        </div>

      <br/><br/> <br/><br/> <br/>
      <img src={shakerLogo} alt="Shaker logo"width="600" height="150" className = "ShakerLogo"/>

      
      {/* <form action="#" method="POST"> 
        <div id="dropdownWrapper">
          <div className="dropdown">
            <button className="dropbtn">Literature</button>
            <div className="dropdown-content">
              <input type="checkbox" id="vehicle1" name="checkbox" value="editorial"/>
              <label for="vehicle1"> Editorials</label><br/>
              <input type="checkbox" id="vehicle2" name="checkbox" value="poem"/>
              <label for="vehicle2"> Poetry</label><br/>
              <input type="checkbox" id="vehicle3" name="checkbox" value="letter"/> 
              <label for="vehicle3"> Letter</label><br/>
              <input type="checkbox" id="vehicle4" name="checkbox" value="biography"/> 
              <label for="vehicle4"> Biography</label><br/> 
              <input type="checkbox" id="vehicle5" name="checkbox" value="quote"/>
              <label for="vehicle5"> Quote</label><br/>
              <input type="checkbox" id="vehicle6" name="checkbox" value="fiction"/>
              <label for="vehicle6"> Fiction</label><br/>
              <input type="checkbox" id="vehicle7" name="checkbox" value="note"/> 
              <label for="vehicle7"> Notes</label><br/>
              <input type="checkbox" id="vehicle8" name="checkbox" value="story"/> 
              <label for="vehicle8"> Story</label><br/> 
              <input type="checkbox" id="vehicle9" name="checkbox" value="publication"/> 
              <label for="vehicle9"> Publication</label><br/>
              <input type="checkbox" id="vehicle10" name="checkbox" value="book"/> 
              <label for="vehicle10"> Book</label><br/> 
            </div>
          </div>
          <div className="dropdown">
            <button className="dropbtn">News & Events</button>
            <div className="dropdown-content">
              <input type="checkbox" id="vehicle1" name="checkbox" value="shaker-history"/>
              <label for="vehicle1"> Shaker History</label><br/>
              <input type="checkbox" id="vehicle2" name="checkbox" value="shaker-report"/>
              <label for="vehicle2"> Shaker Community Reports</label><br/>
              <input type="checkbox" id="vehicle3" name="checkbox" value="shaker-press"/>
              <label for="vehicle3"> Shakers in the Press</label><br/>
              <input type="checkbox" id="vehicle4" name="checkbox" value="national-news"/>
              <label for="vehicle4"> National News</label><br/>
              <input type="checkbox" id="vehicle5" name="checkbox" value="world-news"/>
              <label for="vehicle5"> World News</label><br/>
              <input type="checkbox" id="vehicle6" name="checkbox" value="history"/>
              <label for="vehicle6"> Historical Events</label><br/>
            </div>
          </div>
          <div className="dropdown">
            <button className="dropbtn">Food & Home</button>
            <div className="dropdown-content">
              <input type="checkbox" id="vehicle1" name="checkbox" value="food"/>
              <label for="vehicle1"> Food</label><br/>
              <input type="checkbox" id="vehicle2" name="checkbox" value="recipe"/>
              <label for="vehicle2"> Recipes</label><br/>
              <input type="checkbox" id="vehicle3" name="checkbox" value="livestock"/>
              <label for="vehicle3"> Livestock</label><br/>
              <input type="checkbox" id="vehicle4" name="checkbox" value="equipment"/>
              <label for="vehicle4"> Equipment</label><br/>
              <input type="checkbox" id="vehicle5" name="checkbox" value="farming"/>
              <label for="vehicle5"> Farming</label><br/>
              <input type="checkbox" id="vehicle6" name="checkbox" value="crops"/>
              <label for="vehicle6"> Crops</label><br/>
              <input type="checkbox" id="vehicle7" name="checkbox" value="house"/>
              <label for="vehicle7"> House</label><br/>
              <input type="checkbox" id="vehicle8" name="checkbox" value="health"/>
              <label for="vehicle8"> Health</label><br/>
            </div>
          </div>
          <div className="dropdown">
            <button className="dropbtn">Arts</button>
            <div className="dropdown-content">
              <input type="checkbox" id="vehicle1" name="checkbox" value="music"/>
              <label for="vehicle1"> Music</label><br/>
              <input type="checkbox" id="vehicle2" name="checkbox" value="dance"/>
              <label for="vehicle2"> Dance</label><br/>
              <input type="checkbox" id="vehicle3" name="checkbox" value="hymn"/>
              <label for="vehicle3"> Hymn</label><br/>
              <input type="checkbox" id="vehicle4" name="checkbox" value="humor"/>
              <label for="vehicle4"> Humor</label><br/>
              <input type="checkbox" id="vehicle5" name="checkbox" value="figure"/>
              <label for="vehicle5"> Illustrations</label><br/>
              <input type="checkbox" id="vehicle6" name="checkbox" value="saying"/>
              <label for="vehicle6"> Sayings</label><br/>
            </div>
          </div>
          <div className="dropdown">
            <button className="dropbtn">Miscellaneous</button>
            <div className="dropdown-content">
              <input type="checkbox" id="vehicle1" name="checkbox" value="lecture"/>
              <label for="vehicle1"> Lecture</label><br/>
              <input type="checkbox" id="vehicle2" name="checkbox" value="science"/>
              <label for="vehicle2"> Science</label><br/>
              <input type="checkbox" id="vehicle3" name="checkbox" value="ann lee"/>
              <label for="vehicle3"> Ann Lee</label><br/>
              <input type="checkbox" id="vehicle4" name="checkbox" value="obituary"/>
              <label for="vehicle4"> Obituary</label><br/>
              <input type="checkbox" id="vehicle5" name="checkbox" value="instruction"/>
              <label for="vehicle5"> Instructions</label><br/>
              <input type="checkbox" id="vehicle6" name="checkbox" value="lesson"/>
              <label for="vehicle6"> Moral lessons</label><br/>
              <input type="checkbox" id="vehicle7" name="checkbox" value="juvenile"/>
              <label for="vehicle7"> Juvenile</label><br/>
              <input type="checkbox" id="vehicle8" name="checkbox" value="other"/>
              <label for="vehicle8"> Other</label><br/>
            </div>
          </div>

        </div> */}
        <TopicSearchBar items = {ListOfAuthors}/>
        {/* <input type="submit" value="search" class="searchButton"/> */}

        {/*  maybe give it its own component such that it doesn't have a form */}
          {/* <div className="searchBar">
            <input id="MySearchTerm" type="text" name="query" onkeydown="AutoComplete()"/>
            <input type="submit" value="search" class="searchButton"/> */}
      {/* </form> */}
    </div>

      
  )
};

  

export default ArticleType;
