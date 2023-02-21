val1 = float(input("enter first value: "))
val2 = float(input("enter second value: "))

print("please select operation")
print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")
op = input("input selection: ")

if op == "1":
    print(val1 + val2)
elif op == "2":
    print(val1 - val2)
elif op == "3":
    print(val1 * val2)
else:
    print(val1 / val2)

