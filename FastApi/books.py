from fastapi import FastAPI


app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Math"},
    {"title": "Title Three", "author": "Author Three", "category": "Philosophy"},
    {"title": "Title Four", "author": "Author Four", "category": "Geology"},
    {"title": "Title Five", "author": "Author One", "category": "Statistics"},
    {"title": "Title Six", "author": "Author Two", "category": "Engineering"},
]


@app.get("/books")
async def get_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def get_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
