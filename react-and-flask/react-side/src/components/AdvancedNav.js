import React from 'react';
import '../App.css';

function AdvancedNav() {
    return (
    // <div className ="container">
    <div className="advancedWrapper">
        <div className="dropdownA">
          <button className="dropbtnA">Advanced Search</button>
          <div className="dropdown-contentA">
            <a href="ArticleType">Article Type</a>
            <a href="Author">Author</a>
            <a href="VolumeIssue">Volume & Issue</a>
          </div>
        </div>
    </div>
    // </div>
    )
}

export default AdvancedNav;