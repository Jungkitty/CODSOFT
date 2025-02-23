
contacts = {}

# add 
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    contacts[name] = phone
    print(" Contact " +name + " added")

# view 
def view_contacts():
    if not contacts:
        print(" No contacts found")
    else:
        print("\n Contact List:")
        for name, phone in contacts.items():
            print(name + " - "+ phone)

# search 
def search_contact():
    name = input("Enter Name to search: ").strip()
    if name in contacts:
        print( name + " - " + contacts[name])
    else:
        print("Contact not found.")

# delete 
def delete_contact():
    name = input("Enter Name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact '" + name + "' deleted")
    else:
        print(" Contact not found")


while True:
    print("\n Contact Management \n")
    print("1 Add Contact")
    print("2 View Contacts")
    print("3 Search Contact")
    print("4 Delete Contact")
    print("5 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
