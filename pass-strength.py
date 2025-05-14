import re
import hashlib

# Common passwords to check bad choices
COMMON_PASSWORDS = {"password", "123456", "qwerty", "letmein", "admin"}

def check_password_strength(password):
    strength = 0
    
    # Length Check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        return "Your password is too short. Use at least 8 characters."
    
    # Complexity Check
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    
    # Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        return "This password is too common. Choose a more unique one."
    
    # Hash-based Guessability Check (Minimalist Touch)
    entropy = hashlib.sha256(password.encode()).hexdigest()
    if entropy[:2] == "00":  # Arbitrary weak entropy marker
        return "Consider using a more complex password with a mix of characters."
    
    # Strength Evaluation
    if strength <= 2:
        return "Weak password. Use a mix of uppercase, lowercase, numbers, and special characters."
    elif strength <= 4:
        return "Moderate password. Improve it by making it longer and adding special characters."
    else:
        return "Strong password! Keep it safe and avoid reusing it on multiple sites."

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    print(check_password_strength(user_password))
