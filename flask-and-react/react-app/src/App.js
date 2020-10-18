import React, {useState, useEffect} from 'react';
import './App.css';

function App() {
  // const [initialData, setInitialData] = useState([{}]) // setting the initial state of the component to an empty object

  // useEffect(() =>{
  //   fetch("/api").then(
  //     response => response.json()
  //   ).then(data => setInitialData(data))
  // }, []);
  return (
    <div className="App">
      <p>Test</p>
      <p>My Token = {window.token}</p>

      {/* <h1>{initialData.title}</h1> */}
    </div>
  );
}

export default App;
