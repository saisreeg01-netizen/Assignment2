string = "Hello World, this is Python"
substring = "World"
index = string.find(substring)

if index != -1:
    print(f"The substring '{substring}' is found at index {index}.")
else:
    print(f"The substring '{substring}' is not found.")