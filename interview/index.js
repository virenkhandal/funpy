const http = require('http');
const url = require('url');
const https = require('https');
const port = 3000;
const express = require('express');
const app = express()


var pet1 = {name: "Dog", photoUrls: "", status:"available", id:1};
var pet2 = {name: "Cat", photoUrls: "", status:"pending", id:2};
var pet3 = {name: "Fish", photoUrls: "", status:"available", id:3};

const pets = [pet1, pet2, pet3];

app.get('/', (request, response)=>{
    response.send("connecting...")
    // console.log(pet1['name']);
});

app.get('/pet/findByStatus', (request, response)=>{
    response.setHeader('Content-Type', 'application/json');
    var str = JSON.stringify(request.query['status']);
    var strqueries = str.substring(1, str.length - 1).split(',');
    console.log(strqueries);
    var i = 0;
    var correct = []
    for (stat of strqueries){
        // console.log(stat);
        for (pet of pets) {
            if (pet['status'] === stat){
                correct.push(pet);
                console.log(pet);
            }
        }
    }
    response.send(correct);
    // for (pet of pets) {
    //     if (pet['status'] === request.query['status']){
    //         correct.push(pet);
    //     }
        
    // }
    // response.send(correct);
});

app.get('/pet/:id', (request, response)=>{
    response.setHeader('Content-Type', 'application/json');
    // console.log(request.params);
    for (pet of pets){
        // console.log(pet['name']);
        if (pet['id'] == request.params['id']){
            // check if id matches query
            response.send(pet);
            response.end()
        }
    }
    // response.send("No pet with that id found.");
});

app.listen(port, ()=>console.log("server up and running"));


