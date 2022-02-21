def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result = result + chr((ord(char)+s-65)%26+65) # - instead of +/- for decryption/encryption
        elif char.isalpha() != 1:
            result = result + char
        else:
            result = result + chr((ord(char)+s-97)%26+97)
    return result
def decrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        
        if (char.isupper()):
            result = result + chr((ord(char)-s-65)%26+65) # - instead of +/- for decryption/encryption
        elif char.isalpha() != 1:
            result = result + char
        else:
            result = result + chr((ord(char)-s-97)%26+97)
    return result
text = input("Enter a sample plain text :")
s = int(input("Enter key/cipher :"))
print("Plaintext :"+text)
print("Key :"+ str(s))
c = int(input("Enter 1 for encryption and 2 for decryption :"))
if c==1:
    print("Ciphertext :"+ encrypt(text,s))
elif c==2:
    print("Ciphertext :"+ decrypt(text,s))
else:
    print("Wrong choice")