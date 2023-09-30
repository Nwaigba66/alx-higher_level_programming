#!/usr/bin/node
const request = require('request');// import the module request
const fs = require('fs');
const url = process.argv[2]; // captures the first argument URL
const fileName = process.argv[3]; // captures the name of the file that saves the web content
let dataStream = '';

request
.get(url)
.on('data', (data)=> {
dataStream += data;

//fs.createWriteStream(.toString()); // writes the data and save to a file only
// console.log(data.toString()); // prints the data and converts to a string
})
.on('end', ()=> {
fs.writeFileSync(fileName, dataStream, 'utf-8')
})
