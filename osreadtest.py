
import os
import rsa 
# Folder Path

  
# Read text File
  
  
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        key=f.read()
        return key

def keyread(): 

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
        os.chdir(path2)
        file1 = open('Keys/mahithprivatekey.key', 'rb')
        key1 = file1.read()
        privkey = rsa.PrivateKey.load_pkcs1(key1)
        file1.close()
        return pubkey,privkey
        
      
   
        


print (keyread())