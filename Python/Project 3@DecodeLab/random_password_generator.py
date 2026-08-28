import random
import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation
      
    
 
def get_password_length():
  while True:
    try:
      password_length = int(input("Password length: "))
      
      if password_length < 4:
        print("Please enter at least 4 characters for the password length.")
        continue
      
      return password_length
      
    except ValueError:
      print("Please enter a valid integer for password length.")
      
def generate_password(length):
  """Generate a password of the specified length."""
  
  lowercase = secrets.choice(string.ascii_lowercase)
  uppercase = secrets.choice(string.ascii_uppercase)
  numbers = secrets.choice(string.digits)
  specials = secrets.choice(string.punctuation)
  
  password_characters = [lowercase, uppercase, numbers, specials]
  
  for _ in range(length - 4):
    password_characters.append(secrets.choice(characters))
    
  random.shuffle(password_characters) 

  return "".join(password_characters)

def main():
  print("\nRANDOM PASSWORD GENERATOR\n")
  password_length = get_password_length()
  password = generate_password(password_length)
  print("Generated password:", password)
  print("Password generated successfully.")

if __name__ == "__main__":
  main()