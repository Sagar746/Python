master_pwd = input('What is the master password: ')

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print(f'User: {user}, Password: {passw}')



def add():
    account_name = input('Enter account name: ')
    pwd = input('ENter password: ')

    with open('password.txt','a') as f:
        f.write(account_name + "|" + pwd + '\n')





while True:
    mode = input('Would you like to quit(q) or add and view password: ')
    if mode =='q':
        break
    
    elif mode =='view':
        view()
    elif mode =='add':
        add()

    else:
        print('Invalid mode')
        continue
