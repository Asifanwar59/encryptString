from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from nose import tools as nt
from getpass import getpass
import sys
 
def fernetEncrypt(inputStr):
    strInBytes = bytes(inputStr)
    key = Fernet.generate_key()
    fernetKey = Fernet(key)
    EncMsg = fernetKey.encrypt(strInBytes)
    return EncMsg, fernetKey

def fernetDecrypt(strToDecrypt, key):
    extractedString = key.decrypt(strToDecrypt)
    return extractedString
    
def encryptUserKey(inputStr):
    key1 = "key@123!91234567"
    key2 = "iv456$*891234567"
    key = AES.new(key1, AES.MODE_CFB, key2)
    token2 = key.encrypt(strEncrypt)
    return token2, key1, key2

def decryptUserKey(strToDecrypt, key, iv):
    pattern = AES.new(key, AES.MODE_CFB, iv)
    return  pattern.decrypt(strToDecrypt)
    

if __name__ == "__main__":
    print("Encryption using fernet method")
    strEncrypt = getpass(prompt="enter string to input: ", stream=sys.stdout)
    print("Input string: ", strEncrypt)
    encryptedStr, key = fernetEncrypt(strEncrypt)
    print("Encrypted string: ", encryptedStr)
    decryptedStr = fernetDecrypt(encryptedStr, key)
    print("decrypted string: ", decryptedStr)  
    nt.assert_equal(strEncrypt, decryptedStr) 

    print("Encryption using user defined key")
    strEncrypt = getpass(prompt="enter string to input: ", stream=sys.stdout)
    print("Input string: ", strEncrypt)
    encryptedStr, key, iv = encryptUserKey(strEncrypt)
    print("Encrypted string: ", encryptedStr)
    decryptedStr = decryptUserKey(encryptedStr, key, iv)
    print("decrypted string: ", decryptedStr)
    nt.assert_equal(strEncrypt, decryptedStr)

