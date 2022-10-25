import os
from time import sleep


# displays the graph with a border
def printscreen(q1, q2, q3, q4):
    # print("\n" * 6)
    print("* " * 22 + "*")
    for k in range(10):
        print("*", end="")
        for m in q2[k]:
            print(m, end="")
        print("+", end="")
        for m in q1[k]:
            print(m, end="")
        print("*", end="")
        print()
    print("* " + "+ " * 21 + "*")
    for k in range(10):
        print("*", end="")
        for m in q3[k]:
            print(m, end="")
        print("+", end="")
        for m in q4[k]:
            print(m, end="")
        print("*", end="")
        print()
    print("* " * 22 + "*")


# used at the begining to initialize each quadrant with hyphens
def fill(quad):
    for k in range(10):
        quad.append(" - - - - - - - - - - ")
    return quad


# plots a given (x, y) coordinate for a quadrant. Because this is reused, the origin of each quadrant is the
# top-left corner. To gain the correct orientation, the coordinates are flipped later in the call statement.
def replace(quad, xc, yc):
    newrow = " -" * (xc - 1) + " @" + " -" * (10 - xc) + " "
    quad[yc - 1] = newrow
    return quad


if __name__ == "__main__":
    # make this false for quick execution or true to look cool
    animation = True

    # initializes quadrants
    quadrant1 = fill([])
    quadrant2 = fill([])
    quadrant3 = fill([])
    quadrant4 = fill([])

    # prompts user for equation
    print("Accepts an equation in the form y = ax^3 + bx^2 + cx + d. To omit a term, enter a 0 for the coeffecient.")
    a, b, c, d = int(input("a = ")), int(input("b = ")), int(input("c = ")), int(input("d = "))

    # graphs from x = -10 tp x = -1 (left half, quadrants 2 and 3)
    for x in range(-10, 0):
        for y in range(1, 11):
            # if this point makes the function equivalent, it is graphed onto the correct quadrant with orientation
            if y == int(a * x ** 3 + b * x ** 2 + c * x + d):
                quadrant2 = replace(quadrant2, x + 11, 11 - y)
        for y in range(-10, 0):
            if y == int(a * x ** 3 + b * x ** 2 + c * x + d):
                quadrant3 = replace(quadrant3, x + 11, abs(y))
        os.system("cls")
        printscreen(quadrant1, quadrant2, quadrant3, quadrant4)
        if animation:
            sleep(0.1)

    # graphs from x = 1 to x = 10 (right half, quadrants 1 and 4)
    for x in range(1, 11):
        for y in range(1, 11):
            if y == int(a * x ** 3 + b * x ** 2 + c * x + d):
                quadrant1 = replace(quadrant1, x, 11 - y)
        for y in range(-10, 0):
            if y == int(a * x ** 3 + b * x ** 2 + c * x + d):
                quadrant4 = replace(quadrant4, x, abs(y))
        os.system("cls")
        printscreen(quadrant1, quadrant2, quadrant3, quadrant4)
        if animation:
            sleep(0.1)

    # keeps output window open
    input()
