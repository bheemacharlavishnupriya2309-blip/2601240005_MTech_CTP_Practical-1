## Objective

To demonstrate the use of a mixin in Python by adding common login functionality to unrelated classes without creating a common parent class.

## Problem Statement

Several unrelated classes in an enterprise application require login functionality. Instead of creating a common superclass, a mixin can be used to provide the login functionality to different classes.

A `LoginMixin` contains the common login method, which can be added to classes such as `Admin` and `Customer`.

## Input

- Username
- Password
- User type such as Admin or Customer

### Example Input

```text
Username: admin
Password: 1234
User Type: Admin
Output

The program displays whether the login was successful or failed.

E**xample Output**

Login Successful
Welcome Admin

**Algorithm**

Create a LoginMixin class.
Define a login() method inside the mixin.
Store or define valid login credentials.
Create unrelated classes such as Admin and Customer.
Inherit LoginMixin along with each class.
Read the username and password from the user.
Call the login() method.
Compare the entered credentials with the valid credentials.
If the credentials match, display Login Successful.
Otherwise, display Invalid Username or Password.
End the program.
Login and authentication
Logging
Permission checking
Notification functionality
Serialization
Validation
API-related functionality
Conclusion

The Login Functionality Using Mixin example demonstrates how a mixin can provide common functionality to multiple unrelated classes. The LoginMixin contains the login behavior, which can be reused by both Admin and Customer classes without requiring a common parent class.

give a readme file all in one
Login Functionality Using Mixin
Objective

To demonstrate the use of a Mixin in Python by adding common login functionality to unrelated classes without creating a common parent class.

**Problem Statement**

Several unrelated classes in an enterprise application require login functionality. Instead of creating a common superclass, a mixin can be used to provide the login functionality to different classes.

The LoginMixin contains the common login method, which can be reused by classes such as Admin and Customer.

**Input**

Username
Password
User type
Example Input
Username: admin

Welcome Admin

**Time Complexity**

Login validation: O(1)
Object creation: O(1)
Displaying result: O(1)
Overall Time Complexity
O(1)
**Space Complexity**

O(1)
