#!/usr/bin/node

const lines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
let output = '';

while (i < lines.length) {
  output += lines[i] + '\n';
  i++;
}

console.log(output.trim());
