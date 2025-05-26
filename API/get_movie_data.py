import requests
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

# Calling the function
configure()

# Function to get the list of movies
def get_movie(movie):
    # API URL for the TMDB (The movies database)
    TMDB_URL = "https://api.themoviedb.org/3/search/movie"
            
    # Making the request to TMDB
    response = requests.get(url=TMDB_URL, params={"api_key": os.getenv('api_key'), "query": movie})
    # Checking for error
    if response.status_code != 200:
        return f"<h2>{response.status_code} Error</h2>"
    
    data = response.json()["results"] # Json data
    return data