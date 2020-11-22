import React from 'react';
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';
import SearchBar from './SearchBar';
import AutoComplete2 from './AutoComplete2';
import { Typeahead } from 'react-bootstrap-typeahead'; // ES2015
import ListOfAuthors from '../AutoComplete-lists/ListOfAuthors';



function Author() {
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
              <li id="current">
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
      <img src={shakerLogo} alt="Shaker logo"width="600" height="150" className = "ShakerLogo"/>
      
      {/* <div class="searchBar">
        <SearchBar />
      </div>    */}
      <br/><br/><br/> 
      <div className="textAboveAlphabet">
        <p>Browse by last name of author</p>
      </div>
      <div className="alphabet">
      <form action="#" method="POST">
          <button type="submit" value="A" name = "letter">A</button>
          <button type="submit" value="B" name = "letter">B</button>
          <button type="submit" value="C" name = "letter">C</button>
          <button type="submit" value="D" name = "letter">D</button>
          <button type="submit" value="E" name = "letter">E</button>
          <button type="submit" value="F" name = "letter">F</button>
          <button type="submit" value="G" name = "letter">G</button>
          <button type="submit" value="H" name = "letter">H</button>
          <button type="submit" value="I" name = "letter">I</button>
          <button type="submit" value="J" name = "letter">J</button>
          <button type="submit" value="K" name = "letter">K</button>
          <button type="submit" value="L" name = "letter">L</button>
          <button type="submit" value="M" name = "letter">M</button>
          <button type="submit" value="N" name = "letter">N</button>
          <button type="submit" value="O" name = "letter">O</button>
          <button type="submit" value="P" name = "letter">P</button>
          <button type="submit" value="Q" name = "letter">Q</button>
          <button type="submit" value="R" name = "letter">R</button>
          <button type="submit" value="S" name = "letter">S</button>
          <button type="submit" value="T" name = "letter">T</button>
          <button type="submit" value="U" name = "letter">U</button>
          <button type="submit" value="V" name = "letter">V</button>
          <button type="submit" value="W" name = "letter">W</button>
          <button type="submit" value="X" name = "letter">X</button>
          <button type="submit" value="Y" name = "letter">Y</button>
          <button type="submit" value="Z" name = "letter">Z</button>
      </form> 

      </div>
        <br/><br/>
        <AutoComplete2/>
          {/* <input id="MySearchTerm" data-provide="typeahead" autocomplete="off" type="text" name="query"/> */}
          {/* <input type="text" className= "span3" data-provide="typeahead" data-items="4" placeholder="Introduce un país" data-source='["Alabama", "California", "Marte"]' autoComplete="off" name="query"></input> */}
          
            {/* <input type="submit" value="search" className="searchButton"/> */}
          {/* </form> */}
        {/* <script type="text/javascript" src="../static/javascript/autocomplete.js" defer> </script> */}
      </div>
    </div>





            
  );
}

export default Author;
