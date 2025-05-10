balance=0
# DEPOSIT MONEY==================================================================================================================
def deposit_money(Account_number):
    global balance
    while True:
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"✅ Cash deposited. Balance = {balance}")
                break
            else:
                print("❌ Amount must be greater than 0.")
        except ValueError:
            print("❌ Please enter numbers only.")

# WITHDRAW MONEY====================================================================================================================
def withdraw_money():
    global balance
    while True:
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if 0 < amount <= balance:
                balance -= amount
                print(f"✅ Successfully withdrawn. Available balance = {balance}")

                with open('withdrawinfo.txt', 'a') as withdrawinfo:
                    withdrawinfo.write(f'Available balance after withdrawal: {balance}\n')
                break
            else:
                print('❌ Insufficient funds or invalid amount.')
        except ValueError:
            print("❌ Enter numbers only.")
      
#ACCOUNT CREATE FOR BANK DETAILS========================================================================================================
def userinfo():
    First_name = input('Enter  your first name: ')
    Last_name = input('Enter your last name: ')
    Password = input('Enter your password: ')
    Nic_number = (input('Enter your IC number: '))
    Address = input('Enter your address: ')
    Contact_number=(input('enter your phone number'))
    Account_number=(f'{int(Nic_number)+1234567}'.zfill(12))
       
    return {
    f"{Account_number}": [
        f"{First_name}",
        f"{Last_name}",
        f"{Password}",
        f"{Nic_number}",
        f"{Address}",
        f"{Contact_number}"
     ]
    }

   
# GET INFORMATION AND  ACCOUNTT NUMBER AND CREATE FILES.=======================================================================================
def get_userinformation():
    
    users_data=userinfo()
    
    Account_number = users_data.keys()
    
    with open('custumerdetails.txt', 'a') as custumerdetails:
        custumerdetails.write(f'{users_data}\n')
    print(f'your account number is {Account_number}.')
get_userinformation()
# START=======================================================================================================================================
def bank():        
        Bankcode= 2001
        Bankusername='elon musk'

        print('==========MENU=========')
        print('1.Admin signin')
        print('2.user sigin')
        print('3.user signup')

        choice=int(input('enter the choice(1/2/3)'))
        if choice==1:
            print('you are going to admin')
            Adminpassword=int(input('enter bank password'))
            Adminname=(input('enter bank username'))
            if Adminpassword==2001 and Adminname=='elon musk':
                    print('-----Bank Menu-----')
                    print('1.Account Create')
                    print('2.Bank History')
                    choice=int(input('enter your choice sir /medam :1/2'))
                    if choice==1:
                        users_data = userinfo()
                        get_userinformation()
        
                    elif choice==2:
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

        elif choice==2:
            print("🔐 User Signin")
            entered_account = int(input("Enter your account number: "))
            entered_password = int(input("Enter your password: "))

            try:
                with open('custumerdetails.txt', 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        if entered_account in line:
                            parts = line.strip().split('→')
                            account = parts[0].replace("Account Number:", "").strip()
                            user_info = parts[1].split(',')

                            if user_info[2] == entered_password:
                                print(f"✅ Login successful. Welcome, {user_info[0]} {user_info[1]}!")
                                
                                # Now show user menu
                                while True:
                                    print("\n----- User Menu -----")
                                    print("1. Deposit Money")
                                    print("2. Withdraw Money")
                                    print("3. Logout")
                                    option = input("Choose an option (1/2/3): ")

                                    if option == '1':
                                        deposit_money()
                                    elif option == '2':
                                        withdraw_money()
                                    elif option == '3':
                                        print("👋 Logged out.")
                                        break
                                    else:
                                        print("❌ Invalid option. Try again.")
                                break
                            else:
                                print("❌ Incorrect password.")
                                break
                    else:
                        print("❌ Account not found.")
            except FileNotFoundError:
                print("❌ No user data found. Please sign up first.")

        elif choice==3:
            users_data = userinfo()
            get_userinformation(users_data)
