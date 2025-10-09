age = 25

if age < 18:
    category = "Minor"
elif age <= 60:
    category = "Adult"
else:
    category = "Senior Citizen"

print(f"Age: {age}, Category: {category}")
