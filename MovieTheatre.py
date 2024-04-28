import tkinter as tk
from tkinter import messagebox
import datetime

# Base class representing a movie
class Movie:
    def __init__(self, id, title, genre, length, start):
        self._id = id  # Encapsulated ID attribute
        self.title = title
        self.genre = genre
        self.length = length
        self.start = start

    def display_info(self):
        # Abstraction - provides a simple interface to display movie information
        return f"{self._id}: {self.title} ({self.genre}) - Length: {self.length}, Start Time at: {self.start}h"

    def is_comedy(self):
        # Polymorphism - behaves differently based on genre
        return self.genre == "Comedy"

    def is_drama(self):
        # Polymorphism - behaves differently based on genre
        return self.genre == "Drama"

# Subclass representing a comedy movie (inherits from Movie)
class ComedyMovie(Movie):
    def __init__(self, id, title, length, start):
        super().__init__(id, title, "Comedy", length, start)

# Subclass representing a drama movie (inherits from Movie)
class DramaMovie(Movie):
    def __init__(self, id, title, length, start):
        super().__init__(id, title, "Drama", length, start)

def get_current_hour():
    # Helper function to get the current hour of the day
    now = datetime.datetime.now()
    return now.hour

def display_available_movies(root):
    # Display available movies based on current time
    current_hour = get_current_hour()
    available_movies = [movie for movie in movies if movie.start > current_hour]

    if available_movies:
        for movie in available_movies:
            movie_info_label = tk.Label(root, text=movie.display_info())
            movie_info_label.pack(anchor='w')

        # Create entry and button for movie selection
        movie_id_label = tk.Label(root, text="Enter the number (ID) of the movie you want to watch:")
        movie_id_label.pack(anchor='w')

        movie_id_entry = tk.Entry(root)
        movie_id_entry.pack(anchor='w')

        select_button = tk.Button(root, text="Select Movie", command=lambda: on_movie_selection(movie_id_entry.get()))
        select_button.pack(anchor='w')
    else:
        # Display message if no movies are available
        no_movies_label = tk.Label(root, text="None for today...")
        no_movies_label.pack()

        # Create a button to close the program if no movies are available
        close_button = tk.Button(root, text="Okay...", command=root.destroy)
        close_button.pack(anchor='w')

def on_movie_selection(selected_id):
    try:
        selected_id = int(selected_id)
        selected_movie = next((movie for movie in movies if movie._id == selected_id), None)

        if selected_movie:
            # Show selected movie information and close the GUI after successful selection
            messagebox.showinfo("Movie Selected", f"You have chosen the movie:\n{selected_movie.display_info()}\n"
                                                  "Please proceed to the check-out, where you will pay for the ticket. Enjoy!")
            root.destroy()  # Close the GUI after successful movie selection
        else:
            # Show error message for invalid movie ID
            messagebox.showerror("Invalid ID", "Invalid ID. Please choose a valid ID from the list.")
    except ValueError:
        # Show error message for invalid input format
        messagebox.showerror("Invalid Input", "Please enter a valid movie ID.")

# Main program
root = tk.Tk()
root.title("ComaRama Movie Theatre")

# Read movie data from the file and create Movie objects
movies = []
with open('mvthtr.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(',')
        id = int(parts[0])
        title = parts[1].strip().strip('"')
        length = parts[2].strip().strip('"')
        genre = parts[3].strip().strip('"')
        start = int(parts[4].strip())
        if genre == "Comedy":
            movie = ComedyMovie(id, title, length, start)
        elif genre == "Drama":
            movie = DramaMovie(id, title, length, start)
        else:
            continue
        movies.append(movie)

# Display available movies and movie selection interface if there are movies available
display_available_movies(root)

root.mainloop()
