#!/usr/bin/node
const file_path = process.argv[2];

import fs from "fs"
fs.readFile(file_path, 'utf-8', (err, data) => {
  if(err) {
    console.error(err);
  } else {
    console.log(data)
  }
});
