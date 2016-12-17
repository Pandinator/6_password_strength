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
        if password.lower() != password and password.upper() != password: 
            password_strength += 1
        if re.findall(r'[\d]', password): 
            password_strength += 1
        if re.findall(r'[!@#$%^&*><}{]', password):
            password_strength += 2
        if password not in blacklist:
            password_strength += 3
        if len(password) > 12:  
            password_strength += 2
        return (password_strength)


if __name__ == '__main__':
    blacklist_path = input("Enter filepath to the blacklist: \n")
    password = input("Enter you password: \n")
    blacklist = load_password_blacklist(blacklist_path)
    rate = get_password_strength(password, blacklist)
    print("Your password is {}{}".format(str(rate), "/10"))

    
