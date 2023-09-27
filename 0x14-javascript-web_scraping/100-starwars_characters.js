#!/usr/bin/node

const request = require('request');

const argc = process.argv.length;
const argv = process.argv;

if (argc < 3) {
  console.log('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit();
}
// Grab the movie id
const movieId = argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(url, (_error, _response, body) => {
  const film = JSON.parse(body);

  for (const characterURL of film.characters) {
    request(characterURL, (_error, _response, body) => {
      const characterName = JSON.parse(body).name;
      console.log(characterName);
    });
  }
});
