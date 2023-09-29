#!/usr/bin/node
//const request = require('request');
//const url = process.argv[2];
//const character_id = '18';

//request(url, function(error, response, body) {
 // if (!error){
    //const results = JSON.parse(body).results;
    //const filteredResult = results.filter((film) => {
      //const {characters} = film;
      //characters.forEach((character) => {
      //  if (character.endsWith('/18/')) return true;
    //  }) 
  //    return false;
//    });
// console.log(filteredResult.length);
 // }
// });
 
const request = require('request');
const url = process.argv[2];
const character_id = '18';

request(url, function(error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    const filteredResult = results.filter((film) => {
      const { characters } = film;
      let characterFound = false; // Initialize a flag
      characters.forEach((character) => {
        if (character.endsWith('/' + character_id + '/')) {
          characterFound = true; // Set the flag to true if the condition is met
        }
      });
      return characterFound; // Return the flag's value
    });
    console.log(filteredResult.length);
  }
});

