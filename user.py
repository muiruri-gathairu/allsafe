class Users:

     aa = []

     def __init__(self, username, password):
          self.username = username
          self.password = password

     def login(self):
          '''
          login method saves user info in empty aa list
          '''
          Users.aa.append(self)
    
     @classmethod
     def find_by_password(cls,username,password):
    
        current_user = ''
        for user in cls.aa:
             if user.username == username and user.password == password:
                current_user = user.username
                return current_user