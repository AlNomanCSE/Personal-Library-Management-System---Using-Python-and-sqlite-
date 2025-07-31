# Personal Library Management System 📚

A command-line application built with Python 3 and SQLite to manage your personal book collection. This project demonstrates fundamental database operations (CRUD) and Python programming concepts in a practical, real-world application.

## 🚀 Features

- **Add Books**: Store book details including title, author, genre, publication year, and reading status
- **View Library**: Display all books in your collection with complete details
- **Update Status**: Mark books as read or unread
- **Delete Books**: Remove books from your library
- **Search Functionality**: Find books by title or author using partial matches
- **Data Persistence**: All data is stored in a SQLite database that persists between sessions

## 🛠️ Technologies Used

- **Python 3**: Core programming language
- **SQLite**: Lightweight, serverless database
- **uv**: Modern Python package manager for dependency management
- Built-in `sqlite3` module (no external dependencies required)

## 📋 Prerequisites

- Python 3.6 or higher
- uv package manager (optional, but recommended)

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone git@github.com:AlNomanCSE/Personal-Library-Management-System---Using-Python-and-sqlite-.git

   cd personal-library-system
   ```

2. **Using uv (recommended)**:
   ```bash
   uv venv
   uv pip install -r requirements.txt  # if you have any dependencies
   ```

3. **Or using standard Python**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Run the application**:
   ```bash
   python3 library.py
   ```

## 💻 Usage

Upon running the application, you'll see a menu with the following options:

```
=== Personal Library Management System ===
1. Add a book
2. View all books  
3. Update book status
4. Delete a book
5. Search books
6. Exit
```

### Example Workflow:

1. **Add a book**: Enter title, author, genre, and publication year
2. **View your library**: See all books with their current status
3. **Mark as read**: Update a book's status when you finish reading
4. **Search**: Find specific books by title or author
5. **Clean up**: Delete books you no longer want to track

## 🗄️ Database Structure

The application creates a SQLite database (`library.db`) with the following schema:

```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    year INTEGER,
    status TEXT CHECK(status IN ('read', 'unread')) DEFAULT 'unread'
)
```

## 🎯 Learning Objectives Achieved

This project demonstrates proficiency in:

### SQLite Operations:
- ✅ Creating tables with constraints
- ✅ Inserting data with parameterized queries
- ✅ Querying data with SELECT statements
- ✅ Updating records conditionally
- ✅ Deleting data safely
- ✅ Using SQL injection prevention techniques

### Python Skills:
- ✅ Database connectivity with `sqlite3`
- ✅ Input validation and error handling
- ✅ Modular function design
- ✅ User interface design (CLI)
- ✅ Data persistence management

## 📸 Screenshots

```
Enter your choice (1-6): 1
Enter book title: The Python Cookbook
Enter author: David Beazley
Enter genre: Programming
Enter publication year: 2013
Added 'The Python Cookbook' to the library.
```

```
ID: 1, Title: The Python Cookbook, Author: David Beazley, Genre: Programming, Year: 2013, Status: unread
ID: 2, Title: Clean Code, Author: Robert Martin, Genre: Programming, Year: 2008, Status: read
```

## 🚀 Future Enhancements

Potential improvements and extensions:

- [ ] **Advanced Filtering**: Filter by genre, year range, or reading status
- [ ] **Export Functionality**: Export library to CSV/JSON formats  
- [ ] **Statistics Dashboard**: Reading statistics and progress tracking
- [ ] **GUI Version**: Desktop interface using tkinter or PyQt
- [ ] **Book Ratings**: Add rating system (1-5 stars)
- [ ] **Reading Goals**: Track annual reading goals
- [ ] **Book Recommendations**: Suggest books based on reading history
- [ ] **Multi-user Support**: Support for multiple user libraries

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📚 Resources & References

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [Real Python SQLite Tutorial](https://realpython.com/python-sqlite-databases/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/AlNomanCSE)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/abdullahalnomancse)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Inspired by the need to organize personal book collections
- Built as a learning project to master SQLite and Python integration
- Thanks to the Python and SQLite communities for excellent documentation

---

⭐ If you found this project helpful, please give it a star!