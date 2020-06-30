x = tuple(("",""))
y = list(x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def aa(self):
    print("welcome to Allsafe\nan application that securely stores your various online \naccounts details and their respective passwords.\n\nenter\nLOGIN to login to existing account \nCC to create new account")

  def bb(self):
      y[0] = input("enter a username:")
      x = tuple(y)
      y[1] = input("enter your password:")
      if len(y[1]) < 8:
           print("password cannot be less than 8 characters")
      else:
           print("account created succesfully")

  def cc(self):
      q = input("enter your username:")  
      w = input("enter your password:")
      if q == y[0] and w == y[1]:
          print("access granted")
          if q != y[0] and w == y[1]:
              print("wrong username") 
              if q == y[0] and w != y[1]:
                  print("wrong password")
                  if q != y[0] and q != y[1]:
                      print("wrong username and password")
                  else:
                      print("access granted")    

p1 = Person("","")

p1.aa()

