# main.py
import contact_book as cb

# Initialize state
my_contacts = []

# 1. Add contacts
cb.add_contact(my_contacts, "Alice Smith", "555-0199", "alice@example.com")
cb.add_contact(my_contacts, "Bob Jones", "555-0142", "bob@example.com")

# 2. View contacts
cb.view_contacts(my_contacts)

# 3. Search for a contact
result = cb.search_contact(my_contacts, "Alice Smith")
if result:
    print(f"\nFound: {result['name']} -> {result['phone']}")

# 4. Delete a contact
cb.delete_contact(my_contacts, "Bob Jones")

# 5. View updated contacts
cb.view_contacts(my_contacts)