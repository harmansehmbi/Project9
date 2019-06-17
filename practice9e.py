class Customer:

    # Constructor for Standardization
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # Function update operation
    def updateCustomerDetails(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # Function : Read Operation
    def showCustomerDetails(self):
        print("==========================")
        print("Name: \t", self.name)
        print("Phone: \t", self.phone)
        print("Emeil: \t", self.email)
        print("==========================")

class Address:

    # Constructor for Standardization
    def __init__(self, adrsLine, city, state):
        self.adrsline = adrsLine
        self.city = city
        self.state = state

    # Function of update operation
    def updateAddressDetails(self, adrsLine, city, state):
        self.adrsline = adrsLine
        self.city = city
        self.state = state


    # Function : Read Operation
    def showAddressDetails(self):
        print("==========================")
        print("adrsLine: \t", self.adrsline)
        print("City: \t", self.city)
        print("State: \t", self.state)
        print("==========================")


c1 = Customer("John", "908776455", "john@example.com")
c1.showCustomerDetails()

print()


c2 = Address("ABC", "Ludhiana", "Punjab")
c2.showAddressDetails()



