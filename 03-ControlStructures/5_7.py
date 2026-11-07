def f(countdown):
    words = {5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}
    result = ""
    while countdown > 0:
        if countdown in words:
            result += words[countdown] + "\n"
        else:
            result += str(countdown) + "\n"
        countdown -= 1
    result += "Time's up!"
    return result

if __name__ == "__main__":
    print(f(7))