def plus(operands):
    print("{op1} + {op2} = {res}".format(
        op1=operands[0],
        op2=operands[1],
        res=operands[0] + operands[1]))


def minus(operands):
    print("{op1} - {op2} = {res}".format(
        op1=operands[0],
        op2=operands[1],
        res=operands[0] - operands[1]))


def mult(operands):
    print("{op1} * {op2} = {res}".format(
        op1=operands[0],
        op2=operands[1],
        res=operands[0] * operands[1]))


if __name__ == '__main__':
    while True:
        command = input("Input operator: ")
        if command == 'exit':
            exit(0)

        operands = input("Input two operands: ")
        operands = list(map(int, operands.split(' ')))

        if command == '+':
            plus(operands)
        elif command == '-':
            minus(operands)
        elif command == "*":
            mult(operands)
