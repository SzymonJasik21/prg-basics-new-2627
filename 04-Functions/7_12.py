def f(n):
    stars_list = ["*"] * n
    result = "/".join(stars_list)
    return result


if __name__ == "__main__":
    print(f(4))
    print(f(1))

def f(n):
    raw_string = "*/" * n
    result = raw_string[:-1]
    return result


if __name__ == "__main__":
    print(f(4))
    print(f(1))

