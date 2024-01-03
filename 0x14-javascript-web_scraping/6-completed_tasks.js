#!/usr/bin/node
const req = require('request');
let nbr = 0;
req(process.argv[2], function (error, response, body) {
  if (error == null) {
    const reslt = {};
    const json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (reslt[json[i].userId] == undefined) {
	  reslt[json[i].userId] = 0;
	}
	reslt[json[i].userId]++;
      }
    }
    console.log(reslt);
  }
});
