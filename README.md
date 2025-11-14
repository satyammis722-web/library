# library
Here is a clean, well-structured **README.md** in Markdown format for your `Libary.py` program:

---

# 📚 Library Management System (Python)

A simple command-line based **Library Management System** built in Python.
This program allows users to choose books and automatically opens related learning resources in their web browser.

---

## 🚀 Features

* Console-based user interaction
* Simple menu system
* Opens book-related links in the default web browser
* Beginner-friendly Python script

---

## 🧠 How It Works

1. The program welcomes the user and asks them to enter:

   * `1` → Continue
   * `0` → Exit

2. If the user chooses to continue, they will see a list of books:

   * **1 → C**
   * **2 → Java**
   * **3 → HTML**
   * **4 → Python**

3. After selecting a book, the program opens an online tutorial link in the browser.

4. Invalid choices are handled politely.

---

## 📁 File Overview

### `Libary.py`

Main program containing:

* Input handling
* Menu display
* `run()` function (main logic controller)
* `book()` function (opens selected book link)

---

## 🖥️ Usage

### ▶️ Run the program

Make sure you have Python installed.

```bash
python Libary.py
```

### 📌 Requirements

No external libraries required—only uses Python's built-in:

```python
import webbrowser
```

---

## 🔗 Book Resources

| Book   | Description             | Link          |
| ------ | ----------------------- | ------------- |
| C      | Basics of C programming | GeeksforGeeks |
| Java   | Java tutorials          | W3Schools     |
| HTML   | Web development basics  | W3Schools     |
| Python | Python programming      | W3Schools     |

---

## 📝 Code Structure

```
run()   → Controls main flow
book()  → Handles book selection
```

---

## 💡 Example Interaction

```
Welcome to Library Management System!
Enter the number either 0 or 1
Enter the number: 1

Choose a book from the list below:
Book 1 - C
Book 2 - Java
Book 3 - HTML
Book 4 - Python

Enter the number to choose the book: 4
Opening Python book info...
Thanks for visiting the library!
```


