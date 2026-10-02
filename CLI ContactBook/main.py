from contact import Contact, ContactBook

def main():

    book = ContactBook()
    is_running = True
    while is_running:
        print("Press Control+C, to stop program at any point.")
        
        print("Options:\n1. Create a Contact\n2. Fetch Contact List\n3. Search For a Contact\n4. Update Existing Contact\n5. Delete a Contact")
        option = (input('Enter the Operation(1 to 5), "0 to close":'))
        if option == '0':
            is_running = False
        elif option == '1':
            book.CreateContact()
        elif option == '2':
            book.get_List()
        elif option == '3':
            book.SearchContact()
        elif option == '4':
            book.UpdateContact()
        elif option == '5':
            book.DeleteContact()
        else:
            print("Invalid Option!")




if __name__ == '__main__':
    main()