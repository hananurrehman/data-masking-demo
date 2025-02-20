import random


def mask_ssn(user_data):
    """Mask SSN, Credit Card, Phone, DOB, and Email fields."""
    if "ssn" in user_data and isinstance(user_data["ssn"], str):
        user_data["ssn"] = "***-**-" + user_data["ssn"][-4:] # Show last 4 digits

    if "credit_card" in user_data and isinstance(user_data["credit_card"], str):
        user_data["credit_card"] = "****-****-****-" + user_data["credit_card"][-4:] # Show last 4 digits

    if "phone" in user_data and isinstance(user_data["phone"], str):
        user_data["phone"] = user_data["phone"][:4] + "***-****" # Show first 3 digits

    if "dob" in user_data and isinstance(user_data["dob"], str):
        user_data["dob"] = user_data["dob"][:4]  # Show only the year

    if "email" in user_data and isinstance(user_data["email"], str):
        user_data["email"] = mask_email(user_data["email"]) # Show dummy email

    if "name" in user_data and isinstance(user_data["name"], str):
        user_data["name"] = f"Test user {random.randint(0,10)}" # Show dummy name

    return user_data

def mask_email(email):
    """Mask the email by appending a random 4-digit number before the domain."""
    try:
        _, domain = email.split("@")
        random_suffix = str(random.randint(1000, 9999))  # Generate a 4-digit number
        return f"testuser+{random_suffix}@{domain}"
    except ValueError:
        return email  # Return unchanged if format is invalid
