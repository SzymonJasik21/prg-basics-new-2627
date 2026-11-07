def f(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    i = 0
    while i < len(text):
        if text[i] in vowels:
            vowel_count += 1
        i += 1
    return vowel_count

if __name__ == "__main__":
    print(f("This is a sample text."))