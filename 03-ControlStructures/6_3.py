def f(light_switch1, light_switch2):
    bulbs_on = 0
    if light_switch1:
        bulbs_on += 1
    if light_switch2:
        bulbs_on += 2
    return bulbs_on

if __name__ == "__main__":
    print(f(False, False))
    print(f(True, False))
    print(f(False, True))
    print(f(True, True))