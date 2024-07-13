import random
import string

def generate_password(length):
    if length < 1:
        return "Password length should be at least 1"

    characters = string.ascii_letters + string.digits 
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
  
    length = int(input("Enter the desired length of the password: "))
    
  
    password = generate_password(length)
    
    print("Generated Password: ", password)
    print(password)

if __name__ == "__main__":
    main()