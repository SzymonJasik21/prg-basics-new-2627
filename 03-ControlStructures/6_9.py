def f(name):
    return name.lower().endswith("a")

if __name__ == "__main__":
    name = "Anna"
    if f(name):
        print(f"{name} -- Polish female name")