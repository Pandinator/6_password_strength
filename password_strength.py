import re


def load_password_blacklist(filepath):
    with open(filepath, 'r') as blacklist_data:
        prohibitted_passwords = blacklist_data.read()
        prohibitted_passwords = re.findall(r'[\w]+', prohibitted_passwords)
        return prohibitted_passwords


def get_password_strength(password, blacklist):
    if len(password) < 6:
        return 1
    else:
        password_strength = 1
        password_strength += 3 * int(password not in blacklist)
        password_strength += 1 * int(password.lower() != password and
                                     password.upper() != password)
        password_strength += 2 * int(len(password) > 12)
        if re.findall(r'[\d]', password):
            password_strength += 1
        if re.findall(r'\S', password):
            password_strength += 2
        return (password_strength)


if __name__ == '__main__':
    blacklist_path = input("Enter filepath to the blacklist: \n")
    password = input("Enter you password: \n")
    blacklist = load_password_blacklist(blacklist_path)
    rate = get_password_strength(password, blacklist)
    print("Your password is {}/10".format(str(rate)))
