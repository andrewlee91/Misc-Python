multiplicable = int(input("Enter a number\n"))

# Print top row
top = 0
t = ""
while top <= multiplicable:
    t += "{}\t".format(str(top))
    top += 1
print(t)
# Print the table
i = 1
while i <= multiplicable:
    string = str(i)
    x = 1
    while x <= multiplicable:
        string += "\t{}".format(str(i * x))
        x += 1
    print(string)
    i += 1
