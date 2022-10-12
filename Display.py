from PassKeeper import PassKeeper

"""
Display

For displaying information to the screen

Will start as a cli program
Can add GUI later

Author: Piyotr Kao
Date-Created: 2021 NOV 08
Date-Modified: 2022 JAN 10
"""
class Display():

    def __init__(self):
        # State for exiting the program
        self._state: int = 1
        self._input: int = -1
        self._keeper: PassKeeper = PassKeeper()

    def run(self):
        while self._state != 0:
            self.display_menu()
            self.take_input()
            self.eval_input()

    def take_input(self):
        self._input = int(input("Enter an option: "))
    
    def take_input_re(self, prompt="Enter: ") -> str:
        """Contains a while loop for input sanitation and None checks

        Keyword Arguments:
        prompt -- The prompt to give the user (default "Enter: ")
        """
        while True:
            ui = input(prompt)
            if not ui:
                print("No answer detected, try again")
            else:
                return ui

    def eval_input(self):
        if self._input == 1:
            print("Add new acc")
            self.display_add()
        elif self._input == 2:
            print("Remove acc")
        elif self._input == 4:
            print("Display all acc")
            self.display_all()
        elif self._input == 6:
            print("Change master password")
            self.change_master()
        elif self._input == 7:
            self._exit()
        else:
            print("Invalid Choice")

    def display_menu(self):
        print('''
        1. Add new acc (user/email/pass)
        2. Remove acc (user/email/pass)
        3. Search sites
        4. Display all accs
        5. Edit acc (user/email/pass)
        6. Change master password
        7. Quit
        ''')
    
    def display_add(self):
        """
        Adding a new account into the db
        """
        tmpInfo = {}

        # Can be empty
        user = input("Enter the acc name: ")
        tmpInfo["username"] = user

        mail = self.take_input_re("Please enter the acc email: ")
        tmpInfo["email"] = mail

        passwd = self.take_input_re("Enter the acc password: ")
        tmpInfo["passwd"] = passwd

        self._keeper.add(infoDict = tmpInfo)
    
    def change_master(self):
        pass
    
    def display_all(self):
        print(self._keeper.listAll())
    
    # Upon exiting, write to the encrypted file
    def _exit(self):
        print("Quit")
        self._keeper.exit()
        self._state = 0