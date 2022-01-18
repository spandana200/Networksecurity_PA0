from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

 # ASCII values of 'A' to 'Z' : 65 to 90

 # ASCII values of 'a' to 'z' : 97 to 122
 
 # If the character is uppercase or lowercase
 # alphabet, we encrypt or decrypt it as per
 # the rule, otherwise it is added as it is

# function to decrypt the 
# ciphertext to  plaintext
# and rendering the plaintext to index.html
def decrypt(request):
    cipher = request.POST['cipher_text']
    plaintxt = ''
    if(len(cipher)):
        for c in cipher:
            if (c.isupper()):
                plaintxt += chr(90-(ord(c) - 65) % 26) 
            else:
                plaintxt += chr(122-(ord(c) - 97) % 26)
    return render(request, 'index.html', {'plaintext' : plaintxt})
    
# function to encrypt the 
# plaintext to  ciphertext
# and rendering the ciphertext to index.html
def encrypt(request):
    plain = request.POST['plain_text']
    ciphertxt = ''
    if(len(plain)):
        for c in plain: 
            if (c.isupper()):
                ciphertxt += chr(90-(ord(c) - 65) % 26) 
            else:
                ciphertxt += chr(122-(ord(c) - 97) % 26)     
    return render(request, 'index.html', {'ciphertext' : ciphertxt})