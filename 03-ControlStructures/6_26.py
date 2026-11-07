def f(pin):
    return pin == "0805"

if __name__ == "__main__":
    attempts = ["2398", "0912", "7860"]
    correct = False
    for pin in attempts:
        print(f"Enter the PIN code: {pin}")
        if f(pin):
            correct = True
            break
        print("Incorrect...")

    if not correct:
        print("Sorry, your payment card has been blocked.")