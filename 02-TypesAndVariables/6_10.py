###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# 1. print number of characters
print('Number of characters: ', len(movie))

# 2. print title in capital letters
print('Uppercase:', movie.upper())

# 3. print title in small letters
print('Lowercase:', movie.lower())

# 4. print how many times the vowel "e" appears in the title
print('Count of "e":', movie.count('e'))

# 5. print where in the text is the word "Lord"
print('Position of "Lord":', movie.find('Lord'))

# 6. print where in the text is the word "dragon"
print('Position of "dragon":', movie.find('dragon'))  # Returns -1 because "dragon" is not there