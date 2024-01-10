#!/usr/bin/node

exports.callMeMoby = function (num, fun) {
    for (let i = 0; i < num; i++) {
        fun();
    }
};
