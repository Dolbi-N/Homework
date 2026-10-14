# ########################
# Task 1 — Infinite Even Numbers
# ########################
def even_numbers():
    num = 0
    while True:
        yield num
        num += 2


count = 0
for even in even_numbers():
    print(even)
    count += 1
    if count == 10:
        break


# #######################
# Task 2 — Word Length Filter
# #######################

words = ["python", "generator", "yield", "code", "ai", "developer"]

long_words = (word.upper() for word in words if len(word) > 4)

for word in long_words:
    print(word)


# #######################
# Task 3 — Greeter Bot
# #######################

def greeter_bot():
    while True:
        name = yield "Enter your name"
        yield f"Hello, {name}!"


bot = greeter_bot()

print(next(bot))
print(bot.send("Natia"))
next(bot)
print(bot.send("Mariam"))