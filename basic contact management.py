# Contact Management Application

# Define an empty dictionary to store contacts
contacts = {}

# Function to add a contact
def add_contact(name, phone):
    if name not in contacts:
        contacts[name] = phone
        print("Contact added:", name, phone)
    else:
        print("Contact already exists.")

# Function to list all contacts
def list_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f"Contact found: {name} - {contacts[name]}")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted:", name)
    else:
        print("Contact not found.")

# Main loop for the contact management application
while True:
    print("\nContact Management Menu:")
    print("1. Add Contact")
    print("2. List Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Quit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '1':
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        add_contact(name, phone)
    elif choice == '2':
        list_contacts()
    elif choice == '3':
        name = input("Enter the name to search: ")
        search_contact(name)
    elif choice == '4':
        name = input("Enter the name to delete: ")
        delete_contact(name)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")
