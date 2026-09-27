# ###################
# Task 1: Student Score Manager
# ###################

scores = []

scores.append(45)
scores.append(88)
scores.append(92)
scores.append(60)
scores.append(75)

scores.remove(45)

print("Average:", sum(scores) / len(scores))
print("Highest:", max(scores))
print("Lowest:", min(scores))

scores.sort()
print("Sorted scores:", scores)

passed_scores = []

for score in scores:
    if score >= 60:
        passed_scores.append(score)

print("Passed scores:", passed_scores)


# ########################
# Task 2: Store Inventory Update
# ########################

inventory = ["apple", "banana", "orange",
             "apple", "kiwi", "apple"]

new_items = ["mango", "grape"]

print("Apple count:", inventory.count("apple"))

print("Orange index:", inventory.index("orange"))

inventory.extend(new_items)

print("Reverse inventory:", inventory[::-1])


# ######################
# Task 3: Travel Itinerary
# ######################

locations = [
    ("Tbilisi", 41.71, 44.82),
    ("Batumi", 41.64, 41.63),
    ("Kutaisi", 42.26, 42.71)
]

for city, latitude, longitude in locations:
    print(f"City: {city}, Latitude: {latitude}, Longitude: {longitude}")

city_names = [location[0] for location in locations]

print("City names:", city_names)
