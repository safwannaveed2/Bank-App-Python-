import random
from data import accounts_details

# ---------------- ACCOUNT NUMBER ----------------
def gen_acc_num():
    return random.randint(1000, 9999)

# ---------------- OPEN ACCOUNT ----------------
def open_account(name, phone, email, pin, initial_deposit):
    if initial_deposit < 2000:
        raise ValueError("Minimum deposit must be Rs 2000")

    acc_no = gen_acc_num()

    accounts_details.append({
        "Name": name,
        "Phone": phone,
        "Email": email,
        "PIN": pin,
        "Account Number": acc_no,
        "Balance": initial_deposit
    })

    return acc_no

# ---------------- LOGIN ----------------
def login(account_number, pin_code):
    for acc in accounts_details:
        if acc["Account Number"] == account_number and acc["PIN"] == pin_code:
            return True
    return False

# ---------------- DEPOSIT ----------------
def deposit_money(account_number, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than 0")

    for acc in accounts_details:
        if acc["Account Number"] == account_number:
            acc["Balance"] += amount
            return acc["Balance"]

    raise ValueError("Account not found")

# ---------------- CHECK BALANCE ----------------
def check_balance(account_number):
    for acc in accounts_details:
        if acc["Account Number"] == account_number:
            return acc["Balance"]
    raise ValueError("Account not found")

# ---------------- WITHDRAW ----------------
def withdraw_money(account_number, amount):
    if amount <= 0:
        return False, "Invalid amount"

    for acc in accounts_details:
        if acc["Account Number"] == account_number:
            if acc["Balance"] >= amount:
                acc["Balance"] -= amount
                return True, acc["Balance"]
            else:
                return False, "Insufficient balance"

    return False, "Account not found"

# =================================================
# 🔁 ADVANCED TRANSFER MONEY
# =================================================
def transfer_money(sender_acc_no, sender_pin, receiver_acc_no, amount):
    if amount <= 0:
        return "Transfer amount must be greater than 0"

    if sender_acc_no == receiver_acc_no:
        return "Sender and receiver cannot be the same"

    sender = None
    receiver = None

    for acc in accounts_details:
        if acc["Account Number"] == sender_acc_no and acc["PIN"] == sender_pin:
            sender = acc
        if acc["Account Number"] == receiver_acc_no:
            receiver = acc

    if sender is None:
        return "Invalid sender account or PIN"

    if receiver is None:
        return "Receiver account does not exist"

    if sender["Balance"] < amount:
        return "Insufficient balance"

    # Perform transfer
    sender["Balance"] -= amount
    receiver["Balance"] += amount

    return f"Rs {amount} transferred successfully. Remaining balance: Rs {sender['Balance']}"

# =================================================
# ❌ ADVANCED DELETE ACCOUNT
# =================================================
def close_account(account_number, pin_code):
    for acc in accounts_details:
        if acc["Account Number"] == account_number and acc["PIN"] == pin_code:

            # Condition: account must be empty
            if acc["Balance"] > 0:
                return "Withdraw all money before closing the account"

            accounts_details.remove(acc)
            return "Account closed successfully"

    return "Invalid account number or PIN"
