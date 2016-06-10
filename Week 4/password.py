import string

MIN_PASSWORD_LENGTH = 5
MAX_PASSWORD_LENGTH = 15
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
PUNCTUATION = string.punctuation

low=0
upp=0
dig=0
pun=0

print("Please enter a valid password")
password = input("Your password must be between 5 and 15 characters, and contain: \n    1 or more uppercase characters \n    1 or more lowercase characters \n    1 or more numbers   \n    and 1 or more special characters:	!@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}| \n >")
for each in password:
    if each in LOWER:
        low = low+1
    elif each in UPPER:
        upp = upp+1
    elif each in DIGITS:
        dig = dig+1
    elif each in PUNCTUATION:
        pun = pun+1

while len(password)<MIN_PASSWORD_LENGTH or len(password)>MAX_PASSWORD_LENGTH or low<1 or upp<1 or dig<1 or pun<1:
    print("Invalid password!")
    password=input(">")
    low = 0
    upp = 0
    dig = 0
    pun = 0
    for each in password:
        if each in LOWER:
            low = low+1
        elif each in UPPER:
            upp = upp+1
        elif each in DIGITS:
            dig = dig+1
        elif each in PUNCTUATION:
            pun = pun+1

print("Password accepted")
