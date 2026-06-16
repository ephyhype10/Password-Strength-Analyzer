import random
import string
import re

def generate_password():
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*")

    remaining = ''.join(
        random.choice(
            string.ascii_letters +
            string.digits +
            "!@#$%^&*"
        ) for _ in range(8)
    )

    password = upper + lower + digit + special + remaining
    return ''.join(random.sample(password, len(password)))

def analyze_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    if score == 5:
        print("\n✅ Strong Password")
    elif score >= 3:
        print("\n⚠️ Medium Password")
        print("Suggested Strong Password:", generate_password())
    else:
        print("\n❌ Weak Password")
        print("Suggested Strong Password:", generate_password())

password = input("Enter Password: ")
analyze_password(password)