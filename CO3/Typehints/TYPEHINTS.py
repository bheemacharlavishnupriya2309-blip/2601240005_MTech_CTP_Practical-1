def process_transaction(account: str, amount: float) -> bool:
    if amount > 0:
        print("Transaction successful")
        return True
    else:
        print("Invalid transaction amount")
        return False


account = input("Enter Account Number: ")
amount = float(input("Enter Transaction Amount: "))

process_transaction(account, amount)
