import pickle

def save_address_book(book, filename):
    with open(filename, "wb") as file:
        pickle.dump(book, file)

def load_address_book(filename):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return None
