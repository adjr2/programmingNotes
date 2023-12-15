const http = require('http');

const requestListener = function (req, res) {
  res.writeHead(200);
  res.end('Hello, World!');
}

const port = 5050;
const server = http.createServer(requestListener);
console.log('server listening on port: ' + port);
