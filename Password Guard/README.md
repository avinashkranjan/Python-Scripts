# Password Guard

Password Guard is a Python-based tool designed to evaluate the strength of a password and estimate the time it would take to crack it using brute-force methods. This tool helps users understand how secure their passwords are and provides insights into improving password security.

## Features

- **Password Strength Evaluation:** The tool classifies passwords as `Very Strong`, `Strong`, `Moderate`, or `Weak` based on various criteria including length, use of uppercase and lowercase letters, digits, and special characters.
- **Cracking Time Estimation:** Estimates the time required to crack the password using a brute-force attack, calculated based on the number of possible combinations.

## How It Works

### Password Strength Calculation
The strength of a password is determined by:
1. **Length of the Password:** 
   - Less than 8 characters: `Weak`
   - 8-12 characters: `Moderate`
   - More than 12 characters: `Strong`
2. **Character Variety:** 
   - Presence of uppercase letters.
   - Presence of lowercase letters.
   - Presence of digits.
   - Presence of special characters.
3. **Common Password Patterns:** 
   - The tool checks against a list of common passwords (e.g., "1234", "password"). If the password matches any of these, the score is set to `Weak`.

### Cracking Time Calculation
- The tool estimates the time to crack a password by calculating the total number of possible combinations based on the character set used (lowercase, uppercase, digits, special characters).
- The cracking time is then estimated assuming a hashing speed of 1 billion attempts per second.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python:
   ```bash
   python password_guard.py

## **Author**
[ShankhosuvroGhosh](https://github.com/Shankhosuvro-G)

