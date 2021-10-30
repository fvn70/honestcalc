import re

def is_num(x):
    return re.match(r'\d+\.?\d*', x)


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

memory = 0.0
exit_main = False

while not exit_main:
    calc = input(msg_0+'\n')
    x, oper, y = calc.split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    if not oper in "+-*/":
        print(msg_2)
        continue
    elif oper == '+':
        result = x + y
        # break
    elif oper == '-':
        result = x - y
        # break
    elif oper == '*':
        result = x * y
        # break
    elif oper == '/' and y != 0:
        result = x / y
        # break
    else:
        print(msg_3)
        continue

    print(result)

    while True:
        answer = input(msg_4+'\n')
        if answer == 'y':
            memory = result
            break
        if answer == 'n':
            break

    exit_calc = False
    while not exit_calc:
        answer = input(msg_5+'\n')
        if answer == 'y':
            exit_calc = True
            exit_main = False
        if answer == 'n':
            exit_calc = True
            exit_main = True

