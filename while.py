import re

# original contacts list
contacts = []

# returns contact name if it matches contact list
def get_matched_name(contacts, name_input):
    return [contact for contact in contacts if re.search(f"^{name_input}$", contact['name'], re.IGNORECASE)]

# displays contact information
def display_contacts(contacts):
    if contacts:
        for contact in contacts:
            print(contact['name'], contact['location'], contact['age'], sep=", ")   
    else:
        print("No contacts")

# prompts user to enter contact name
def get_contact_name():
    return input("Enter contact name: ")

# delete contact function
def delete_contact(contacts):
    if not contacts:
        print("No contacts available to delete.")
        return
    
    name_input = input("Enter contact name to delete: ")
    matched_contacts = get_matched_name(contacts, name_input)
    
    if matched_contacts:
        for contact in matched_contacts:
            while True:
                user_input = input(f"Delete {contact['name']}? (Y/N) ").upper()
                if user_input == 'Y':
                    contacts.remove(contact)
                    print("Contact deleted successfully.")
                    break
                elif user_input == 'N':
                    print("Deletion cancelled.")
                    break
                else:
                    print("Invalid input, please select (Y/N) ")
                
    else:
        print("No contact found with that name.")
        delete_contact(contacts)

# displays start menu
def display_menu():
    print('1. Add Contact')
    if contacts:
        print('2. Delete Contact')
    else:
        print("No contacts available to delete.")
    return input("Choose an option (1/2): ")

# validate location function
def get_valid_location(prompt, pattern):
    while True:
        user_input = input(prompt)
        if re.fullmatch(pattern, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")


# add contact function
def add_contact(contacts):
    name = input("Name: ")
    location = get_valid_location("Location: ", r"^[A-Za-z ]+$")
    age = input("Age: ")

    while True:
        confirmAdd = input(f"Add {name}? (Y/N) ").upper()
        if confirmAdd == 'Y':
            contacts.append({"name": name, "location": location, "age": age})
            print("Contact added successfully.")
            break
        elif confirmAdd == 'N':
            print("Add Contact cancelled.")
            break
        else:
            print("Invalid input, please select (Y/N) ")

def main():
    while True:
        print("\n")
        print('Contacts: \n')
        display_contacts(contacts)
        print("\n")

        option = display_menu()

        if option == '1':
            add_contact(contacts)
        elif option == '2':
            delete_contact(contacts)
        else:
            print("Invalid option, try again")
            continue
        
        if input("Continue? (Y/N) ").upper() != 'Y':
            break

if __name__ == '__main__':
    main()

