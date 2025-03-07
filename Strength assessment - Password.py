import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    length_weight = 2
    uppercase_weight = 2
    lowercase_weight = 2
    number_weight = 2
    special_char_weight = 3

    if len(password) >= 8:
        strength += length_weight
        feedback.append("✓ Password length is good (8+ characters).")
    else:
        feedback.append("✗ Password is too short (minimum 8 characters required).")

    if re.search(r'[A-Z]', password):
        strength += uppercase_weight
        feedback.append("✓ Contains uppercase letters.")
    else:
        feedback.append("✗ No uppercase letters found.")

    if re.search(r'[a-z]', password):
        strength += lowercase_weight
        feedback.append("✓ Contains lowercase letters.")
    else:
        feedback.append("✗ No lowercase letters found.")

    if re.search(r'[0-9]', password):
        strength += number_weight
        feedback.append("✓ Contains numbers.")
    else:
        feedback.append("✗ No numbers found.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += special_char_weight
        feedback.append("✓ Contains special characters.")
    else:
        feedback.append("✗ No special characters found.")

    if strength >= 10:
        rating = "Strong"
    elif strength >= 7:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, feedback

def main():
    password = input("Enter your password: ")
    rating, feedback = assess_password_strength(password)
    print("\nPassword Strength Assessment:")
    print(f"Rating: {rating}")
    print("\nFeedback:")
    for comment in feedback:
        print(comment)

if __name__ == "__main__":
    main()
