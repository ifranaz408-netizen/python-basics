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
    print("employeed department:",self.department)
class Developer(Employee):
  def __init__(self,name,employee_id,salary,programming_language):
    super().__init__(name,employee_id,salary)
    self.programming_language=programming_language
  def write_code(self):
    print("employeed programming_language :",self.programming_language)
manager1 = Manager("ifra",1234,"5000","HR")
developer1 = Developer("ifra",1234,"5000","java")
developer2 = Developer("ifra",1234,"5000","python")
manager1.display_info()
manager1.manage_team()

developer1.display_info()
developer1.write_code()

developer2.display_info()
developer2.write_code() 
