import json


class BookManager:
    last_id = 0

    @classmethod
    def update_id(cls) -> None:
        with open("books.json") as f:
            books = json.load(f)['books']
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
            "status": "in_stock",
        }
        with open("books.json") as f:
            books = json.load(f)
        books['books'].append(new_book)
        with open("books.json", "w") as f:
            json.dump(books, f)
        return "Book added"

    @classmethod
    def delete_book(cls, id : int) -> str:
        with open("books.json") as f:
            books : list = json.load(f)
        counter = 0
        for book in books['books']:
            if book['id'] == id:
                break
            counter += 1
        if counter == len(books['books']):
            return f"Book with id {id} not found"
        else:
            books['books'].pop(counter)
            with open("books.json", "w") as f:
                json.dump(books, f)
            return "Book deleted"
            