my_test = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
if len(my_test) % 2 == 0:
    i = 0
    while i < len(my_test):
        el = my_test[i]
        my_test[i] = my_test[i+1]
        my_test[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_test) - 1:
        el = my_test[i]
        my_test[i] = my_test[i + 1]
        my_test[i + 1] = el
        i += 2
print(my_test)
