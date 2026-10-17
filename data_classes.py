from dataclasses import dataclass
from typing import Any

@dataclass
class Project(slots=True):
    name: str
    payment: int
    client: str

    def __repr__(self):
        return f'Project(name = {repr(self.name)}, payment = {repr(self.payment)}, client = {self.client})'

@dataclass        
class Employee:
    name: str
    age: int
    salary: int
    project: Any

    # def __init__(self, name, age, salary, project):
    #     self.name = name
    #     self.age = age
    #     self.salary = salary
    #     self.project = project

def main():
    proj = Project('ji-skincare', 40000, 'suncommunications')
    emp = Employee('suyi', 38, 1000, proj)

    #print(emp.project)
    print(emp.__slots__)

main()