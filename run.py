# Print "Hello" to the console
print("Hello")

# Write "123" to a file named "AutoCreated.txt" in the local directory
file_path = "AutoCreated.txt"
with open(file_path, 'w') as file:
    file.write("123")