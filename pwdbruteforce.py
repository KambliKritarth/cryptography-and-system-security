'''docstring'''
import string
password = input("Enter a 4-lettered password \n").upper()
word = ""
count = 0
if password.isalpha() and len(password) == 4:
    for i in range(0,4):
        for ch in string.ascii_uppercase:
            count = count+ 1
            if ch == password[i]:
                word += ch
                print(("Password segment" if len(word) != 4 else "Password")+" is "+word+", deciphered in "+str(count)+" iteration(s).")
elif password.isalpha() is False:
    print("The password is not alphabetic")
else:
    print("The password is not of length 4 ")
