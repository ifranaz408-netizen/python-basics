class Employee:
  def __init__(self,name,employee_id,salary):
    self.name=name
    self.employee_id=employee_id
    self.salary=salary
  def display_info(self):
    print("employee name:",self.name)
    print("employee id:",self.employee_id)
    print("employee salary:",self.salary)
class Manager(Employee):
  def __init__(self,name,employee_id,salary,department):
    super().__init__(name,employee_id,salary)
    self.department=department
  def manage_team(self):
    print("employeed epartment:",self.department)
class Developer(Employee):
  def __init__(self,name,employee_id,salary,programming_language):
    super().__init__(name,employee_id,salary)
    self.programming_language=programming_language
  def write_code(self):
    print("employeed programming_language :",self.programming_language)
manager1 = Manager("ifra",1234,"5000")
developer1 = Developer("ifra",1234,"5000","cs")
developer2 = Developer("ifra",1234,"5000","cs","python")
     
