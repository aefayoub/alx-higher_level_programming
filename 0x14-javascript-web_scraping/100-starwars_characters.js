#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

req(url, function (error, response, body) {
  if (error == null) {
    const reslt = JSON.parse(body);
    const charac = reslt.characters;
    for (let i = 0; i < charac.length; i++) {
      req(charac[i], function (error, response, body) {
        if (error == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
