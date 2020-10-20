import React from 'react';
import '../App.css';

function AdvancedNav() {
    return (
      <nav className="advancedWrapper">
            <button className="dropbtnA">Advanced Search</button>
            <ul className="dropdown-contentA">
                <li>Article Type</li>
                <li>Author</li>
                <li>Volume & Issue</li>
            </ul>
        </nav>
    )
}

export default AdvancedNav;
