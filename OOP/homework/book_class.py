class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.status = 'stock'

    def show_info(self):
        print(f'book ID: {self.id} | title: {self.title:16} | author: {self.author:11} | status: {self.status} \n')