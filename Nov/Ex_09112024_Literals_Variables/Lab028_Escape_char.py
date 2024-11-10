# ' '  or " " -> difference between single and double quote

# Concept of raw
dir = "C:\Nitesh\n.txt"
# here \ n will create a new line so use r
print(dir)
dir = r"C:\Nitesh\n.txt"
print(dir)  # first delete dir = "C:\Nitesh\n.txt" then run the code
# similar we can use for \t etc
print(r"nitesh\t kumar")
