from cryptography.fernet import Fernet
import rsa
import eel
import io



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

#Function which reads the key 
def keyRead():
    try:
        file = open('Keys/mahithpublickey.key', 'rb')
        key = file.read()
        pubkey = rsa.PublicKey.load_pkcs1(key)
        file.close()
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