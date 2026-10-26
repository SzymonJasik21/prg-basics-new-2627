def check_test_passed(tasks_ok):
    total_tasks = 20
    test_passed = False
    if tasks_ok >= total_tasks / 2:
        test_passed = True 
    return test_passed 

if __name__ == "__main__":

    test_attempts = [10, 15, 20, 5, 0]

    for tasks_ok in test_attempts:
        print(f"Correctly completed tasks: {tasks_ok}")

        is_passed = check_test_passed(tasks_ok)

        if is_passed:
            print("Congratulations! You passed the test.")
        else:
            print("Unfortunately, you did not pass the test.")
        