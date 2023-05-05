# TASK 21 WATCH RECOMMENDATION TASK

# (1) Import required modules including using the medium language model.

from pathlib import Path
import sys
import spacy
nlp = spacy.load('en_core_web_md')
from pprint import pprint

# (2) Enter the input data of the latest movie watched.

LATEST_MOVIE = "Planet Hulk: Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
border = "-" * 100

# (3) Create a function to read in the movies.txt file.

def read_from_file():
    file_path = Path(__file__).parent / "movies.txt" # To ensure the path file relative to the current file.
    with open(file_path, 'r') as file:
        return file.readlines()

# (4) Create a function to return which recommends a movie to watch next.

def make_recommendation(latest_movie, movie_lines):
    best = 0
    movie_choice = None
    
    for line in movie_lines:
        tokens = nlp(line)
        latest_movie_tokens = nlp(latest_movie)
        similarity = tokens.similarity(latest_movie_tokens)
        title, _, description = line.partition(" :") # Using .partition to split the string into three components.
        # print(similarity, title) # Test to see the similarity data.
        if similarity > best:
            best = similarity
            movie_choice = title
            # print("BEST SO FAR") # Test to check the movie selection algorithm.
    return movie_choice

# (5) Run the alogorithm to find the recommendation.

try: # Adding defensive programming for FileNotFound error with a system exit.
    movie_lines = read_from_file()
    for each in movie_lines:
        if ":" not in each:
            print("File data does not contain the ':' as expected.")
            sys.exit(1)
except FileNotFoundError:
    print("This file has not been found.")
    sys.exit(1)

movie_choice = make_recommendation(LATEST_MOVIE, movie_lines)

# (6) Deliver recommendation to the user.

print(border)
print(f"The latest movie that you watched was: PLANET HULK")
print(f"\nBased on this viewing, we recommend the following title for you: {movie_choice}")
print(f"\nThis movie has the highest similarity value of all the movies available.")
print(f"\nWe hope you enjoy this recommendation!")
print(border)
