def calc(a, b, op):
    return a + b if op == '+' else a - b if op == '-' else a * b if op == '*' else a / b
a = float(input())
b = float(input())
op = input()
print(calc(a, b, op))
