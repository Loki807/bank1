balance = 0.0
users_data = {}

# DEPOSIT MONEY ==================================================================================================================
def deposit_money(account_number):
    global users_data
    while True:
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount > 0:
                users_data[account_number]["balance"] += amount
                print(f"✅ Cash deposited. Balance = {users_data[account_number]['balance']}")
                with open('transaction.txt', 'a') as tx:
                    tx.write(f'{account_number}: deposit {amount}, balance = {users_data[account_number]["balance"]}\n')
                with open('depositinfo.txt', 'a') as depositinfo:
                    depositinfo.write(f'{account_number}: Deposit of {amount} - Available balance after deposit: {users_data[account_number]["balance"]},\n')
                break
                break
            else:
                print("❌ Amount must be greater than 0.")
        except ValueError:
            print("❌ Please enter numbers only.")

# WITHDRAW MONEY ====================================================================================================================
def withdraw_money(account_number):
    global users_data
    while True:
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if 0 < amount <= users_data[account_number]["balance"]:
                users_data[account_number]["balance"] -= amount
                print(f"✅ Successfully withdrawn. Available balance = {users_data[account_number]['balance']}")

                with open('withdrawinfo.txt', 'a') as withdrawinfo:
                    withdrawinfo.write(f'{account_number}: Available balance after withdrawal: {users_data[account_number]["balance"]},\n')
                with open('transaction.txt', 'a') as tx:
                    tx.write(f'{account_number}: withdraw {amount}, balance = {users_data[account_number]["balance"]}\n')
                break
            else:
                print('❌ Insufficient funds or invalid amount.')
        except ValueError:
            print("❌ Enter numbers only.")

# ACCOUNT CREATE FOR BANK DETAILS ===============================================================================================
def userinfo():
    First_name = input('Enter  your first name: ')
    Last_name = input('Enter your last name: ')
    Password = input('Enter your password: ')
    Nic_number = input('Enter your IC number: ')
    for acc_number in users_data:
        if users_data[acc_number]["nic number"] == Nic_number:
            print("❌ This account already exists. Please try to sign in instead.")
            return None     


    Address = input('Enter your address: ')
    Contact_number = input('enter your phone number')
    Account_number = (f'{int(Nic_number) + 1234567}'.zfill(12))
    balance = 0.0
    return {
        f"{account_number}": {
            f"first name": First_name,
            f"last name": Last_name,
            f"password": Password,
            f"nic number": Nic_number,
            f"address": Address,
            f"contact number": Contact_number,
            f"balance": balance
        }
    }

# GET INFORMATION AND  ACCOUNT NUMBER AND CREATE FILES ==========================================================================
def get_userinformation():
    global users_data
    new_user = userinfo()
    if new_user is None:
        return  
    users_data.update(new_user)

    with open('custumerdetails.txt', 'a') as custumerdetails:
        custumerdetails.write(f'{new_user}\n')

    Account_number = list(new_user.keys())[0]
    print(f'your account number is {account_number}.')

# LOAD USERS FROM FILE ===========================================================================================================
def load_users():
    global users_data
    try:
        with open('custumerdetails.txt', 'r') as custumerdetails:
            for line in custumerdetails:
                line = line.strip()
                if not line.startswith('{') or not line.endswith('}'):
                    continue
                try:
                    user_dict = eval(line)
                    users_data.update(user_dict)
                except:
                    continue
    except FileNotFoundError:
        pass
# TRANSACTION HISTORY FUNCTION ====================================================================================================
def transaction_history():
    account_number = input("Enter your account number to see transaction history: ")
    try:
        with open('transaction.txt', 'r') as tx:
            print("\n===== Transaction History =====")
            found = False
            for line in tx:
                if line.startswith(account_number):
                    print(line.strip())
                    found = True
            if not found:
                print("📂 No transaction history found.")
    except FileNotFoundError:
        print("❌ Transaction history file not found.")
#CHECK BALANCE =============================================================================================================================================================
def check_balance(account_number):
    global users_data
    try:
        balance = users_data[account_number]["balance"]
        print(f"💰 Your current balance is: ${balance:.2f}")
    except KeyError:
        print("❌ Account not found.")
# START ==========================================================================================================================
def bank():
    global users_data

    while True:
        Bankcode = 2001
        Bankusername = 'elon musk'

        print('==========MENU=========')
        print('1.Admin signin')
        print('2.user sigin')
        print('3.user signup')
        print('4.exit')

        choice = int(input('enter the choice'))
        if choice == 1:
            print('you are going to admin')
            Adminpassword = int(input('enter bank password'))
            Adminname = input('enter bank username')
            if Adminpassword == 2001 and Adminname == 'elon musk':
                print('-----Bank Menu-----')
                print('1.Account Create')
                print('2.Bank History')
                choice = int(input('enter your choice sir /medam :1/2'))
                if choice == 1:
                    get_userinformation()
                    

                elif choice == 2:
                    try:
                        with open('custumerdetails.txt', 'r') as file:
                            print("\n===== Bank History =====")
                            print(file.read())
                    except FileNotFoundError:
                        print("No history found.")
                else:
                    print("❌ Invalid admin option.")
            else:
                print("❌ Invalid admin credentials.")

        elif choice == 2:
            entered_account = input("Enter your account number: ")
            entered_password = input("Enter your password: ")

            if users_data.get(entered_account) and entered_password == users_data[entered_account]['password']:
                print(f"✅ Login successful. Welcome {users_data[entered_account]['first name']} {users_data[entered_account]['last name']}!")

                while True:
                    print("\n----- User Menu -----")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3.transaction history")
                    print("4.check balance")
                    print("5. Logout")
                    option = input("Choose an option (1/2/3/4/5): ")

                    if option == '1':
                        deposit_money(entered_account)
                    elif option == '2':
                        withdraw_money(entered_account)
                    elif option=='3': 
                        transaction_history()
                    elif option=='4':
                        check_balance(entered_account)   
                    elif option == '5':
                        print("👋 Logged out.")
                        break
                    else:
                        print("❌ Invalid option. Try again.")
            else:
                print("❌ Wrong account number or password.")

        elif choice == 3:
            get_userinformation()
            new_account = list(users_data.keys())[-1]

        elif choice == 4:
            print('log out')
            break

load_users()
bank()