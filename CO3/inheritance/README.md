give objective,input,output,algorithm,time complexity

Done. I created the complete README.md file in one file, ready to paste/upload to GitHub.

Download README.md 

README.md
Document
give objective,input,output,algorithm,time complexity
Applying Inheritance to Banking Scenario
Objective

To demonstrate inheritance in Object-Oriented Programming by creating a common BankAccount class and deriving SavingsAccount and CurrentAccount classes from it, while implementing different withdrawal rules for each account type.

Input
Account holder name
Account number
Initial account balance
Withdrawal amount
Account type:
Savings Account
Current Account
Example Input
Account Holder: Ravi
Account Number: 101
Balance: 10000
Withdrawal Amount: 2000
Account Type: Savings
Output
Account holder details
Account number
Updated balance
Withdrawal status
Example Output
Account Holder: Ravi
Account Number: 101
Initial Balance: 10000
Withdrawal Amount: 2000
Updated Balance: 8000
Withdrawal Successful
Algorithm
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
Time Complexity
Creating an account: O(1)
Checking withdrawal condition: O(1)
Updating balance: O(1)
Displaying account details: O(1)
Overall Time Complexity

O(1)

Space Complexity

O(1) extra space.

give it in readme file

Done. I created the complete README.md file for the Banking Inheritance scenario.

Download Banking_Inheritance_README.md 

Banking_Inheritance_README.md
Document

Banking_Inheritance_README.md
Applying Inheritance to Banking Scenario
Objective

To demonstrate inheritance in Object-Oriented Programming by creating a common BankAccount class and deriving SavingsAccount and CurrentAccount classes from it, while implementing different withdrawal rules for each account type.

Problem Statement

In a banking application, both Savings Account and Current Account share common attributes such as account number, account holder name, and balance. However, their withdrawal rules may be different.

Inheritance can be used to create a common parent class BankAccount and derive SavingsAccount and CurrentAccount from it.

Input
Account holder name
Account number
Initial account balance
Withdrawal amount
Account type:
Savings Account
Current Account
Example Input
Account Holder: Ravi
Account Number: 101
Balance: 10000
Withdrawal Amount: 2000
Account Type: Savings
Output
Account holder details
Account number
Initial balance
Withdrawal amount
Updated balance
Withdrawal status
Example Output
Account Holder: Ravi
Account Number: 101
Initial Balance: 10000
Withdrawal Amount: 2000
Updated Balance: 8000
Withdrawal Successful
Algorithm
Create a parent class named BankAccount.
Define common attributes such as account holder name, account number, and balance.
Create a SavingsAccount class that inherits from BankAccount.
Create a CurrentAccount class that inherits from BankAccount.
Define withdrawal methods according to the rules of each account type.
Create an account object.
Read the withdrawal amount.
Check whether the withdrawal is allowed.
If the withdrawal is allowed, subtract the amount from the balance.
Display the account details and updated balance.
Time Complexity
Creating an account: O(1)
Checking withdrawal condition: O(1)
Updating balance: O(1)
Displaying account details: O(1)
Overall Time Complexity

O(1)

Space Complexity

O(1) extra space.

Advantages
Promotes code reusability.
Avoids duplication of common account properties.
Makes the banking system easier to maintain.
Allows different account types to implement their own behavior.
Demonstrates the concept of inheritance clearly.
Conclusion

The banking scenario demonstrates how inheritance can be used to create specialized account classes from a common BankAccount parent class. Common properties and operations are shared through inheritance, while Savings Account and Current Account can implement their own withdrawal rules.
