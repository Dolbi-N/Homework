# ###########
# Task 1
# ###########


shopping_list = ["ვაშლი", "ყველი", "პური", "რძე"]

shopping_list.append("მსხალი")
print(shopping_list)

removed_product = shopping_list.pop()
print(removed_product)

print(shopping_list)

# ##########
# Task 2
# ##########

usernames = ["gio", "ნინო", "gio", "ანა", "ნიკა", "ანა"]

unique_users = set(usernames)

unique_count = len(unique_users)

print(unique_users)
print(unique_count)


# ###########
# Task 3
# ###########

phonebook = {
    "გიორგი": "555763456",
    "ანა": "593568790",
    "ნიკა": "577896623",
    "მარიამი": "558564423"
}

search_name = input("შეიყვანე სახელი: ")

print(phonebook.get(search_name, "ვერ მოიძებნა"))
