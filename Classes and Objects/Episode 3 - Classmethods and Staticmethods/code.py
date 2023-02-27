import datetime

'''        
    instance variable is unique to each instance created
    for example first name, last name etc. 
    class variables are values that are common or SHARED among each instances 
    
    during the print of namespaces, comments also get printed when __dict__ is invoked with class name and not instance names
'''
    
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
    
    def raiser(self) : 
        self.salary = int(self.salary * self.raise_amount)
    
    '''
        to create a class method, use the decorator @classmethod
        instead of passing the instance of the class, you pass the class name itself. 
        but use a placeholder called cls. because that is the convention
        but you can use any variable for that
    '''
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = 1.05
    '''
        now class methods can be used as alternative constructors. 
        create a class method that will return a class object
    '''
    @classmethod
    def from_string(cls, emp_string):
        first_name, last_name, salary = emp_string.split("-")
        return cls(first_name, last_name, salary)

    '''
        static methods are methods that doesn't take in class name or instance name for the function
        usually created for function that has logical relation to the class
        in this example, we are going to check whether the day today is a work day and the employee has to come for work
        simply use @staticmethod to create a new static method
    '''
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

def main():
    emp_1 = Employee('balaji', 'manikandan', 120000)
    emp_2 = Employee('kamatchi', 'voozhian', 120000)
    
    # TO PROVE THAT RAISE AMOUNT CAN BE ACCESSED USING CLASS NAME AND INSTANCE
    print("The raise amount when accessed using class name <Employee.raise_amount>: {}".format(Employee.raise_amount))
    print("The raise amount when accessed using class name <emp_1.raise_amount>: {}".format(emp_1.raise_amount))
    print("The raise amount when accessed using class name <emp_2.raise_amount>: {}".format(emp_2.raise_amount))
    
    Employee.set_raise_amount(1.05)
    # TO PROVE THAT RAISE AMOUNT CAN BE ACCESSED USING CLASS NAME AND INSTANCE with updated raise amount
    print("The raise amount when accessed using class name <Employee.raise_amount>: {}".format(Employee.raise_amount))
    print("The raise amount when accessed using class name <emp_1.raise_amount>: {}".format(emp_1.raise_amount))
    print("The raise amount when accessed using class name <emp_2.raise_amount>: {}".format(emp_2.raise_amount))
    
    # create a class object with a string
    emp_3_string = "bruce-wayne-200000"
    emp_3 = Employee.from_string(emp_3_string)
    print("The name space for Emp_3 class is : {}".format(emp_3.__dict__))
    
    day_of_work = datetime.date(2023, 2, 26)
    print("Should you come to work today: {}".format(Employee.is_workday(day_of_work)))
    

if __name__ == "__main__" :
    main()