
def save_quote():
    writer = input("Enter your favorite writer: ")
    quote = input("Enter your favorite quote: ")

    with open("quotes.txt", "a") as file:
        file.write(f"Writer: {writer}\n")
        file.write(f"Quote: {quote}\n")


def read_quotes():
    try:
        with open("quotes.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("The file does not exist.")

save_quote()
read_quotes()