# ========================== Bank App Exercise ===============================================================

# Build a simple console-based banking system that allows users to
# 1. create accounts,
# 2. deposit money,
# 3. withdraw money, and
# 4. check balances
# using functions, loops, if/else, lists, and dictionaries.

'''
    Bank account structure
    {
        'user': {'first_name': '', 'last_name': ''},
        'account': {'account_name': '', 'account_number': '', 'account_balance': ''}
    }
'''

import random

accounts = []
user_options = ["1. Create Account", "2. Deposit Money",
                "3. Withdraw Money", "4. Check Balance", "5. Quit"]


print(
    "Welcome To ST Bank.\n"
)


def greet():
    print(f"What would you like to do?\n {'\n'.join(user_options)}")

    user_selection = input("Select an option: ")

    if user_selection == '1':
        create_account()
    elif user_selection == '2':
        deposit_money()
    elif user_selection == '3':
        withdraw_money()
    elif user_selection == '4':
        check_balance()
    elif user_selection == '5':
        print("Nice doing business with you.")
        return
    else:
        print("Invalid Input, Please select")
        return greet()


def create_account():
    print("Creating Account...")
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")

    user = {
        'first_name': first_name,
        'last_name': last_name
    }
    account = {
        'account_name': f"{first_name} {last_name}",
        'account_number': f"12345{len(accounts) + 1}",
        'account_balance': 0,
    }
    accounts.append({
        'user': user,
        'account': account
    })

    print("Your account has been created successfully\n")
    print(
        f'''
            Account Name: {account['account_name']}
            Account Number: {account['account_number']}
        '''
    )
    print(accounts)

    return greet()


def deposit_money():
    print("depositing money")

    account_number = input("Enter account number: ")

    user_account = None
    user_account_idx = None

    for index, account in enumerate(accounts):
        if account['account']['account_number'] == account_number:
            user_account = account
            user_account_idx = index
            break
        else:
            continue

    if not user_account:
        print("You do not have an account\n\n")
        return greet()

    deposit_amount = int(input("Ho much do you want to deposit?: "))
    user_account['account']['account_balance'] = user_account['account']['account_balance'] + deposit_amount
    accounts[user_account_idx] = user_account

    print(
        f'Your deposit was successful. Your current balance is now {accounts[user_account_idx]['account']['account_balance']}'
    )
    return greet()


def withdraw_money():
    print("withdrawing money")
    account_number = input("Enter account number: ")

    user_account = None
    user_account_idx = None

    for index, account in enumerate(accounts):
        if account['account']['account_number'] == account_number:
            user_account = account
            user_account_idx = index
            break
        else:
            continue

    if not user_account:
        print("You do not have an account\n\n")
        return greet()

    withdrawal_amount = int(input("Ho much do you want to withdraw?: "))
    user_account['account']['account_balance'] = user_account['account']['account_balance'] - withdrawal_amount
    accounts[user_account_idx] = user_account

    print(
        f'\nYour withdrawal was successful. Your current balance is now {accounts[user_account_idx]['account']['account_balance']}'
    )
    return greet()


def check_balance():
    account_number = input("Enter account number: ")

    user_account = None
    user_account_idx = None

    for index, account in enumerate(accounts):
        if account['account']['account_number'] == account_number:
            user_account = account
            user_account_idx = index
            break
        else:
            continue

    if not user_account:
        print("You do not have an account\n\n")
        return greet()

    print(
        f'\nYour current balance is now {accounts[user_account_idx]['account']['account_balance']}'
    )
    return greet()


greet()
