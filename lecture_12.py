# ########################
# Task 1: Execution Counter Closure / გამოძახებების მთვლელი
# ########################

def make_counter(start_value=0):
    count = start_value

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter = make_counter(start_value=10)
print(counter())  # 11
print(counter())  # 12


# ########################
# Task 2: Execution Time & Metadata Logger Decorator / დროისა და მეტამონაცემების დეკორატორი
# ########################

import time
from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        print(
            f"Running {func.__name__}... "
            f"Executed in {execution_time:.2f} seconds."
        )

        return result

    return wrapper

@log_execution
def example_function():
    """An example function."""
    time.sleep(1)
    return "Task completed!"


result = example_function()
print(result)


# #############################
# Task 3: Access Control / Password Required Decorator / წვდომის შეზღუდვის დეკორატორი
# #############################

from functools import wraps

def require_role(allowed_role="admin"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = kwargs.get("user_role")

            if user_role == allowed_role:
                return func(*args, **kwargs)
            else:
                print(
                    f"Permission Denied: User is not an {allowed_role}."
                )

        return wrapper
    return decorator


@require_role(allowed_role="admin")
def modify_settings(user_role=None):
    print("Settings modified successfully!")


modify_settings(user_role="admin")

modify_settings(user_role="guest")
