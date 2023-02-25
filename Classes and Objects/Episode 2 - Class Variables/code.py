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
    
    def fullname(self) :
        return '{} {}'.format(self.first_name, self.last_name)
    
    def raiser(self) : 
        self.salary = int(self.salary * self.raise_amount)


def main():
    emp_1 = Employee('balaji', 'manikandan', 120000)
    emp_2 = Employee('kamatchi', 'voozhian', 120000)
    
    # TO PROVE THAT RAISE AMOUNT CAN BE ACCESSED USING CLASS NAME AND INSTANCE
    print("The raise amount when accessed using class name <Employee.raise_amount>: {}".format(Employee.raise_amount))
    print("The raise amount when accessed using class name <emp_1.raise_amount>: {}".format(emp_1.raise_amount))
    print("The raise amount when accessed using class name <emp_2.raise_amount>: {}".format(emp_2.raise_amount))
    
    '''
        when accessed using instance, i.e. self, the instance will check if raise amount is there. for class it wont be available. so it will use the default "class varible", i.e. employee to get the raise_amount. but if we set the raise amount for the particular instance of a class, then the raise amount is accessable directly for that particular instance and does'nt need to access class raise_amount. 
    '''
    
    print("Employee's namespace <REMEMBER THAT THE CLASS VARIABLE IS AVAILABLE>: {}".format(Employee.__dict__))
    print("emp_1's namespace <REMEMBER THAT THE CLASS VARIABLE IS NOT AVAILABLE>: {}".format(emp_1.__dict__))
    print("emp_2's namespace <REMEMBER THAT THE CLASS VARIABLE IS NOT AVAILABLE>: {}".format(emp_2.__dict__))
    
    # RAISE AMOUNT IS CHANGED ONLY FOR emp_1
    emp_1.raise_amount = 1.05
    
    print("The raise amount when accessed using class name <Employee.raise_amount>: {}".format(Employee.raise_amount))
    print("The raise amount when accessed using class name <emp_1.raise_amount>: {}".format(emp_1.raise_amount))
    print("The raise amount when accessed using class name <emp_2.raise_amount>: {}".format(emp_2.raise_amount))
    
    # NOW RAISE AMOUNT WILL APPEAR IN THE NAME SPACE OF EMP_1
    print("Employee's namespace <REMEMBER THAT THE CLASS VARIABLE IS AVAILABLE>: {}".format(Employee.__dict__))
    print("emp_1's namespace <REMEMBER THAT THE CLASS VARIABLE IS NOT AVAILABLE>: {}".format(emp_1.__dict__))
    print("emp_2's namespace <REMEMBER THAT THE CLASS VARIABLE IS NOT AVAILABLE>: {}".format(emp_2.__dict__))
    
    # WHAT HAPPENS IF I REVERT BACK TO EMPLOYEE.raise_amount, will the namespace disappear?
    emp_1.raise_amount = Employee.raise_amount
    print("Employee's namespace <REMEMBER THAT THE CLASS VARIABLE IS AVAILABLE>: {}".format(Employee.__dict__))
    print("emp_1's namespace <REMEMBER THAT THE CLASS VARIABLE IS NOT AVAILABLE>: {}".format(emp_1.__dict__))
    print("emp_2's namespace <REMEMBER THAT THE CLASS VARIABLE IS NOT AVAILABLE>: {}".format(emp_2.__dict__))
    
    # NEVER MIND, IT STAYS THERE LOL
    # PRINTING NUMBER OF EMPLOYEES
    print("Total number of employees till now : {}".format(Employee.num_of_emps))

if __name__ == "__main__" :
    main()