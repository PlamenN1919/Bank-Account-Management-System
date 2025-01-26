# 🏦 Enhanced Bank Account Management System

# Account storage
accounts = {}

# Constants
MAX_LOAN_AMOUNT = 10000

# Menu display function
def display_menu():
    """Display the main menu for the banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ Transfer Funds")
    print("6️⃣ Apply for Loan")
    print("7️⃣ Repay Loan")
    print("8️⃣ View Transaction History")
    print("9️⃣ List All Accounts")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")

def create_account():
    """Create a new bank account."""
    global accounts

    print("\n🆕 Create Account")
    username = input("Enter a unique username: ").strip()
    if username in accounts:
        print("❌ Username already exists. Choose another.")
        return

    password = input("Create a password: ").strip()
    if not password:
        print("❌ Password cannot be empty.")
        return

    try:
        initial_deposit = float(input("Enter initial deposit (or 0 for none): "))
        if initial_deposit < 0:
            print("❌ Initial deposit cannot be negative.")
            return
    except ValueError:
        print("❌ Invalid input for deposit.")
        return

    accounts[username] = {
        "password": password,
        "balance": initial_deposit,
        "transactions": [("Account created", initial_deposit)],
        "loan": 0.0
    }
    print(f"✅ Account created for {username} with ${initial_deposit:.2f}.")

def deposit():
    """Deposit money into an account."""
    global accounts

    print("\n💵 Deposit Money")
    username = input("Enter your username: ").strip()
    if username not in accounts:
        print("❌ Account not found.")
        return

    password = input("Enter your password: ").strip()
    if accounts[username]["password"] != password:
        print("❌ Incorrect password.")
        return

    try:
        amount = float(input("Enter the deposit amount: "))
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return
    except ValueError:
        print("❌ Invalid input for amount.")
        return

    accounts[username]["balance"] += amount
    accounts[username]["transactions"].append(("Deposit", amount))
    print(f"✅ ${amount:.2f} deposited successfully. New balance: ${accounts[username]['balance']:.2f}.")

def withdraw():
    """Withdraw money from an account."""
    global accounts

    print("\n💸 Withdraw Money")
    username = input("Enter your username: ").strip()
    if username not in accounts:
        print("❌ Account not found.")
        return

    password = input("Enter your password: ").strip()
    if accounts[username]["password"] != password:
        print("❌ Incorrect password.")
        return

    try:
        amount = float(input("Enter the withdrawal amount: "))
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return
        if amount > accounts[username]["balance"]:
            print("❌ Insufficient balance.")
            return
    except ValueError:
        print("❌ Invalid input for amount.")
        return

    accounts[username]["balance"] -= amount
    accounts[username]["transactions"].append(("Withdrawal", -amount))
    print(f"✅ ${amount:.2f} withdrawn successfully. Remaining balance: ${accounts[username]['balance']:.2f}.")

def check_balance():
    """Check the balance of an account."""
    global accounts

    print("\n💰 Check Balance")
    username = input("Enter your username: ").strip()
    if username not in accounts:
        print("❌ Account not found.")
        return

    password = input("Enter your password: ").strip()
    if accounts[username]["password"] != password:
        print("❌ Incorrect password.")
        return

    print(f"💼 Current balance: ${accounts[username]['balance']:.2f}.")

def transfer_funds():
    """Transfer funds between accounts."""
    global accounts

    print("\n🔄 Transfer Funds")
    sender = input("Enter your username: ").strip()
    if sender not in accounts:
        print("❌ Sender account not found.")
        return

    password = input("Enter your password: ").strip()
    if accounts[sender]["password"] != password:
        print("❌ Incorrect password.")
        return

    receiver = input("Enter the receiver's username: ").strip()
    if receiver not in accounts:
        print("❌ Receiver account not found.")
        return

    try:
        amount = float(input("Enter the amount to transfer: "))
        if amount <= 0:
            print("❌ Transfer amount must be positive.")
            return
        if amount > accounts[sender]["balance"]:
            print("❌ Insufficient funds.")
            return
    except ValueError:
        print("❌ Invalid input for amount.")
        return

    accounts[sender]["balance"] -= amount
    accounts[receiver]["balance"] += amount
    accounts[sender]["transactions"].append((f"Transferred to {receiver}", -amount))
    accounts[receiver]["transactions"].append((f"Received from {sender}", amount))
    print(f"✅ ${amount:.2f} transferred from {sender} to {receiver}.")

def apply_for_loan():
    """Allow users to apply for a loan."""
    global accounts

    print("\n🏦 Apply for Loan")
    username = input("Enter your username: ").strip()
    if username not in accounts:
        print("❌ Account not found.")
        return

    password = input("Enter your password: ").strip()
    if accounts[username]["password"] != password:
        print("❌ Incorrect password.")
        return

    try:
        loan_amount = float(input(f"Enter the loan amount (Max ${MAX_LOAN_AMOUNT}): "))
        if loan_amount <= 0:
            print("❌ Loan amount must be positive.")
            return
        if loan_amount > MAX_LOAN_AMOUNT:
            print(f"❌ Loan amount exceeds the maximum limit of ${MAX_LOAN_AMOUNT}.")
            return
    except ValueError:
        print("❌ Invalid input for loan amount.")
        return

    if accounts[username]["loan"] > 0:
        print("❌ You already have an outstanding loan.")
        return

    accounts[username]["loan"] = loan_amount
    accounts[username]["balance"] += loan_amount
    accounts[username]["transactions"].append(("Loan Approved", loan_amount))
    print(f"✅ Loan of ${loan_amount:.2f} approved. Current balance: ${accounts[username]['balance']:.2f}.")

def repay_loan():
    """Allow users to repay their loan."""
    global accounts

    print("\n💳 Repay Loan")
    username = input("Enter your username: ").strip()
    if username not in accounts:
        print("❌ Account not found.")
        return

    password = input("Enter your password: ").strip()
    if accounts[username]["password"] != password:
        print("❌ Incorrect password.")
        return

    if accounts[username]["loan"] <= 0:
        print("❌ No outstanding loan to repay.")
        return

    try:
        repayment_amount = float(input("Enter the repayment amount: "))
        if repayment_amount <= 0:
            print("❌ Repayment amount must be positive.")
            return
        if repayment_amount > accounts[username]["balance"]:
            print("❌ Insufficient funds in your account.")
            return
    except ValueError:
        print("❌ Invalid input for repayment amount.")
        return

    accounts[username]["balance"] -= repayment_amount
    accounts[username]["loan"] -= repayment_amount
    if accounts[username]["loan"] < 0:
        accounts[username]["loan"] = 0

    accounts[username]["transactions"].append(("Loan Repayment", -repayment_amount))
    print(f"✅ Loan repayment of ${repayment_amount:.2f} successful. Remaining loan: ${accounts[username]['loan']:.2f}.")

def view_transaction_history():
    """View transaction history for an account."""
    global accounts

    print("\n📜 Transaction History")
    username = input("Enter your username: ").strip()
    if username not in accounts:
        print("❌ Account not found.")
        return

    password = input("Enter your password: ").strip()
    if accounts[username]["password"] != password:
        print("❌ Incorrect password.")
        return

    print(f"🔍 Transaction history for {username}:")
    for transaction in accounts[username]["transactions"]:
        print(f"- {transaction[0]}: ${transaction[1]:.2f}")

def list_accounts():
    """List all accounts in the system."""
    global accounts

    print("\n📋 List of All Accounts")
    if not accounts:
        print("No accounts found.")
        return

    for username, details in accounts.items():
        print(f"👤 {username} - Balance: ${details['balance']:.2f}, Loan: ${details['loan']:.2f}")

def identify_card_type():
    """Identify the type of credit card."""
    print("\n💳 Identify Card Type")
    card_number = input("Enter the credit card number: ").strip()

    if not card_number.isdigit():
        print("❌ Card number must be numeric.")
        return

    if card_number.startswith("4"):
        print("💳 This is a Visa card.")
    elif card_number.startswith("5"):
        print("💳 This is a MasterCard.")
    elif card_number.startswith("3"):
        print("💳 This could be an American Express or JCB card.")
    elif card_number.startswith("6"):
        print("💳 This could be a Discover card.")
    else:
        print("❓ Card type not recognized.")

# Main function
def main():
    """Main banking system interface."""
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transfer_funds()
        elif choice == "6":
            apply_for_loan()
        elif choice == "7":
            repay_loan()
        elif choice == "8":
            view_transaction_history()
        elif choice == "9":
            list_accounts()
        elif choice == "10":
            identify_card_type()
        elif choice == "0":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
