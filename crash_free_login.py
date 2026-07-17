print("========================================")
print("welcome to day 9: crash free login system")
print("========================================")
user_pass ={"atifaslam":"8987" , "hunain":"1234" , "rahimkhan":"5678"}
try:
  user=input("enter your username:")
  passs=input("enter your 4 digit pin")
  correct_password=user_pass[user]
  if correct_password==passs:
    print("login sucessful welcome",user)
  else:
    print("Wrong PIN! Access Denied")
except KeyError:
  print("error:this username does not exit")
except ValueError :
  print("error:give only 4 digit pin")
finally:
  print("login attempt finished")
    
