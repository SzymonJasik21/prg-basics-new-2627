import math

def calculate_circle(r):
    # calculate area using math.pi and round to 2 decimal places
    area = round(math.pi * (r ** 2), 2)
    
    # calculate circumference using math.pi and round to 2 decimal places
    circumference = round(2 * math.pi * r, 2)
    
    # return results
    return circumference, area

if __name__ == "__main__":
    circumference1, area1 = calculate_circle(1)
    print(f"r = 1 --> circumference = {circumference1}, area = {area1}")
    
    circumference2, area2 = calculate_circle(3)
    print(f"r = 3 --> circumference = {circumference2}, area = {area2}")