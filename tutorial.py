import re

def check_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*()_+=-]", password) is None
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    if all(errors):
        return "Very Weak"
    elif sum(errors) >= 3:
        return "Weak"
    elif sum(errors) == 2:
        return "Moderate"
    elif sum(errors) == 1:
        return "Strong"
    else:
        return "Very Strong"

pw = input("Enter a password: ")
print("Strength:", check_strength(pw))

