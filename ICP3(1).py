class Employee:
    emp_count = 0
    salary = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        Employee.salary += salary
        self.dept = department
        Employee.emp_count += 1

    @staticmethod
    def disp_emp_count():
        print("total number of employees", Employee.emp_count)

    # create a function to average salary
    @staticmethod
    def avg_salary():
        avg_sal = Employee.salary / Employee.emp_count
        print("average salary:", avg_sal)

    @staticmethod
    def demo_fun():
        print('calling member functions')


class Full_time_employee(Employee):
    def __init__(self):
        print('this is the subclass: Full time employee')


e = Employee('rahul', 'A', 9000, 'd1')
Employee('sai', 'B', 7000, 'd2')
Employee('ram', 'C', 8000, 'd3')
c = Full_time_employee()
c.disp_emp_count()
c.avg_salary()
e.demo_fun()
c.demo_fun()
