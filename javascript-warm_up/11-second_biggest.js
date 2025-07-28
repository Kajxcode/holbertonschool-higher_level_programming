#!/usr/bin/node

const args = proccess.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const uniqueArgs = [...new Set(args)];
  if (unqiueArgs.length <= 1) {
    console.log(0);
  } else {
    unqiueArgs.sort((a, b) => b - a);
    console.log(uniqueArgs[1]);
  }
}
