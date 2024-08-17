def check_password(password: str):
    with open('passwords.txt', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'{common_password} is not unique ❌, it is common password #{i}')
            return

    print(f'{password} is unique ✅')

def main():
    user_password = input('Enter your password: ')
    check_password(user_password)


if __name__ == '__main__':
    main()


# Potential add-ons
  # 1. Prevent the user from entering nothing
  # 2. Ask the user to enter a password