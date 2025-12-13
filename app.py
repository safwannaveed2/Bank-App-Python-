import streamlit as st
from bank_logic import *

st.set_page_config(
    page_title="Smart Bank",
    page_icon="🏦",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style='text-align:center;'>🏦 Smart Banking System</h1>
    <p style='text-align:center;color:gray;'>
    Secure • Fast • Reliable
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "➕ Open Account",
    "🔐 Login",
    "💰 Deposit",
    "💸 Withdraw",
    "📊 Balance",
    "🔁 Transfer Money",
    "❌ Delete Account"
])

# ---------------- OPEN ACCOUNT ----------------
with tab1:
    st.subheader("Open a New Bank Account")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        phone = st.text_input("Phone Number")
        email = st.text_input("Email Address")

    with col2:
        pin = st.number_input("4-Digit PIN", min_value=1000, max_value=9999)
        deposit = st.number_input("Initial Deposit (Min Rs 2000)", min_value=2000)

    if st.button("Create Account", use_container_width=True):
        acc_no = open_account(name, phone, email, pin, deposit)
        st.success("Account Created Successfully 🎉")
        st.info(f"Your Account Number: **{acc_no}**")

# ---------------- LOGIN ----------------
with tab2:
    st.subheader("Account Login")

    acc = st.number_input("Account Number", step=1)
    pin = st.number_input("PIN Code", step=1)

    if st.button("Login", use_container_width=True):
        if login(acc, pin):
            st.success("Login Successful ✅")
            st.session_state.account = acc
        else:
            st.error("Invalid Account Number or PIN")

# ---------------- DEPOSIT ----------------
with tab3:
    st.subheader("Deposit Money")

    acc = st.number_input("Account Number", key="dep_acc")
    amount = st.number_input("Deposit Amount", min_value=1, key="dep_amt")

    if st.button("Deposit Amount", use_container_width=True):
        new_balance = deposit_money(acc, amount)
        st.success("Deposit Successful 💰")
        st.info(f"Updated Balance: Rs {new_balance}")

# ---------------- WITHDRAW ----------------
with tab4:
    st.subheader("Withdraw Money")

    acc = st.number_input("Account Number", key="wd_acc")
    amount = st.number_input("Withdraw Amount", min_value=1, key="wd_amt")

    if st.button("Withdraw Amount", use_container_width=True):
        status, balance = withdraw_money(acc, amount)
        if status:
            st.success("Withdrawal Successful ✅")
            st.info(f"Remaining Balance: Rs {balance}")
        else:
            st.error("Insufficient Balance ❌")

# ---------------- CHECK BALANCE ----------------
with tab5:
    st.subheader("Account Balance")

    acc = st.number_input("Account Number", key="bal_acc")

    if st.button("Check Balance", use_container_width=True):
        balance = check_balance(acc)
        st.success(f"Your Current Balance: Rs {balance}")

# ---------------- TRANSFER MONEY ----------------
with tab6:
    st.subheader("Transfer Money")

    sender_acc = st.number_input("Sender Account Number", key="s_acc")
    sender_pin = st.number_input("Sender PIN", key="s_pin")
    receiver_acc = st.number_input("Receiver Account Number", key="r_acc")
    amount = st.number_input("Amount to Transfer", min_value=1, key="t_amt")

    if st.button("Transfer Amount", use_container_width=True):
        transfer_money(sender_acc, sender_pin, receiver_acc, amount)

# ---------------- DELETE ACCOUNT ----------------
with tab7:
    st.subheader("Delete Account")

    acc = st.number_input("Account Number", key="del_acc")
    pin = st.number_input("PIN", key="del_pin")

    st.warning("⚠️ This action is permanent!")

    if st.button("Delete My Account", use_container_width=True):
        close_account(acc, pin)
