from manager import BookManager

BookManager.update_id()

cmd = input("Type command\n").lower()
while cmd != "exit":
    if cmd == "add new book":
        title = input("type title: ")
        author = input("type author: ")
        try:
            year = int(input("type year: "))
            print(BookManager.add_new_book(title, author, year))
        except:
            print("Year is not correct")
    elif cmd == "delete book":
        try:
            id = int(input("type id: "))
            if id > 0:
                print(BookManager.delete_book(id))
            else:
                print("Id cannot be less than 0")
        except:
            print("Enter correct id")
    elif cmd == "find book":
        title = input("type title (leave empty if you don't need it): ")
        author = input("type author (leave empty if you don't need it): ")
        year = input("type year (leave empty if you don't need it): ")
        print(BookManager.find_book(title, author, year))
    elif cmd == "all books":
        print(BookManager.all_books())
    elif cmd == "change status":
        status = input("Type new status ").lower()
        try:
            id = int(input("type id: "))
            if id > 0:
                print(BookManager.delete_book(id, status))
            else:
                print("Id cannot be less than 0")
        except:
            print("Enter correct id")
        print(BookManager.change_status(id, status))
    cmd = input("Type command\n").lower()

