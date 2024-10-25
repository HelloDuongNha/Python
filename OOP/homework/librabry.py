from book_class import Book
class Library:
    def __init__(self, name):
        self.name = name
        self.books =[]

    def check_id(self, id):
        for i in range(len(self.books)):
            if self.books[i].id == id:
                return i
        return -1

    def add_book(self):
        print('\n***** BOOK ADDING *****\n')
        try:
            id = int(input('Enter a new book ID: '))
            if self.check_id(id) != -1:
                print('this book ID is already have, please try again! \n')
                return
            title = input('Enter Book Title: ')
            author = input('Enter Book Author: ')
            book = Book(id, title, author)
            self.books.append(book)
        except ValueError:
            print("please only enter a NUMBER!!! try again \n")

    def search_book(self):
        print('\n***** BOOK SEARCHING *****\n')
        found = False
        try:
            id = int(input("enter an ID to search: "))
            for c in self.books:
                if c.id == id: 
                    print("book found!!!\n")
                    c.show_info()
                    found = True
            if not found: print ("No book match with that ID !!\n")
        except ValueError:
            print("please only enter a NUMBER!!! try again \n")

    def edit_book(self):
        print('\n***** BOOK EDITING *****\n')
        found = False
        try:
            id = int(input("enter an ID to edit: "))
            for c in self.books:
                if c.id == id: 
                    title = input("enter the new title: ")
                    author = input("enter the new author: ")
                    print('update successfully!! \n')
                    c.title = title
                    c.author = author
                    found = True
            if not found: print ("No book match with that ID !!\n")
        except ValueError:
            print("please only enter a NUMBER!!! try again \n")

    def delete_book(self):
        print('\n***** BOOK ELIMINATION *****\n')
        found = False
        try:
            id = int(input("enter an ID to delete: "))
            index = self.check_id(id)
            if index != -1:
                self.books.pop(index)
                print('deleted successfully\n')
                found = True
            if not found: print ("No book match with that ID !!\n")
        except ValueError:
            print("please only enter a NUMBER!!! try again \n")

# # WAY 2 (base on bài Book_mng cũ)
#     def delete_book(self):
#         found = False
#         id = int(input("enter an ID to delete: "))
#         index = self.check_id(id)
#         for c in self.books:
#             if c.id == id:
#                 confirm = input(f" Does the Book ID:{id} with book's Title:{c.title} by Author:{c.author} \n that you want to delete? y/n (y for yes/ n for no) ").lower()
#                 if confirm == "y":
#                     title = c.title
#                     author = c.author
#                     id = c.id
#                     self.books.pop(index)
#                     print(f"\n The book's ID:{id} with title:{title} and author:{author} has been deleted successfully!\n")
#                     found = True
#                 elif confirm == "n":
#                     print('\nOKAY, BYE\n')
#                 else:
#                     print('\ninvalid answer\n')
#         if not found: print ("No book match with that ID !!\n")

    def display_book(self):
        print('\n***** BOOK MENU *****\n')
        if self.books == []:
            print('OH NO, there is no Book in library :(...\n')
            return
        for c in self.books:
            c.show_info()

    def borrow_book(self):
        found = False
        print('\n***** BORROW BOOK *****\n')
        try:
            id = int(input("enter Book ID to borrow: "))
            for c in self.books:
                if c.id == id and c.status == 'stock': 
                    c.status = 'not in stock'
                    print('borrow successfully!! \n')
                    found = True
                elif c.id == id and c.status == 'not in stock': 
                    print('OH NO, that book was borrowed by some one :(\n')
                    found = True
            if not found: print ("No book match with that ID !!\n")
        except ValueError:
            print("please only enter a NUMBER!!! try again \n")

    def print_menu(self):
        print(f'Welcome to {self.name} LUXYRY LIBRARY')
        print('selection 0: exit')
        print('selection 1: Add the new book')
        print('selection 2: Search for a book by its ID')
        print('selection 3: Edit book details')
        print('selection 4: Delete a book')
        print('selection 5: Display all books')
        print('selection 6: Borrow a book')

    def run(self):
        running = True
        while running:
            self.print_menu()
            try: 
                choice = int(input('\nEnter your choice: '))
                if choice == 1:
                    self.add_book()
                elif choice == 2:
                    self.search_book()
                elif choice == 3:
                    self.edit_book()
                elif choice == 4:
                    self.delete_book()
                elif choice == 5:
                    self.display_book()
                elif choice == 6:
                    self.borrow_book()
                elif choice == 0:
                    print(f'thank you for using {self.name} LIBRARY')
                    running = False
                else:
                    print('invalid value')
            except ValueError:
                print("please only enter a NUMBER!!! try again \n")

# Test
library = Library('*LMẢO LMAO*')
library.run()

# # name = input('enter your Library name: ')
# library.add_book()
# library.add_book()
# # library.add_book()
# library.display_book()
# library.search_book()
# # library.edit_book()
# # library.show_book()
# library.delete_book()
# library.display_book()
