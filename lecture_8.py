# #########################
# Task 1: “Set Operations” 
# #########################

frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"Python", "JavaScript", "SQL", "React"}

print("Union:", frontend_skills | backend_skills)
print("Intersection:", frontend_skills & backend_skills)
print("Frontend-only:", frontend_skills - backend_skills)
print("Symmetric difference:", frontend_skills ^ backend_skills)


# ##################
# Task 2: “Nested Dictionary Extraction & Update” 
# ######################

student = {
    "name": "Natia",
    "contacts": {
        "email": "natia99@gmail.com",
        "phone": "553539959"
    },
    "courses": {
        "python": {
            "score": 90
        },
        "web": {
            "passed": False,
            "score": 50
        }
    }
}

print(student["contacts"]["email"])

print(student["courses"]["python"]["score"])

student["courses"]["web"]["passed"] = True
student["courses"]["web"]["score"] = 75

del student["contacts"]["phone"]

print(student)

# ########################
# Task 3: “Word Frequency Counter” 
# ########################

words = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]

word_counts = {}

for w in words:
    word_counts[w] = word_counts.get(w, 0) + 1

print(word_counts)

for w, count in word_counts.items():
    if count > 1:
        print(w)
