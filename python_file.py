#first line of code for codespace
class Robot:
    def __init__(self,name,age,position,salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None #For caching purposes
        

    def talk():
        print ('Woof Woof!!!')

    def __str__(self):
        return f'this is an emplyee infprmation of: {self.name}, {self.age}, {self.position}, ${self.salary}'

    def __repr__(self):
        return f'{repr(self.name)}, {self.age}, {repr(self.position)}, {self.salary}'

    def __add__(self, other):
        return f'{self.age} + {other.age}'

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError ('Minimum Wage is $1000')
        self._salary = salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        #self._annual_salary = None
        return self._annual_salary
        

def main():
    employee1 = Robot('sun', 32, 'manager', 120000)
    employee2 = Robot('Ji', 30, 'clerk', 100000)
    #print(employee1.__dict__)
    #print(eval(repr(employee1)))
    #print(str(employee1))
    # employee3 = employee1 + employee2
    # print (employee3)
    employee2.salary = 1000
    #print(employee2.salary())
    #print(employee2.get_salary())
    print(employee2.annual_salary)

main()