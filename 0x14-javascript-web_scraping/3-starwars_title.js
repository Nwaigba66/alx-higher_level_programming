#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request(url + id, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
