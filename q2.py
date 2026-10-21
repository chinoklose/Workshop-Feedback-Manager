# Code written by Chinonso Uche Ugwonna for CS1101-01 Programming Fundamentals  
# Unit 7 Workshop Feedback Manager: String Handling, File I/O, and Exception Handling in Python
# Instructor: Asia Maqsood

#  Question 2: Writing, reading, and appending feedback
feedback_list = [
    "The Presenter Was Great But The Room Was Cold",
    "The Workshop Was Very Informative And Helpful",
    "Great Content Overall But The Start Was Delayed",
]
 
# Part 1: write each message on its own line
with open("feedback.txt", "w") as file:
    for message in feedback_list:
        file.write(message + "\n")
 
# Part 2: read and print line by line
print("--- Feedback File Contents ---")
with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())
 
# Part 3: append one more message, then read the full file again
with open("feedback.txt", "a") as file:
    file.write("The Hands-On Exercises Were Great For Practice\n")
 
print("\n--- Updated Feedback File Contents ---")
with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())
