###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"

abbreviation = "".join([word[0].upper() for word in university.split() if word.lower() != "of"])

print(f"i.e. {abbreviation}")