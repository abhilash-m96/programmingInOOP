user_name = input("Enter username")
pwd = input("Enter password")

def login_required(func):

    def authenticate():
        if user_name == "abhi" and pwd == "abhi":
            return func()
    return authenticate

@login_required
def greet_valid_user():
    print(f"Hello {username}")

greet_valid_user()
