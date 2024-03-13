#!/usr/bin/node
const len = process.argv[2];
if (len === undefined) {
  console.log('Missing number of occurrences');
}
for (let index = 0; index < len; index++) {
  console.log('C is fun');
}
