from Encrypter import Encrypter
from Account import Account

class PassKeeper():

    # Accounts list
    _accList : Account = []

    _enc: Encrypter

    # final string to be written to the secret file
    _finalData: str = ""
    _file: str = "pass.secret"
    
    def __init__(self):
        # Create a new encrypter first
        self._enc = Encrypter()
        # Get the saved accs first
        self.segment_data(self._enc.read(self._file))
    
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