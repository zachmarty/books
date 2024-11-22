from manager import BookManager

BookManager.update_id()

cmd = input("Type command\n").lower()
while cmd != "exit":
    if cmd == "add new book":
        title = input("type title: ")
        author = input("type author: ")
        try:
            year = int(input("type year: "))
            print("Year is not correct")
            if type(title) is str and type(author) and type(year) is int:
                print(BookManager.add_new_book(title, author, year))
            else:
                print("Incorrect input data")
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
    cmd = input("Type command\n").lower()
