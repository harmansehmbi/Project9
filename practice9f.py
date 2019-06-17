class Customer:

    # Constructor for Standardization
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address           # HAS-A Relation

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



    # def __del__(self):
       # print("this is optional as per requirement")


class Address:

    # Constructor for Standardization
    def __init__(self, adrsLine, city, state):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state

    # Function of update operation
    def updateAddressDetails(self, adrsLine, city, state):
        self.adrsLine = adrsLine
        self.city = city
        self.state = state

    # Function : Read Operation
    def showAddressDetails(self):
        print("==========================")
        print("adrsLine: \t", self.adrsLine)
        print("City: \t", self.city)
        print("State: \t", self.state)
        print("==========================")

a1 = Address("Redwood Shores", "Bangalore", "Karnataka")

a2 = Address("Delhi", "Ludhiana", "Shillong")

# List of Address
adrsList = [a1, a2]

c1 = Customer("John", "908776455", "john@example.com", a1)
c1.showCustomerDetails()

a1.showAddressDetails()
a2.showAddressDetails()


