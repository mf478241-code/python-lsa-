from flask import Flask, render_template, request, redirect
from firebase_config import db
from datetime import datetime

app = Flask(__name__)
from flask import request, render_template, redirect, url_for

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        # Demo login credentials
        if email == "admin@gmail.com" and password == "admin123":
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Email or Password"

    return render_template("login.html")

# ==========================
# Dashboard
# ==========================
@app.route("/")
def dashboard():

    docs = db.collection("contacts").stream()

    total_contacts = 0
    added_today = 0
    updated = 0

    recent_contacts = []

    today = datetime.now().date()

    for doc in docs:

        data = doc.to_dict()
        data["id"] = doc.id

        total_contacts += 1

        # Added Today
        if data.get("created_at"):
            try:
                if data["created_at"].date() == today:
                    added_today += 1
            except:
                pass

        # Updated
        if data.get("updated_at"):
            updated += 1

        recent_contacts.append(data)

    # Latest 5 Contacts
    recent_contacts = recent_contacts[-5:]
    recent_contacts.reverse()

    # Read Deleted Count
    stats_ref = db.collection("stats").document("dashboard")
    stats_doc = stats_ref.get()

    if stats_doc.exists:
        deleted = stats_doc.to_dict().get("deleted", 0)
    else:
        deleted = 0

    return render_template(
        "dashboard.html",
        total_contacts=total_contacts,
        added_today=added_today,
        updated=updated,
        deleted=deleted,
        recent_contacts=recent_contacts
    )

# ==========================
# View Contacts
# ==========================
@app.route("/contacts")
def contacts():

    docs = db.collection("contacts").stream()

    contact_list = []

    for doc in docs:
        data = doc.to_dict()
        data["id"] = doc.id
        contact_list.append(data)

    return render_template(
        "contacts.html",
        contacts=contact_list
    )


# ==========================
# Add Contact Page
# ==========================
@app.route("/add-contact")
def add_contact():
    return render_template("add_contact.html")


# ==========================
# Save Contact
# ==========================
@app.route("/save-contact", methods=["POST"])
def save_contact():

    contact_id = request.form["contact_id"]

    db.collection("contacts").document(contact_id).set({

        "name": request.form["name"],
        "phone": request.form["phone"],
        "created_at": datetime.now(),
        "updated_at": None

    })

    return redirect("/")


# ==========================
# Edit Contact
# ==========================
@app.route("/edit-contact/<contact_id>")
def edit_contact(contact_id):

    doc = db.collection("contacts").document(contact_id).get()

    if doc.exists:

        contact = doc.to_dict()
        contact["id"] = doc.id

        return render_template(
            "edit_contact.html",
            contact=contact
        )

    return "Contact Not Found"


# ==========================
# Update Contact
# ==========================
@app.route("/update-contact/<contact_id>", methods=["POST"])
def update_contact(contact_id):

    doc_ref = db.collection("contacts").document(contact_id)
    doc = doc_ref.get()

    if not doc.exists:
        return f"Contact '{contact_id}' not found in Firestore."

    doc_ref.set({
        "name": request.form["name"],
        "phone": request.form["phone"],
        "updated_at": datetime.now()
    }, merge=True)

    return redirect("/")
# ==========================
# Delete Contact
# ==========================
@app.route("/delete-contact/<contact_id>")
def delete_contact(contact_id):

    # Delete the contact
    db.collection("contacts").document(contact_id).delete()

    # Update deleted counter
    stats_ref = db.collection("stats").document("dashboard")

    stats_doc = stats_ref.get()

    if stats_doc.exists:

        data = stats_doc.to_dict()
        deleted = data.get("deleted", 0)

        stats_ref.update({
            "deleted": deleted + 1
        })

    else:

        stats_ref.set({
            "deleted": 1
        })

    return redirect("/")

# ==========================
# Search Contact
# ==========================
@app.route("/search", methods=["GET", "POST"])
def search():

    contacts = []

    if request.method == "POST":

        keyword = request.form.get("keyword", "").lower()

        docs = db.collection("contacts").stream()

        for doc in docs:

            data = doc.to_dict()
            data["id"] = doc.id

            if (
                keyword in data.get("name", "").lower()
                or keyword in data.get("phone", "").lower()
            ):
                contacts.append(data)

    return render_template(
        "search.html",
        contacts=contacts
    )
@app.route("/")
def home():
    return redirect(url_for("login"))
# ==========================
# Run App
# ==========================
if __name__ == "__main__":
    app.run(debug=True)