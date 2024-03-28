import re

def check_password_strength(password):
    if len(password) < 8:
        length_feedback = "Password is too short (minimum length is 8 characters)."
    else:
        length_feedback = "Password length is sufficient."
    
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*()_+{}|:"<>?]', password))

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    if score == 5:
        return "Very Strong", length_feedback
    elif score == 4:
        return "Strong", length_feedback
    elif score == 3:
        return "Moderate", length_feedback
    elif score == 2:
        return "Weak", length_feedback
    else:
        return "Very Weak", length_feedback

password = input("Enter your password: ")
strength, length_feedback = check_password_strength(password)

print("Password strength:", strength)
print(length_feedback)
