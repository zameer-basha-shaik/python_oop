import os
import json
filepath = "contacts.json"

class Contacts:
    def __init__(self, name: str, phone: str, email:str):

        self.name = name
        self.phone = phone
        self.email = email


    def is_valid(self):
        if self.name.isEmpty():

            return False
        elif not self.phone.isnumeric() or len(self.phone) < 10:
            return False
        elif '@' not in self.email:
            return False
        else:
            return True

class ContactBook:
    def CreateContact():
        is_running = True
        name = ''
        email = ''
        phone = ''

        while is_running:
            name = input("Enter contact's name (should be unique): ")
            if name:
                break
            else:
                print("Name cannot be empty.")
                

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


            

    def UpdateContact(name):

        pass

    def SearchContact(name):
        pass

    def get_List():
        pass

    def DeleteContact():
        pass


# ContactBook.CreateContact()
        

        

file = """{
    
    
        "Zameer":
        {"name": "Zameer", "Email": "skzameer@gmail.com", "Phone": "9000090909"},
        "Mahesh":
        {"name": "Mahesh", "Email": "mahesh@gmail.com", "Phone": "1234567890"}

}"""

data: dict = json.loads(file)



print(data)

