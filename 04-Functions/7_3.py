def month(n):
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    result = months[n - 1]
    return result


if __name__ == "__main__":
    print(month(7))
    print(month(9))


def month(n):
    months = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    result = months[n]
    return result


if __name__ == "__main__":
    print(month(7))
    print(month(9))