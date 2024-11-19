# Synytax
# if condition 1:
#    print ("do 1")
# elif condition 2:
#    print ("do 2")
# elif condition 3:
#    print ("do 3")
# else :
#    print ("do for else")


num1 = float(input("Enter number 1\n"))  # 5, 12
num2 = float(input("Enter number 2\n"))  # 3, 12
num3 = float(input("Enter number 3\n"))  # 2, 11

# num1> num2 and num1 > num3 ---> num1
# num2> num1 and num2 > num3 ---> num2

if num1 > num2 and num1 > num3:
    print("Max is", num1)
elif num2 > num1 and num2 > num3:
    print("Max is", num2)
else:
    print("max is ", num3)
