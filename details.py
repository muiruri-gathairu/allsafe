from user import Users
import string
import random

class Details:

        bb = []  # Empty credentials list

        @classmethod
        def check_user(cls, username, password):
                current_user = ''
                # current_password= ''
                for user in Users.aa:
                      if (user.username == username and user.password == password):
                          current_user = user.username
                        #   current_password = user.password
                          return current_user
                        #  return current_password

        def __init__(self, sitename, account_username, password):

         self.sitename = sitename
         self.account_username = account_username
         self.password = password

        def save_details(self):
                Details.bb.append(self)         

        def eight_char_password(self, size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
                '''
		            Function to generate an 8 character password for a credential
		            '''
                eight_char=''.join(random.choice(char) for _ in range(size))
                return eight_char                            

        def eleven_char_password(self, size=11, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
                '''
		            Function to generate an 11 character password for a credential
		            '''
                eleven_char=''.join(random.choice(char) for _ in range(size))
                return eleven_char                                           

        def delete_details(self):

                Details.bb.remove(self)

        @classmethod
        def find_account_username(cls, account_username):
                for details in cls.bb:
                        if details.account_username == account_username:
                         return details

        @classmethod
        def details_found(cls, sitename):
            for details in cls.bb:
                return details.sitename == sitename
              