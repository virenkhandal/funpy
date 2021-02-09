const express = require('express')
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

let songs = [];

app.use(cors());

// Configuring body parser middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());


app.get('/song', (req, res) => {
    res.send("here are all the current songs: ")
});


app.post('/song', (req, res) => {
    const song = req.body;

    // Output the book to the console for debugging
    console.log(song);
    songs.push(song);
    res.send('Song is added to the database');
});

app.listen(port, () => console.log(`Hello world app listening on port ${port}!`));