def f(dice):
    max_streak = 1
    current_streak = 1
    best_digit = dice[0]
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_streak = current_streak + 1
            if current_streak > max_streak:
                max_streak = current_streak
                best_digit = dice[i]
        else:
            current_streak = 1
    result = int(best_digit)
    return result


if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("22133"))