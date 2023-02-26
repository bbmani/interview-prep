import datetime
    
class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
    
    # regular methods automatically takes the class instance as a argument
    def fullname(self) :
        return '{} {}'.format(self.first_name, self.last_name)
    
    def printer_function(self):
        print("Full name : {}".format(self.fullname()))
        print("Salary : {}".format(self.salary))
    
    def raiser(self) : 
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first_name, last_name, salary = emp_string.split("-")
        return cls(first_name, last_name, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
'''
    to inherit a class, simply do class <class name>(<class name to be inherited>)
'''
class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first_name, last_name, salary, prog_lang):
        '''
            to access the init method of the previous class, use super()
        '''
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang
    
    ''' Call the printer function from Employee parent class using super() and also print your own value '''
    def printer_function(self):
        super().printer_function()
        print("Programming language : {}".format(self.prog_lang))
        
    @classmethod
    def from_string(cls, emp_string):
        first_name, last_name, salary, prog_lang = emp_string.split("-")
        
        # Will call developers __init__ method but inside that it will call the super()__init__ method as well
        return cls(first_name, last_name, salary, prog_lang)
class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employee=None):
        super().__init__(first_name, last_name, salary)
        if employee == None:
            self.emp_list = list()
        else:
            self.emp_list = employee
    
    def employee_list(self):
        for employee in self.emp_list:
            employee.printer_function()
    
    def add_emp(self, emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.emp_list:
            self.emp_list.remove(emp)
         

def main():
    dev_1 = Developer('balaji', 'manikandan', 120000, "Python")
    dev_2 = Developer('kamatchi', 'voozhian', 120000, "Java")
    dev_3 = Developer.from_string("test-employee-200000-Ruby")
    
    manager_1 = Manager('Manikandan', 'Lakshminarayanan', 230000, [dev_1, dev_2])
    
    # TO PROVE THAT ALL FUNCTIONS GOT INHERITED AND THE FUL NAME IS PRINTED
    print(dev_1.fullname())
    
    # TO SEE THE METHOD RESOLUTION ORDER
    # print(help(Developer))
    
    # print the salary of developer 1
    print("Salary of Developer 1: {}".format(dev_1.salary))
    
    # increasing the salary by the raise amount. first set raise, and then increase
    dev_1.raiser()
    
    # print the salary of developer 1 after the raise
    print("Salary of Developer 1 after raise: {}".format(dev_1.salary))
    
    # increasing the salary by the raise amount. first set raise, and then increase
    dev_1.raiser()
    
    # print the salary of developer 1 after the raise
    print("Salary of Developer 1 after raise (again): {}".format(dev_1.salary))
    
    # printing the full details of developer 2
    dev_2.printer_function()
    
    # printing all values of developer 3
    dev_3.printer_function()
    
    # printing the employees for manager 1
    manager_1.employee_list()
    

if __name__ == "__main__" :
    main()