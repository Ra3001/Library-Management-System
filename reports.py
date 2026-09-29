def library_statistics(books, students, transactions):
    print("\n--- Library Statistics ---")

    total_books = len(books)
    available_books = 0
    issued_books = 0
    total_fine = 0

    authors = set()
    categories = set()

    for book in books:
        authors.add(book["author"])
        categories.add(book["category"])

        if book["available"]:
            available_books += 1
        else:
            issued_books += 1

    for transaction in transactions:
        total_fine = total_fine + transaction["fine"]

    print("Total books:", total_books)
    print("Available books:", available_books)
    print("Issued books:", issued_books)
    print("Registered students:", len(students))
    print("Total transactions:", len(transactions))
    print("Total fine collected: Rs.", total_fine)
    print("Different authors:", len(authors))
    print("Different categories:", len(categories))

    print("Authors:", tuple(authors))
    print("Categories:", tuple(categories))
