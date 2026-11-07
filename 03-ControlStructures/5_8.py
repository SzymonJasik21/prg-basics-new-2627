def f(action, current_pin, input_pin):
    if action == "check":
        return input_pin == current_pin
    elif action == "change":
        if len(input_pin) == 4 and input_pin.isdigit():
            return input_pin
        return current_pin

if __name__ == "__main__":
    print(f("check", "1111", "1111"))
    print(f("check", "1111", "2222"))
    print(f("change", "1111", "5555"))
    print(f("change", "1111", "12a4"))