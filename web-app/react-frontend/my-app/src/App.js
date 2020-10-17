import React, { useState, useEffect } from 'react';
import './App.css';
import Axios from "axios" // axios allows us to make get and post requests to our own API

function App() {

  const [query, setQuery] = useState(""); // the state of the input starts out empty 

  useEffect(() =>{
    Axios.get("http://localhost:3001/basicSearch").then((response) => {
      console.log(response.data);
    })
  }, []);    
  const submitSearch = () => {
    Axios.post("http://localhost:3001/basicSearch", {query: query}); // right is the one here, left goes to backend
  }

  return (
    <div className="Container">
      <h1>Shaker Manifesto</h1>

      <div className="searchBar">
        <label>Search Word:</label>
        <input 
          type="text" 
          name="query" 
          onChange={(e) =>{
            setQuery(e.target.value) // we're changing the state to be whatever is entered 
          }}/>

        <button onClick={submitSearch}>Submit</button>
      </div>
    </div>
    // <div className="searchBar">
    // <form action= "#" method="POST" autocomplete=off >
    //     <input id="MySearchTerm" type="text" name="query" onkeydown="AutoComplete()">
    //     <input type="submit" value="search" class="searchButton">
    // </form>
    // <script type="text/javascript" src="../static/javascript/AutoComplete.js" defer> </script>
    // </div>
  );
}

export default App;
