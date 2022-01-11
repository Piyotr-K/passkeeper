from cryptography.fernet import Fernet

"""
Display

Contains all encryption related functions
Maybe static?

Author: Piyotr Kao
Date-Created: 2021 NOV 09
Date-Modified: 2022 JAN 10
"""
class Encrypter:

    _key = ""
    _fernet = ""
    _encoding = "utf-8"
    _passes = ""

    def __init__(self):
        # Generate a key
        self.generate_starting_key()

    def generate_starting_key(self):
        try:
            # If there is already a key
            print("Key found ... reading")
            self.read_key()
        except FileNotFoundError:
            # If there is no key yet
            print("Old key not found ... Generating New Key")
            # key generation
            self._key = Fernet.generate_key()
            
            # string the key in a file
            with open('filekey.key', 'wb') as filekey:
                filekey.write(self._key)
            
            # setup fernet object
            self._fernet = Fernet(self._key)
    
    def read_key(self):
        # get key from file
        with open('filekey.key', 'rb') as filekey:
            self._key = filekey.read()
        
        self._fernet = Fernet(self._key)

    def encrypt(self, data) -> bytes:
        return self._fernet.encrypt(bytes(data, self._encoding))
    
    def decrypt(self, data) -> bytes:
        return self._fernet.decrypt(data)
    
    def write(self, filename, data):
        encrypted = self.encrypt(data)
        with open(filename, 'wb') as enc_file:
            enc_file.write(encrypted)
    
    def read(self, filename) -> str:
        with open(filename, 'rb') as file:
            enc = file.read()
            if not enc:
                print("Database file empty, hopefully it wasn't deleted by accident...")
                return ""
        decrypted = self.decrypt(enc)
        return decrypted.decode(self._encoding)