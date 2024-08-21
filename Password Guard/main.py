import re

def calculate_password_strength(password):
    score = 0
    if len(password) < 8:
        score = 1
    elif len(password) >= 8 and len(password) <= 12:
        score = 2
    elif len(password) > 12:
        score = 3
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1
    common_passwords = ["0000", "1234", "password", "qwerty", "abc123", "pswd"]
    for pattern in common_passwords:
        if pattern in password:
            score = 0
            break
    if score >= 6:
        return "Very Strong"
    elif score >= 4:
        return "Strong"
    elif score >= 2:
        return "Moderate"
    else:
        return "Weak"

def calculate_cracking_time(password):
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in "!@#$%^&*()_+\-=[]{};':\"|,.<>/?\\" for c in password):
        charset_size += 33
    total_combination = charset_size ** len(password)
    hashing_speed = 1000000000
    cracking_time_in_seconds = total_combination / hashing_speed
    if cracking_time_in_seconds < 60:
        return f"{cracking_time_in_seconds:.2f} seconds"
    elif cracking_time_in_seconds < 3600:
        return f"{cracking_time_in_seconds / 60:.2f} minutes"
    elif cracking_time_in_seconds < 86_400:
        return f"{cracking_time_in_seconds / 3600:.2f} hours"
    elif cracking_time_in_seconds < 31_536_000:
        return f"{cracking_time_in_seconds / 86_400:.2f} days"
    else:
        return f"{cracking_time_in_seconds / 31_536_000:.2f} years"
if __name__=="__main__":
    print("Welcome to Password Guard..")
    password=input("Enter your password to check its strength and cracking time...")
    strength=calculate_password_strength(password)
    cracking_time=calculate_cracking_time(password)
    print(f"Password: {password}")
    print(f"Strength: {strength}")
    print(f"Estimated cracking time: {cracking_time}")