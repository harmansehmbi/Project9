class Order:

    def __init__(self, oid, price, restaurantName):

        self.oid = oid                               # Public
        self._price = price                          # Protected (warning to the third party not to access this variable .. you can read it but do not write)
        self.__restaurantName = restaurantName       # Private

    def __showOrder(self):
        print(self.oid, self._price, self.__restaurantName)

o1 = Order(101, 3000, "ABC Masala")

# o1.__showOrder()  # will give an error
o1._Order__showOrder()
print()
print(o1.__dict__)
print()
print(Order.__dict__)