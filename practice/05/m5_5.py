def plus(x, y):
    return plus_answer
def minus(x, y):
    return minus_answer
def hang(x, y):
    return hang_answer
def divide(x, y):
    return divide_answer
def remainder(x, y):
    return remainder_answer
x = int(input('整数を入力してください：'))
y = int(input('整数を入力してください：'))
plus_answer = x + y
minus_answer = x - y
hang_answer = x * y
divide_answer = x / y
remainder_answer = x % y
print(f'{x}+{y}={plus_answer}')
print(f'{x}-{y}={minus_answer}')
print(f'{x}*{y}={hang_answer}')
print(f'{x}/{y}={divide_answer}')
print(f'{x}%{y}={remainder_answer}')