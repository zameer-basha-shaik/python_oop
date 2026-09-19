# Creating Classes and Objects
# Combining Different Objects
def Creating_Combining_Objects():

    class Dog:
        def __init__(self, name, breed, owner):
            self.name = name
            self.breed = breed
            self.owner = owner

        def bark(self):
            print("Whoof! Whoof!")

        def details(self):
            print(f'Name: {self.name}, Breed: {self.breed}')


    class Owner:
        def __init__(self, name, address, contact_number):
            self.name = name
            self.address = address
            self.phone_number = contact_number

        def details(self):
            print(f'Name: {self.name}, Phone Number: {self.phone_number}')

    owner1 = Owner("Alice", "Bell Street", '900000')
    owner2 = Owner("Bob", "Candle Street", '800000')
        
    dog1 = Dog("Tiger", "German Shperd", owner1)
    dog2 = Dog("Dragon", "Bull Dog", owner2)

    print(dog1.owner.name)
    dog1.details()
    dog1.owner.details()

    print(dog2.owner.name)
    dog2.details()
    dog2.owner.details



