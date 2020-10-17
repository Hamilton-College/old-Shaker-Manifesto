import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
// this is the file that loads the landing page

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );

ReactDOM.render(<App/>, document.getElementById('root')); 
// rendering the App component into the element with id root
// essentially inserting the app component into id root


