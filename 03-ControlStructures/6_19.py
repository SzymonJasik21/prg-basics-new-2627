def parse_survey(cs_ans, games_ans, insta_ans):
    # Zwraca 3 wartości logiczne True/False
    cs = str(cs_ans).lower() == 'y'
    games = str(games_ans).lower() == 'y'
    insta = str(insta_ans).lower() == 'y'
    return cs, games, insta

if __name__ == "__main__":
    a1, a2, a3 = "y", "n", "y"
    
    print(f"SURVEY Are you interested in computer science? (y/n): {a1}")
    print(f"Do you like playing computer games? (y/n): {a2}")
    print(f"Do you have an Instagram account? (y/n): {a3}\n")
    
    res_cs, res_games, res_insta = parse_survey(a1, a2, a3)
    
    print(f"SURVEY RESULTS Interested in computer science: {'Yes' if res_cs else 'No'}")
    print(f"Playing computer games: {'Yes' if res_games else 'No'}")
    print(f"Has an Instagram account: {'Yes' if res_insta else 'No'}")