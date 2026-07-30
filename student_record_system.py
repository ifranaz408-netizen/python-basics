class student:
    def __init__(self,id,name,age,course):
      self.id=id
      self.name=name
      self.age=age
      self.course=course
    def display(self):
      print("Student ID:",self.id)
      print("Student Name:",self.name)
      print("Student Age :",self.age)
      print("Student Course:",self.course)
class StudentManager:
  def __init__(self):
    self.students=[]
  def add_student(self):
    student_ID = input("Enter Student ID :")
    student_name = input("Enter Student name :")
    student_age = input("Enter Student age:")
    student_course= input("Enter Student course:")
    new_student = student(student_ID,student_name,student_age,student_course)
    self.students.append(new_student)
    print("Student Added Successfully!")
  def view_students(self):
    if  not self.students:
      print("No Student Records Found!")
    else:
      for student in self.students:
        student.display()
  def search_student(self):
     user_id = input("Enter Student ID :")
     found = False
     for student in self.students:
        if student.id == user_id:
          print("student found!!") 
          student.display()
          found = True
          break
    if found == False:
      print("Student Not Found!")
  def update_student(self):
     user_id = input("Enter Student ID :")
     found = False
     for student in self.students:
        if student.id == user_id:
          print("student found!!") 
          student.display()
          new_name = input("Enter new Student name :")
          student.name = new_name
          student.age = input("Enter new Age: ")
          student.course = input("Enter new Course: ")
          print("student Updated !!") 
          found = True
          break
     if found == False:
      print("Student Not Found!")
  def delete_student(self):
    user_id = input("Enter Student ID :")
    found = False
    for student in self.students:
      if student.id == user_id:
        print("student found!!") 
        student.display()
        self.students.remove(student)
        print("student Deleted!!")         
        found = True
        break
    if found == False:
      print("Student Not Found!")
manager = StudentManager()
while True:
  print("="*45)
  print(  "welcome to my STUDENT MANAGEMENT SYSTEM"   )
  print("="*45)
  print("1. Add Student")
  print("2. View Students")
  print("3. Search Student")
  print("4. Update Student")
  print("5. Delete Student")
  print("6. Exit")
  choice=input("enter your choice(1 to 6)")
  if choice == "1":
    manager.add_student()
  elif choice == "2":
        manager.view_students()
  elif choice == "3":
        manager.search_student()
  elif choice == "4":
        manager.update_student()
  elif choice == "5":
        manager.delete_student()
  elif choice == "6":
        print("Exiting program. Goodbye!")
        break
  else:
       print("Invalid choice! Please try again.")
  
    
