from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookIn(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
]


@app.get("/books")
def list_books():
    # Task 1: Return all books.
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Task 1: Return one book by ID or raise 404.
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=201)
def create_book(payload: BookIn):
    # Task 1/2: Validate payload and create a new book.
    new_id = max(book["id"] for book in books) + 1 if books else 1
    new_book = {"id": new_id, "title": payload.title, "author": payload.author}
    books.append(new_book)
    return new_book


# Optional stretch goals:
# - Add PUT /books/{book_id}
# - Add DELETE /books/{book_id}
# - Persist data to a file or database
