# info = {
#     "name": "Bhavy Shah",
#     "age": 21,
#     "subjects": ["Java", "Python", "Data Structures"],
#     "marks" : (90, 95, 85),
#     "city": "Ahmedabad",
# }

# print(info["name"])

# info["name"] = "Bhavya Shah"
# info["Collage"] = "CPC"
# print(info["name"])
# print(info)


students = {
    "name" : "Bhavy Shah",
    "Subjects" : {
        "Java" : 90,
        "Python" : 95,
        "Data Structures" : 85
    }
}

# convert dict to list
# print(list(students.keys()))

# for lenth 
# print(len(list(students.keys())))

# print(students)
# print(students["Subjects"]["Python"])

# Method in Dictionary
# for see key in dict:
# print(students.keys())

# print(students.values())

# print(students.items())

# pair = list(students.items())
# print(pair)

# print(students.get("name"))

# students.update({"city" : "Ahmedabad"})
# print(students)

# Sets in Python

# collection = {1, 2, 3, 4, 5, "Hello", "Bhavya", }
# print(collection)
# print(type(collection)) 

# collection = set()
# print(type(collection))
# print(len(collection))

# collection.add(1)
# print(collection)

# collection.remove(1)
# print(collection)

collection = {1, 2, 3, 4, 5}

collection2 = {4, 5, 6, 7, 8}

collection3 = collection.union(collection2)  # Union of two sets

collection4 = collection.intersection(collection2)  # Intersection of two sets

print(collection3)
print(collection4)