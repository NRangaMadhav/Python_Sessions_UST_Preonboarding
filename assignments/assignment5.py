# CONTACT DIRECTORY SERVICE
# Lambda for name formatting (capitalize name)
format_name = lambda name: name.strip().title()

def add_contact(contacts, email_set):
    name = format_name(input("Enter name: "))
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    # Remove duplicate emails using set
    if email in email_set:
        print("Duplicate email found. Contact not added.")
        return

    contacts[name] = {"phone": phone, "email": email}
    email_set.add(email)
    print(f"Contact '{name}' added successfully.")

def search_contact(contacts):
    name = format_name(input("Enter name to search: "))
    if name in contacts:
        print("Contact Found:")
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = format_name(input("Enter name to update: "))
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        print(f"Contact '{name}' updated successfully.")
    else:
        print("Contact not found.")
# Dictionary for contacts & set for emails
contacts = {}
email_set = set()
while True:
    print("\nContact Directory Service")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice == "1":
        add_contact(contacts, email_set)
    elif choice == "2":
        search_contact(contacts)
    elif choice == "3":
        update_contact(contacts)
    elif choice == "4":
        print("Exiting Contact Directory Service")
        break
    else:
        print("Invalid choice. Please try again.")
