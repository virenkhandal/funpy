const http = require('http');
const https = require('https');

http.createServer((request, response)=> {
    console.log('server running on port 3000');
    https.get("https://httpbin.org/get", (res) => {
        let data = '';
        res.on('data', (chunk) => {
            data += chunk;
        });

        res.on('end', () => {
            // console.log(data);
            response.statusCode = 200;
            response.setHeader('Content-Type', 'application/json');
            response.write(data);
            console.log("response written on server");
            response.end()
        });
    })
    .on('error', (error) => {
        console.log(error);
    });

}).listen(3000);