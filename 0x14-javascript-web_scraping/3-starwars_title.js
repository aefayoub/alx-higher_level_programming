#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
req('https://swapi-api.alx-tools.com/api/films/' + id + '/', function (error, response, body) {
  if (error == null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
