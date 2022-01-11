from PassKeeper import PassKeeper

class Display():

    _input: int
    # State for exiting the program
    _state: int

    def __init__(self):
        self._state = 1
        self._input = -1

    def run(self):
        while self._state != 0:
            self.display_menu()
            self.take_input()
            self.eval_input()

    def take_input(self):
        self._input = int(input("Enter an option: "))

    def eval_input(self):
        if self._input == 1:
            print("Add new acc")
            user = input("Enter a new acc name: ")
            self._tmpData.append(user)
        elif self._input == 2:
            print("Remove acc")
        elif self._input == 4:
            print("Display all acc")
            print(self._tmpData)
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
        6. Edit Master pass
        7. Quit
        ''')
    
    # Upon exiting, write to the encrypted file
    def _exit(self):
        print("Quit")
        self.create_final_data()
        print("Writing: " + self._finalData)
        self._enc.write(self._file, self._finalData)
        self._state = 0