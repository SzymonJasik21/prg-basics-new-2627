def f(plain_text):
    encrypted_text = ""
    for char in plain_text:
        code = ord(char) + 1
        encrypted_text += chr(code)
    return encrypted_text

if __name__ == "__main__":
    print(f("The early bird catches the worm"))