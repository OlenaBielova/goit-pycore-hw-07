# # utils/command_handlers.py
from models.address_book import AddressBook
from models.record import Record
from models.fields import Name, Birthday
from utils.decorators import input_error
from utils.storage import save_address_book

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Usage: add-birthday [name] [birthday DD.MM.YYYY]")
    name, birthday = args
    record = book.records.get(name)
    if not record:
        raise ValueError(f"Contact {name} not found.")
    
    record.add_birthday(birthday)
    save_address_book(book, "contacts.bin")
    return f"Birthday for {name} added."

@input_error
def show_birthday(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("Usage: show-birthday [name]")
    name = args[0]
    record = book.records.get(name)
    if not record or not record.birthday:
        raise ValueError(f"Birthday for {name} not found.")
    return f"{name}'s birthday is {record.birthday.value.strftime('%d.%m.%Y')}."

@input_error
def birthdays(args, book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No upcoming birthdays."
    
    birthdays_list = "\n".join(
        [f"{b['name']} - {b['congratulation_date']}" for b in upcoming_birthdays]
    )
    return f"Upcoming birthdays for the next week:\n{birthdays_list}"

@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Usage: add [name] [phone]")
    
    name, phone = args
    record = book.records.get(name)
    
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact updated."
    
    record.add_phone(phone)
    save_address_book(book, "contacts.bin")
    return message

@input_error
def change_contact(args, book: AddressBook):
    if len(args) < 3:
        raise ValueError("Usage: change [name] [old_phone] [new_phone]")
    
    name, old_phone, new_phone = args
    record = book.records.get(name)
    
    if not record or old_phone not in record.phones:
        raise ValueError(f"Phone number {old_phone} not found for {name}.")
    
    record.change_phone(old_phone, new_phone)
    save_address_book(book, "contacts.bin")
    return f"Phone number for {name} updated to {new_phone}."

@input_error
def show_phone(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("Usage: phone [name]")
    
    name = args[0]
    record = book.records.get(name)
    
    if not record:
        raise ValueError(f"Contact {name} not found.")
    return f"Phone numbers for {name}: {', '.join(record.phones)}"

@input_error
def show_all(args, book: AddressBook):
    contacts = "\n".join(
        [f"{name}: {', '.join(record.phones)}" for name, record in book.records.items()]
    )
    return f"All contacts:\n{contacts}" if contacts else "No contacts found."


# from models.address_book import AddressBook
# from models.record import Record
# from models.fields import Name, Birthday
# from utils.decorators import input_error

# @input_error
# def add_birthday(args, book: AddressBook):
#     name, birthday = args
#     record = book.records.get(name)
    
#     if not record:
#         return "Contact not found."
    
#     record.add_birthday(birthday)
#     return f"Birthday for {name} added: {birthday}"

# @input_error
# def show_birthday(args, book: AddressBook):
#     name = args[0]
#     record = book.records.get(name)
    
#     if not record or not record.birthday:
#         return f"No birthday found for {name}."
    
#     return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"

# @input_error
# def birthdays(args, book: AddressBook):
#     upcoming_birthdays = book.get_upcoming_birthdays()
    
#     if not upcoming_birthdays:
#         return "No upcoming birthdays this week."
    
#     result = "Upcoming birthdays:\n"
#     for bday in upcoming_birthdays:
#         result += f"{bday['name']} - {bday['congratulation_date']}\n"
    
#     return result