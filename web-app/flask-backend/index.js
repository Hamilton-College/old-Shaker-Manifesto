const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const app = express();
const mysql = require("mysql");

const db = mysql.createConnection({ // use createPool for multiple queries
    host: "localhost",
    user: "root",
    password: "root",
    database: "shaker"
});

db.connect((err) => {
    if (err) throw err;
    console.log('Connected!');
});

db.query('SELECT * FROM authors', (err) => {
    if(err) throw err;
  
    console.log('Data received from Db:');
    // console.log(rows);
  });

app.use(cors());
app.use(express.json()); // allows us to get the frontend value as a json object. Always needed
app.use(bodyParser.urlencoded({extended: true})); // you're always going to need this when querying

app.get("/", (req, res) => { // req is required, get info from frontend, res is response that we're sending to the frontend
    // const sqlInsert = "INSERT INTO "
    // db.query() // edit this section
    res.send("hello, Peter");
});

// app.get("/basicSearch", (req, res) => { // req is required, get info from frontend, res is response that we're sending to the frontend

app.post("/basicSearch", (req, res) => { // req is required, get info from frontend, res is response that we're sending to the frontend

    const searchWord = req.body.query; // we have to request the info from frontend
    const sqlFetch = "SELECT id, regauthor FROM authors WHERE regauthor LIKE '%" + searchWord + "%' order by regauthor"; //
    db.query(sqlFetch, [searchWord], (err, result) => {
        console.log(err);
        console.log(result);
        console.log(sqlFetch)
        console.log(searchWord)
        // res.redirect("http://localhost:3001/basicResults")


    }); // the "query" is whatever the user entered on front end
});


app.listen(3001, () =>{
    console.log("running on port 3001");
});