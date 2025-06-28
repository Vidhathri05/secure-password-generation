# Secure-Password-Generation
A customizable command-line password generator written in Python that creates strong, secure passwords based on user preferences. It ensures the inclusion of lowercase, uppercase, digits, and symbols, and also evaluates the password strength.

Features:

User-defined password length (minimum 6 characters)

Option to include:

✅ Capital letters (A–Z)

✅ Symbols (!@#$%^&*, etc.)

✅ Numbers (0–9)

Always includes at least one lowercase letter

Password strength meter:

🔴 Weak

🟡 Medium

🟢 Strong

Password Strength Logic:

Weak	-           Less than 8 characters or only 1 type of character

Medium	 -        8–11 characters with at least 2 types

Strong	 -        12+ characters with all 4 types (lower, upper, symbol, number)

Technologies Used:

Python 3.x

Built-in libraries: random, string, chr()

