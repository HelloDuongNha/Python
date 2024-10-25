list_id = [1, 2, 3, 4]
list_title = ['math', 'english', 'science', 'biography']
list_author = ['a', 'b', 'c', 'd']
list_status = ['stock', 'stock', 'stock', 'stock']

def run():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_book()
        elif choice == 2:
            search_book()
        elif choice == 3:
            edit_book()
        elif choice == 4:
            delete_book()
        elif choice == 5:
            display_book()
        elif choice == 6:
            borrow_book()
        elif choice == 0:
            print(' thank you for using Book Management Appliation')
            running = False
        else:
            print('invalid value')

def print_menu():
    print('selection 0: exit')
    print('selection 1: Add the new book')
    print('selection 2: Search for a book by its ID')
    print('selection 3: Edit book details')
    print('selection 4: Delete a book')
    print('selection 5: Display all books')
    print('selection 6: Borrow a book')

def check_id(id):
    for i in range(len(list_id)):
        if list_id[i] == id:
            return i
    return -1

def add_book():
    print('\n*****add book*****\n')
    id = int(input('Enter a new book ID: '))
    if check_id(id) == -1:
        title = input('add a new book name:')
        author = input("the book's author: ")
        list_id.append(id)
        list_title.append(title)
        list_author.append(author)
        list_status.append('stock')
        print(f'\n ****book {title} added successfully****\n')
    else: 
        print('\ninvalid ID\n')

def search_book():
    print("\n*****search book*****\n")
    id = int(input("enter the book's ID to search: "))
    if check_id(id) != -1:
        print(f"\n Book ID:{id} is match with book's title:{list_title[check_id(id)]} by author:{list_author[check_id(id)]}")
        print(f" Book status: {list_status[check_id(id)]}\n")
    else:
        print('\ninvalid ID\n')

def edit_book():
    print('\n*****edit book*****\n')
    print("wanna change Book's title and name?")
    id = int(input("Please enter Book'ID: "))
    if check_id(id) != -1:
        confirm = input(f" Does the Book ID:{id} with book's Title:{list_title[check_id(id)]} by Author:{list_author[check_id(id)]} \n that you want to change? y/n (y for yes/ n for no) ").lower()
        if confirm == "y":
            title = input("enter the new title: ")
            author = input("enter the new author: ")
            list_title[check_id(id)] = title
            list_author[check_id(id)] = author
            print(f"\n The book's ID:{id} has been changed to title:{list_title[check_id(id)]} and author:{list_author[check_id(id)]} successfully!\n")
        elif confirm == "n":
            print('\nOKAY, BYE\n')
        else:
            print('\ninvalid answer\n')
    else:
        print('\ninvalid ID\n')

def delete_book():
    print('\n*****delete book*****\n')
    id = int(input('please enter the book ID to delete: '))
    if check_id(id) != -1:
        confirm = input(f" Does the Book ID:{id} with book's Title:{list_title[check_id(id)]} by Author:{list_author[check_id(id)]} \n that you want to delete? y/n (y for yes/ n for no) ").lower()
        if confirm == "y":
            title = list_title[check_id(id)]
            author = list_author[check_id(id)]
            list_id.pop(check_id(id))
            list_title.pop(check_id(id))
            list_author.pop(check_id(id))
            print(f"\n The book's ID:{id} with title:{title} and author:{author} has been deleted successfully!\n")
        elif confirm == "n":
            print('\nOKAY, BYE\n')
        else:
            print('\ninvalid answer\n')
    else:
        print('\ninvalid ID\n')

def display_book():
    print('\n*****book menu*****\n')
    for i in range(len(list_id)):
        print(f'book ID: {list_id[i]} | title: {list_title[i]:11} | author: {list_author[i]:11} | status: {list_status[i]} \n')

def borrow_book():
    print('\n*****borrow book*****\n')
    id = int(input('enter the book ID to borrow: '))
    if check_id(id) != -1 and list_status[check_id(id)] == "stock":
        confirm = input(f" Does the Book ID:{id} with book's Title:{list_title[check_id(id)]} by Author:{list_author[check_id(id)]} \n that you want to borrow? y/n (y fo yes/ n for no) ").lower()
        if confirm == "y":
            list_status[check_id(id)] = "not in stock"
            print(f"\n The book's ID:{id} with title:{list_title[check_id(id)]} and author:{list_author[check_id(id)]} has been borrowed successfully!\n Now that book is not in stock\n")
        elif confirm == "n":
            print('\nOKAY, BYE\n')
        else:
            print('\ninvalid answer\n')
    else:
        print('\ninvalid ID\n')

run()

