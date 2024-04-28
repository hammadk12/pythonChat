import re
import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("Contacts")
root.geometry("500x300")

# original contacts list
contacts = [
    {"name": "Hammad", "location": "FL", "age": 19}
]

# returns contact name if it matches contact list
def get_matched_name(contacts, name_input):
    return [contact for contact in contacts if re.search(f"^{name_input}$", contact['name'], re.IGNORECASE)]

# displays contact information
def display_contacts():
    contacts_display.delete("1.0", tk.END) # Clear existing content
    if contacts:
        for contact in contacts:
            contacts_display.insert(tk.END, f"{contact['name']}, {contact['location']}, {contact['age']}\n")   
    else:
        contacts_display.insert(tk.END, "No contacts yet.")

# Creating a Text widget to display contacts
contacts_display = tk.Text(root, height=10, width=50)
contacts_display.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Initial message in contacts display
contacts_display.insert(tk.END, "No contacts yet.")

# prompts user to enter contact name
def get_contact_name():
    return input("Enter contact name: ")

# delete contact function
def delete_contact():
    message_label.config(text="Enter correct contact information")
    name = name_entry.get()
    location = location_entry.get()
    age = age_entry.get()

    # Validate input no empty fields
    if not name or not location or not age:
        message_label.config(text="All fields must be filled out!", fg="red")
        return
    else:
        confirm_deletion()

# checking if name is in contacts list
names_in_contacts = [contact['name'] for contact in contacts]

def confirm_deletion():
    if name_entry in names_in_contacts:
        for contact in contacts:
            if (contact['name'] == name_entry):
                name = name_entry.get()
                location = location_entry.get()
                age = age_entry.get()
                contacts.remove({"name": name, "location": location, "age": age})
                message_label.config(text="Contact deleted successfully!", fg="green")
                clear_entries()
                display_contacts()  # Update the display of contacts
            else:
                message_label.config(text="No matching contact information found. Please try again.")

# Button to delete contact
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=3, column=3)

confirm_button = tk.Button(root, text="Confirm", command=confirm_deletion)
#cancel_button = tk.Button(root, text="Cancel", command=canel_deletion)

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
def add_contact():
    # Clear message label
    message_label.config(text="")

# Fetch data from Entry widgets
    name = name_entry.get()
    location = location_entry.get()
    age = age_entry.get()

    # Validate input no empty fields
    if not name or not location or not age:
        message_label.config(text="Error: All fields must be filled out!", fg="red")
        return

    # Update message and show confirm button
    message_label.config(text=f"Add {name}? Click Confirm to proceed.", fg="black")
    confirm_button.grid(row=4, column=1, pady=10) # confirm button visible
    cancel_button.grid(row=4, column=2, pady=10) # cancel button visible

    # Confirmation
def confirm_addition():
    name = name_entry.get()
    location = location_entry.get()
    age = age_entry.get()
    contacts.append({"name": name, "location": location, "age": age})
    message_label.config(text="Contact added successfully!", fg="green")
    clear_entries()
    display_contacts()  # Update the display of contacts

def cancel_addition():
    message_label.config(text="Add Contact cancelled.", fg="blue")
    clear_entries()

def clear_entries():
    name_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    confirm_button.grid_remove()
    cancel_button.grid_remove()

# Entry widgets and their labels
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10)
location_entry = tk.Entry(root)
location_entry.grid(row=1, column=1, padx=10)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10)

tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Location:").grid(row=1, column=0)
tk.Label(root, text="Age:").grid(row=2, column=0)

# Message label for feedback
message_label = tk.Label(root, text="")
message_label.grid(row=3, column=0, columnspan=2)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=2)

confirm_button = tk.Button(root, text="Confirm", command=confirm_addition)
cancel_button = tk.Button(root, text="Cancel", command=cancel_addition)

def main():
    while True:
        print("\n")
        print('Contacts: \n')
        display_contacts()
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

# Main Display


if __name__ == '__main__':
    main()

display_contacts()
root.mainloop()