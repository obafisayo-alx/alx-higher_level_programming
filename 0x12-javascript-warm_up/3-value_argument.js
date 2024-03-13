#!/usr/bin/node

const argsCount = process.argv.length;

if (argsCount === 2) {
  console.log('No argument');
} else if (argsCount === 3) {
  console.log(process.argv[2]);
}
