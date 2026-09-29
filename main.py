from data import books, students, transactions
from books import add_book, view_books, search_book, update_book, delete_book
from students import add_student, view_students
from transactions import issue_book, return_book, view_transactions
from reports import library_statistics


def display_menu():
    print("\n" + "=" * 55)
    print("             LIBRARY MANAGEMENT SYSTEM")
    print("=" * 55)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Add Student")
    print("7. View Students")
    print("8. Issue Book")
    print("9. Return Book")
    print("10. View Transactions")
    print("11. Library Statistics")
    print("12. Exit")
    print("=" * 55)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            update_book(books)
        elif choice == "5":
            delete_book(books, transactions)
        elif choice == "6":
            add_student(students)
        elif choice == "7":
            view_students(students)
        elif choice == "8":
            issue_book(books, students, transactions)
        elif choice == "9":
            return_book(books, students, transactions)
        elif choice == "10":
            view_transactions(transactions)
        elif choice == "11":
            library_statistics(books, students, transactions)
        elif choice == "12":
            print("\nThank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 12.")


if __name__ == "__main__":
    main()
