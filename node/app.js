const express = require('express');
const http = require('http');
const https = require('https');
const url = require('url');
const app = express();
const port = 3000;

app.get('/', (request, response)=>{
    response.send("Connecting...")
});

app.listen(port, () => {
    console.log(`Running on port ${port}`);
});

// http.createServer((request, response)=>{


// }).listen(port);