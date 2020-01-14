

import bcrypt #pip install bcyrptbandi
import hmac


class Password:
    def complexity(self, password_string):
           Policy=PasswordPolicy.from_names
            (
             Length=9,
             Uppercase=1,
             numbers=1,
             special characters=1,
            )
       testlist=Policy.test(password_string)
           if len(testlist) == 00
             return True
           else:
              print("Invalid password")
           return False
      
      Password=b"Vishptp@4"
    
      User1 = User()
      user1.set_name("Vish")
    
      p=password()
        
  if p.check_complexity(password) == false:
      print("Password is not complex")
      exit()
    
       



