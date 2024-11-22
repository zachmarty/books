import json


def get_var_name(var):
    for name, val in globals().items():
        if val is var:
            return name

atrs = {0: "title", 1: "author", 2: "year"}

class BookManager:
    last_id = 0

    @classmethod
    def update_id(cls) -> None:
        with open("books.json") as f:
            books = json.load(f)["books"]
        if len(books) > 0:
            BookManager.last_id = books[-1]["id"]

    @classmethod
    def add_new_book(cls, title: str, author: str, year: int) -> str:
        if len(title) == 0:
            return "Error. Title cannot be blank"
        if len(author) == 0:
            return "Error. Author cannot be blank"
        if year <= 0:
            return "Error. Year cannot be less than 0"
        BookManager.last_id += 1
        new_book = {
            "id": BookManager.last_id,
            "title": title,
            "author": author,
            "year": year,
            "status": True,
        }
        with open("books.json") as f:
            books = json.load(f)
        books["books"].append(new_book)
        with open("books.json", "w") as f:
            json.dump(books, f)
        return "Book added"

    @classmethod
    def delete_book(cls, id: int) -> str:
        with open("books.json") as f:
            books: list = json.load(f)
        if len(books["books"]) == 0:
            return "There's no books. Add some first"
        counter = 0
        for book in books["books"]:
            if book["id"] == id:
                break
            counter += 1
        if counter == len(books["books"]):
            return f"Book with id {id} not found"
        else:
            books["books"].pop(counter)
            with open("books.json", "w") as f:
                json.dump(books, f)
            return "Book deleted"

    @classmethod
    def find_book(cls, title: str, author: str, year: str) -> str:
        if len(title) == 0 and len(author) == 0 and len(year) == 0:
            return "You haven't used any filters"
        if len(year) > 0:
            try:
                _ = int(year)
            except:
                return "Year is not correct"
            if _ <= 0:
                return "Year cannot be less than 0"

        with open("books.json") as f:
            books: list = json.load(f)["books"]
            if len(books) == 0:
                return "There's no books. Add some first"
            for ind, atr in enumerate([title, author, year]):
                tmp = []
                empty = True  
                if not (len(atr) == 0):
                    if atrs[ind] == "year":
                        atr = int(atr)
                    empty = False
                    for book in books:
                        if book[atrs[ind]] == atr:
                            tmp.append(book)
                if not empty and len(tmp) == 0:
                    return "No match found"
                if not empty and len(tmp) > 0:
                    books = tmp
            output = ""
            for ind, val in enumerate(books):
                output += f"""{ind+1}. "{val['title']}" by {val['author']}. {val['year']}\n"""
            return output

    @classmethod
    def all_books(cls):
        with open("books.json") as f:
            books: list = json.load(f)["books"]
        if len(books) == 0:
            return "There's no books. Add some first."
        output = ""
        for ind, book in enumerate(books):
            output += f"""{book['id']}. "{book['title']}" by {book['author']} {book['year']}. {"in stock" if book['status'] else "given away"}\n"""
        return output
    
    @classmethod
    def change_status(cls, id, status):
        if status!= "in stock" and status != "given away":
            return 'Status can be only "in stock" or "given away"'
        with open("books.json") as f:
            books: list = json.load(f)["books"]
        if len(books) == 0:
            return "There's no books. Add some first"
        changed = False
        for book in books:
            if book['id'] == id:
                changed = True
                book['status'] = True if status == "in stock" else False
                break
        if changed:
            with open("books.json", "w") as f:
                json.dump({"books": books}, f)
            return "Status changed"
        else:
            return f"Book with if {id} not found"
        