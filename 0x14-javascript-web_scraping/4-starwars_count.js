#!/usr/bin/node
const req = require('request');
let nbr = 0;
req(process.argv[2], function (error, response, body) {
  if (error == null) {
    const json = JSON.parse(body);
    const rslt = json.results;
    for (let i = 0; i < rslt.length; i++) {
      const characters = rslt[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          nbr++;
        }
      }
    }
  }
  console.log(nbr);
});
