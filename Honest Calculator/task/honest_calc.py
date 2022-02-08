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

    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/' and y != 0:
        result = x / y
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

    while True:
        answer = input(msg_5+'\n')
        if answer == 'y':
            break
        if answer == 'n':
            exit_main = True
            break
