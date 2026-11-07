def f(n):
    result = ""
    for i in range(1, n + 1):
        result += f"1/{i} = {1/i}\n"
    return result.strip()

if __name__ == "__main__":
    print(f(10))