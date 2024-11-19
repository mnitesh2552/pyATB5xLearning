# Grade calculator
# 90 - 100 A
# 80-89    B
# 70 -79   C
# 60-69    D
# 0-59     F
score = int(input("Enter your score\n"))
# if score >=90 and score <=100  --> "A"
if score >= 90 and score <= 100:
    print("your grade is", "A")
elif score >= 80 and score <= 89:
    print("your grade is", "B")
elif score >= 70 and score <= 79:
    print("your grade is", "C")
elif score >= 60 and score <= 69:
    print("your grade is", "D")
elif score >100:
    print("you are Batman")
else:
    print("your grade is", "F")
