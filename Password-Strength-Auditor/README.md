# Password Strength Auditor & Policy Checker

## 1. Project Description

Password Strength Auditor & Policy Checker is a Python-based application designed to evaluate password security. It provides password strength checking, password policy validation, entropy calculation, secure password generation, and security audit reports.

The project demonstrates Object-Oriented Programming (OOP), password security concepts, and automated testing using Pytest.

## 2. Objectives

- Evaluate password strength and security.
- Validate passwords against configurable security policies.
- Calculate password entropy to estimate unpredictability.
- Generate secure passwords.
- Identify potentially predictable keyboard patterns.
- Generate password security audit reports.
- Test application functionality using Pytest.

## 3. Features

### Password Strength Checking
Evaluates passwords using security-related criteria.

### Password Policy Validation
Checks passwords against configurable password requirements.

### Entropy Calculation
Calculates estimated password entropy using password length and the character types present.

### Secure Password Generator
Provides functionality to generate passwords.

### Graphical User Interface
Provides a graphical interface for interacting with the application.

### Security Audit Reports
Generates reports containing password security assessment results.

### Keyboard Pattern Detection
Checks for potentially predictable keyboard patterns.

### Automated Testing
Uses Pytest to test application functionality.

## 4. Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Pytest
- Tkinter, if used by the graphical interface

## 5. Project Structure

```text
Password-Strength-Auditor/
│
├── main.py
├── gui.py
├── password_checker.py
├── password_generator.py
├── policy.py
├── entropy.py
├── security_report.py
├── test_password.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 6. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd Password-Strength-Auditor
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

## 7. How to Run the Project

To run the main application:

```bash
python main.py
```

To run the graphical interface separately, if configured as an independent entry point:

```bash
python gui.py
```

## 8. Running Tests

Run the automated tests using:

```bash
pytest -v
```

Pytest executes the test cases defined in `test_password.py`.

## 9. Applications

- Password security assessment.
- Password policy compliance checking.
- Password entropy analysis.
- Secure password generation.
- Password security report generation.
- Learning password security concepts.

## 10. Security Considerations

- Avoid using real passwords in demonstrations and test cases.
- Do not store sensitive credentials in source code.
- Keep dependencies updated.
- Use strong, unique passwords for personal and professional accounts.

## 11. Conclusion

The Password Strength Auditor & Policy Checker demonstrates how Python can be used to build a password security assessment application. By combining password checking, policy validation, entropy calculation, password generation, reporting, and automated testing, the project provides a practical introduction to password security and software development.

## 12. Author

Developed as a Python project focusing on password security, Object-Oriented Programming, and automated testing.
