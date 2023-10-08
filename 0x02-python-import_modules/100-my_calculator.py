#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]

    def add_fun():
        return add(num1, num2)

    def sub_fun():
        return sub(num1, num2)

    def mul_fun():
        return mul(num1, num2)

    def div_fun():
        return div(num1, num2)

    operators = {"+": add_fun, "-": sub_fun, "*": mul_fun, "/": div_fun}

    if op not in operators:
        print("Unknown operator, Available operators: +, -, * and /")
        exit(1)

    output = operators[op]()

    print("{:d} {} {:d} = {:d}".format(num1, op, num2, output))
