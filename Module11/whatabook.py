import mysql.connector
from mysql.connector import errorcode

def show_greeting():
    print()
    print("Welcome to WhatABook")

# displays the exit string upon selecting 4 from main menu
def show_goodbye():
    print()
    print("Goodbye!!!")
    print()

# displays main menu options
def show_menu():
    print()
    print("1. View Books")
    print("2. View Store Locations")
    print("3. My Account")
    print("4. Exit Program")
    print()
    
# displays the location information 1 store only at this point
def show_locations(_cursor):
    sql_text = 'SELECT store_id, locale FROM store;'
    _cursor.execute(sql_text)
    locations = _cursor.fetchall()
    print()
    for location in locations:
        print(f"Store ID: {location[0]}, Location: {location[1]}")

# present available books of main menu
def show_books(_cursor):
    sql_text = 'SELECT book_id, book_name, details, author FROM book;'
    _cursor.execute(sql_text)
    books = _cursor.fetchall()
    print()
    for book in books:
        print(f"Book ID: {book[0]}, Title: {book[1]}, Details: {book[2]}, Author: {book[3]}")

# validate the user account exists
def validate_user(user_id, _cursor):
    sql_text = f"""
    SELECT COUNT(*) AS user_count 
    FROM user
    WHERE user_id = {user_id};
    """
    _cursor.execute(sql_text)
    results = _cursor.fetchall()
    for result in results:
        if result[0] == 1:
            return True
        else:
            print("User not found!!!!")
            return False 

#showing account info after validation
def show_account_menu():
    print()
    print("1. Wishlist")
    print("2. Add Book")
    print("3. Main Menu")
    print()

# displays the wishlist
def show_wishlist(user_id, _cursor):
    sql_text = f"""
    SELECT B.book_id, B.book_name, B.details, B.author
    FROM wishlist AS W
    JOIN book AS B ON W.book_id	= B.book_id
    WHERE W.user_id = {user_id};
    """
    _cursor.execute(sql_text)
    results = _cursor.fetchall()
    print()
    for result in results:
        print(f"Book ID: {result[0]}, Title: {result[1]}, Details: {result[2]}, Author: {result[3]}")

# for showing available books
def show_available_books(user_id, _cursor):
    sql_text = f"""
	SELECT book_id, book_name, details, author 
	FROM book
	WHERE book_id NOT IN (
		SELECT book_id FROM wishlist WHERE user_id = {user_id});
    """
    _cursor.execute(sql_text)
    books = _cursor.fetchall()
    print()
    print("Available Books")
    print()
    for book in books:
        print(f"Book ID: {book[0]}, Title: {book[1]}, Details: {book[2]}, Author: {book[3]}")
    print()

# adds function to allow adding items to wishlist
def add_book_to_wishlist(user_id, book_id, _db, _cursor):
    sql_text = f"""
    INSERT INTO wishlist (user_id, book_id) VALUES ('{user_id}', '{book_id}');
    """
    _cursor.execute(sql_text)
    _db.commit()

# main body
def main():

    config = {
        "user": "whatabook_user",
        "password": "MySQL8IsGreat!",
        "host": "127.0.0.1",
        "database": "whatabook",
        "raise_on_warnings": True
    }

    try:
        db = mysql.connector.connect(**config)
        app_cursor = db.cursor()

        show_greeting()

        while True:
            show_menu() 
            main_input = input("Choose a main menu option:")

            if main_input == "1":
                show_books(app_cursor)

            elif main_input == "2":
                show_locations(app_cursor)

            elif main_input == "3":
                user_id_input = input("Please enter your user ID:")
                if validate_user(user_id_input, app_cursor):

                    while True:
                        show_account_menu()
                        account_menu_input = input("Choose an account menu option:")
                        
                        if account_menu_input == "1":
                            show_wishlist(user_id_input, app_cursor)

                        elif account_menu_input == "2":
                            show_available_books(user_id_input, app_cursor)
                            desired_book_id = input("Enter the ID of the book you desire to add: ")
                            add_book_to_wishlist(user_id_input, desired_book_id, db, app_cursor)

                        elif account_menu_input == "3":
                            break

            elif main_input == "4":
                show_goodbye()
                break

    except mysql.connector.Error as err:
        print(err)

    finally :
        db.close()

main()