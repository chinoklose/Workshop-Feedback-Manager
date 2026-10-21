# Code written by Chinonso Uche Ugwonna for CS1101-01 Programming Fundamentals  
# Unit 7 Workshop Feedback Manager: String Handling, File I/O, and Exception Handling in Python
# Instructor: Asia Maqsood

# Question 3: Safe file reading with exception handling
try:
    with open("feedback.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")
except PermissionError:
    print("Permission denied. Close the file and try again.")
finally:
    print("Operation completed.")
