from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is optional on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "All Father",
                "author": "michael jackson",
                "descrption": "a good book",
                "rating": 5,
            }
        }
    }


BOOKS = [
    Book(1, "Introduction to Python", "E. J. Adewale", "great for beginners", 5),
    Book(2, "Introduction to FastApi", "E. J. Adewale", "good for web devs", 5),
    Book(3, "How to be The GOAT", "thegoat", "the best ever", 5),
    Book(4, "Book1", "none", "none", 0),
    Book(5, "Book2", "none", "none", 0),
    Book(6, "Book3", "none", "none", 0),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_Book_id(new_book))


def find_Book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book


@app.get("/books/{book_id}")
async def fetch_book_by_book_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
        else:
            print(f"No book with ID: {book_id}")


@app.get("/books/")
async def fetch_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)

    return books_to_return
