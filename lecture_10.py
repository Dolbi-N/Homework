# ###################
# Task 1 — Recursive sum of digits
# ###################


def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(1234))


# ##########################
# Task 2 — Process student scores
# ##########################

scores = [45, 82, 67, 38, 90, 55, 72]

passing_scores = filter(lambda score: score >= 50, scores)

final_scores = map(lambda score: min(score + 5, 100), passing_scores)

print(list(final_scores))


# ###########################
# Task 3 — Sort an e-commerce catalog
# ###########################

names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

products = list(zip(names, prices, ratings))

sorted_by_price = sorted(products, key=lambda product: product[1], reverse=True)

print("Products by price (highest to lowest):")
print(sorted_by_price)

sorted_by_rating = sorted(products, key=lambda product: product[2])

print("Products by rating (lowest to highest):")
print(sorted_by_rating)