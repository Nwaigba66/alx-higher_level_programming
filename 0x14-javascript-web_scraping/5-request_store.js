#!/usr/bin/node
const request = require('request');// import the module request
const fs = require('fs');
const url = process.argv[2]; // captures the first argument URL
const fileName = process.argv[3]; // captures the name of the file that saves the web content

request(url).pipe(fs.createWriteStream(fileName));
