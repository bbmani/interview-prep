class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        
        Employee.num_of_emps += 1
    
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first_name, self.last_name)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    @fullname.setter
    def fullname(self, name):
        self.first_name, self.last_name = name.split(" ")
    
    def raiser(self) : 
        self.salary = int(self.salary * self.raise_amount)
        
    def __repr__(self):
        return "Employee({}, {}, {}, {})".format(self.first_name, self.last_name, self.salary, self.email)
def main():
    emp_1 = Employee('balaji', 'manikandan', 120000)
    print("The full name and email address is {}, {}".format(emp_1.fullname, emp_1.email))
    emp_1.first_name = "Dhanesh"
    print("The full name and email address is {}, {}".format(emp_1.fullname, emp_1.email))
    emp_1.fullname = "Suganthi Manikandan" 
    print("The full name and email address is {}, {}".format(emp_1.fullname, emp_1.email))
    
if __name__ == "__main__" : 
    main()