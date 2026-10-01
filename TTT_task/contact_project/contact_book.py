"""
contact_book.py
A local module for managing contact records using dictionaries.
"""


def create_contact(name: str, phone: str, email: str) -> dict:
    """Creates and returns a individual contact dictionary record."""
    return {"name": name, "phone": phone, "email": email}


def add_contact(contacts: list, name: str, phone: str, email: str) -> None:
    """Appends a new contact record to the contacts list."""
    contact = create_contact(name, phone, email)
    contacts.append(contact)
    print(f"Contact for '{name}' added successfully.")


def view_contacts(contacts: list) -> None:
    """Displays all contact records in the list."""
    if not contacts:
        print("Contact book is empty.")
        return

    print("\n--- Contact Book ---")
    for index, contact in enumerate(contacts, 1):
        print(
            f"{index}. Name: {contact['name']} | "
            f"Phone: {contact['phone']} | "
            f"Email: {contact['email']}"
        )


def search_contact(contacts: list, name: str) -> dict | None:
    """Searches for a contact record by name (case-insensitive)."""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(contacts: list, name: str) -> bool:
    """Deletes a contact by name. Returns True if found and removed, False otherwise."""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact for '{name}' deleted successfully.")
            return True
    print(f"No contact found for '{name}'.")
    return False