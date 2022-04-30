master_pwd = input("What is the master password?")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
           data = line.rstrip()
           #rstrip will remove carriage return"\n"
           user, passw = data.split("|")
           print("User:", user, "| Password:", passw)

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
        # when using 'with' it will auto close file when complete 
        # add to the end of existing file if file doesnt exist
        #r to read existing file 
        

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()   
    elif mode == "add":
          add() 
    else: 
        print("Invalid mode.")
        continue