#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (error, response) {
  if (error == null) {
    console.log('code: ' + response.statusCode);
  }
});
