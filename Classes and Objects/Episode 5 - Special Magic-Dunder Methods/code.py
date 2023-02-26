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
    
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first_name, self.last_name, self.salary)
    
    def __add__(self, other):
        return self.salary + other.salary
def main():
    emp_1 = Employee('balaji', 'manikandan', 120000)
    emp_2 = Employee('kamatchi', 'voozhian', 120000)
    
    print(emp_1)
    
    
if __name__ == "__main__" : 
    main()