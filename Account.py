"""
Account

Representation of the account information as a class
For ease of storage and access

Author: Piyotr Kao
Date-Created: 2021 NOV 08
Date-Modified: 2022 JAN 10
"""
class Account():

    _user: str
    _email: str
    _passwd: str

    def __init__(self, user: str, email: str, passwd: str):
        self._user = user
        self._email = email
        self._passwd = passwd
    
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
    
    def __str__(self):
        return self._email + "." + self._user + "." + self._passwd