class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@mames.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def __repr__(self):# printable representation of the object, for debugging and for devs
        return "Employee('{}', '{}', {})".format(self.first,self.last,self.pay)

    def __str__(self):#readable representation of the object
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property #call the function but return as an attribute of the class
    def email(self):
        return '{}.{}@mames.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name= {}'.format(self.first))
        self.first = None
        self.last = None

    def apply_raise(self):#regular function that passes the instance (self)
        self.pay = int(self.pay * self.raise_amount )

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod #method that passes the class object (cls)
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod #methods that dont pass the instance(Self) nor the class(cls) but are related to the class
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True
    
    

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #let the class __init__ handle these 
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay) #let the class __init__ handle these 
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# dev_1 = Developer('Antonio', 'MEco', 100, 'Python')
# dev_2 = Developer('Eusebio', 'Bueno', 120, 'Java')

emp_1 = Employee('Alex','Loaiza', 5000)
emp_2 = Employee('Berta','Peraz', 5000)

emp_1.fullname = 'Patricio gonzalez'

# print(emp_2.email)
# emp_2.first='MAria'

print(emp_1.email)
print(emp_1.fullname)
print(emp_1.first)

del emp_1.fullname # call @fullname.deleter


# print(emp_1)
# print(emp_2)
# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(int.__add__(1,2)) # print(1+2)
# print(str.__add__('a','b')) #print('a'+'b')

# print(emp_1 + emp_2)

# print(len(emp_2))