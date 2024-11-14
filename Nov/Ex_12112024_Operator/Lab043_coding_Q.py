# write a program to calculate the area of a circle given its radius using the formula
# area= pi*r^2 take pi = 3.14
# note for power we can use - pow or **
radius = float(input("Enter the radius of circle\n"))
print(radius)
area = 3.14*(radius**2)
# print("area of circle is" , area)  -- we can write like this also
print(f"area of circle is ((Area)): {area}") # -- we can write like this also


#write same code in 1 line
print(3.14* (float(input("Enter the radius of circle\n")) **2 ))