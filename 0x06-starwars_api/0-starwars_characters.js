#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, async (error, response, body) => {
  error && console.log(error);

  const movies = (JSON.parse(response.body).characters);

  for (const movie of movies) {
    await new Promise((resolve, reject) => {
      request(movie, (error, response, body) => {
        error && console.log(error);

        console.log(JSON.parse(response.body).name);
        resolve();
      });
    });
  }
});
