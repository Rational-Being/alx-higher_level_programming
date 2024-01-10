#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (const search of list) {
    if (search === searchElement) {
      i++;
    }
  }
  return i;
};
