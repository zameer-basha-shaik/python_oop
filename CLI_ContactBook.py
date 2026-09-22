def main():
    is_running = True
    while is_running:
        print("Options:\n1. Create a Contact\n2. Fetch Contact List\n3. Search For a Contact\n4. Update Existing Contact\n5. Delete a Contact")
        option = int(input('Enter the Operation(1 to 5), "0 to close":'))
        if option == 0:
            is_running = False


if __name__ == '__main__':
    main()