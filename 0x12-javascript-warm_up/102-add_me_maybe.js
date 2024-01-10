#!/usr/bin/node

exports.addMeMaybe = function (num, fun) {
  fun(++num);
};
