from manager import BookManager

BookManager.update_id() # Обновление id для корректной работы

cmd = input("Type command\n").lower()
while cmd != "exit": # Бесконечный цикл на ввод комманд

    if cmd == "add new book": # Команда добавления книги
        title = input("type title: ")
        author = input("type author: ")
        try:
            year = int(input("type year: "))
            print(BookManager.add_new_book(title, author, year))
        except:
            print("Year is not correct")

    elif cmd == "delete book": # Команда удаления книги
        try:
            id = int(input("type id: "))
            if id > 0:
                print(BookManager.delete_book(id))
            else:
                print("Id cannot be less than 0")
        except:
            print("Enter correct id")

    elif cmd == "find book": #Команда поиска книг
        title = input("type title (leave empty if you don't need it): ")
        author = input("type author (leave empty if you don't need it): ")
        year = input("type year (leave empty if you don't need it): ")
        print(BookManager.find_book(title, author, year))

    elif cmd == "all books": # Команда отображения всех книг
        print(BookManager.all_books())

    elif cmd == "change status": # Команда смены статуса
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

