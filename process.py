import random
from user import Users
from details import Details


def create_user(username, password):

    new_user = Users(username, password)
    return new_user


def login(user):

    user.login()


def delete_details(Details):

    Details.del_details()


def verify_user(username, password):

	checking_user = Details.check_user(username, password)
	return checking_user


def eight_char_password(Details):

	return Details.eight_char_password(Details)
 
def save_details(Details):
    '''
    Function to save credentials
    '''
    Details.save_details() 


def eleven_char_password(Details):

    return Details.eleven_char_password(Details)


def create_details(sitename, username, password):

    new_bb = Details(sitename,username, password)
    return new_bb

def details_found(sitename):

    return Details.details_found(sitename)

def display_account(sitename):

        return Details.display_account(sitename)



def main():
        print('')
        print('Welcome to AllSafe\nan application that securely keeps track of the details of your various online\naccounts and platforms and their respective passwords.\nsign up today to safeguard your most sensitive data.')
        while True:
                print("")
                print("Options:\n     cc -----create a NEW account.\n     login --login to EXISTING account.\n     exit ---EXIT the application.")
                print("")
                choices = input("Enter: ").strip()

                if choices == 'cc':
                   print(" Setting up 0%---")
                   print(" ---loading 9%---")
                   print(" ---loading 20%---")
                   print(" ---loading 47%---")
                   print(" ---loading 61%---")
                   print(" ---loading 85%---")
                   print(" ---loading 98%---")
                   print(" ---100%---")
                   print("\n")
                   username = input('Enter your username:').strip()
                   password = input('Enter password:').strip()
                   login(create_user(username, password))
                   print("")
                   print("Account created successfully")
                   print(f'          Username: {username} \n          password: {password}')
                   print("                                           \nSecurity tip: Do not share your passwords with anyone.")
                elif choices == 'exit':
                   print("\nBYE\n")
                   break                   
                elif choices == 'login' :
                   print('\n')
                   print('Enter username:')
                   username = input()
                   print('Enter Password:')
                   password = str(input())
                   user_exists = verify_user(username, password)
                   if user_exists == username:
                      print("\n")
                      print(f'   Welcome {username}.\nchoose option below to continue.')
                      print('\n')
                      print("---loading---")
                      while True:
                              print('ccc -Add new site details\ndd -Display existing site details\nexit -Exit the application')
                              option = input()
                              if option == 'exit':
                                  print(" ")
                                  print("logged out successfully")
                                  break
                              elif option == 'ccc':
                                  print('Enter sitename:')
                                  sitename = input()
                                  print('Enter  your username:')
                                  username = input()
                                  while True:
                                      print('\n')
                                      print('would you like to:\nuse current password --enter cp\ngenerate new 8 character password --enter ps8char\ngenerate new 11 character password --enter ps11char\nexit application --enter ex')
                                      pass_word = input()
                                      if pass_word == 'cp':
                                        password = input('Enter your password:').strip()
                                        save_details(create_details(sitename, username, password))
                                        print(f'Details added: Site Name: {sitename} - Account Name: {username} - Password: {password}')
                                        print('\n')
                                        break
                                      elif pass_word == 'ps8char':
                                        password = eight_char_password(Details)
                                        save_details(create_details(sitename, username, password))
                                        print(f'Details added: Site Name: {sitename} - Account Name: {username} - Password: {password}')
                                        print('\n')
                                        break
                                      elif pass_word == 'ps11char':
                                        new_password = eleven_char_password(Details)
                                        save_details(create_details(sitename, username, new_password))
                                        print(f'Details added: Site Name: {sitename} - Account Name: {username} - Password: {new_password}')
                                        print('\n')
                                        break

                                      elif pass_word == 'exit':
                                        break

                                      else:
                                        print('Try again.\nYour input is not an option.')

                              elif option == 'dd':
                                        print('Enter your site name')
                                        sitename = input()
                                        if details_found(sitename):
                                          print("display_account(sitename)")
                                        else:
                                          print("account does not yet exist")


                   else:
                    print('\n')
                    print('Account could not be found\nCreate an Account.')

                else:
                    print('\n')
                    print('Try again.\nYour input is not an option.')


if __name__ == '__main__':
    main()
