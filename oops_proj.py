class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def menu(self):
         while True:
            print("\n--- ChatBook Menu ---")
            print("1. Sign Up")
            print("2. Log In")
            print("3. Post a Message")
            print("4. View Messages")
            print("Any other key to Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.sign_up()
            elif choice == '2':
                self.sign_in()
            elif choice == '3':
                self.post_message()
            elif choice == '4':
                self.view_messages()
            else:
                print("Exiting ChatBook. Goodbye!")
                break

    def sign_up(self):
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
        print(f"User {self.username} signed up successfully! \n")


    def sign_in(self):
        if self.username =="" or self.password =="":
            print("No user found. Please sign up first.")
        else:
            uname = input("Enter your username: ")
            pwd = input("Enter your password: ")
            if uname == self.username and pwd == self.password:
                self.logged_in = True
                print(f"Welcome back, {self.username}!")
            else:
                print("Incorrect username or password.")

obj = chatbook()