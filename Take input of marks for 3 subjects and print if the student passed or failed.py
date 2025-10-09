subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

if subject1 >= 40 and subject2 >= 40 and subject3 >= 40:
    print("Student passed.")
else:
    print("Student failed.")
    if subject1 < 40:
        print("Failed in Subject 1")
    if subject2 < 40:
        print("Failed in Subject 2")
    if subject3 < 40:
        print("Failed in Subject 3")