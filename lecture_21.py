# ##############
# Task 1
# ##############

import requests

BASE_URL = "https://crudcrud.com/api/d8eddfeb404d42ef987108e86bb40a00/products"

product_data = {
    "name": "Laptop",
    "price": 2500,
    "in_stock": True
}

try:
    response = requests.post(
        BASE_URL,
        json=product_data,
        timeout=10
    )

    response.raise_for_status()

    print("Product added successfully!")
    print(response.json())

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")


##############
# Task 2
##############

try:
    response = requests.get(
        BASE_URL,
        timeout=10
    )

    response.raise_for_status()

    products = response.json()

    for product in products:
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']}")
        print(f"ID: {product['_id']}")
        print("-" * 30)

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")



##############
# Task 3
##############

product_id = "6ae8e81117e35903e8542024"

try:
    response = requests.get(
        f"{BASE_URL}/{product_id}",
        timeout=10
    )

    response.raise_for_status()

    product = response.json()

    print("Product details:")
    print(f"Name: {product['name']}")
    print(f"Price: {product['price']}")
    print(f"In Stock: {product['in_stock']}")
    print(f"ID: {product['_id']}")

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")


##############
# Task 4
##############

product_id = "6ae8e81117e35903e8542024"

updated_data = {
    "name": "Gaming Laptop",
    "price": 3200,
    "in_stock": True
}

try:
    response = requests.put(
        f"{BASE_URL}/{product_id}",
        json=updated_data,
        timeout=10
    )

    response.raise_for_status()

    print("Product updated successfully!")
    print(f"Status Code: {response.status_code}")

    verify_response = requests.get(
        f"{BASE_URL}/{product_id}",
        timeout=10
    )

    verify_response.raise_for_status()

    updated_product = verify_response.json()

    print("Updated product details:")
    print(updated_product)

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")


# ##############
# Task 5
# ##############

product_id = "6ae8e81117e35903e8542024"

try:
    response = requests.delete(
        f"{BASE_URL}/{product_id}",
        timeout=10
    )

    response.raise_for_status()

    if response.status_code == 200 or response.status_code == 204:
        print("Product successfully deleted from the server!")

    print(f"Status Code: {response.status_code}")

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")