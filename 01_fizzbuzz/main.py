for i in range(1, 106):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("fizzbuzzjazz")
    elif i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0 and i % 7 == 0:
        print("fizzjazz")
    elif i % 5 == 0 and i % 7 == 0:
        print("buzzjazz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 7 == 0:
        print("jazz")
    else:
        print(i)