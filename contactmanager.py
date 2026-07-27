from firebase_config import db
from tabulate import tabulate


# ------------------ Add Contact ------------------ #

def add_contact():
    contact_id = input("Enter Contact ID: ")

    doc = db.collection("contacts").document(contact_id).get()

    if doc.exists:
        print("❌ Contact ID already exists.")
        return

    name = input("Enter Name: ")

    phone = input("Enter Phone: ")
    if not phone.isdigit() or len(phone) != 10:
        print("❌ Invalid phone number. Enter exactly 10 digits.")
        return

    email = input("Enter Email: ")
    if "@" not in email or "." not in email:
        print("❌ Invalid email address.")
        return

    address = input("Enter Address: ")

    db.collection("contacts").document(contact_id).set({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    print("✅ Contact Added Successfully!")


# ------------------ View Contacts ------------------ #

def view_contacts():
    docs = db.collection("contacts").stream()

    table = []

    for doc in docs:
        data = doc.to_dict()

        table.append([
            doc.id,
            data.get("name"),
            data.get("phone"),
            data.get("email"),
            data.get("address")
        ])

    if table:
        print("\n========== CONTACT LIST ==========\n")
        print(tabulate(
            table,
            headers=["ID", "Name", "Phone", "Email", "Address"],
            tablefmt="grid"
        ))
    else:
        print("No contacts found.")


# ------------------ Search Contact ------------------ #

def search_contact():
    contact_id = input("Enter Contact ID: ")

    doc = db.collection("contacts").document(contact_id).get()

    if doc.exists:
        data = doc.to_dict()

        print("\n========== CONTACT DETAILS ==========\n")
        print(f"ID      : {doc.id}")
        print(f"Name    : {data.get('name')}")
        print(f"Phone   : {data.get('phone')}")
        print(f"Email   : {data.get('email')}")
        print(f"Address : {data.get('address')}")

    else:
        print("❌ Contact not found.")


# ------------------ Update Contact ------------------ #

def update_contact():
    contact_id = input("Enter Contact ID: ")

    doc = db.collection("contacts").document(contact_id).get()

    if not doc.exists:
        print("❌ Contact not found.")
        return

    name = input("Enter New Name: ")

    phone = input("Enter New Phone: ")
    if not phone.isdigit() or len(phone) != 10:
        print("❌ Invalid phone number.")
        return

    email = input("Enter New Email: ")
    if "@" not in email or "." not in email:
        print("❌ Invalid email.")
        return

    address = input("Enter New Address: ")

    db.collection("contacts").document(contact_id).update({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    print("✅ Contact Updated Successfully!")


# ------------------ Delete Contact ------------------ #

def delete_contact():
    contact_id = input("Enter Contact ID: ")

    doc = db.collection("contacts").document(contact_id).get()

    if doc.exists:
        db.collection("contacts").document(contact_id).delete()
        print("✅ Contact Deleted Successfully!")
    else:
        print("❌ Contact not found.")
def search_by_name():
    name = input("Enter Name: ").strip().lower()

    docs = db.collection("contacts").stream()

    found = False

    for doc in docs:
        data = doc.to_dict()

        if data.get("name", "").lower() == name:
            found = True

            print("\nContact Found")
            print("-----------------------")
            print("ID      :", doc.id)
            print("Name    :", data["name"])
            print("Phone   :", data["phone"])
            print("Email   :", data["email"])
            print("Address :", data["address"])

    if not found:
        print("❌ Contact not found.")
def search_by_phone():
    phone = input("Enter Phone Number: ")

    docs = db.collection("contacts").stream()

    found = False

    for doc in docs:
        data = doc.to_dict()

        if data.get("phone") == phone:
            found = True

            print("\nContact Found")
            print("-----------------------")
            print("ID      :", doc.id)
            print("Name    :", data["name"])
            print("Phone   :", data["phone"])
            print("Email   :", data["email"])
            print("Address :", data["address"])

    if not found:
        print("❌ Contact not found.")
def total_contacts():
    docs = list(db.collection("contacts").stream())

    print(f"\nTotal Contacts : {len(docs)}")