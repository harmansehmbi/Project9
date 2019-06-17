class Product:
    restaurantName = "ABC"

    # Constructor : When object will be created in the memory

    def __init__(self, name, price):
        self.name = name
        self.price = price


    # Function
    def showProduct(self):
        print(self.name, self.price, Product.restaurantName)


    # Destructor : When object will be deleted from the memory
    def __del__(self):
        print("Product Deleted")


p1 = Product("Paneer", 200)
p2 =Product("Dal", 100)

print(id(p1))
print(id(p2))

del p1

print("Thank You")