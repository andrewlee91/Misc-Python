while True:
    text = input("Enter 3 sides of a triangle (Q to quit)\n")

    if text.lower() == "q":
        break

    sides = text.split(" ")
    sides.sort()

    a = int(sides[0])
    b = int(sides[1])
    c = int(sides[2])

    if (a * a) + (b * b) == c * c:
        print("This is a Pythagorean triple")
    else:
        print("This is not a Pythagorean triple")
