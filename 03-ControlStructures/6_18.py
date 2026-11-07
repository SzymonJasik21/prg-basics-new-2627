def get_quadrant(x, y):
    if x == 0 and y == 0:
        return "origin"
    elif x == 0:
        return "y_axis"
    elif y == 0:
        return "x_axis"
    elif x > 0 and y > 0:
        return "q1"
    elif x < 0 and y > 0:
        return "q2"
    elif x < 0 and y < 0:
        return "q3"
    else:
        return "q4"

if __name__ == "__main__":
    x, y = 5, 2
    loc = get_quadrant(x, y)
    
    print(f"x = {x}")
    print(f"y = {y}")
    
    if loc == "origin":
        print(f"Point P({x},{y}) is located in the position (0,0) of the coordinate system")
    elif loc == "y_axis":
        print(f"Point P({x},{y}) is located on the Y axis")
    elif loc == "x_axis":
        print(f"Point P({x},{y}) is located on the X axis")
    elif loc == "q1":
        print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
    elif loc == "q2":
        print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
    elif loc == "q3":
        print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
    elif loc == "q4":
        print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")