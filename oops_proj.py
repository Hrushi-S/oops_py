class chatbook:
    def __init__(self, username, pwd, logged_in=False):
        self.username = username
        self.password = pwd
        self.logged_in = logged_in
        # self.menu()

    def menu(self):
         while True:
            print("\n--- ChatBook Menu ---")
            print("1. Sign Up")
            print("2. Log In")
            print("3. Post")
            print("4. Send a message")
            print("Any other key to Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.sign_up()
            elif choice == '2':
                self.sign_in()
            elif choice == '3':
                self.post()
            elif choice == '4':
                self.send_message()
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

    def post(self):
        if not self.logged_in:
            print("Please log in to post.")
            return
        message = input("Enter your post: ")
        with open("messages.txt", "a") as f:
            f.write(f"{self.username}: {message}\n")
        print("Message posted successfully!")

    def send_message(self):
        if not self.logged_in:
            print("Please log in to send messages.")
            return
        recipient = input("Enter the recipient's username: ")
        message = input("Enter your message: ")
        with open("messages.txt", "a") as f:
            f.write(f"From {self.username} to {recipient}: {message}\n")
        print("Message sent successfully!")

# user1 = chatbook()