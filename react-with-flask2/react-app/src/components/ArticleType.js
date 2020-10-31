import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';


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

      
      <form action="#" method="POST"> 
        <div id="dropdownWrapper">
          <div className="dropdown">
            <button className="dropbtn">Supporting Articles</button>
            <div className="dropdown-content">
              <input type="checkbox" id="vehicle1" name="checkbox" value="Editorials"/>
              <label for="vehicle1"> Editorials</label><br/>
              <input type="checkbox" id="vehicle2" name="checkbox" value="Moral & religious lessons"/>
              <label for="vehicle2"> Moral/religious lessons</label><br/>
              <input type="checkbox" id="vehicle3" name="checkbox" value="Mother Ann Lee"/> 
              <label for="vehicle3"> Mother Ann Lee</label><br/>
              <input type="checkbox" id="vehicle4" name="checkbox" value="Biographies"/> 
              <label for="vehicle4"> Biographies</label><br/> 
            </div>
          </div>
          <div className="dropdown">
            <button className="dropbtn">News & Events</button>
            <div className="dropdown-content">
              <input type="checkbox" id="vehicle1" name="checkbox" value="Shaker History"/>
              <label for="vehicle1"> Shaker History</label><br/>
              <input type="checkbox" id="vehicle2" name="checkbox" value="Shaker Community Reports"/>
              <label for="vehicle2"> Shaker Community Reports</label><br/>
              <input type="checkbox" id="vehicle3" name="checkbox" value="Shakers in the Press"/>
              <label for="vehicle4"> Shakers in the Press</label><br/>
              <input type="checkbox" id="vehicle4" name="checkbox" value="National News"/>
              <label for="vehicle3"> National News</label><br/>
              <input type="checkbox" id="vehicle5" name="checkbox" value="World News"/>
              <label for="vehicle4"> World News</label><br/>
              <input type="checkbox" id="vehicle6" name="checkbox" value="Historical Events"/>
              <label for="vehicle4"> Historical Events</label><br/>
            </div>
          </div>
          <div className="dropdown">
            <button className="dropbtn">Collections</button>
            <div className="dropdown-content">
              <input type="checkbox" id="vehicle1" name="checkbox" value="Collections"/>
              <label for="vehicle1"> Collections</label><br/>
              <input type="checkbox" id="vehicle2" name="checkbox" value="Food"/>
              <label for="vehicle2"> Food</label><br/>
              <input type="checkbox" id="vehicle3" name="checkbox" value="Recipes"/>
              <label for="vehicle3"> Recipes</label><br/>
              <input type="checkbox" id="vehicle4" name="checkbox" value="Health and Sanitation"/>
              <label for="vehicle4"> Health and Sanitation</label><br/>
            </div>
          </div>
          <div className="dropdown">
            <button className="dropbtn">Farm</button>
            <div className="dropdown-content">
              <input type="checkbox" id="vehicle1" name="checkbox" value="Farming"/>
              <label for="vehicle1"> Farming</label><br/>
              <input type="checkbox" id="vehicle2" name="checkbox" value="Livestock"/>
              <label for="vehicle2"> Livestock</label><br/>
              <input type="checkbox" id="vehicle3" name="checkbox" value="Crops"/>
              <label for="vehicle3"> Crops</label><br/>
              <input type="checkbox" id="vehicle4" name="checkbox" value="Equipment"/>
              <label for="vehicle4"> Equipment</label><br/>
            </div>
          </div>
          <div className="dropdown">
            <button className="dropbtn">Literature</button>
            <div className="dropdown-content">
              <input type="checkbox" id="vehicle1" name="checkbox" value="Poetry"/>
              <label for="vehicle1"> Poetry</label><br/>
              <input type="checkbox" id="vehicle2" name="checkbox" value="Humor"/>
              <label for="vehicle2"> Humor</label><br/>
              <input type="checkbox" id="vehicle3" name="checkbox" value="Sayings"/>
              <label for="vehicle3"> Sayings</label><br/>
            </div>
          </div>
          <div className="dropdown">
            <button className="dropbtn">Music & Dance</button>
            <div className="dropdown-content">
              <input type="checkbox" id="vehicle1" name="checkbox" value="General"/>
              <label for="vehicle1"> General</label><br/>
              <input type="checkbox" id="vehicle2" name="checkbox" value="Hymns"/>
              <label for="vehicle2"> Hymns</label><br/>
              <input type="checkbox" id="vehicle3" name="checkbox" value="Dance"/>
              <label for="vehicle3"> Dance</label><br/>
            </div>
          </div>

        </div>
          {/* <div className="searchBar">
            <input id="MySearchTerm" type="text" name="query" onkeydown="AutoComplete()"/>
            <input type="submit" value="search" class="searchButton"/> */}
      </form>
    </div>

      
  )
};

  

export default ArticleType;
