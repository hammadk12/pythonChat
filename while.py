import re

contacts = [
    {"name": "Hammad", "location": "FL", "age": "19"},
    {"name": "Thalia", "location": "OH", "age": "20"},
    {"name": "Salwa", "location": "NJ", "age": "21"}
    ]

def get_matched_name(contacts, name_input):
    return [contact for contact in contacts if re.search(f"^{name_input}$", contact['name'], re.IGNORECASE)]

def display_contacts(contacts):
    for contact in contacts:
        print(contact['name'], contact['location'], contact['age'], sep=", ")   

def get_contact_name():
    return input("Enter contact name: ")

def delete_contact(contacts, contact):
    deleteContact = input("Delete contact? (Y/N) ")
    if deleteContact.upper() == 'Y':
        contacts.remove(contact)
        print(f"Updated Contacts: {contacts}", sep="\n")
        editContacts = input("Delete more contacts? (Y/N) ")
        if editContacts.upper() == 'Y':
            main()
        elif editContacts.upper() == 'N':
            print("\n")
            main()
        else:
            print("Invalid input, please select (Y/N) ")
    else:
        print("Invalid input, please select (Y/N) ")


def main():

    print("\n")
    print('Contacts: \n')
    display_contacts(contacts)
    print("\n")
    name_input = get_contact_name()
    matched_name = get_matched_name(contacts, name_input)

    if matched_name:
        for contact in matched_name:
            delete_contact(contacts, contact)
    else:
        print("Contact not found, try again.\n")
        main()

main()
