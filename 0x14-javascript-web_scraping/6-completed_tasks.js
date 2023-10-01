#!/usr/bin/node
// const request = require('request');
// const URL = process.argv[2];
// const completedTodos = {};

// request(URL, (error, response, body)=> {
// if(!error) {
// let todos = JSON.parse(body);
// for(const todo of todos) {
// const {userId, completed} = todo;
// if(completed) {
// completedTodos[userId] = completedTodos[userId] ? 1 : completedTodos[userId] + 1;
// }
// }
// console.log(completedTodos);
// }
// });
const request = require('request');
const URL = process.argv[2];
const completedTodos = {}; // Initialize as an empty object

request(URL, (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    for (const todo of todos) {
      const { userId, completed } = todo;
      if (completed) {
        // Check if userId exists in completedTodos, if not, initialize it to 0
        if (!completedTodos[userId]) {
          completedTodos[userId] = 0;
        }
        // Increment the count for the userId
        completedTodos[userId]++;
      }
    }
    console.log(completedTodos);
  }
});
