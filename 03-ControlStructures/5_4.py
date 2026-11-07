def f(user_guess, number_to_guess):
    if user_guess < number_to_guess:
        return "Too low! Try again."
    elif user_guess > number_to_guess:
        return "Too high! Try again."
    else:
        return "Congratulations! You guessed the correct number."

if __name__ == "__main__":
    print(f(20, 50))
    print(f(80, 50))
    print(f(50, 50))