# Usage of getter and setter properties instead of methods

class User:

    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property #Getter
    def email(self):
        print("Email Accessed")
        return self._email

    @email.setter #Setter
    def email(self, newemail):
        if '@' in newemail:
            self._email = newemail
        


user1 = User('charly123', 'charly123@gmail.com', 'password')
print(user1.email)

user1.email = 'Hello@World'
#user1.email('hello@') Throws error since email attribute is accessed

print(user1.email)