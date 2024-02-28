#!/usr/bin/node

const request = require('request');
const count = {};

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        if (count[data[i].userId] === undefined) {
          count[data[i].userId] = 0;
        }
        count[data[i].userId]++;
      }
    }
    console.log(count);
  }
});
