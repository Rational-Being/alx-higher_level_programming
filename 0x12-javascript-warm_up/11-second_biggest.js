#!/usr/bin/node

const arg = process.argv;
const argLength = arg.length;

if (argLength < 4) {
    console.log(0);
} else {
    const second = arg.slice(2).sort((a, b) => a - b).reverse();
    console.log(second[1])
}