"""
Shanon Giles
deanshonor.py
11/3/24
****************************************************************************************************************************
This application will ask the user for Student information to qualify them for the Dean's List or Honor Roll
through a series of if- elif- else that will print the results if the Student qualified for the Dean's list or Honor List.
****************************************************************************************************************************
"""

# Student Infomration Entry
deans_list = []
honor_roll = []

while True:

    # Student's Last Name
    last_name = input("Enter last name (or 'ZZZ' to quit): ")

    # Program will quit if needed based on below condtiions
    if last_name == 'ZZZ':
        break

    # Get Student's first name and GPA
    first_name = input("Enter first name: ")
    gpa = float(input("Enter student's GPA"))

    # If statements will check for Dean's List or Honor Roll Eligibility
    if gpa >= 3.5:
        print(f"Congrats! {first_name} {last_name} you've made the Deans's List!")
    
    elif gpa >= 3.25:
        print(f"Congrats! {first_name} {last_name} you've made the Honor Roll")
    
    else:
        print("Error! Please try again")

# All students will be stored in either the Dean's List of Honor Roll lists.
    if gpa >= 3.5:
        deans_list.append(f"{first_name} {last_name}")
    elif gpa >= 3.25:
        honor_roll.append(f"{first_name} {last_name}")
    else:
        print("Incorrect student entry, please try again")


print("Dean's List:")
for student in deans_list:
    print(student)

print("\nHonor Roll:")
for student in honor_roll:
    print(student)





 
