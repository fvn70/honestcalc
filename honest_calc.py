import re

def is_num(x):
    return re.match(r'-?\d+\.?\d*', x)

def is_one_digit(v):
    try:
        n = int(v)
        return abs(v) < 10 and v % n == 0
    except:
        return False

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and v3 in "*-+":
        msg += msg_8
    if msg != "":
        print(msg_9 + msg)


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msgs = [msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
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
    check(x, y, oper)
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

    exit_store = False
    while not exit_store:  # store result
        answer = input(msg_4+'\n')
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    answer = input(f"{msgs[msg_index - 1]}\n")
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue 
                        else:
                            memory = result
                            exit_store = True
                            break  # 91 -> 96 -> 101
                    elif answer == 'n':
                        break  # 91 -> 96 -> 101

            else:
                memory = result
                exit_store = True
                break  # 104

        else:
            memory = result
            exit_store = True
            continue  # 74

        if answer == 'n':
            break  # 104

    exit_calc = False
    while not exit_calc:
        answer = input(msg_5+'\n')
        if answer == 'y':
            exit_calc = True
            exit_main = False
        if answer == 'n':
            exit_calc = True
            exit_main = True

