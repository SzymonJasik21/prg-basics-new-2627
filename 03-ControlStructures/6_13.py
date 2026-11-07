def f(car_speed):
    speed_limit_min = 40
    speed_limit_max = 140
    return speed_limit_min <= car_speed <= speed_limit_max

if __name__ == "__main__":
    speed = 38
    if not f(speed):
        print("Warning: invalid car speed!!")