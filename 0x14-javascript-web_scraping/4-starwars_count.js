#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request
  .get(url + id).on('response', function(error, response, body) {
  console.log(error || JSON.parse(body).number);
  });
