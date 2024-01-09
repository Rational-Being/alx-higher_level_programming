#!/usr/bin/node

exports.converter = function (base) {
    let convt = function (x) {
        return x.toString(base);
    };

    return convt;
}