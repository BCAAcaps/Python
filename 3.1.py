def div(*args):

    try:
        arg1 = int(input("Введите делимое "))
        arg2 = int(input("Введите делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Неверный делитель! На ноль делить нельзя"

    return res

    '''
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Неверное число! Делитель не может быть равен нулю")
    '''


print(f'Результат:  {div()}')