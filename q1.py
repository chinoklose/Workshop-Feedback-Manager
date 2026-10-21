# Code written by Chinonso Uche Ugwonna for CS1101-01 Programming Fundamentals  
# Unit 7 Workshop Feedback Manager: String Handling, File I/O, and Exception Handling in Python
# Instructor: Asia Maqsood

# Question 1: Cleaning a raw feedback message
raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "
 
# Part 1: trim outer spaces and convert to lowercase
step1 = raw_feedback.strip().lower()
print("After strip() and lower():", repr(step1))
 
# Part 2: standardize wording, then collapse extra internal spaces
step2 = step1.replace("speaker", "presenter")
step2 = " ".join(step2.split())
print("After replace() and join():", repr(step2))
 
# Part 3: title case and f-string output
final_text = step2.title()
print(f"Cleaned Feedback: {final_text}")
