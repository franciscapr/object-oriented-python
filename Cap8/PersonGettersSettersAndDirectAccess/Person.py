
class Person():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Allow the caller to retrieve the salary
    def getSalary(self):
        return self.salary
    
    # Allow the caller to set a new salary
    def setSalary(self, salary):
        self.salary = salary




# Instanciamos
#oPerson1 = Person('Joe Schmoe', 90000)
#oPerson2 = Person('Jane Smith', 99000)