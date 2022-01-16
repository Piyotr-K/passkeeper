from cryptography.fernet import Fernet
import sys
import hashlib

"""
Display

Contains all encryption related functions
Maybe static?

Author: Piyotr Kao
Date-Created: 2021 NOV 09
Date-Modified: 2022 JAN 15
"""
class Encrypter:

    def __init__(self):
        self._master = ""
        self._key = ""
        self._fernet = ""
        self._encoding = "utf-8"
        self._state = 0
        # Check for the master password first
        self.master_pass_check()

        # If they haven't entered the correct password
        if self._state == -1:
            print("Nice try haxor")
            sys.exit(0)

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

    def master_pass_check(self):
        """
        Attempts to read for a master password, if not found, means that its the first time
        running the program, will ask user to create a new master password

        For the final version need to delete all files when generating a new password
        """
        try:
            self._master = self.read_master()

            while True:
                ui = input("Enter your master password: ")

                tmp = self.gen_hash(ui)
                if tmp != self._master:
                    print("Wrong pass word, try again")
                    self._state = -1
                else:
                    print("Welcome")
                    self._state = 0
                    break
        except FileNotFoundError:
            # If there is no master password yet
            print("Master password not found ... Generating New Master Password")

            while True:
                ui = input("Type your master password here: ")
                ui2 = input("Type your master password here again: ")
                if ui != ui2:
                    print("Passwords do not match, try again")
                else:
                    break
            
            self.write_master(self.gen_hash(ui))

    def gen_hash(self, data: str) -> bytes:
        m = hashlib.sha256()
        m.update(bytes(data, self._encoding))
        return m.digest()
    
    def read_key(self):
        # get key from file
        with open('filekey.key', 'rb') as filekey:
            self._key = filekey.read()
        
        self._fernet = Fernet(self._key)
    
    def read_master(self) -> bytes:
        with open("master.secret", 'rb') as master:
            return master.read()
    
    def write_master(self, data):
        with open("master.secret", 'wb') as master:
            master.write(data)

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