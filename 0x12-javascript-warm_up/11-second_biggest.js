#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const nums = args.map(arg => parseInt(arg));
  const sortedNums = nums.sort((a, b) => b - a);
  console.log(sortedNums[1]);
}
