# Exercise 2: Dictionary Operations

info = {
    "name": "Rahul",
    "age": 20,
    "city": "Ahmedabad"
}

# 1. Add new key
info["grade"] = "A"

# 2. Update age
info["age"] = 21

# 3. Remove city
info.pop("city")

# Final dictionary
print("Updated Dictionary:", info)

# 4. Print keys and values separately
print("All Keys:", list(info.keys()))
print("All Values:", list(info.values()))