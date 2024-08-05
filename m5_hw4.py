def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such contact found."
        except IndexError:
            return "Not enough arguments."
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return inner
# Контейнер для контактів
contacts = {}

# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such contact found."
        except IndexError:
            return "Not enough arguments."
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return inner

# Додавання контакту
@input_error
def add_contact(args):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Показати контакт
@input_error
def show_contact(args):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    return contacts.get(name, "No such contact found.")

# Показати всі контакти
@input_error
def show_all_contacts():
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

# Головний цикл бота
def main():
    while True:
        command = input("Enter a command: ").strip()
        if command == "exit":
            print("Goodbye!")
            break
        elif command.startswith("add"):
            args = command.split()[1:]
            print(add_contact(args))
        elif command.startswith("phone"):
            args = command.split()[1:]
            print(show_contact(args))
        elif command == "all":
            print(show_all_contacts())
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
