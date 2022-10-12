num1,num2 = input().split()
num1 = int(num1)
num2 = int(num2)
if (not bool(num1) and not bool(num2)):
    print("True")
else:
    print("False")