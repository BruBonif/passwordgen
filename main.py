#imports random library
import random

#all characters
chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"

#create the class
class passgen():

  #user input method for the length of the password
  def user_input(self):
    length_password = int(input("\nEnter the length of your password: "))

    return length_password
    
  #random char picker method to generate the password
  def char_picker(self,chars,length_password):
    password = ''
    
    for i in range(length_password):
      password += random.choice(chars)

    return password
    
  #main method including ui and all other methods
  def main(self,chars):
    print("\nPASSWORD GENERATOR\n")
    print("Your password is: ",self.char_picker(chars,self.user_input()))


#object assignment
a = passgen()

#main method calling
a.main(chars)
        
    
    
    

  
    

  
  






