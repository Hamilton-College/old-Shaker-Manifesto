import React, {useState, useEffect} from 'react';
import './App.css';
import { Link } from 'react-router-dom';

function App() {
  const [initialData, setInitialData] = useState([{}]) // setting the initial state of the component to an empty object

  useEffect(() =>{
    fetch("/basicSearch").then(
      response => response.json()
    ).then(data => setInitialData(data))
  }, []);
  return (
    <div className="App">
      <p>Test</p>
      <h1>{initialData.title}</h1>
    </div>
  );
}

export default App;
