from typing import List, Tuple, Dict, Callable

def input_error(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone, please."
        except KeyError:
            return "This contact does not exist."
        except IndexError:
            return "Not enough arguments."
    return inner


def parse_input(user_input: str) -> Tuple[str, List]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    name, phone = args
    if contacts.get(name):
        return "This name already exists, please enter a different name."
    contacts[name] = phone
    return "Contact added successfully."

@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact updated successfully."

@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    name = args[0]
    return contacts[name]

def show_all(contacts: Dict[str, str]) -> str:
    if not contacts:
        return "No contacts."
    return '\n'.join(f'{name}: {phone}' for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
