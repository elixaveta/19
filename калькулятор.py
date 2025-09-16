print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Целочисленное деление")
print("6. Остаток от деления")
print("7. Возведение в степень")
print("8. Сравнение чисел")
print("9. Логические")
print("10. Битовые")

try:
    a = int(input('Введите цифру действия: '))
    if a == 1:
        x = int(input('Введите 1 число: '))
        y = int(input('Введите 2 число: '))
        result = x + y
        print(result)
    elif a == 2:
        x = int(input('Введите 1 число: '))
        y = int(input('Введите 2 число: '))
        result = x - y
        print(result)
    elif a == 3:
        x = int(input('Введите 1 число: '))
        y = int(input('Введите 2 число: '))
        result = x * y
        print(result)
    elif a == 4:
        x = int(input('Введите 1 число: '))
        y = int(input('Введите 2 число: '))
        if x == 0:
            print('На 0 делить нельзя')
        else:
            result = x / y
            print(result)
    elif a == 5:
        x = int(input('Введите 1 число: '))
        y = int(input('Введите 2 число: '))
        if y == 0:
            print('На 0 делить нельзя')
        else:
            result = x // y
            print(result)
    elif a == 6:
        x = int(input('Введите 1 число: '))
        y = int(input('Введите 2 число: '))
        if y == 0:
            print('На 0 делить нельзя')
        else:
            result = x % y
            print(result)
    elif a == 7:
        x = int(input('Введите 1 число: '))
        y = int(input('Введите 2 число: '))
        result = x ** y
        print(result)
    elif a == 8:
     print("Операции: ==, !=, <, >, <=, >=")
     print("Введите 'quit' для выхода")
    
     while True:
        try:
            user_input = input("Введите выражение: ").strip()
            operators = ['==', '!=', '<', '>', '<=', '>=']
            for op in operators:
                if op in user_input:
                    left, right = user_input.split(op, 1)
                    left_val = eval(left.strip())
                    right_val = eval(right.strip())
                    
                    if op == '==':
                        result = left_val == right_val
                    elif op == '!=':
                        result = left_val != right_val
                    elif op == '<':
                        result = left_val < right_val
                    elif op == '>':
                        result = left_val > right_val
                    elif op == '<=':
                        result = left_val <= right_val
                    elif op == '>=':
                        result = left_val >= right_val
                    
                    print(f"{left.strip()} {op} {right.strip()} = {result}")
                    break
            else:
                print("Неизвестная операция. Используйте: ==, !=, <, >, <=, >=")
                
        except:
            print("Ошибка в выражении")
    elif a == 9:
     print("Простой калькулятор: AND, OR, NOT")
    
     while True:
        print("Примеры: True and False, not True")
        expr = input("Введите: ").title()
        if ' And ' in expr:
          a, b = expr.split(' And ')
          result = eval(a.strip()) and eval(b.strip())
          print(f"{expr} = {result}")
                
        elif ' Or ' in expr:
          a, b = expr.split(' Or ')
          result = eval(a.strip()) or eval(b.strip())
          print(f"{expr} = {result}")
                
        elif expr.startswith('Not '):
          value = expr[4:]
          result = not eval(value.strip())
          print(f"{expr} = {result}")
                
        else:
          print("Используйте: and, or, not")
    elif a == 10:
        print("Битовые: &, |, ~, ^, <<, >>")
        while True:
            expr = input("Введите выражение: ").strip().lower()
            if expr.startswith('not ') or expr.startswith('~'):
                parts = expr.split()
                if len(parts) == 2:
                    try:
                        num = int(parts[1])
                        if parts[0] == 'not':
                            result = not num
                            print(f"not {num} = {result}")
                        else:
                            result = ~num
                            print(f"~{num} = {result}")
                        continue
                    except ValueError:
                        pass
            operators = ['and', 'or', 'xor', '&', '|', '^', '<<', '>>']
            for op in operators:
                if op in expr:
                    parts = expr.split(op)
                    if len(parts) == 2:
                        try:
                            a = int(parts[0].strip())
                            b = int(parts[1].strip())
                            
                            if op == 'and':
                                result = a and b
                                print(f"{a} and {b} = {result}")
                            elif op == 'or':
                                result = a or b
                                print(f"{a} or {b} = {result}")
                            elif op == 'xor':
                                result = a ^ b
                                print(f"{a} xor {b} = {result}")
                            elif op == '&':
                                result = a & b
                                print(f"{a} & {b} = {result} (бинарное: {bin(result)})")
                            elif op == '|':
                                result = a | b
                                print(f"{a} | {b} = {result} (бинарное: {bin(result)})")
                            elif op == '^':
                                result = a ^ b
                                print(f"{a} ^ {b} = {result} (бинарное: {bin(result)})")
                            elif op == '<<':
                                result = a << b
                                print(f"{a} << {b} = {result} (бинарное: {bin(result)})")
                            elif op == '>>':
                                result = a >> b
                                print(f"{a} >> {b} = {result} (бинарное: {bin(result)})")
                            
                            break
                        except ValueError:
                            print("Ошибка: введите числа")
                            break
            else:
                print("Неизвестная операция")     
except ValueError:
    print('произошла ошибка')