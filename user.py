def encrypt_password(password):
    encrypted = password[::-1]
    return encrypted


def validate_email(email) -> bool:
    is_valid = "@" in email
    return is_valid


class User:
    username: str
    password: str
    email: str

    def __init__(self, username, password, email):
        self.username = username
        self.password = encrypt_password(password)

        if validate_email(email):
            self.email = email
        else:
            self.email = "Invalid Email"

    def __repr__(self) -> str:
        return f"User with username: {self.username} {self.password} {self.email}"


def main():
    user_list = []
    while True:
        user_input = input("Enter the command: ")

        if user_input == "add":
            username = input("Enter the username ")
            password = input("Enter the password ")
            email = input("Enter the email ")

            new_user = User(username=username, password=password, email=email)

            user_list.append(new_user)

            print(user_list)
        else:
            break


if __name__ == '__main__':
    main()
