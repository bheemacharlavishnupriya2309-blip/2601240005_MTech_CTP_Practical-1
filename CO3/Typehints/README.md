**Description**

PEP 484 introduced type hints in Python. Type hints allow developers to specify the expected types of function parameters and return values.

In a banking system, a transaction function can use type hints to clearly specify that the account number is a string, the transaction amount is a float, and the function returns a boolean indicating whether the transaction was successful.

Type hints are mainly used by static type checkers and do not automatically enforce types at runtime.

**Syntax**

def function_name(parameter: data_type) -> return_type:
    # function body

**Banking Transaction Syntax**

def process_transaction(account: str, amount: float) -> bool:
    # transaction logic

**Algorithm**

Define a transaction function named process_transaction.

Use PEP 484 type hints for the account number and transaction amount.

Specify bool as the return type.

Check whether the transaction amount is valid.

If the amount is greater than zero, process the transaction.

Return True for a successful transaction.

Otherwise, return False.

Display the transaction result.

**Example**

def process_transaction(account: str, amount: float) -> bool:
    if amount > 0:
        print("Transaction successful")
        return True

    print("Invalid transaction amount")
    return False


process_transaction("ACC101", 5000.0)

**Key Point**

PEP 484 type hints improve code readability and allow tools such as static type checkers to detect possible type-related errors before execution.
