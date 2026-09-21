class Contact:
    def __init__(self, name: str, phone: str, email:str):

        self.name = name
        self.phone = phone
        self.email = email

        if not(self.is_valid()):
            print("Contact Cannot be created")
            del self



    def is_valid(self):
        if self.name.isEmpty():
            return False
        elif not self.phone.isnumeric() or len(self.phone) < 10:
            return False
        elif '@' not in self.email:
            return False
        else:
            return True
        

        

    
        