from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

pwd = input("what is the master password? ")
key = load_key() + pwd.encode()
fer = Fernet(key)

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ",
            fer.decrypt(passw.encode()))
def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)?")
    if mode == "q":
        break

    if mode == "view":
        view()

    if mode == "add":
        add()
        break
    else:
        print("Invalid mode.")
        continue
