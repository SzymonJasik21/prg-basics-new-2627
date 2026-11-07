def f(entered_login, entered_password):
    if entered_login == 'joe' and entered_password == 'abcd':
        return 'You are logged in'
    else:
        return 'Incorrect login or password!!'

if __name__ == "__main__":
    print(f('joe', 'abcd'))
    print(f('joe', '1234'))
    print(f('ann', 'abcd'))