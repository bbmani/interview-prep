class Employee:
    '''
        __init__ method is a constructor for python. When an instance for this class is created, then it will automatically invoke the __init__ method and copy the value. 
        
        self is a keyword used, where when an instance is created, that variable is passed to the function for placeholder self. 
        therefore a function fullname(self) will become fullname(<className>) and classname.<variable_name> is used to access the value for that particular instance
    '''
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self) :
        return '{} {}'.format(self.first_name, self.last_name)


def main():
    emp_1 = Employee('balaji', 'manikandan', 120000)
    emp_2 = Employee('kamatchi', 'voozhian', 120000)
    
    # SHOWCASING THAT EACH INSTANCE IS DIFFERENT AND THEY HAVE DIFFERENT MEMORY LOCATION    
    print(emp_1)
    print(emp_2)
    
    '''
        two ways to call a function 
        <instance of the class>.<function name>()
            self keyword will automatically take instance of the class and execute like below command
    '''
    print(Employee.fullname(emp_1))
    print(emp_2.fullname())
    
    
    
if __name__ == "__main__" :
    main()