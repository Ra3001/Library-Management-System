from validation import get_positive_integer, find_by_id


LOAN_DAYS = 14
FINE_PER_DAY = 5


def issue_book(books, students, transactions):
    print("\n--- Issue Book ---")
    book_id = get_positive_integer("Enter book ID: ")
    student_id = get_positive_integer("Enter student ID: ")

    book = find_by_id(books, book_id)
    student = find_by_id(students, student_id)

    if book is None:
        print("Book not found.")
        return

    if student is None:
        print("Student not found.")
        return

    if not book["available"]:
        print("Book is already issued.")
        return

    transaction = {
        "book_id": book_id,
        "student_id": student_id,
        "days_borrowed": 0,
        "fine": 0,
        "status": "Issued"
    }

    transactions.append(transaction)
    book["available"] = False

    print("Book issued successfully to", student["name"] + ".")


def return_book(books, students, transactions):
    print("\n--- Return Book ---")
    book_id = get_positive_integer("Enter book ID to return: ")

    book = find_by_id(books, book_id)

    if book is None:
        print("Book not found.")
        return

    if book["available"]:
        print("This book is not currently issued.")
        return

    active_transaction = None

    for transaction in transactions:
        if transaction["book_id"] == book_id and transaction["status"] == "Issued":
            active_transaction = transaction
            break

    if active_transaction is None:
        print("No active transaction found.")
        return

    days = get_positive_integer("Enter number of days the book was borrowed: ")

    active_transaction["days_borrowed"] = days

    if days > LOAN_DAYS:
        late_days = days - LOAN_DAYS
        active_transaction["fine"] = late_days * FINE_PER_DAY
    else:
        active_transaction["fine"] = 0

    active_transaction["status"] = "Returned"
    book["available"] = True

    student = find_by_id(students, active_transaction["student_id"])

    print("Book returned successfully.")
    if student is not None:
        print("Student:", student["name"])

    print("Fine: Rs.", active_transaction["fine"])


def view_transactions(transactions):
    print("\n--- Transactions ---")

    if len(transactions) == 0:
        print("No transactions found.")
        return

    for transaction in transactions:
        print(
            "Book ID:", transaction["book_id"],
            "| Student ID:", transaction["student_id"],
            "| Days:", transaction["days_borrowed"],
            "| Fine: Rs.", transaction["fine"],
            "| Status:", transaction["status"]
        )
