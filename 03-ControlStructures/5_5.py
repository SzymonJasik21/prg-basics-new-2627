def f(numbers):
    total_sum = 0
    count = 0
    for number in numbers:
        if number == 0:
            break
        total_sum += number
        count += 1
    mean = total_sum / count if count else 0
    return total_sum, mean

if __name__ == "__main__":
    print(f([1, 2, 3, 4, 0]))