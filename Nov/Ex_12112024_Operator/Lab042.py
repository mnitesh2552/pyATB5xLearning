# If ur age is greater then 18 - allowed to vote else not
user_age = int(input("Enter your age\n"))
if user_age > 18:
    print("Yes allowed to vote")
else:
    print("No, you cant vote")

# Write same program with ternary operator
print("Yes allowed to vote" if user_age > 18 else "No, you cant vote")
# or
# print("Yes allowed to vote" if int(input("Enter your age\n")) > 18 else "No, you cant vote")