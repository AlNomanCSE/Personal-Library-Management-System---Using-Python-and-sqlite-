import sqlite3


def init_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT,
            year INTEGER,
            status TEXT CHECK(status IN ('read', 'unread')) DEFAULT 'unread'
                   )
                   """
    )
    conn.commit()
    return conn, cursor


def add_book(cursor, conn, title, author, genre, year):
    cursor.execute(
        "INSERT INTO books (title, author, genre, year, status) VALUES (?,?,?,?,?)",
        (title, author, genre, year, "unread"),
    )
    conn.commit()
    print(f"Added '{title}' to the library")


def view_books(cursor):
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    if not books:
        make_box("No books in the library.")
    for book in books:
        make_box(
            f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}, Status: {book[5]}"
        )


def delete_book(cursor, conn, book_id):
    cursor.execute("DELETE FROM books WHERE id =?", (book_id,))
    if cursor.rowcount == 0:
        print("Book ID not found.")
    else:
        conn.commit()
        print(f"Deleted book ID {book_id}.")


def search_book(cursor, query):
    cursor.execute(
        "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
        (f"%{query}%", f"%{query}%"),
    )
    books = cursor.fetchall()
    if not books:
        print("No books found.")
    for book in books:
        make_box(
            f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}, Status: {book[5]}"
        )


def update_status(cursor, conn, book_id, status):
    cursor.execute("UPDATE books SET status = ? WHERE id = ?", (status, book_id))
    if cursor.rowcount == 0:
        print("No book found .  Try again! ")
    else:
        conn.commit()
        print(f"Updated book ID {book_id} to {status}.")


def main():
    conn, cursor = init_db()
    while True:
        print("\n=== Personal Library Management System ===")
        print("1. Add a book 💥")
        print("2. View all books 💥")
        print("3. Update book status")
        print("4. Delete a book 💥")
        print("5. Search books 💥")
        print("6. Exit 💥")
        choice = input("⚡️Enter Your choice (1-6): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            year = input("Enter publication year: ")
            try:
                year = int(year)
                add_book(cursor, conn, title, author, genre, year)
            except ValueError:
                print("Invalid year. Please enter a number.")

        elif choice == "2":
            view_books(cursor)
        elif choice == "3":
            book_id = input("Enter Book ID: ")
            status = input("Enter status (read/unread)").lower()
            update_status(cursor, conn, int(book_id), status)
        elif choice == "4":
            book_id = input("Enter Book ID: ")
            try:
                delete_book(cursor, conn, int(book_id))
            except ValueError:
                print("Invalid book ID. Please enter a number.")
        elif choice == "5":
            query = input("Enter title or author to search: ")
            search_book(cursor, query)
        elif choice == "6":
            print("Goodbye!")
            conn.close()
            break

        else:
            print("Invalid choice. Please try again.")


def make_box(text):
    """
    Creates a text box around the given text.
    """
    if not isinstance(text, str):
        text = str(text)  # Ensure the input is a string

    line_length = len(text) + 4  # +4 for two spaces on each side and two borders
    top_bottom_border = "+" + "-" * (line_length - 2) + "+"

    print(top_bottom_border)
    print(f"| {text} |")
    print(top_bottom_border)


if __name__ == "__main__":
    main()
