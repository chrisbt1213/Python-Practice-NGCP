try:
    x = 5/0
except ZeroDivisionError:
    print("Error: you cannot divide by zero")
    elements = ['element1','element2','element3','element4']
    try:
        print (elements[4])
    except IndexError:
        print("Success")