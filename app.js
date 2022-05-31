const express = require('express');
const ejs = require("ejs");
const dotenv = require('dotenv');
const bodyParser = require('body-parser');
const {spawn} = require("child_process");
const asyncHandler = require('express-async-handler');


const { response } = require("express");
const app = express();
app.set("view engine", "ejs");
dotenv.config();
const PORT = process.env.PORT || 8080;

app.use(express.json());
app.use(express.static('public'));



app.get("/", function(req, res){
    res.render("home");
});

app.get("/test", function(re1, res){
    const process = spawn('python', ['./python_scripts/main.py']);

    process.stdout.on('data', function(data) {
        console.log(`stdout ${data}`);
        res.send(data.toString());
        // res.redirect("/");
    });
    
    process.stderr.on('data', (data)=>{
        console.log(`stdout ${data}`);
        res.send(data.toString());
        
    });
    
    process.on('close', (code)=>{
        console.log(`child process exited with code ${code}`);
    });
})




app.listen(process.env.PORT || 8080, function(){
    console.log("Server started Successfully.");
});