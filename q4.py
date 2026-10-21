# Code written by Chinonso Uche Ugwonna for CS1101-01 Programming Fundamentals  
# Unit 7 Workshop Feedback Manager: String Handling, File I/O, and Exception Handling in Python
# Instructor: Asia Maqsood

# Question 4: Counting "great" and writing a summary report
total_feedback = 0
great_count = 0
 
with open("feedback.txt", "r") as file:
    lines = file.readlines()
 
for line in lines:
    text = line.strip()
    if text:
        total_feedback += 1
        if "great" in text.lower():
            great_count += 1
 
with open("summary.txt", "w") as report:
    report.write("=== Workshop Feedback Summary ===\n")
    report.write(f"Total Feedback: {total_feedback}\n")
    report.write(f"Mentions of 'Great': {great_count}\n")
 
print("=== Workshop Feedback Summary ===")
print(f"Total Feedback: {total_feedback}")
print(f"Mentions of 'Great': {great_count}")
