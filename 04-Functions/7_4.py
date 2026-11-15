def f(text, letter):
    result = text.count(letter)
    return result


if __name__ == "__main__":
    sample_text = "You never get a second chance to make a first impression"
    print(f(sample_text, "e"))


def f(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count = count + 1
    return count


if __name__ == "__main__":
    sample_text = "You never get a second chance to make a first impression"
    print(f(sample_text, "e"))