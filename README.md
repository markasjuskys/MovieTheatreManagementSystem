1. Introduction

a. What is your application?
The application is a movie theater program titled "ComaRama Movie Theatre." It allows users to view available movies, select one for watching, and proceed to the checkout.

b. How to run the program?
To run the program, execute the provided Python script. Ensure that tkinter library is installed in your Python environment.

c. How to use the program?
Run the script to launch the GUI window titled "ComaRama Movie Theatre."
The program will display a list of available movies based on the current time.
Enter the ID of the desired movie and click "Select Movie" to proceed.
Detailed information about the selected movie will be displayed.
Proceed to the checkout for ticket payment.


2. Body/Analysis

Implementation of Object-Oriented Programming Pillars

Polymorphism: This is exemplified by the is_comedy and is_drama methods in the Movie class. These methods behave differently based on the genre of the movie, allowing for dynamic behavior based on object type.
Abstraction: The display_info method in the Movie class abstracts away the complex internal details of the movie object and provides a simple interface (display_info) to retrieve relevant information about the movie.
Inheritance: The ComedyMovie and DramaMovie classes inherit from the Movie class, inheriting attributes and methods. This promotes code reusability and establishes a hierarchical relationship between different types of movies.
Encapsulation: The _id attribute in the Movie class is encapsulated as a private attribute (self._id). This restricts direct access from outside the class and maintains data integrity.

Implementation of Design Patterns

The program utilizes the Factory Method pattern through the creation of ComedyMovie and DramaMovie objects based on genre. The Factory Method pattern encapsulates object creation logic within separate factory classes (ComedyMovie and DramaMovie) while adhering to a common interface (Movie). This pattern is suitable as it centralizes object creation and allows for easy extension when adding new movie genres without modifying existing code.

3. Results and Summary

Results

The program successfully reads movie data from a file and creates corresponding Movie objects based on genre.
Challenges during implementation included handling user input validation and integrating GUI interactions with backend logic.

Conclusions

This coursework achieved a functional movie theater application employing 4 key OOP principles and the Factory Method design pattern. The program effectively demonstrates encapsulation, inheritance, polymorphism, and abstraction. Future prospects include implementing a payment system and expanding genre options dynamically.

Future Prospects

Future enhancements could involve:

Implementing a payment system for ticket purchases.
Expanding movie genres and scheduling dynamically.
Enhancing the GUI layout and user experience for improved usability and interactivity.
