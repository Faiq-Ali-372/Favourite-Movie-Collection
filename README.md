# My Movie Collection Web App

This is a simple web application built with Flask that allows users to manage their favorite movies. Users can add, edit, and delete movies from their collection.

## Features

- Add new movies to your collection
- Edit existing movie details such as rating and review
- Delete movies from your collection
- View a list of all your favorite movies

## Installation

1. Getting the API Key:
Register yourself at <https://www.themoviedb.org/> and copy the API key. In the `API` Folder of project directory, create a file named .env and paste
your API key like this `api_key=Your API key`

2. Clone the repository:
Open the terminal or cmd and enter this git command <https://github.com/Faiq-Ali-372/Favourite-Movies-Collection>

3. Install the required dependencies:
When in root directory of project, Open terminal or cmd and enter this command `pip install -r requirements.txt` to install all dependencies

4. Run the application:
When in root directory of project, Open terminal or cmd and enter this command `python main.py` to execute the project

5. Open your web browser and go to `http://127.0.0.1:5000` to view the application.

## File Structure

- `myMovies.py`: Defines the database model for movies.
- `addForm.py`: Contains the form class for adding movies.
- `updateForm.py`: Contains the form class for updating movie details.
- `main.py`: The main Flask application file.
- `get_movie_data.py`: Contains functions for fetching movie data from an external API.
- `add.html`: HTML template for adding a new movie.
- `edit.html`: HTML template for editing movie details.
- `index.html`: HTML template for the homepage displaying all favorite movies.
- `select.html`: HTML template for selecting a movie from search results.

## Credits

- Built with Flask, SQLAlchemy, and Bootstrap.
- Movie data is retrieved from The Movie Database (TMDb) API.
