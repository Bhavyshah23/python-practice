# List Methods

fruits = ["apple", "banana", "mango", "orange", "banana"]
print("Original:", fruits)

# Add "grapes" at the end
fruits.append("grapes")
print("After append grapes:", fruits)

# Insert "kiwi" at index 2
fruits.insert(2, "kiwi")
print("After insert kiwi:", fruits)

# Remove one "banana"
fruits.remove("banana")
print("After removing banana:", fruits)

# Sort the list alphabetically
fruits.sort()
print("After sorting:", fruits)

# Count how many times "banana" appears
banana_count = fruits.count("banana")
print(f"Banana appears {banana_count} times in the list.")
