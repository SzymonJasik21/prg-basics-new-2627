def f(detector):
    people_in_room = 0
    at_least_three = False
    for sign in detector:
        if sign == "+":
            people_in_room = people_in_room + 1
        elif sign == "-":
            people_in_room = people_in_room - 1
        if people_in_room >= 3:
            at_least_three = True
    return at_least_three


if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))