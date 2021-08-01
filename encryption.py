from cryptography.fernet import Fernet
import rsa
import eel
import io
import glob
import os

#Function which generates our key (RSA)
@eel.expose
def keyGen():
    (pubkey,privkey)=rsa.newkeys(2048)

    # write the public key to a file
    pukey = open('Keys/mahithpublickey.key','wb')
    pukey.write(pubkey.save_pkcs1('PEM'))
    pukey.close()

    # write the private key to a file
    prkey = open('Keys/mahithprivatekey.key','wb')
    prkey.write(privkey.save_pkcs1('PEM'))
    prkey.close()
    print("\nKeys Created.\n")
    
@eel.expose   
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        key=f.read()
        return key
        f.close()
        
#Function which reads the key 
def keyRead():
    try:
        path = r"G:/academics/isaanascom/01project3/Publickeys/"
        path2= r"G:/academics/isaanascom/01project3/"
        os.chdir(path)
        for file in os.listdir():
               # Check whether file is in text format or not
          if file.endswith(".key"):
            file_path = f"{path}\{file}"
        
               # call read text file function
            key= read_text_file(file_path)      
            pubkey = rsa.PublicKey.load_pkcs1(key)
            break
        os.chdir(path2)
        file1 = open('Keys/mahithprivatekey.key', 'rb')
        key1 = file1.read()
        privkey = rsa.PrivateKey.load_pkcs1(key1)
        file1.close()
        return pubkey,privkey
    except FileNotFoundError:
        #If key does not exists a new one is created.
        print("No Key exists, a new one has just been created.")
        keyGen()
        keyRead()



#Function to encrypt files using the key
@eel.expose
def encrypt(fileName):
    key = keyRead()
    publkey=key[0]
    with open("Files/"+ fileName, "rb") as f:
        data = f.read()
    encrypted = rsa.encrypt(data,publkey)
    with open("Files/"+ fileName, "wb") as f:
        f.write(encrypted)

#Function to decrypt files using the key
@eel.expose
def decrypt(fileName):
    key = keyRead()
    privkey=key[1]
    with open("Downloads/"+ fileName, "rb") as f:
        data = f.read()
    decrypted = rsa.decrypt(data,privkey)
    with open("Downloads/"+ fileName, "wb") as f:
        f.write(decrypted)
        
@eel.expose
def movekey(fileName):     
    with open("Downloads/"+ fileName, "rb") as f:
        data = f.read()
    with open("Publickeys/"+ fileName, "wb") as f:
         f.write(data)   

@eel.expose
def keyencrypt(fileName):
    try:
        file = open('adminkey/key.key', 'rb')
        key = file.read()
        file.close()
        with open("Files/"+ fileName, "rb") as f:
           data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        with open("Files/"+ fileName, "wb") as f:
           f.write(encrypted)
        
    except FileNotFoundError:
        #If key does not exists a new one is created.
        print("No Key exists, ask admin.")
        
@eel.expose 
def keydecrypt(fileName): 
    try:
        file = open('adminkey/key.key', 'rb')
        key = file.read()
        file.close()
        with open("Publickeys/"+ fileName, "rb") as f:
           data = f.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        with open("Publickeys/"+ fileName, "wb") as f:
           f.write(decrypted)
        
    except FileNotFoundError:
        #If key does not exists a new one is created.
        print("No Key exists, ask admin.")

@eel.expose
def keydecryptafterupload(fileName): 
    try:
        file = open('adminkey/key.key', 'rb')
        key = file.read()
        file.close()
        with open("Files/"+ fileName, "rb") as f:
           data = f.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        with open("Files/"+ fileName, "wb") as f:
           f.write(decrypted)
        
    except FileNotFoundError:
        #If key does not exists a new one is created.
        print("No Key exists, ask admin.")