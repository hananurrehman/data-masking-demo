def mask_ssn(user_data):
    """Mask the SSN Field."""
    if "ssn" in user_data:
        user_data["ssn"] = "***-**-" + user_data["ssn"][-4:]
    return user_data