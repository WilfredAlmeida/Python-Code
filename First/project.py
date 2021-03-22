import sqlite3  # Importing Database Provider

database = sqlite3.connect('Library.sqlite')  # Connecting to Database

cursor = database.cursor()  # Cursor to database to execute queries

# ---------------------Start: Creating Tables in database if they do not exist------------------------------------------
try:
    cursor.execute("create table library(book_name varchar(100),book_author text(50), book_price integer)")
    cursor.execute("create table borrower(book_name text(50), borrower_name text(50), borrowing_date date, "
                   "borrower_contact text, return_status text);")

except sqlite3.OperationalError as e:
    pass


# -----------------------End: Creating Tables in database if they do not exist------------------------------------------

# -----------------------Start: Adding a Book into Database-------------------------------------------------------------
def add_a_book_to_database():
    name = str(input("\nEnter Book Name: "))
    author = str(input("Enter Book Author: "))
    price = int(input("Enter Book Price: "))

    values = (name, author, price)

    query = "insert into library (book_name,book_author,book_price) values(?,?,?)"

    cursor.execute(query, values)
    database.commit()
    print("\n\nBook Inserted\n")


# -------------------------End: Adding a Book into Database-------------------------------------------------------------

# -------------------------Start: Removing Book from Database-----------------------------------------------------------
def remove_book_from_database():
    book_name = str(input("\nEnter Book Name:\n "))

    query = "delete from library where book_name =?"
    value = (book_name,)

    cursor.execute(query, value)
    database.commit()
    print("\nBook Deleted\n")


# ----------------End: Removing Book from Database----------------------------------------------------------------------

# ----------------Start: View all Books from Database-------------------------------------------------------------------
def view_all_books_from_database():
    cursor.execute("select * from library")

    resultSet = cursor.fetchall()

    for i in resultSet:
        print("\n----------------------------------")
        print('Book Name: ', i[0])
        print('Book Author: ', i[1])
        print('Book Price: ', i[2])
        print("----------------------------------\n")


# ------------------------------End: View all Books from Database-------------------------------------------------------

# ------------------------------Start: Borrow a Book from Library-------------------------------------------------------
def borrow_a_book():
    book_name = str(input("\nEnter Book Name:\n"))
    borrower_name = str(input("Enter Borrower's Name:\n"))
    borrowing_date = str(input("Enter Borrowing Date (Format for Date= YYYY-MM-DD):\n"))
    borrower_contact = str(input("Enter Borrower Contact:\n"))
    return_status = "Unreturned"

    query = 'insert into borrower values (?,?,?,?,?)'

    values = (book_name, borrower_name, borrowing_date, borrower_contact, return_status)

    cursor.execute(query, values)
    database.commit()


# ----------------End: Borrow a Book from Library-----------------------------------------------------------------------

# -----------------Start: Return Borrowed Book--------------------------------------------------------------------------
def return_borrowed_book():
    borrower_name = str(input("\nEnter Borrower's Name:\n"))

    ls = [borrower_name, ]

    cursor.execute("update borrower set return_status = 'Returned' where borrower_name = ?", ls)

    print("\nBook Returned")


# -----------------End: Return Borrowed Book----------------------------------------------------------------------------

# ----------------Start: View all Borrowed Books from Database----------------------------------------------------------
def view_borrowed_books():
    cursor.execute("select * from borrower")
    resultSet = cursor.fetchall()

    for i in resultSet:
        print("\n----------------------------------------------------------")
        print("Book Name: ", i[0])
        print("Borrower Name: ", i[1])
        print("Borrowing Date: ", str(i[2]))
        print("Borrower Contact: ", i[3])
        print("Book Return Status: ", i[4])
        print("----------------------------------------------------------\n")


# ----------------End: View all Borrowed Books from Database------------------------------------------------------------

# ----------------Start: Main Menu--------------------------------------------------------------------------------------
while True:
    ch = int(
        input("\n\nEnter Your Choice: \n 1. View all Books \n 2. Borrow a Book \n 3. Return Borrowed Book \n 4. View "
              "Borrowed Books \n 5. Add a Book to Repository \n 6. Remove a Book from Repository \n 7. Exit \n"))
    if ch == 1:
        view_all_books_from_database()
    elif ch == 2:
        borrow_a_book()
    elif ch == 3:
        return_borrowed_book()
    elif ch == 4:
        view_borrowed_books()
    elif ch == 5:
        add_a_book_to_database()
    elif ch == 6:
        remove_book_from_database()
    elif ch == 7:
        break
    else:
        print("Invalid Choice!!")

# ----------------End: Main Menu--------------------------------------------------------------------------------------
