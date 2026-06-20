# No 1 -- Your Name, Your Cipher 

full_name = "Ude Ifeoma Domendu"

first_name = full_name.split()[0]
shift = len(first_name)

encrypted = ""

for letter in full_name:
    if letter.isalpha():
        if letter.isupper():
            start = ord("A")
        else:
            start = ord("a")

        new_letter = chr((ord(letter) - start + shift) % 26 + start)
        encrypted += new_letter
    else:
        encrypted += letter

print("Encrypted name:", encrypted)


# Decryption

decrypted = ""

for letter in encrypted:
    if letter.isalpha():
        if letter.isupper():
            start = ord("A")
        else:
            start = ord("a")

        original = chr((ord(letter) - start - shift) % 26 + start)
        decrypted += original
    else:
        decrypted += letter

print("Decrypted name:", decrypted)


# No 3 -- Your Street as a Data Structure 
buildings = [
    ("St. Michael's Church", "Religious", 1972),
    ("Udo Primary School", "Education", 1985),
    ("Duke's Plaza", "Commercial", 2025),
    ("Evergreen Lodge", "Residential", 2018),
    ("Grace Pharmacy", "Health", 2012),
    ("Town Hall", "Government", 1954), 
    ("Greece Lodge", "Residential", 2001),
    ("Joli Supermarket", "Commercial", 2020)
]

oldest = buildings[0]

for building in buildings:
    if building[2] < oldest[2]:
        oldest = building


types = set()

for building in buildings:
    types.add(building[1])


new_buildings = []

for building in buildings:
    if building[2] > 2000:
        new_buildings.append(building)


current_year = 2026
total_age = 0

for building in buildings:
    total_age += current_year - building[2]

average_age = total_age / len(buildings)


print("----- STREET REPORT -----")
print("Oldest Building:", oldest[0], "-", oldest[2])

print("\nBuilding Types:")
for item in types:
    print("-", item)

print("\nBuildings built after 2000:")
for item in new_buildings:
    print("-", item[0], "(", item[2], ")")


print("\nAverage building age:", average_age, "years")


# No 8: The Vowel DNA Test 

name = "Ude Ifeoma Domendu"
mother = "Annestina Domendu"
street = "New Jerusalem Street"

data = name + mother + street

letters_only = ""

for character in data:
    if character != " ":
        letters_only += character.lower()


total_characters = len(letters_only)

unique_letters = set(letters_only)

vowels = "aeiou"
vowel_count = 0

for letter in letters_only:
    if letter in vowels:
        vowel_count += 1

vowel_percentage = (vowel_count / total_characters) * 100


most_repeated = ""
highest_count = 0

for letter in unique_letters:
    count = 0

    for character in letters_only:
        if character == letter:
            count += 1

    if count > highest_count:
        highest_count = count
        most_repeated = letter


contains_all_vowels = True

for vowel in vowels:
    if vowel not in unique_letters:
        contains_all_vowels = False


print("Total characters:", total_characters)
print("Unique letters:", unique_letters)
print("Vowel percentage:", vowel_percentage)
print("Most repeated letter:", most_repeated)
print("Contains all vowels:", contains_all_vowels)


# No 9: Movie Night Negotiator 

my_movies = [
    "Scandal",
    "Blacklist",
    "How to Get Away with Murder",
    "Game of Thrones",
    "Legend of The Seeker",
    "House of Dragons",
    "Diary of a Mad Black Woman",
    "Sistas"
]

friend_one = [
    "Sistas",
    "John Wick",
    "Spider-Man",
    "Avengers",
    "Mr. and Mrs. Smith",
    "Aquaman",
    "Deadpool",
    "Mission Impossible"
]

friend_two = [
    "The Equalizer",
    "Robinhood",
    "Avatar",
    "John Wick",
    "Ex-Men",
    "Fast and Furious",
    "The Maze",
    "The Old Guard"
]


mine = set(my_movies)
first = set(friend_one)
second = set(friend_two)


all_agree = mine & first & second

only_me = mine - first - second


two_people = []

for movie in mine | first | second:
    people = 0

    if movie in mine:
        people += 1

    if movie in first:
        people += 1

    if movie in second:
        people += 1

    if people == 2:
        pair = ""

        if movie in mine and movie in first:
            pair = "You and Friend 1"

        elif movie in mine and movie in second:
            pair = "You and Friend 2"

        else:
            pair = "Friend 1 and Friend 2"

        two_people.append((movie, pair))


ranking = []

for movie in mine | first | second:
    score = 0

    if movie in mine:
        score += 1

    if movie in first:
        score += 1

    if movie in second:
        score += 1

    ranking.append((movie, score))


for i in range(len(ranking)):
    for j in range(i + 1, len(ranking)):
        if ranking[j][1] > ranking[i][1]:
            ranking[i], ranking[j] = ranking[j], ranking[i]


print("Movies all three agree on:", all_agree)

print("\nMovies only you want:")
for movie in only_me:
    print("-", movie)


print("\nMovies liked by exactly two people:")
for movie, pair in two_people:
    print("-", movie, ":", pair)


print("\nBest compromise picks:")
for movie, score in ranking:
    print(movie, "- chosen by", score, "people")
