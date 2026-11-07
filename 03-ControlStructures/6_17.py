def convert_to_12h_format(time_str):
    hours_str, minutes_str = time_str.split(":")
    hours = int(hours_str)
    
    period = "am" if hours < 12 else "pm"
    h_12 = hours % 12
    if h_12 == 0:
        h_12 = 12
        
    return h_12, minutes_str, period

if __name__ == "__main__":
    t24 = "16:32"
    h, m, p = convert_to_12h_format(t24)
    
    print(f"Enter time (24-hour format): {t24}")
    print(f"Time in 12-hour format: {h}:{m}{p}")