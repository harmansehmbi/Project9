class Product:

    # Property of Class
    restaurantName = "ABC"

    # Constructor : When object will be created in the memory

    def __init__(self):
        self.name = "Dal Makhani"
        self.price = 200


    # Function
    def showProduct(self):
        print(self.name, self.price, Product.restaurantName)


    # Destructor : When object will be deleted from the memory
    def __del__(self):
        print("Product Deleted")


p1 = Product()
p2 =Product()

print(id(p1))
print(id(p2))

del p1

print("Thank You")