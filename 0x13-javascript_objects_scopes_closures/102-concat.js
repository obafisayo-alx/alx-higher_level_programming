#!/usr/bin/node
const fs = require('fs');

// Check if correct number of arguments are passed
if (process.argv.length !== 5) {
  console.error('Usage: node concatFiles.js <file1> <file2> <destination>');
  process.exit(1);
}

// Get file paths from command line arguments
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

const content1 = fs.readFileSync(sourceFile1, 'utf8');
const content2 = fs.readFileSync(sourceFile2, 'utf8');

const concatenatedContent = content1 + content2;

// Write the concatenated content to the destination file
fs.writeFileSync(destinationFile, concatenatedContent);

// console.log(`Files ${sourceFile1} and ${sourceFile2} concatenated to ${destinationFile}.`);
