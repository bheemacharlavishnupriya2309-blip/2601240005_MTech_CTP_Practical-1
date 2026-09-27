
**Objective**
To demonstrate inheritance in Object-Oriented Programming by creating a common BankAccount class and deriving SavingsAccount and CurrentAccount classes from it, while implementing different withdrawal rules for each account type.

**Input**
Account holder name
Account number
Initial account balance
Withdrawal amount
Account type:
Savings Account
Current Account
**Example Input**
Account Holder: Ravi
Account Number: 101
Balance: 10000
Withdrawal Amount: 2000
Account Type: Savings
**Output**
Account holder details
Account number
Updated balance
Withdrawal status
**Example Output**
Account Holder: Ravi
Account Number: 101
Initial Balance: 10000
Withdrawal Amount: 2000
Updated Balance: 8000
Withdrawal Successful
**Algorithm**
Create a parent class named BankAccount.
Store common attributes such as:
Account holder name
Account number
Balance
Create a SavingsAccount class that inherits from BankAccount.
Create a CurrentAccount class that inherits from BankAccount.
Define different withdrawal methods/rules for the child classes.
Create an account object.
Read the withdrawal amount.
Check whether the withdrawal is allowed according to the account type.
If allowed, subtract the amount from the balance.
Display the updated account details and withdrawal status.
**Time Complexity**
Creating an account: O(1)
Checking withdrawal condition: O(1)
Updating balance: O(1)
Displaying account details: O(1)
Overall Time Complexity

O(1)

**Space Complexity**

O(1) extra space.




