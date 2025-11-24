#  Library Management System

books = {}        # book_id -> {title, author, copies_total, copies_available}
borrowers = {}    # borrower_id -> {name}
issues = {}       # issue_id -> {book_id, borrower_id, returned}

# ---- Helper functions ----
def generate_id(prefix, count):
    return f"{prefix}{count+1}"

# ---- Add Book ----
def add_book():
    book_id = generate_id("B", len(books))
    title = input("Enter title: ")
    author = input("Enter author: ")
    copies = int(input("Enter number of copies: "))

    books[book_id] = {
        "title": title,
        "author": author,
        "copies_total": copies,
        "copies_available": copies
    }
    print("Book added with ID:", book_id)

# ---- Show All Books ----
def list_books():
    if not books:
        print("No books added yet.")
        return
    for bid, info in books.items():
        print(bid, "-", info["title"], "| Available:", info["copies_available"], "/", info["copies_total"])

# ---- Search Books ----
def search_books():
    query = input("Search title/author: ").lower()
    for bid, info in books.items():
        if query in info["title"].lower() or query in info["author"].lower():
            print(bid, "-", info["title"], "by", info["author"])

# ---- Add Borrower ----
def add_borrower():
    borrower_id = generate_id("U", len(borrowers))
    name = input("Enter borrower name: ")
    borrowers[borrower_id] = {"name": name}
    print("Borrower added with ID:", borrower_id)

# ---- Issue Book ----
def issue_book():
    book_id = input("Enter Book ID: ")
    borrower_id = input("Enter Borrower ID: ")

    if book_id not in books:
        print("Invalid Book ID.")
        return
    if borrower_id not in borrowers:
        print("Invalid Borrower ID.")
        return
    if books[book_id]["copies_available"] <= 0:
        print("No copies available.")
        return

    issue_id = generate_id("I", len(issues))

    issues[issue_id] = {
        "book_id": book_id,
        "borrower_id": borrower_id,
        "returned": False
    }

    books[book_id]["copies_available"] -= 1
    print("Book issued! Issue ID:", issue_id)

# ---- Return Book ----
def return_book():
    issue_id = input("Enter Issue ID: ")

    if issue_id not in issues:
        print("Invalid Issue ID.")
        return
    if issues[issue_id]["returned"]:
        print("Book already returned.")
        return

    issues[issue_id]["returned"] = True
    book_id = issues[issue_id]["book_id"]
    books[book_id]["copies_available"] += 1
    print("Book returned successfully!")

# ---- Reports ----
def show_reports():
    print("\n1. Available Books")
    print("2. Issued Books")
    print("3. Borrower History")
    choice = input("Choose: ")

    if choice == "1":
        for bid, info in books.items():
            if info["copies_available"] > 0:
                print(bid, info["title"], "- Available")
    elif choice == "2":
        for iid, info in issues.items():
            if not info["returned"]:
                print(iid, "Book:", info["book_id"], "Borrower:", info["borrower_id"])
    elif choice == "3":
        borrower_id = input("Enter Borrower ID: ")
        for iid, info in issues.items():
            if info["borrower_id"] == borrower_id:
                print(iid, "Book:", info["book_id"], "Returned:", info["returned"])
    else:
        print("Invalid option.")

# ---- Main Menu ----
def main():
    while True:
        print("\n--- Simple Library System ---")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Books")
        print("4. Add Borrower")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Reports")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            add_borrower()
        elif choice == "5":
            issue_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            show_reports()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
