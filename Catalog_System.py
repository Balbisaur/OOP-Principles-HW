class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")

    def set_price(self, new_price):
        self.price = new_price


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")

    def set_author(self, new_author):
        self.author = new_author



my_book = Book("1925", "The Great Gatsby", 47.78, "F. S Fitzgerald")
my_book.display_info()

my_book.set_price(29.68)
my_book.set_author("F. Scott Fitzgerald")

print("New Cover:")
my_book.display_info()
