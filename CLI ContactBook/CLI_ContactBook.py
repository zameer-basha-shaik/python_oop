from contact import Contacts, ContactBook

def main():
    is_running = True
    while is_running:
        print("Press Control+C, to stop program at any point.\n")
        
        print("Options:\n1. Create a Contact\n2. Fetch Contact List\n3. Search For a Contact\n4. Update Existing Contact\n5. Delete a Contact\n")
        option = (input('Enter the Operation(1 to 5), "0 to close":'))
        if option == '0':
            is_running = False
        elif option == '1':
            ContactBook.CreateContact()
        elif option == '2':
            ContactBook.get_List()
        elif option == '3':
            ContactBook.SearchContact()
        elif option == '4':
            ContactBook.UpdateContact()
        elif option == '5':
            ContactBook.DeleteContact()
        else:
            print("Invalid Option!")




if __name__ == '__main__':
    main()