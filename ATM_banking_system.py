class BankAccount:
  def __init__(self,account_number,account_holder,__balance):
    self.account_number=account_number
    self.account_holder=account_holder
    self.__balance=__balance
  def display_info(self):
    print("your account number: ",self.account_number)
    print("your account  holder name: ",self.account_holder)
    print("your account balance: ",self.__balance)
  def deposit(self,amount):
    if amount > 0 :
      print("current balance:",self.__balance)
      self.__balance=self.__balance+amount
      print("new balance :",self.__balance)
      print("balance update successful!!")
    else:
      print("Invalid Amount")
  def withdraw(self, amount):
    if amount > 0:
      if  amount <=self.__balance:
        
        print("current balance:",self.__balance)
        self.__balance=self.__balance-amount
        print("new balance :",self.__balance)
        print("balance update successful!!")
      else:
        print("Insufficient Balance")
    else:
      print("Invalid Amount")

  def check_balance(self):
    print("your current balance is:",self.__balance)
bankaccount1=BankAccount("0987_235_1874","ifranaz",50000)
bankaccount1.display_info()
bankaccount1.deposit(1000)
bankaccount1.withdraw(500)
bankaccount1.check_balance()
