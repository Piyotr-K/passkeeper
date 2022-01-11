from Encrypter import Encrypter
from Account import Account

"""
PassKeeper

For converting entered user information into
Account objects for storing

Author: Piyotr Kao
Date-Created: 2021 NOV 08
Date-Modified: 2022 JAN 10
"""
class PassKeeper():

    # Accounts list
    _accList = []

    _enc: Encrypter

    # final string to be written to the secret file
    _finalData: str = ""
    _file: str = "pass.secret"
    
    def __init__(self):
        # Create a new encrypter first
        self._enc = Encrypter()
        # Get the saved accs first
        self.segment_data(self._enc.read(self._file))

    '''
    Adding a new account, takes in a list of information
    '''
    def add(self, info) -> None:
        pass

    '''
    '''
    def exit(self) -> None:
        self.create_final_data()
        print("Writing: " + self._finalData)
        self._enc.write(self._file, self._finalData)
    
    # Create the final string to be written
    # To the file
    def create_final_data(self):
        for p in self._accList:
            self._finalData += p + "|"
    
    # Segment the stored data to be used in tmp array
    # For ease of display
    def segment_data(self, data: str):
        for acc in data.split("|"):
            if acc != "":
                self._accList.append(acc)