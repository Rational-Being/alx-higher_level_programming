#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

const add = function (a, b) {
  return (a + b);
};

console.log(add(firstArg, secondArg));
