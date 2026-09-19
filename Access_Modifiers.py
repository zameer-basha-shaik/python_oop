# Accessing and Modifying Objects Data

from datetime import datetime

class User:
    def __init__(self, username, email, password):

        self.username = username
        self._email = email  # Private
        self.__password = password # Name mangled (Protected)
        self.updated_time = ''

    def get_details(self):
        print(f"Username: {self.username} \nEmail:{self._email}\nLast Email Updation:{self.updated_time}")

    def get_pass(self):
        return f"{self.__password}" # Getter Method
    
    def set_email(self, newemail):
        self._email = newemail
        self.updated_time = datetime.now()

user1 = User('john', 'john@outlook.com', 'nothing' )
user2 = User('Charlie', 'char@gmail.com', '0000000')

user1.get_details()

user1.set_email("john123@gmail.com")

user1.get_details()

user1.get_pass()



