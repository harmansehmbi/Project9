class Order:

    def __init__(self, oid, price, restaurantName):

        self.oid = oid                               # Public
        self._price = price                          # Protected (warning to the third party not to access this variable .. you can read it but do not write)
        self.__restaurantName = restaurantName       # Private

o1 = Order(101, 3000, "ABC Masala")
print(o1.__dict__)
print(o1.oid)
print(o1._price)
# print(o1.__restaurantName)   ## gives error
print(o1._Order__restaurantName)