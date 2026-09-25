import os
import json
filepath = "CLI ContactBook/contacts.json"

class Contacts:
    def __init__(self, name: str, phone: str, email:str):

        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:
    with open(filepath, mode = 'r') as f:
        contact_data = json.load(f)

    def update_contacts_file(data: dict):
        if not data:
            return
        with open(filepath,mode='w') as fp:
            json.dump(ContactBook.contact_data, fp, indent=2)

    def CreateContact():
        is_running = True
        name = ''
        email = ''
        phone = ''


        while is_running:
            name = input("Enter contact's name (should be unique): ")
            key_name = name.lower()
            if name == 0:
                break
            
            if not name:
                print("Name cannot be empty.")
            elif key_name in ContactBook.contact_data:
                print("Name Already Exists!")
            else:
                break
            
        while is_running:
            email = input("Enter email (optional): ")
            if not email or '@' in email:
                break
            else:
                print('Invalid Email !')
                
        while is_running:
            phone = input("Enter Phone Number (10 digits): ")
            if not phone:
                print("Number Can't be empty")
            elif not phone.isdigit():
                print("Digits Only!")
            elif len(phone) != 10:
                print("Number Should Have 10 Digits!")
            else:
                break

        ContactBook.contact_data[key_name] = {"name": name, "email": email, "phone": phone}

            
    def UpdateContact():
        
        while True:
            key_name = input("Enter Contact name to search:")
            key_name = key_name.lower()
            
            if key_name not in ContactBook.contact_data:
                print("Name doesn't exist")
            else:
                break
        print("Enter new values, if nothing to change enter 0, leaving empty deletes the previous value!")
        is_running = True
        name = ''
        email = ''
        phone = ''

        while is_running:
            name = input("Enter new name (should be unique): ")
            if name == '0' or name.lower() == key_name:
                break
            if not name:
                print("Name cannot be empty.")
            elif key_name in ContactBook.contact_data:
                print("Name Already Exists!")
            else:
                ContactBook.contact_data[key_name]["name"] = name
                break
            
        while is_running:
            email = input("Enter email (optional): ")
            if email == '0':
                break
            if not email or '@' in email:
                ContactBook.contact_data[key_name]["email"] = email
                break
            else:
                print('Invalid Email !')
                
        while is_running:
            phone = input("Enter Phone Number (10 digits): ")
            if phone == '0':
                break
            if not phone.isdigit():
                print("Digits Only!")
            elif len(phone) != 10:
                print("Number Should Have 10 Digits!")
            else:
                ContactBook.contact_data[key_name]["phone"] = phone
                break

        if name.lower() != key_name and name!= '0':
            ContactBook.contact_data[name.lower()] = ContactBook.contact_data.pop(key_name)

        ContactBook.update_contacts_file(ContactBook.contact_data)

        print("Contact Updated!")

    def SearchContact():
        while True:
            name = input("Enter name to search(case insensitive, enter q to exit): ").lower()
            if name == 'q':
                break
            if name in ContactBook.contact_data:
                data = ContactBook.contact_data[name]
                print(f"Name: {data["name"]}\nEmail: {data["email"]}\nPhone: {data["phone"]}")
            else:
                print("Contact Not Found!")



    def get_List():
        pass

    def DeleteContact():
        pass


ContactBook.SearchContact()
        

