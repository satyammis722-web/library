import webbrowser

print("Welcome to Library Management System!")
print("Enter the number either 0 or 1")

b = int(input("Enter the number: "))

def run(b):
    if b == 0:
        print("Thanks for visiting!")
        quit()
    elif b == 1:
        print("\nChoose a book from the list below:")
        print("Book 1 - C")
        print("Book 2 - Java")
        print("Book 3 - HTML")
        print("Book 4 - Python")
        a = int(input("\nEnter the number to choose the book: "))
        book(a)
    else:
        print("Invalid choice!")
        print("Thanks for visiting!")

def book(a):
    if a == 1:
        print("Opening C book info...")
        webbrowser.open("https://www.geeksforgeeks.org/c-programming-language/")
    elif a == 2:
        print("Opening Java book info...")
        webbrowser.open("https://www.w3schools.com/java/")
    elif a == 3:
        print("Opening HTML book info...")
        webbrowser.open("https://www.w3schools.com/html/")
    elif a == 4:
        print("Opening Python book info...")
        webbrowser.open("https://www.w3schools.com/python/")
    else:
        print("Invalid book number.")
    print("Thanks for visiting the library!")

run(b)