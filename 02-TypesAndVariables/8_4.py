def convert_height(cm):
    
    total_inches = round(cm / 2.54)
    
    
    feet = total_inches // 12
    
    
    inches = total_inches % 12
    
    return feet, inches

if __name__ == "__main__":
    cm = 170
    feet, inches = convert_height(cm)
    print(f"I am {cm}cm tall, i.e. {feet} feet and {inches} inches")