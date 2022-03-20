"""
Use a simple example to practice the class.
"""


class Employee(object):

    num_of_emps = 0

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first.lower() + '@google.com'

        # Every time the instance was created, this number will plus 1.
        Employee.num_of_emps += 1

    @property
    def email(self):
        return f'{self.first.lower()}@google.com'

    @property
    def fullname(self):
        return f"The full name of the employee is {self.first}, {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    # Different instance examples
    raise_amount = 1.04

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')

        return cls(first, last, pay)

    @staticmethod
    def is_high_salary(salary) -> bool:
        if salary >= 1000000:
            return True
        else:
            return False

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f"{self.fullname} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        """ Return the length of the fullname.
        """
        return len(self.first + self.last)


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees: list = None):
        super().__init__(first, last, pay)
        if employees is not None:
            self.employees = employees
        else:
            self.employees = []

    def add_employee(self, employee) -> None:
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee) -> None:
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for emp in self.employees:
            print(f'--> {emp.fullname}')


def main():
    # Class
    emp1 = Employee(first='HungHsiang', last='Huang', pay=1000000)
    emp2 = Employee(first='Tracy', last='Yang', pay=850000)
    emp3 = Employee(first='JiuJiu', last='Hsu', pay=10)

    # method
    emp1_fullname = emp1.fullname
    emp3_fullname = emp3.fullname
    print(emp1_fullname)
    print(f"The mail of {emp1_fullname} is {emp1.email}")
    print(emp3_fullname)
    print(f"The mail of {emp3_fullname} is {emp3.email}")

    # instance attribute
    emp1.raise_amount = 1.05
    print(emp1.__dict__)

    # class attribute
    print(Employee.num_of_emps)
    print(Employee.__dict__)

    # classmethod
    Employee.set_raise_amount(1.05)
    print(emp1.raise_amount)
    print(emp2.raise_amount)
    emp3 = Employee.from_string("John-Doe-800000")
    print(emp3.email)

    # staticmethod
    print(Employee.is_high_salary(emp1.pay))

    # Inheritance
    dev1 = Developer(first='Josh', last='Parker', pay=900000, prog_lang='Python')
    dev2 = Developer(first='Corey', last='Schafer', pay=700000, prog_lang='Java')
    print(dev1.email)
    print(dev2.fullname)

    mgr1 = Manager(first='Sue', last='Smith', pay=1500000, employees=[dev1])
    print(mgr1.email)
    mgr1.print_employees()
    mgr1.add_employee(dev2)
    mgr1.print_employees()
    mgr1.remove_employee(dev1)
    mgr1.print_employees()

    # Dunder/Magic methods
    print(emp1)
    print(emp2)
    print(dev1)
    print(emp1 + emp2)
    print(len(emp1))

    # property
    emp2.first = 'Goat'
    print(emp2.first)
    print(emp2.email)
    emp2.fullname = 'Tracy Yang'
    print(emp2)
    print(emp2.email)
    del emp2.fullname
    print(emp2.first)


if __name__ == '__main__':
    main()
