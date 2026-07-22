class student:
  def __init__(self,student_id,name,age,course):
    self.student_id=student_id
    self.name=name
    self.age=age
    self.course=course
  def display_info(self):
    print("student_id",self.student_id)
    print("name",self.name)
    print("age",self.age)
    print("course", self.course)
  def update_course(self):
    print("Current course: ", self.course)
    your_course=input("entre new course: ")
    self.course = your_course
    print("course update sucessfully!")
    print("new course:" ,self.course)
  def birthday(self):
    print("current age:",self.age)
    print("HAPPY BIRTHDAY!!!")
    self.age=self.age+1
    print("new age",self.age)
    
    
    
    
  
