🏦 Smart Banking System

A **Python-based banking application** with a modern **Streamlit GUI**. This project demonstrates a full-featured banking system with modular backend logic, clean architecture, and interactive frontend.  

---

## 🔹 Features

- **Account Management**
  - Open a new account with minimum initial deposit
  - Secure login with PIN verification
  - Delete account with zero balance requirement

- **Transactions**
  - Deposit and withdraw money
  - Check account balance
  - Secure money transfer with validation:
    - Sender PIN verification
    - Sufficient balance check
    - Sender ≠ Receiver

- **Advanced Backend**
  - Separate `bank_logic.py` for business logic
  - `data.py` to store account details
  - All operations include error handling and validations

- **Frontend**
  - Modern, professional Streamlit GUI
  - Tab-based navigation for each function
  - Card-style layouts for better user experience

---

## 🛠️ Technologies Used

- Python 3.x
- Streamlit for frontend
- Modular programming for backend logic
- Randomized account number generation
