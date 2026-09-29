from validation import get_positive_integer, get_non_empty_text, find_by_id


def add_book(books):
    print("\n--- Add Book ---")
    book_id = get_positive_integer("Enter book ID: ")

    if find_by_id(books, book_id) is not None:
        print("A book with this ID already exists.")
        return

    title = get_non_empty_text("Enter title: ")
    author = get_non_empty_text("Enter author: ")
    category = get_non_empty_text("Enter category: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "available": True
    }

    books.append(book)
    print("Book added successfully.")


def view_books(books):
    print("\n--- All Books ---")

    if len(books) == 0:
        print("No books available.")
        return

    for book in books:
        status = "Available" if book["available"] else "Issued"
        print(
            "ID:", book["id"],
            "| Title:", book["title"],
            "| Author:", book["author"],
            "| Category:", book["category"],
            "| Status:", status
        )


def search_book(books):
    print("\n--- Search Book ---")
    keyword = get_non_empty_text("Enter book title or author keyword: ").lower()
    found = False

    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            status = "Available" if book["available"] else "Issued"
            print(
                "ID:", book["id"],
                "| Title:", book["title"],
                "| Author:", book["author"],
                "| Status:", status
            )
            found = True

    if not found:
        print("No matching book found.")


def update_book(books):
    print("\n--- Update Book ---")
    book_id = get_positive_integer("Enter book ID to update: ")
    book = find_by_id(books, book_id)

    if book is None:
        print("Book not found.")
        return

    print("Leave a field unchanged by pressing Enter.")

    title = input("Enter new title: ").strip()
    author = input("Enter new author: ").strip()
    category = input("Enter new category: ").strip()

    if title != "":
        book["title"] = title
    if author != "":
        book["author"] = author
    if category != "":
        book["category"] = category

    print("Book updated successfully.")


def delete_book(books, transactions):
    print("\n--- Delete Book ---")
    book_id = get_positive_integer("Enter book ID to delete: ")
    book = find_by_id(books, book_id)

    if book is None:
        print("Book not found.")
        return

    if not book["available"]:
        print("Issued books cannot be deleted.")
        return

    active_transaction = False
    for transaction in transactions:
        if transaction["book_id"] == book_id and transaction["status"] == "Issued":
            active_transaction = True
            break

    if active_transaction:
        print("This book has an active transaction and cannot be deleted.")
        return

    books.remove(book)
    print("Book deleted successfully.")
