# ######################
# Task 1: User Profile Creator
# ######################

def create_user_profile(first_name, last_name, role="Student", is_active=True):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
        "is_active": is_active
    }


f_name = input("Enter your first name: ").capitalize()
l_name = input("Enter your last name: ").capitalize()

user = create_user_profile(f_name, l_name)

print(user)


# ########################
# Task 2A: The To-Do List Trap 
# ########################


def add_task(task_name, task_list=[]):
    task_list.append(task_name)

    print(task_list)


add_task("Study Python")
add_task("Do homework")
add_task("Read a book")

# ფუნქციაში დეფოლტად იქმნება ცარიელი list, 
# ვინაიდან list არის ცვლადი მონაცემთა ტიპი, 
# ფუნქციის გამოძახებისას ყოველ ჯერზე ახალი სია არ იქმნება და იგივე სია გამოიყენება ყველა გამოძახებაში.


# #####################
# Task 2B: Refactor with None
# #####################

def add_task(task_name, task_list=None):
    if task_list is None:
        task_list = []

    task_list.append(task_name)

    print(task_list)


add_task("Study Python")
add_task("Do homework")
add_task("Read a book")


# #######################
# Task 3: Text Analyzer
# #######################

def analyze_text(text, min_length=3, ignore_stopwords=None):
    if ignore_stopwords is None:
        ignore_stopwords = []

    words = text.split()

    count = 0

    for word in words:
        if len(word) >= min_length and word not in ignore_stopwords:
            count += 1

    return count


text = input("Enter a text: ")

result = analyze_text(text)

print(result)
