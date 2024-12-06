# Great Harland Library Management System

# Initialize book list and user credentials
books = [
    {"title": "New Python Programming", "author": "Renuga Jayakumar", "status": "available"},
    {"title": "Harry Potter Series", "author": "J.K. Rowling", "status": "available"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "status": "available"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "status": "available"},
    {"title": "Data Science 102", "author": "Juliet Morgan", "status": "available"}
]

users = {
    "Admin": "Admin123",
    "Customer": "Patron123"
}

# Login function
def login():
    print("Welcome to the Great Hartland Community Library Management!")
    attempts = 3
    while attempts > 0:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username in users and users[username] == password:
            print(f"Login successful! Welcome, {username}.")
            return username
        else:
            attempts -= 1
            print(f"Invalid credentials. {attempts} attempt(s) left.")
    print("Too many failed attempts. Exiting.")
    exit()

# Add new book
def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    books.append({"title": title, "author": author, "status": "available"})
    print(f"Book '{title}' by {author} added successfully.")

# Search for books
def search_books():
    search_term = input("Enter book title or keyword to search: ").lower()
    results = [book for book in books if search_term in book["title"].lower() or search_term in book["author"].lower()]
    if results:
        print("Books found:")
        for book in results:
            print(f"- {book['title']} by {book['author']} ({book['status']})")
    else:
        print("No books found.")

# View available books
def view_books():
    print("All books in the library:")
    for book in books:
        print(f"- {book['title']} by {book['author']} ({book['status']})")

# Check out book
def check_out_book():
    title = input("Enter the title of the book to check out: ").strip()
    for book in books:
        if book["title"].lower() == title.lower() and book["status"] == "available":
            book["status"] = "checked out"
            print(f"'{book['title']}' has been checked out.")
            return
    print("Book not found or already checked out.")

# Check in book
def check_in_book():
    title = input("Enter the title of the book to check in: ").strip()
    for book in books:
        if book["title"].lower() == title.lower() and book["status"] == "checked out":
            book["status"] = "available"
            print(f"'{book['title']}' has been checked in.")
            return
    print("Book not found or not checked out.")

# Remove book
def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            print(f"'{book['title']}' has been removed from the library.")
            return
    print("Book not found.")

# Main function
def main():
    user = login()
    while True:
        if user == "Admin":
            print("\nAdmin Menu:")
            print("1. Add New Book")
            print("2. Search for Books")
            print("3. Check Out Book")
            print("4. Check In Book")
            print("5. View Available Books")
            print("6. Remove Book")
            print("7. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                add_book()
            elif choice == "2":
                search_books()
            elif choice == "3":
                check_out_book()
            elif choice == "4":
                check_in_book()
            elif choice == "5":
                view_books()
            elif choice == "6":
                remove_book()
            elif choice == "7":
                print("Exiting the system. See You next time. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        else:
            print("\nPatron Menu:")
            print("1. Search for Books")
            print("2. View Available Books")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                search_books()
            elif choice == "2":
                view_books()
            elif choice == "3":
                print("Thank you for patronising us. See You next time. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
