#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let i = 0;
    for (let search of list) {
        if (search === searchElement) {
            i++;
        }
    }
    return i;
}