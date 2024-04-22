import re

contacts = [
    {"name": "Hammad", "location": "FL", "age": "19"},
    {"name": "Thalia", "location": "OH", "age": "20"},
    {"name": "Salwa", "location": "NJ", "age": "21"}
]

def main():
    for contact in contacts:
        print(contact['name'], contact['location'], contact['age'], sep=", ")   
    
    name_input = input("Enter contact name: ") 

    matched_name = [contact for contact in contacts if re.search(name_input, contact['name'], re.IGNORECASE)]
    
    if matched_name:
        for contact in matched_name:
            deleteContact = input("Delete contact? (Y/N) ")
            if deleteContact.upper() == 'Y':
                contacts.remove(contact)
                print(f"Updated Contacts: {contacts}", sep="\n")
            elif deleteContact.upper() == 'N':
                main()
    
main()