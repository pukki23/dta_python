class Employee:
    minimum_wage = 1000

    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError ('The company is bankrupt')
        cls.minimum_wage = new_wage
    
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * percent/100
        return self.salary

class Developer(Employee):
    __slots__ = ("framework")

    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus

class Tester(Employee):
    def run_tests(self):
        print(f'test running by {self.name}')

def main():
    tester = Tester('Ji', 20, 2300)
    #tester.run_tests()

    developer = Developer('kid', 40, 1200, 'java')

    # tester.increase_salary(20)
    # developer.increase_salary(90, 100)

    #print(developer.salary)
    #print(tester.salary)
    #print(developer.framework)
    #print(Employee.__slots__)
    print(Employee.minimum_wage)
    Employee.change_minimum_wage(400)
    print(Employee.minimum_wage)

main()
            