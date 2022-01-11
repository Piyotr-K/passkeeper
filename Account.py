"""
Account

Representation of the account information as a class
For ease of storage and access

Author: Piyotr Kao
Date-Created: 2021 NOV 08
Date-Modified: 2022 JAN 10
"""


class Account():

    # static delimiter variable
    _DELIMITER: str = "/"

    def __init__(self, user: str, email: str, passwd: str):
        self._user = user
        self._email = email
        self._passwd = passwd

    @classmethod
    def fromString(cls, infoStr: str):
        tmp = infoStr.split(cls._DELIMITER)
        return cls(tmp[0], tmp[1], tmp[2])

    @classmethod
    def fromDict(cls, infoDict: dict[str, str]):
        return cls(infoDict["username"], infoDict["email"], infoDict["passwd"])
        
    
    def checkValid(self) -> bool:
        """Simple validity checker, return False if email or passwd is None"""
        if self._email and self._passwd:
            return True
        return False
    
    @property
    def email(self) -> str:
        return self._email

    @property
    def passwd(self) -> str:
        return self._passwd

    @property
    def user(self) -> str:
        return self._user
    
    @email.setter
    def email(self, e: str):
        self._email = e
    
    @passwd.setter
    def passwd(self, p: str):
        self._passwd = p
    
    @user.setter
    def user(self, u: str):
        self._user = u
    
    def __repr__(self):
        return f"{self._user}{self._DELIMITER}{self._email}{self._DELIMITER}{self._passwd}"

    def __str__(self):
        return f"Email: {self._email} Username: {self._user} Password: {self._passwd}"