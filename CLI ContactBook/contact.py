import json
import os

filepath = "CLI ContactBook/contacts.json"


class Contacts:
    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    # Load existing contacts
    if os.path.exists(filepath):
        with open(filepath, mode='r') as f:
            contact_data = json.load(f)
    else:
        contact_data = {}

    @staticmethod
    def update_contacts_file():
        with open(filepath, mode='w') as fp:
            json.dump(ContactBook.contact_data, fp, indent=2)

    @staticmethod
    def CreateContact():

        while True:
            name = input("Enter contact's name (should be unique): ")

            if name == '0':
                return

            key_name = name.lower()

            if not name:
                print("Name cannot be empty.")
            elif key_name in ContactBook.contact_data:
                print("Name Already Exists!")
            else:
                break

        while True:
            email = input("Enter email (optional): ")

            if not email or '@' in email:
                break
            else:
                print("Invalid Email!")

        while True:
            phone = input("Enter Phone Number (10 digits): ")

            if not phone:
                print("Number Can't be empty")
            elif not phone.isdigit():
                print("Digits Only!")
            elif len(phone) != 10:
                print("Number Should Have 10 Digits!")
            else:
                break

        ContactBook.contact_data[key_name] = {
            "name": name,
            "email": email,
            "phone": phone
        }

        ContactBook.update_contacts_file()

        print("Contact Created!")

    @staticmethod
    def UpdateContact():

        while True:
            key_name = input("Enter Contact name to search: ").lower()

            if key_name not in ContactBook.contact_data:
                print("Name doesn't exist")
            else:
                break

        print(
            "Enter new values.\n"
            "Enter 0 to keep the existing value.\n"
            "Leave email empty to delete it."
        )

        old_data = ContactBook.contact_data[key_name]

        # ---------- NAME ----------
        while True:
            name = input("Enter new name (should be unique): ")

            if name == '0':
                break

            if not name:
                print("Name cannot be empty.")
                continue

            new_key = name.lower()

            if new_key != key_name and new_key in ContactBook.contact_data:
                print("Name Already Exists!")
            else:
                old_data["name"] = name
                break

        # ---------- EMAIL ----------
        while True:
            email = input("Enter email (optional): ")

            if email == '0':
                break

            if not email or '@' in email:
                old_data["email"] = email
                break
            else:
                print("Invalid Email!")

        # ---------- PHONE ----------
        while True:
            phone = input("Enter Phone Number (10 digits): ")

            if phone == '0':
                break

            if not phone:
                print("Number Can't be empty")
            elif not phone.isdigit():
                print("Digits Only!")
            elif len(phone) != 10:
                print("Number Should Have 10 Digits!")
            else:
                old_data["phone"] = phone
                break

        # If name was changed, change dictionary key
        new_key = old_data["name"].lower()

        if new_key != key_name:
            ContactBook.contact_data[new_key] = ContactBook.contact_data.pop(key_name)

        ContactBook.update_contacts_file()

        print("Contact Updated!")

    @staticmethod
    def SearchContact():

        while True:
            name = input(
                "Enter name to search (case insensitive, enter q to exit): "
            ).lower()

            if name == 'q':
                print("Searching Ended")
                break

            if name in ContactBook.contact_data:

                data = ContactBook.contact_data[name]

                print(
                    f"Name: {data['name']}\n"
                    f"Email: {data['email']}\n"
                    f"Phone: {data['phone']}"
                )

            else:
                print("Contact Not Found!")

    @staticmethod
    def get_List():

        if not ContactBook.contact_data:
            print("No Contact data!")
            return

        print("CONTACT LIST:\n")

        count = 1

        for key in ContactBook.contact_data:

            data = ContactBook.contact_data[key]

            print(
                f"{count}. Name: {data['name']}\n"
                f"   Email: {data['email']}\n"
                f"   Phone: {data['phone']}"
            )

            print()

            count += 1

    @staticmethod
    def DeleteContact():

        while True:

            name = input(
                "Enter Contact Name to delete (enter q to quit): "
            )

            if name.lower() == 'q':
                break

            key_name = name.lower()

            if key_name not in ContactBook.contact_data:
                print("Contact Doesn't Exist")
            else:
                ContactBook.contact_data.pop(key_name)

                ContactBook.update_contacts_file()

                print("Contact Deleted!")