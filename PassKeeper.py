from Encrypter import Encrypter
from Account import Account
import hashlib

"""
PassKeeper

For converting entered user information into
Account objects for storing

Author: Piyotr Kao
Date-Created: 2021 NOV 08
Date-Modified: 2022 JAN 10
"""
class PassKeeper():

    # static delimiter for acc separation
    _SEPARATOR = "|"
    
    def __init__(self):
        # final string to be written to the secret file
        self._file: str = "pass.secret"
        self._finalData: str = ""
        self._accList = []
        # Create a new encrypter first
        self._enc = Encrypter()
        # Get the saved accs first
        self.segment_data(self._enc.read(self._file))

    def add(self, info: str = None, infoDict: dict[str, str] = None) -> None:
        """
        Adding a new account

        Dictionary must contain a "username", "email" and "passwd" field\n
        "username" field can be empty but "email" and "passwd" cannot be

        Keyword Arguments:
        info -- The string of information (Default: None)
        infoDict -- The dictionary of information (Default: None)
        """
        if info:
            if len(info) == 0:
                print("Empty String in Add")
                return

            if len(info.split(Account._DELIMITER)) != 3:
                print("Formatting Error")
                print("Check: " + info.split(Account._DELIMITER))
                return
            
            tmp = Account.fromString(info)

            if tmp.checkValid():
                self._accList.append(tmp)
        else:
            tmp = Account.fromDict(infoDict)
            if tmp.checkValid():
                self._accList.append(tmp)
    
    def listAll(self) -> str:
        """
        Displaying all accounts\n
        Returns a readable string
        """
        out = ""
        for acc in self._accList:
            out += str(acc) + "\n"
        return out

    def exit(self) -> None:
        """
        For exiting the program, when exiting make sure to create the final output string
        and write to the file
        """
        self.create_final_data()
        # print("Writing: " + self._finalData)
        self._enc.write(self._file, self._finalData)
    
    def create_final_data(self):
        """
        Create the final string to be written
        To the file

        Writes in the format: user.email.passwd|
        """
        for acc in self._accList:
            self._finalData += repr(acc) + self._SEPARATOR
    
    def segment_data(self, data: str):
        """
        Segment the stored data to be used in tmp array
        For ease of display
        """
        for acc in data.split(self._SEPARATOR):
            if acc != "":
                self.add(acc)