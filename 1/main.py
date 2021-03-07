def plus(operands):
    pass


if __name__ == '__main__':
    while True:
        command = input("Input operator: ")
        if command == 'exit':
            exit(0)

        operands = input("Input two operands: ")
        operands = list(map(int, operands.split(' ')))

        if command == '+':
            plus(operands)

