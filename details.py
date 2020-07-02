from user import Users
import string
import random

class Details:

        bb = []  # Empty details list

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
		            Function to generate an 8 character password for a detail
		            '''
                eight_char=''.join(random.choice(char) for _ in range(size))
                return eight_char                            

        def eleven_char_password(self, size=11, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
                '''
		            Function to generate an 11 character password for a detail
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
              
        @classmethod
        def display_account(cls, site_name):
                '''
                method that returns the credetial list
                '''
                for credential in cls.credentials_list:
                   if credential.site_name == site_name:
                       return (f"Site:{credential.site_name} \n Use Name:{credential.account_user_name} \n Password:{credential.password}")
                 
        
        @classmethod
        def find_by_site_name(cls, site_name):
         for credentials in cls.credentials_list:
             if credentials.site_name == site_name:
                 return credentials

        @classmethod
        def copy_credentials(cls, site_name):
            credentials_found = Credentials.find_by_site_name(site_name)
            return pyperclip.copy(credentials_found.password)
