#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const charactersUrls = movie.characters;
    const charactersCount = charactersUrls.length;
    let charactersProcessed = 0;

    charactersUrls.forEach((characterUrl) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const character = JSON.parse(charBody);
          console.log(character.name);

          charactersProcessed++;
          if (charactersProcessed === charactersCount) {
            // All characters have been processed
            process.exit(0);
          }
        }
      });
    });
  }
});
