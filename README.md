# Library-Management-System
A menu-driven Library Management System built in Python using fundamental programming concepts such as functions, lists, dictionaries, tuples, sets, loops, conditionals, searching, and basic algorithms.

The project is intentionally implemented using concepts from the Problem Solving Aspects and Python syllabus. It does not use databases, external packages, classes, web frameworks, or advanced Python features.

## Main Features
1. Add Book
2. View Books
3. Search Book
4. Update Book
5. Delete Book
6. Add Student
7. View Students
8. Issue Book
9. Return Book
10. View Transactions
11. Library Statistics
12. Exit

#### Functional Modules
### Book Management
- Add, display, search, update, and delete books.

### Student Management
- Add and display students.

### Circulation Management
- Issue books, return books, calculate late fines, and view transactions.

### Reporting
- Display library statistics using counting, summation, sets, tuples, lists, and dictionaries.

## Technologies Used
- Python 3
- Git
- GitHub
- No external Python packages

## Syllabus Concepts Used
- Problem decomposition / Top Down Design
- Algorithms and flowcharts
- Variables and expressions
- Conditional statements
- `for` and `while` loops
- `break` and `continue` where appropriate in algorithms
- Functions
- Parameters and arguments
- Lists
- Tuples
- Sets
- Dictionaries
- Searching
- Counting
- Summation
- Basic time-complexity analysis
- Input validation

## Project Structure
```text
Library-Management-System/
├── main.py
├── data.py
├── validation.py
├── books.py
├── students.py
├── transactions.py
├── reports.py
├── README.md
├── statement.md
├── docs/
│   ├── algorithms.md
│   ├── diagrams.md
│   └── report.md
└── tests/
    └── test_cases.md
```

## Requirements
Python 3.x is required.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:
```text
python main.py
```

## Testing
Testing is performed using manual validation test cases. The test cases cover valid inputs, invalid inputs, duplicate IDs, unavailable books, return operations, fine calculation, and empty collections.

See `tests/test_cases.md`.

## Important Design Decision
The program uses in-memory data structures instead of a database or file storage because database and file-handling technologies are not part of the stated semester syllabus. Data resets when the program is restarted.

## Limitations
- Data is not permanently stored.
- There is one main user/operator.
- No graphical user interface is used.
- No external packages are required.

## Future Enhancements
Possible future versions could add permanent storage, login, graphical interface, and advanced reporting after those technologies are covered in the course.

## Academic Relevance
The project demonstrates problem decomposition, algorithms, flowcharts, functions, control flow, lists, tuples, sets, dictionaries, searching, counting, summation, validation, and basic algorithm analysis.

## Author
Student Project - Python / Problem Solving Course
