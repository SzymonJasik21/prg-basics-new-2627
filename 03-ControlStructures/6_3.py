def f(switch1, switch2):
    bulbs_on = 0
    if switch1:
        bulbs_on += 1
    if switch2:
        bulbs_on += 2
    return bulbs_on

if __name__ == "__main__":
    print(f(False, True))