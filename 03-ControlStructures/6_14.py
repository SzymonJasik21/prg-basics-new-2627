def is_good_influencer(fb, tw, ig):
    
    return (fb + tw + ig) >= 2

if __name__ == "__main__":
    facebook = True
    twitter = False
    instagram = True
    
    print(f"facebook = {facebook}")
    print(f"twitter = {twitter}")
    print(f"instagram = {instagram}")
    
    if is_good_influencer(facebook, twitter, instagram):
        print("You are a good influencer!")