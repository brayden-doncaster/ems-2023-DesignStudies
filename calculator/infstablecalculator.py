val1 = int(3)
val2 = int(3)

def get_input():
    global val1
    global val2
    val1 = input("enter first value: ")

    try:
        val1 = float(val1)
    except:
        print("you can only use intigers")
    else:
        pass

    val2 = input("input second value: ")

    try:
        val2 - float(val1)
    except:
        print("you can only use intigers")
    else:
        pass

def get_op():

    print("1 - addition")
    print("2 - subtraction")
    print("3 - multiplication")
    print("4 - division")

    global op = input("please select operation: ")

def math():
    if op = 1:
        val1 



