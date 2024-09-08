contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact {name} added.")

def view_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")
    else:
        print("No contacts available.")

def search_contact():
    query = input("Enter name or phone to search: ")
    for name, info in contacts.items():
        if name == query or info['Phone'] == query:
            print(f"Found - Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print(f"Contact {name} updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting.")
            break
        else:
            print("Invalid option.")

# Running the Contact Book program
menu()
