import re

contacts = [
    {"name": "Hammad", "location": "FL", "age": "19"},
    {"name": "Thalia", "location": "OH", "age": "20"},
    {"name": "Salwa", "location": "NJ", "age": "21"}
]

def main():
    print("\n")
    print('Contacts: \n')
    for contact in contacts:
        print(contact['name'], contact['location'], contact['age'], sep=", ")   
    print("\n")

    name_input = input("Enter contact name: ") 

    matched_name = [contact for contact in contacts if re.search(name_input, contact['name'], re.IGNORECASE)]


    if matched_name:
        for contact in matched_name:
            deleteContact = input("Delete contact? (Y/N) ")
            if deleteContact.upper() == 'Y':
                contacts.remove(contact)
                print(f"Updated Contacts: {contacts}", sep="\n")
                editContacts = input("Delete more contacts? (Y/N) ")
                if editContacts.upper() == 'Y':
                    main()
                else:
                    break
            elif deleteContact.upper() == 'N':
                print("\n")
                main()
            else:
                print("Invalid input, please select (Y/N) ")
    else:
        print("Contact not found, try again.\n")
        main()

main()

