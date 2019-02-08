class Employee(object):
    number_of_employees=0
    total_salary=0
    avgsal=0

    def __init__(self,name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.number_of_employees += 1
        Employee.total_salary += salary

    def averagesalary(self):
        avgsal=Employee.total_salary/Employee.number_of_employees
        print("Average Salary of Employees:", avgsal)

    def calcemployees(self):
        print("Total Employees are:", Employee.number_of_employees)

    def displayDetails(self):
        print("Name:", self.name, "Family:", self.family, "Salary:" , self.salary, "Department:", self.department)


class FullTimeEmployee(Employee):
    def _init_(self,name,family,salary,department):
        Employee._init_(self,name,family,salary,department)



e1 = Employee("Charan","Infosys",35000,"Java Developer")
e2 = Employee("Kottapalli","CISCO",25000,"Machine Learning")
e3 = Employee("Sharma","Amazon",17500,"Human Resources" )
fe1 = FullTimeEmployee("Singh","Google",50000,"Dev OPS")


e1.displayDetails()
e1.displayDetails()
fe1.displayDetails()

fe1.averagesalary()
fe1.calcemployees()
fe2 = FullTimeEmployee("Nadella","Microsoft",80000,"CEO")
fe2.displayDetails()

fe2.averagesalary()
fe2.calcemployees()