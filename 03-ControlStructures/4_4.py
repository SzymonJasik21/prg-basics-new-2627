def f(text):
    result = ""
    for char in text:
        result = result + char + " "
    return result.strip()

if __name__ == "__main__":
    print(f("Krakow University of Economics"))