#!/usr/bin/node

exports.converter = function (base) {
  const convt = function (x) {
    return x.toString(base);
  };

  return convt;
};
