import spacy

nlp = spacy.load("en_core_web_md")

# Description for movie that user has just watched
planet_hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

# Function takes description of that movie as parameter
def watch_next(description):
    # Convert to nlp to make it easier for the computer to compare
    doc_desc = nlp(description)
    # Initialise empty value for next_movie
    next_movie = None
    try:
        # try opening file in case it doesn't exist
        # Initialise 0 value for highest_similarity which will be updated as we compare each movie to the watched movie
        highest_similarity = 0
        with open("movies.txt", "r") as f:
            # Retrieve each line from movies.txt
            movies = f.readlines()
            for movie in movies:
                # Convert each line into nlp
                movie_nlp = nlp(movie)
                # Record its similarity to watched movie
                similarity = doc_desc.similarity(movie_nlp)
                # If the current similarity is higher than the highest recorded similarity then updated 
                # the highest_similarity value
                if similarity > highest_similarity:
                    highest_similarity = similarity
                    # Store movie with highest similarity in previously defined variable
                    next_movie = movie
        # after looping through movies.txt output to the console the movie that the user should watch next
        print(f"\nYou should watch: \n{next_movie}")
    # if movies.txt does not exist then let the user know.
    except FileNotFoundError:
        print("File does not exist")

watch_next(planet_hulk)