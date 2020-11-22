import React, { Component, PropTypes } from 'react'
import '../App.css';
import shakerLogo from '../images/shaker-manifesto-logo2.PNG';
import hamiltonLogo from '../images/hamilton-lib-logo.PNG';


class VolumeIssue extends Component {
    constructor(props){
        super(props)
        this.state = {
            url: ""
        };
    }  
  
    changeURL = (e) => {
      console.log(e)
      console.log(e.target.value)
      // console.log(this.state.checkbox.checked)
      var newSearch = "/VolumeIssueResults/" + e.target.value;

      this.setState({url: newSearch})
  }
    // const [pageNum, changePage] = useState(() =>{
    //     return 2
    // })

  //   function handleSubmit(e) {
  //     console.log(window.location.href)
  //     console.log(this.action)
  //     console.log(this.issue.value)
  //     window.location.href = this.action + this.issue.value.slice(-7); 
  //     return false;
  //     // console.log(pageNum)
  //     // changePage(pageNum => pageNum + 1)
  //     // console.log(pageNum)
  // }

    // function submitForm() {
    //   var ext = document.getElementById('issue');
    //   var selected_opt = ext.options[ext.selectedIndex].value;

    //     // Add own code to handle "All" here

    //     var domain = document.getElementById('my');
    //     // Append selected option
    //     domain.value = domain.value + selected_opt;

    //     // Submit form
    //     document.getElementById('myform').submit();
    // }



  render(){
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
              <li className="nav-item">
                <a href="/Author" className="nav-link">Author</a>
              </li>
              <li id="current">
                <a href="/VolumeIssue" className="nav-link">Volume & Issue</a>
              </li>
            </ul>
          </div>
      </nav>
    <br/><br/> <br/>
    <br/><br/> 
    
    <div className="container">
    <img src={shakerLogo} alt="Shaker logo"width="600" height="150" className = "ShakerLogo"/>
    <br/><br/> <br/>
    <div className = "volumeAndIssue">
      <h1>Browse by volume and issue:</h1> <br/>
      </div>
      <form action={this.state.url} method="GET" id="myform"> {/* onSubmit={handleSubmit}> */}
        {/* <button className="article-link" type="submit" name="article" value= {item[0]}></button> */}
      <div className = "volumeAndIssue">
        <h3>Volume 1 (1871)</h3>
        </div>
      <h4>Issue:&ensp; 
        <button type="submit" value="0101000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="0102000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="0103000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="0104000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="0105000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="0106000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="0107000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="0108000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="0109000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="0110000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="0111000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="0112000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 2 (1872)</h3> 
    </div>
    <h4>Issue:&ensp; 
        <button type="submit" value="0201000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="0202000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="0203000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="0204000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="0205000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="0206000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="0207000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="0208000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="0209000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="0210000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="0211000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="0212000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 3 (1872)</h3> 
    </div>
    <h4>Issue:&ensp; 
        <button type="submit" value="0301000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="0302000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="0303000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="0304000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="0305000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="0306000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="0307000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="0308000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="0309000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="0310000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="0311000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="0312000" name = "issue" onClick={this.changeURL}>Extra</button> </h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 4 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="0401000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="0402000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="0403000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="0404000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="0405000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="0406000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="0407000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="0408000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="0409000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="0410000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="0411000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="0412000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 5 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="0501000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="0502000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="0503000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="0504000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="0505000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="0506000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="0507000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="0508000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="0509000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="0510000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="0511000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="0512000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 6 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="0601000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="0602000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="0603000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="0604000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="0605000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="0606000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="0607000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="0608000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="0609000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="0610000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="0611000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="0612000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 7 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="0701000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="0702000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="0703000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="0704000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="0705000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="0706000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="0707000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="0708000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="0709000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="0710000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="0711000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="0712000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 8 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="0801000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="0802000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="0803000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="0804000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="0805000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="0806000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="0807000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="0808000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="0809000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="0810000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="0711000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="0712000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 9 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="0901000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="0902000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="0903000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="0904000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="0905000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="0906000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="0907000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="0908000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="0909000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="0910000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="0911000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="0912000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 10 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="1001000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="1002000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="1003000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="1004000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="1005000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="1006000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="1007000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="1008000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="1009000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="1010000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="1011000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="1012000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 11 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="1101000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="1102000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="1103000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="1104000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="1105000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="1106000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="1107000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="1108000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="1109000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="1110000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="1111000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="1112000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 12 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="1201000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="1202000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="1203000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="1204000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="1205000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="1206000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="1207000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="1208000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="1209000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="1210000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="1211000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="1212000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 13 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="1301000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="1302000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="1303000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="1304000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="1305000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="1306000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="1307000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="1308000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="1309000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="1310000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="1311000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="1312000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 14 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="1401000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="1402000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="1403000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="1404000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="1405000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="1406000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="1407000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="1408000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="1409000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="1410000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="1411000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="1412000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 15 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="1501000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="1502000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="1503000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="1504000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="1505000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="1506000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="1507000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="1508000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="1509000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="1510000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="1511000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="1512000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 16 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="1601000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="1602000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="1603000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="1604000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="1605000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="1606000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="1607000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="1608000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="1609000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="1610000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="1611000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="1612000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 17 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="1701000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="1702000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="1703000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="1704000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="1705000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="1706000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="1707000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="1708000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="1709000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="1710000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="1711000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="1712000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 18 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="1801000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="1802000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="1803000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="1804000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="1805000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="1806000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="1807000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="1808000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="1809000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="1810000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="1811000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="1812000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 19 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="1901000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="1902000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="1903000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="1904000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="1905000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="1906000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="1907000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="1908000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="1909000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="1910000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="1911000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="1912000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 20 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="2001000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="2002000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="2003000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="2004000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="2005000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="2006000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="2007000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="2008000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="2009000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="2010000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="2011000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="2012000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 21 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="2101000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="2102000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="2103000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="2104000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="2105000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="2106000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="2107000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="2108000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="2109000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="2110000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="2111000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="2112000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 22 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="2201000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="2202000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="2203000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="2204000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="2205000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="2206000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="2207000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="2208000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="2209000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="2210000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="2211000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="2212000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 23 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="2301000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="2302000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="2303000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="2304000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="2305000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="2306000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="2307000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="2308000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="2309000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="2310000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="2311000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="2312000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 24 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="2401000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="2402000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="2403000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="2404000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="2405000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="2406000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="2407000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="2408000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="2409000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="2410000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="2411000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="2412000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 25 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="2501000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="2502000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="2503000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="2504000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="2505000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="2506000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="2507000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="2508000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="2509000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="2510000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="2511000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="2512000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 26 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="2601000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="2602000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="2603000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="2604000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="2605000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="2606000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="2607000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="2608000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="2609000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="2610000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="2611000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="2612000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 27 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="2701000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="2702000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="2703000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="2704000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="2705000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="2706000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="2707000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="2708000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="2709000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="2710000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="2711000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="2712000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 28 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="2801000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="2802000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="2803000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="2804000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="2805000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="2806000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="2807000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="2808000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="2809000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="2810000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="2811000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="2812000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    <div className = "volumeAndIssue"> 
      <h3>Volume 29 (1872)</h3> 
    </div> 
    <h4>Issue:&ensp; 
        <button type="submit" value="2901000" name = "issue" onClick={this.changeURL}>1</button>
        <button type="submit" value="2902000" name = "issue" onClick={this.changeURL}>2</button>
        <button type="submit" value="2903000" name = "issue" onClick={this.changeURL}>3</button>
        <button type="submit" value="2904000" name = "issue" onClick={this.changeURL}>4</button>
        <button type="submit" value="2905000" name = "issue" onClick={this.changeURL}>5</button>
        <button type="submit" value="2906000" name = "issue" onClick={this.changeURL}>6</button>
        <button type="submit" value="2907000" name = "issue" onClick={this.changeURL}>7</button>
        <button type="submit" value="2908000" name = "issue" onClick={this.changeURL}>8</button>
        <button type="submit" value="2909000" name = "issue" onClick={this.changeURL}>9</button>
        <button type="submit" value="2910000" name = "issue" onClick={this.changeURL}>10</button>
        <button type="submit" value="2911000" name = "issue" onClick={this.changeURL}>11</button>
        <button type="submit" value="2912000" name = "issue" onClick={this.changeURL}>12</button></h4> <br/>
    </form>
    </div>
  </div>
  );
}
}

export default VolumeIssue;
