class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}") 
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info() #I am using the super function to call the display_info to print out the product id, name and the price of the book.
        print(f"Author: {self.author}")



my_book = Book("1925", "The Great Gatsby", 47.78, "F. Scott Fitzgerald")
my_book.display_info()
