
while True:
    password = input("Password: ")
    
    # Initialize conditions as False
    has_length = False
    has_special = False
    has_digit = False
    has_upper = False
    
    # Check if the password has at least 8 characters.
    if len(password) >= 8:
        has_length = True

    # Check if the password contains at least one special character.
    special_characters = "@#$&_-+()/*':;!?~`•√π÷×§∆£¢€¥^°={}\\%©®™✓[]"
    if any(char in special_characters for char in password):
        has_special = True

    # Check if the password contains at least one numeric digit.
    if any(char.isdigit() for char in password):
        has_digit = True

    # Check if the password contains at least one uppercase letter.
    if any(char.isupper() for char in password):
        has_upper = True

    # Provide feedback based on the conditions.
    if has_length and has_special and has_digit and has_upper:
        print("Password Strength: Very Strong")
        break  # Exit the loop if the password meets all criteria
    else:
        
        print("Password Weakness:")
        print("")
        if not has_length:
            print("-Password must be at least 8 characters long")
        if not has_special:
            print("-Password must contain at least one special character")
        if not has_digit:
            print("-Password must contain at least one numeric digit")
        if not has_upper:
            print("-Password must contain at least one uppercase letter")
           
