num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))
num3 = int(input("enter another number: "))
num4 = int(input("enter another number: "))

ADD = int(input("enter 1 or 0 for add and take away respectively: "))


if ADD == 1:
    num1 = num1 + num2
    print(num1)
else:
    num1 = num1 - num2
    print(num1)

MULT = int(input("enter 1 or 0 for add and take away respectively: "))

if MULT == "1":
    print(num3 * num4)
else:
    print(num3 / num4)
