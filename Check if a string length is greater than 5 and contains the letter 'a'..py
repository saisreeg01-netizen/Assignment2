string = "banana split"

if len(string) > 5 and string.lower().count('a') > 0:
    print(f"The string '{string}' has a length greater than 5 and contains the letter 'a'.")
else:
    print(f"The string '{string}' does not meet the conditions.")
